import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

def getLLMResponse(input_text, no_words, blog_style):
    # Initialize the ChatGroq LLM
    llm = ChatGroq(
        model_name="llama-3.1-70b-versatile",
        groq_api_key="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",
        temperature=0.7,
    )

    # Create the prompt template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    # Format the prompt
    formatted_prompt = prompt.format(
        blog_style=blog_style, input_text=input_text, no_words=no_words
    )

    # Pass the formatted prompt as a HumanMessage
    response = llm([HumanMessage(content=formatted_prompt)])
    print(response.content)  # For debugging in the console
    return response.content

# Streamlit App
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.title("AI Blog Generator 🤖")

# Input for Blog Topic
input_text = st.text_input("Enter the Blog Topic")

# Additional fields using columns
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words')
with col2:
    blog_style = st.selectbox(
        'Writing the blog for',
        ('Researchers', 'Data Scientist', 'Common People'),
        index=0
    )

# Generate button
submit = st.button("Generate")

# Final response
if submit:
    if not input_text or not no_words:
        st.error("Please fill in all fields!")
    else:
        try:
            response = getLLMResponse(input_text, no_words, blog_style)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
