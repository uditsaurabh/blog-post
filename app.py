import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


def open_ai_api_key():
    st.title("Openai API key")
    password = st.text_input("Enter Openai api key:", type="password")
    return password


def get_topic():
    st.title("Enter Topic")
    return st.text_input("Enter Blog topic:", type="default")


def create_llm(api_key):
    return OpenAI(openai_api_key=api_key)


def generate_response(llm, topic):
    template = """
    As experienced author of best selling psychology and self-improvement bools, 
    generate a 400-word blog post about {topic}.   
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: 
    This post has X words.
    """
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    print("the response is as follows", response)
    return st.write(response)


def main():
    api_key = open_ai_api_key()
    topic = get_topic()
    if api_key and topic:
        llm = create_llm(api_key)
        generate_response(llm, topic)


if __name__ == "__main__":
    main()
