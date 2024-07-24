import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def main():
  st.title("Gen AI Chat Bot")
  input = st.chat_input("Input message.", key="input")
  cont1 = st.container()
  with cont1:
    with st.chat_message("user"):
      if input == None: return
      st.write(input)
    with st.chat_message("AI"):
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