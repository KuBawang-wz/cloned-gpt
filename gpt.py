from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def generate_content(background, subject, model_name, creativity, api_key):
    problem_template = ChatPromptTemplate.from_messages(
        [
            ("system", "{background}"),
            ("human", "{subject}")
        ]
    )

    model = ChatOpenAI(model=model_name, openai_api_key=api_key, temperature=creativity,
                       openai_api_base="https://api.aigc369.com/v1")

    problem_chain = problem_template | model

    reply = problem_chain.invoke({"background": background, "subject": subject}).content

    return reply
# print(generate_content("无背景", "gpt模型", "gpt-3.5-turbo", 0.7, "sk-nttGL7NbnbG7en8jB3Cb80Aa8b874dA29c2aFb264e54A6C2"))
# print(generate_script("sora模型", 1, 0.7, os.getenv("OPENAI_API_KEY")))
