import streamlit as st
import time
from PIL import Image
import os

# Title of the web app
st.title("Solar Panel Defect Detection")

# Instructions
st.write("Upload solar panel images to detect defects. Please upload images in a grid format.")

# Create tabs
tab1, tab2 = st.tabs(["Upload Images", "Detection Result"])

# Tab 1: Image Upload
with tab1:
    # Create a form for image uploads
    with st.form(key='upload_form'):
        # Create columns for grid-like upload
        col1, col2 = st.columns(2)
        
        with col1:
            uploaded_files_col1 = st.file_uploader("Column 1 Images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
        
        with col2:
            uploaded_files_col2 = st.file_uploader("Column 2 Images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
        
        # Submit button
        submit_button = st.form_submit_button(label='Process Images')

# Tab 2: Result Display
with tab2:
    if submit_button and (uploaded_files_col1 or uploaded_files_col2):
        st.write("Processing images... Please wait.")
        
        # Simulate processing time (30 seconds)
        with st.spinner('Analyzing solar panels...'):
            time.sleep(30)
        
        # Display the specific result image
        st.subheader("Defect Detection Result")
        result_image_path = "path/to/your/result_image.jpg"  # Replace with your actual image path
        if os.path.exists(result_image_path):
            result_image = Image.open(result_image_path)
            st.image(result_image, caption="Detection Result", use_column_width=True)
        else:
            st.warning("Result image not found. Please ensure the path is correct.")
            # Display a placeholder image
            st.image("https://via.placeholder.com/400x300.png?text=Result+Image", caption="Placeholder Result")
        
        st.success("Processing complete!")
    else:
        st.write("Please upload images and click 'Process Images' in the Upload Images tab to see the result.")

