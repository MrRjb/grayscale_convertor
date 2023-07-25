import streamlit

from PIL import Image

with streamlit.expander('Start Camera'):
    
    # Start the Camera
    camera_img = streamlit.camera_input("Camera")

if camera_img:
    
    #   Create a Pillow Image Instance    
    img = Image.open(camera_img)

    #   Convert the Pillow Image to Grayscale
    gray_img = img.convert("L")

    #   Render the grayscale image on the webpage
    streamlit.image(gray_img)