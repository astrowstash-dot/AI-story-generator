import streamlit as st
from story_generator import Generate_story_from_images
from PIL import Image


st.title("AI story generator.")
st.markdown("Add 1-10 images of choice, choose the style of story then let AI do the magic.")

uploaded_files = st.file_uploader(
    "upload your images....",
    accept_multiple_files=True,
    type=["png", "jpeg", "jpg"]
)


with st.sidebar:

    st.header("controls")

    style = st.selectbox(
        "Story style",
        ["Sci-fi", "Romantic", "Fantasy", "Comedy", "Horror", "Crime"]
    )

    Button = st.button(
        "Generate", type= "primary"
    )

# Main logic

if Button :
    if not uploaded_files:
        st.warning("No files uploaded, Images needed!")
    elif len(uploaded_files)>10 :
        st.warning("Maximum of 10 files can be uploaded.")
    else:
        with st.spinner("Your story is getting ready, might take a few minutes"):

            try:
                pil_images= [Image.open(uploaded_file) for uploaded_file in uploaded_files]
                st.subheader("your image inspiration: ")
                image_columns= st.columns(len(pil_images))

                for i , image in enumerate(pil_images):
                    with image_columns[i]:
                        st.image(image, use_container_width= True)

                generate_story = Generate_story_from_images(pil_images,style)
                if "error" in generate_story or "failed" in generate_story or "API key" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"Your {style} story:")
                    st.success(generate_story)

            except Exception as e:
                st.error(f"An application error occurred {e}")



            
            



    