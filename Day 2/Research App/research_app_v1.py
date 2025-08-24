import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

st.header("Research App")

paper_input = st.text_input("enter your research paper")
paper_style = st.selectbox("Select Paper Style", ["Beginner Friendly", "Technical", "Code Oriented" ,"Mathematical"])
length = st.selectbox("Select Length", ["Short (1 paragraph)", "Medium (2-3 paragraph)", "Long (Detailed Explanation)"])

template = load_prompt("research_paper_summary_template.json")

# Generic way to invoke the template
# prompt = template.invoke({
#     "paper_input":paper_input,
#     "paper_style":paper_style, 
#     "length":length
#     })

if st.button("Submit"):
    # Using the template with the model
    chain = template| model
    result = chain.invoke({
    "paper_input":paper_input,
    "paper_style":paper_style, 
    "length":length
    })
    st.write(result.content)