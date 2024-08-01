import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def setup():
  st.set_page_config(page_title="OpenAI Powered Chat Bot", page_icon=":robot:")
  st.markdown("# OpenAI powered Chat Bot")
  if "messages" not in st.session_state:
    st.session_state.messages = []
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def main():
  input = st.chat_input("Input message.", key="input")
  if input:
    with st.chat_message("user"):
      st.write(input)
      st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("AI"):
      st.write_stream(stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": "You are a python programmer that is especially knowledgable about streamlit and pytorch."},
          {"role": "user", "content": input},
          ],
        stream=True
      ))
      st.session_state.messages.append({"role": "ai", "content": input})

if __name__ == "__main__":
  setup()
  main()