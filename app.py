import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from LLAMA2 model
def getLlamaResponse(input_text, no_of_words, blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 512,
                                'temperature': 0.01})

    template = """Write a blog for {style} job profile for a topic {text} within {n_words} words."""

    prompt = PromptTemplate(input_variables=["style", "text", "n_words"],
                            template=template)
    
    # Generate Response
    response = llm(prompt.format(style=blog_style, text=input_text, n_words=no_of_words))
    print(response)
    return response

st.set_page_config(page_title="Blog Generator",
                   page_icon='😊',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs")

input_text = st.text_input("Enter Blog Topic")

# Creating two columns for additional 2 fields
col1, col2 = st.columns([5, 5])

with col1:
    no_of_words = st.text_input('Number of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Authors'), index=0)
submit = st.button("Generate")

# Final Response
if submit:
    if input_text and no_of_words.isdigit() and blog_style:
        st.write(getLlamaResponse(input_text, no_of_words, blog_style))
    else:
        st.error("Please fill all the fields correctly.")
