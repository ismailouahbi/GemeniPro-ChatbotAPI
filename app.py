## Import necessary libraries

import streamlit as st


# Browser App title
st.set_page_config(page_title="Gemeni Pro Chatbot")

# add stremlit sidebar
st.sidebar.title("Gemeni Pro Chatbot")

# add components to sidebar
st.sidebar.markdown("### Created by [Ismail Ouahbi](https://www.linkedin.com/in/ismail-ouahbi) ###")

"""
Description of the project
"""

# add components to main page
st.title("Gemeni Pro Chatbot")

# more description
st.markdown("##### Source Code [GitHub link](https://github.com/ismailouahbi/GemeniPro-ChatbotAPI)")
st.markdown("> Follow the provided instructions there for easy implementation.")

# --------------
# main app 
# import libraries
from langchain_google_genai import ChatGoogleGenerativeAI


# configure the API key [ get it from https://makersuite.google.com/app/apikey]
GOOGLE_API_KEY = "YOUR API KEY HERE"
# Keep it private!

# define the llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# start chatbot App using streamlit

st.markdown("### Ask me anything... ###")

def generate_response(input_text):
    # generate response
    # response = generate_text(input_text)[0]['generated_text']
    # response = "I am a chatbot & I am still learning, please be patient with me 🙏"
    response =  llm.invoke(input_text)
    # return st.info("I am a chatbot & I am still learning, please be patient with me 🙏")
    return st.info(response.content)

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')

     
  # when submitted generate response and clear text area
  if submitted:
    generate_response(text)



# end chatbot

# add separator
st.markdown("---")

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["More info", "News & Updates"])

# add components to the tabs

# tab1
# app design image
tab1.write("### App design ###")
tab1.image("assets/introduction.jpeg")
# links
tab1.markdown("> * [blog](https://medium.com/@ismailouahbi)")
tab1.markdown("> * [portfolio](https://ismailouahbi.github.io/)")

# tab2
tab2.markdown("> * [Subscribe](https://ismailouahbi.medium.com/subscribe)")
