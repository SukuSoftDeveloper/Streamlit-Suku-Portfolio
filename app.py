from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none
    return r.json()
#--Local CSS---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

#---Load assets----

lottie_coding = load_lottieurl("https://lottie.host/9f4a6f87-f615-4fb3-9f7f-b81f257aa50e/9LFVceCtCy.json")
# img_contact_form1 = Image.open("Images/code1.jpg")
# img_contact_form2 = Image.open("Images/code2.jpg")

with st.container():
    st.subheader("Hii, Iam Sudheer Kumar :wave:")
    st.title("A Dot Net Developer from India")
    st.write("Iam a passionate about finding ways to use Dot Net and C# to be more efficient and effective")
    st.write("[Learn More >](https://pythonvba.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            On my Youtube channel, I am creating tutorials for people who:
            - Are looking for way to levarage the power of python.
            - Are want to become full stack python developers.
            - Are want to become a Data Analyst with Python.
            """
        )
        st.write("[Youtube Channel >](https://youtube.com)")
    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")
# ---- Projects ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    text_column = st.columns((1,1))
    # with image_column:
    #     st.image("Images/code1.jpg")
    st.subheader("Integrate Lottie Animations Inside your Streamlit App")
    st.write(
            """
            Learn how to use lottie Files in Staremlit!
            Animations make to use use in our Web more enaging fun, and lotties files are earsiest way to do.
            In this tutorials, we can learn all those things.
            """
    )
    st.markdown("[Watch Video...](https://youtube.com)")
with st.container():
    st.write("##")
    text_column = st.columns((1,1))
    # with image_column:
    #     st.image("Images/code2.jpg")
    st.subheader("Integrate Lottie Animations Inside your Streamlit App")
    st.write(
            """
            Learn how to use lottie Files in Staremlit!
            Animations make to use use in our Web more enaging fun, and lotties files are earsiest way to do.
            In this tutorials, we can learn all those things.
            """
    )
    st.markdown("[Watch Video...](https://youtube.com)")

with st.container():
    st.write("---")
    st.header("Get in Touch With Me")
    st.write("##")

    #--formsubmit ---
    contact_form ="""
    <form action="https://formsubmit.co/annameti2000@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <input type="text" name="Number" placeholder="Mobile Number" required>
     <input type="date" name="date" placeholder="DOB" required>
     <textarea name="message" placeholder= "Address" required></textarea>

     <button type="submit">Send</button>
    </form>"""
 

   
    left_column , right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



   

       



       

   