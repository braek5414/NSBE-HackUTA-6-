import streamlit as st
import base64
import os

# Function to optimize setting background
def set_background(image_file):
    # Read and encode the image
    image_path = os.path.join('images', image_file)
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    # Inject CSS for the background
    css_code = f"""
    <style>
    .stApp {{
        background: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
     .title-shadow {{
        color: white;  /* Text color */
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7); /* Shadow settings */
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

# Dictionary to store the timeline info and backgrounds
eras = {
    "2000-2002": {
        "description": "The early launch era of the PS2, featuring iconic games like 'Gran Turismo 3' and 'Metal Gear Solid 2.'",
        "background": "ps2_early_era.jpg"
    },
    "2003-2005": {
        "description": "The mid-life era where blockbuster franchises like 'GTA: San Andreas' and 'God of War' reigned supreme.",
        "background": "ps2_mid_era.webp"
    },
    "2006-2013": {
        "description": "The late era as the PS3 started to gain traction, with continued support for games like 'Persona 4' and 'Shadow of the Colossus.'",
        "background": "ps2_late_era.jpg"
    }
}

# Selectbox to choose PS2 era
st.markdown("<h1 class='title-shadow'>PlayStation 2: A Journey Through the Eras</h1>", unsafe_allow_html=True)
selected_era = st.selectbox(
    "Select a PS2 Era",
    list(eras.keys())
)

# Set the background based on the selected era
era_info = eras[selected_era]
set_background(era_info["background"])

# Display information about the selected era
st.subheader(f"PS2 Era: {selected_era}")
st.write(era_info["description"])
