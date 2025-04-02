import streamlit as st
import time
from PIL import Image
import os

# Title of the web app
st.title("Solar Panel Defect Detection")

# Instructions
st.write("Specify the grid size and upload all solar panel images at once to detect defects.")

# Create tabs
tab1, tab2 = st.tabs(["Upload Images", "Detection Result"])

# Tab 1: Image Upload
with tab1:
    # User inputs for rows and columns
    num_rows = st.number_input("Number of Rows", min_value=1, max_value=10, value=2, step=1)
    num_cols = st.number_input("Number of Columns", min_value=1, max_value=10, value=2, step=1)
    
    total_images = num_rows * num_cols
    st.write(f"Total images to upload: {total_images}")

    # Upload all images at once
    uploaded_files = st.file_uploader("Upload all images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
    
    # Submit button
    process_images = st.button("Process Images")

# Tab 2: Result Display
with tab2:
    if process_images and uploaded_files and len(uploaded_files) == total_images:
        st.write("Processing images... Please wait.")
        
        # Simulate processing time (30 seconds)
        with st.spinner('Analyzing solar panels...'):
            time.sleep(30)
        
        # Alert user to move to the result tab
        st.warning("Images processed! Move to the 'Detection Result' tab to view results.")
        
        # Display the specific result image
        st.subheader("Defect Detection Result")
        result_image_path = "path/to/your/result_image.jpg"  # Replace with actual image path
        if os.path.exists(result_image_path):
            result_image = Image.open(result_image_path)
            st.image(result_image, caption="Detection Result", use_column_width=True)
        else:
            st.warning("Result image not found. Please ensure the path is correct.")
            # Display a placeholder image
            st.image("https://raw.githubusercontent.com/PramodhKumarVanjarapu/Fake/refs/heads/main/Fake.jpg", caption="Placeholder Result")
        
        st.success("Processing complete!")
    elif process_images:
        st.warning(f"Please upload exactly {total_images} images.")
    else:
        st.write("Specify the grid size, upload images, and click 'Process Images' in the Upload Images tab to see the result.")


