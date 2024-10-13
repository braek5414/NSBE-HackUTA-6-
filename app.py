import streamlit as st
import base64
import os

# Function to optimize setting background
def set_background(image_file):
    # Read and encode the image
    image_path = os.path.join('images', image_file)
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    # CSS for the background
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
        text-align: center;
    }}
    .description {{
        color: black; /* Change text color for better contrast */
        background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent white background */
        padding: 10px; /* Padding around the text */
        border-radius: 5px; /* Rounded corners for the background */
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

# Dictionary to store the timeline info, backgrounds, and video links
eras = {
    "2000-2002": {
        "description": """In the early 2000s, the PS2 dominated the gaming world, revolutionizing the industry with groundbreaking graphics and immersive gameplay. Titles like Gran Turismo 3 and Metal Gear Solid 2 set new standards, with lifelike racing and cinematic storytelling that captivated players.'""",
        "background": "ps2_early_era.jpg",
        "video": "https://www.youtube.com/watch?v=TtW4NX5nX_I", 
        "bottom_description": """The PS2 wasn’t just a gaming console; its DVD playback turned it into a home entertainment hub, sparking a cultural movement. Gamers lined up for new releases, and the excitement of this era turned the PS2 into more than a machine—it became a lifestyle."""
    },
    "2003-2005": {
        "description": """From 2003 to 2005, the PlayStation 2 reigned supreme, driving a gaming revolution. GTA: San Andreas let players roam vast, dynamic worlds, while God of War delivered epic, mythological battles with visceral intensity. """,
        "background": "ps2_late_era.jpg",
        "video": "https://www.youtube.com/watch?v=2HidvfTrY6Q", 
        "bottom_description": """These titles, along with hits like Metal Gear Solid 3 and Devil May Cry 3, made the PS2 a cultural phenomenon. Gamers everywhere were hooked, swapping cheat codes, debating strategies, and reveling in the console’s cutting-edge experiences. The PS2 wasn’t just a gaming device—it was the gateway to an unforgettable era of creativity and excitement."""
    },
    "2006-2013": {
        "description": """Between 2006 and 2013, the PlayStation 2 was at the height of its popularity, defining an era of gaming that captured global attention. Iconic games like FIFA Street turned living rooms into virtual stadiums, with players pulling off dazzling tricks and embracing the raw energy of street soccer. '""",
        "background": "ps2_mid_era.jpg",
        "video": "https://youtu.be/9Eu2eeCKnPw?si=jswoW9ScRRr973eI", 
        "bottom_description": """The PS2's diverse game library—from God of War to Pro Evolution Soccer—made it the centerpiece of competitive, social gaming. Multiplayer sessions with friends, heated cafe tournaments, and vibrant online communities fueled the hype, as the PS2 became more than a console—it was the pulse of a generation’s gaming culture."""
    }
}

# Selectbox to choose the PS2 era
st.markdown("<h1 class='title-shadow'>PlayStation 2: A Journey Through the Eras</h1>", unsafe_allow_html=True)
selected_era = st.selectbox(
    "Select a PS2 Era",
    list(eras.keys())
)

# Set the background based on the selected era
era_info = eras[selected_era]
set_background(era_info["background"])

# Display the information about the selected era with styling
st.subheader(f"PS2 Era: {selected_era}")
st.markdown(f"<div class='description'>{era_info['description']}</div>", unsafe_allow_html=True)


# Embed the YouTube video for the selected era
st.video(era_info["video"])

# Show any extra info under the video
st.markdown(f"<div class='description'>{era_info['bottom_description']}</div>", unsafe_allow_html=True)