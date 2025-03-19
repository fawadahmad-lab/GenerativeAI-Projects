from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()

# loading Google gemini model 
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash',temperature=0,max_completion_tokens=5)
st.header("AI Research Assistant")
st.write("your AI research assistant..")


# User Inputs
paper_input = st.selectbox("Select Research Paper Name", ["Attention is All You Need", "BERT: Pre-Training of Deep Bidirectional Transformers"])
style_input = st.selectbox("Select Style", ['Maths Heavy', 'Code Heavy', 'Beginner Friendly'])
length_input = st.selectbox("Select Length", ["One Paragraph", "Medium (2-3 paragraphs)", "Long (Detailed Explanation)"])


# loading template
template=load_prompt('template.json')




# streamlit button 
if st.button("submit"):
    chain=template | model
    result=chain.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
    })
    st.write(result.content)


