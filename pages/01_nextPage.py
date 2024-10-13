import streamlit as st

# Use CSS to set the background image
def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()

    # Create base64 encoding of the image
    import base64
    encoded_img = base64.b64encode(img_data).decode()

    # Set the background via a markdown block
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded_img}');
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_background('images/gamePageBackground.webp')