import streamlit as st
st.title("Ask a question") #sets title
st.header("Upload an image") #sets header
file=st.file_uploader("",type=["jpeg","jpg","png"]) #uploads file
if file:
    st.image(file, use_column_width=True) #displays image
    user_question=st.text_input("Ask a question about your image: ") #text input
    #agent response
    if user_question and user_question !="":
        st.write("dummy response lol")