import streamlit as st



st.title("AI story generator.")
st.markdown("Add 1-10 images of choice, choose the style of story then let AI do the magic.")


with st.sidebar:
    st.header("controls")

# sidebar option to upload images

st.file_uploader(
    "upload your images")

    