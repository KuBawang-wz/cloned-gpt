import streamlit as st
from gpt import generate_content

st.title("Clone-ChatGPT")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

model = st.selectbox("请选择你要用的模型",
                     ["gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-16k"],
                     index=None)
background = st.text_area("请给AI传递背景，或给AI安排个性或角色：")
subject = st.text_area("请输入你的问题：")
creativity = st.slider("请输入模型的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)
submit = st.button("生成回答")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not model:
    st.info("请选择你要用的模型")
    st.stop()
if submit and not background:
    st.info("请给AI传递背景，或给AI安排个性或角色（没有填无）")
    st.stop()
if submit and not subject:
    st.info("请输入你的问题")
    st.stop()
if submit:
    with st.spinner("AI正在思考中，请稍等..."):
        reply = generate_content(background, subject, model, creativity, openai_api_key)
    st.success("AI已做出回答！")
    st.subheader("回答")
    st.write(reply)
