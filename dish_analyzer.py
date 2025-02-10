import google.generativeai as genai
import streamlit as st
from PIL import Image


def analyze_dish(api_key, uploaded_file):
    """Processes the uploaded image using Gemini AI model and displays results."""
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="✅ Uploaded Image", use_container_width=True)

            with st.spinner("🤖 Analyzing the dish... Please wait 🍲"):
                prompt = """
                You will receive a food image from the user. Your task:
                - Identify the **Dish Name**
                - List **Ingredients** with quantities
                - Provide a **Step-by-Step Recipe**

                **Format Output Like This:**
                🍽️ **Dish Name:**  
                - Name of the dish
                
                🥕 **Ingredients:**  
                1. Ingredient-1: quantity  
                2. Ingredient-2: quantity  
                ...
                
                📜 **Recipe:**  
                1. Step 1  
                2. Step 2  
                ...
                """
                response = model.generate_content([prompt, image])

            st.markdown("---")
            st.subheader("🍛 **Detected Dish Details**")
            st.markdown(response.text)
    else:
        st.warning("⚠️ Please enter your API key in the sidebar to proceed.")