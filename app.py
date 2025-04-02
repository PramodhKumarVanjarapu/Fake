import streamlit as st
import time
from PIL import Image
import os

# Title of the web app
st.title("Solar Panel Defect Detection")

# Instructions
st.write("Specify the grid size and upload solar panel images to detect defects.")

# Create tabs
tab1, tab2 = st.tabs(["Upload Images", "Detection Result"])

# Tab 1: Image Upload
with tab1:
    # User inputs for rows and columns
    num_rows = st.number_input("Number of Rows", min_value=1, max_value=10, value=2, step=1)
    num_cols = st.number_input("Number of Columns", min_value=1, max_value=10, value=2, step=1)
    
    total_images = num_rows * num_cols
    st.write(f"Total images to upload: {total_images}")

    # Create a form for image uploads
    with st.form(key='upload_form'):
        # Dynamic grid for file uploaders
        uploaded_files = []
        for row in range(num_rows):
            cols = st.columns(num_cols)
            for col in range(num_cols):
                with cols[col]:
                    file = st.file_uploader(f"Row {row+1}, Col {col+1}", type=['png', 'jpg', 'jpeg'], key=f"file_{row}_{col}")
                    uploaded_files.append(file)
        
        # Submit button
        submit_button = st.form_submit_button(label='Process Images')

# Tab 2: Result Display
with tab2:
    if submit_button and any(uploaded_files):
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
        st.write("Please specify the grid size, upload images, and click 'Process Images' in the Upload Images tab to see the result.")

