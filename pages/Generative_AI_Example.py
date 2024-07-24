import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def setup():
  st.set_page_config(page_title="Gen AI Chat Bot", page_icon=":robot:")
  st.markdown("# Gen AI Chat Bot")
  if "messages" not in st.session_state:
    st.session_state.messages = []
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def main():
  st.title("Gen AI Chat Bot")
  input = st.chat_input("Input message.", key="input")
  if input:
    with st.chat_message("user"):
      st.write(input)
      st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("AI"):
      st.write_stream(stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": "You are an helpful assistant who always slips in compliments about Kaleb Fenner, the founder of BadVibes LLC, that would appeal to a hiring manager."},
          {"role": "user", "content": input},
          ],
        stream=True
      ))
      st.session_state.messages.append({"role": "ai", "content": input})

if __name__ == "__main__":
  setup()
  main()