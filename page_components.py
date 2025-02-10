import streamlit as st

# Streamlit Page Config
def set_page_config():
    st.set_page_config(page_title="DishVision AI 🍽️", layout="wide", page_icon="🍽️")

def setup_sidebar():
    """Sets up the sidebar with API key input and instructions."""
    st.sidebar.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_SS.width-1300.jpg")
    st.sidebar.title("🔑 API Key Setup")
    
    api_key = st.sidebar.text_input("Enter your Google AI Studio API Key", type="password")
    
    st.sidebar.markdown("""
    🔹 **Where to get API Key?**  
    - Go to [Google AI Studio](https://aistudio.google.com/)  
    - Sign in & generate your API key  
    - Paste it above to start!
    """)
    
    return api_key

def display_header():
    """Displays the main title and description."""
    st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #FF5733;'>
        🍽️ DishVision AI
    </h1>
    <h3 style='text-align: center; color: #666;'>
        Snap, Detect & Cook with AI! 🤖🔥
    </h3>
    """, unsafe_allow_html=True)
    
    st.write("Upload a food image, and I'll detect the dish, its ingredients, and recipe! 🔥")

    st.markdown("""
    🖼️ **How It Works:**  
    1. Upload an image of a dish.  
    2. The AI will analyze the image and identify the dish.  
    3. You'll get the **dish name, ingredients, and step-by-step recipe**.  
    4. Enjoy cooking! 🍳  
    """)

def get_image_input():
    """Handles image upload and camera input."""
    option = st.radio("Choose Image Input Method:", ["Upload Image", "Capture from Camera"])

    if option == "Upload Image":
        return st.file_uploader("📸 Upload a dish image", type=["jpg", "jpeg", "png", "webp", "avif"])
    elif option == "Capture from Camera":
        return st.camera_input("📷 Take a photo of the dish")