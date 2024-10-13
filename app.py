import streamlit as st
import base64

# Function to set the background
def set_background(image_file):
    with open(image_file, "rb") as f:
        image_data = f.read()
    encoded_image = base64.b64encode(image_data).decode()

    background_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# Dictionary to store the timeline info and backgrounds
eras = {
    "2000-2002": {
        "description": "The early launch era of the PS2, featuring iconic games like 'Gran Turismo 3' and 'Metal Gear Solid 2.'",
        "background": "ps2_launch_era.jpg"
    },
    "2003-2005": {
        "description": "The mid-life era where blockbuster franchises like 'GTA: San Andreas' and 'God of War' reigned supreme.",
        "background": "ps2_mid_life_era.jpg"
    },
    "2006-2013": {
        "description": "The late era as the PS3 started to gain traction, with continued support for games like 'Persona 4' and 'Shadow of the Colossus.'",
        "background": "ps2_late_era.jpg"
    }
}

# Streamlit selectbox to choose an era
st.title("PlayStation 2: A Journey Through the Eras")
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
