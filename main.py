import streamlit

from PIL import Image

with streamlit.expander("Upload a file"):
    
      #   Upload an image from local computer
    uploaded_image = streamlit.file_uploader("Upload Image")

with streamlit.expander('Start Camera'):
    
      #   Start the Camera
    camera_image = streamlit.camera_input("Camera")

if camera_image:
    
    #   Create a Pillow Image Instance    
    img = Image.open(camera_image)

    #   Convert the Pillow Image to Grayscale
    gray_img = img.convert("L")

    #   Render the grayscale image on the webpage
    streamlit.image(gray_img)
    
if uploaded_image:
    
     #   Create a Pillow Image Instance    
    img = Image.open(uploaded_image)
    
     #   Convert the Pillow Image to Grayscale
    gray_img = img.convert("L")
    
    #   Render the grayscale image on the webpage
    streamlit.image(gray_img)