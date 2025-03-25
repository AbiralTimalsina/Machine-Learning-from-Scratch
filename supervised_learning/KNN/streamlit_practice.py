import streamlit as st


st.title('Hello World')
st.header("This is the header")
st.subheader("This is the subheader")
st.text("Hello Streamlit")
st.markdown("### This is a Markdown")
st.success("Successful")

st.text_input("Enter your name","Value",30)
st.checkbox("Are you a human?")
st.radio("Select your gender",options=['male','female'])
st.selectbox("Select your age",options=[i for i in range(1,101)])
st.multiselect("Select multiple options", options=['Option 1', 'Option 2', 'Option 3'])