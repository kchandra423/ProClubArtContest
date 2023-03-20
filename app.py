import os

import requests
import streamlit as st
from dotenv import load_dotenv
import dropbox

load_dotenv()

dropbox_key = os.getenv('DROPBOX_KEY')
dbx = dropbox.Dropbox(dropbox_key)

demo_file = open('res/coding_art_demo.mp4', 'rb')
demo_bytes = demo_file.read()

audio_demo_file = open('res/jukebox_audo_sample.mp3', 'rb')
audio_demo_bytes = audio_demo_file.read()

st.header('Programming Club\'s Art Contest!')
st.subheader('Due April 4th')
st.write(
    'It\'s time for the Programming Club\'s Art Contest! We\'re looking for the best art made with code. The contest is open to all students, and the winner will receive a $50 Amazon gift card. The deadline is April 4th, and the winner will be announced on April 5th. To enter, submit your art to the #art channel on our Discord server. For more information, check out the #art channel on our Discord server. Good luck!')

st.markdown("""---""")

st.subheader('Prizes')

award1, award2, award3 = st.columns(3)
with award1:
    st.subheader('Most Creative')
    st.write(
        'The most creative and interesting application of computer science will win this prize (think outside the box!)')
with award2:
    st.subheader('Highest Quality')
    st.write('The highest quality art will win this prize (the best looking art)')
with award3:
    st.subheader('Most Challenging')
    st.write(
        'The most technically challenging piece of art will win this prize (making a nueral network from scratch, or developing your own algorithim)')

st.markdown("""---""")

st.subheader('Here some samples of what we are looking for:')
col1, col2 = st.columns(2)
with col1:
    st.caption('Randomly Generating Trees with recursion in Processing')
    st.video(demo_bytes)
    st.caption(
        'Open Ai\'s (The people behind Chat - GPT) jukebox project, creating a country song in the style of Alan Jackson')
    st.audio(audio_demo_bytes)
with col2:
    st.caption('A poem created by PoetryGeneratorAI.com')
    st.write('My love for programming knows no bounds,'
             '\nTo craft complex and intricate sounds\n'
             'My skills improve with practice that I find,\n'
             'As I go deep into the programming mind.\n\n'
             'My confidence grows as I learn more each day,\n'
             'My coding skills more powerful each way\n'
             'I take on challenges with no fear in sight,\n'
             'My knowledge and power will only grow tonight.\n\n'
             'My passion for coding is never ceasing,\n'
             'My skills and output are ever increasing\n'
             'I find joy in every code I write,\n'
             'My passion for coding a sublime delight.\n\n'
             'The joy of programming, I will never tire,\nMy love for coding with me, I inspire')

st.markdown("""---""")
st.subheader('Rules')
rule1, rule2, rul3 = st.columns(3)
with rule1:
    st.write('1. All submissions must be original work')
with rule2:
    st.write('2. All submissions must be school appropriate')
with rul3:
    st.write('3. All submissions must be made with code')
with st.form():
    st.subheader('Enter the contest!')
    name = st.text_input('Enter your name')
    email = st.text_input('Enter your email')
    st.write('By entering the contest, you agree to the rules')
    file = st.file_uploader('Upload your art (any format works, code, images, videos, etc.)', accept_multiple_files=True)
    description = st.text_area('Enter a description of your art')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Thank you for entering the contest! Good luck!')


        def newer():
            url = 'https://USERNAME:PASSWORD@www.googleapis.com/upload/drive/v3/files?uploadType=media'
            data = '''{{
              "name":"testing.txt",
            }}'''
            response = requests.post(url, data=data, key = auth_key)
            print(response.text)
