import streamlit as st
import getpass, os
from langchain.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4")

def main():
  st.title("Generative AI Example using OpenAI and LangChain")
  input = st.text_input("Ask me anything!", key="input")

  if input:
    output = model([HumanMessage(content=input)])
    st.write(output)

if __name__ == '__Main__':
  main()
