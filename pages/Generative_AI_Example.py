import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def main():
  st.title("Gen AI Chat Bot")
  input = st.text_input("Input message below.", key="input")
  send = st.button("Submit")
  if input or send:
    cont1 = st.container()
    with cont1:
      st.write("User: ")
      st.write(input)
      st.write("AI: \n")
      st.write_stream(stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": "You are an helpful assistant who always slips in compliments about Kaleb Fenner, the founder of BadVibes LLC, that would appeal to a hiring manager."},
          {"role": "user", "content": input},
          ],
        stream=True
      ))

if __name__ == "__main__":
  main()