import streamlit as st
import cv2
import matplotlib.pyplot as plt

header=st.container()
images=st.container()
input = st.container()
output=st.container()

img1=cv2.imread('image_data\image/img1.jpg')
img2=cv2.imread('image_data\image/img2.jpg')

with header:
    st.title('Streamlit app')

with images:
    st.title('Images')
    
    st.image([img1,img2])


    
with output:
    inp=st.number_input('enter parameters:',min_value=0,max_value=255)
    gray=st.button('gray')
    if gray:
        gray_image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        st.image([gray_image1,gray_image2])
                 
    blur=st.button('blur')
    if blur:
        blur1=cv2.blur(img1,(100,100))
        blur2=cv2.blur(img2,(100,100))
        st.image([blur1,blur2])
        
    edge=st.button('edge')
    if edge:
        edge1=cv2.Canny(img1,0,inp)
        edge2=cv2.Canny(img2,0,inp)
        st.image([edge1,edge2])
        
        
      

