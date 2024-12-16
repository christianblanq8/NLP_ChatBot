from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join([p.get_text() for p in paragraphs])
        return content
    except HTTPError as hp:
        print(hp)

llm = OllamaLLM(model="vicuna", temperature=0)

prompt = PromptTemplate(
    input_variables=["content", "question"],
    template="""
You are an expert summarizer and analyzer. Given the following webpage content:

{content}

Answer the user's question below:

Question: {question}

Answer:
"""
)

chain = RunnableSequence(prompt | llm)

def analyze_link(url, question):
    content = fetch_webpage_content(url)
    if "Error" in content:
        return content
    return chain.invoke({"content": content, "question": question})


if __name__ == "__main__":
    user_gateway = input("Enter 1 to access bot! Enter 0 to exit: ")

    while user_gateway == "1":
        url = input("Paste a Link: ")
        question = input('Enter a question: ')
        print("Answer:", analyze_link(url,question))
        user_gateway = input("Enter 2 to continue! Enter 0 to exit: ")
        
        while user_gateway == "2":
                question = input('Enter a question: ')
                print("Answer:", analyze_link(url,question))
                user_gateway = input("Enter 2 to continue! Enter 0 to exit: ")

    
    if user_gateway == "0":
        print("Goodbye")

