import streamlit as st
from gtts import gTTS
import os
from IPython.display import Audio

# Title of the app
st.title('Text to Speech Converter')

# Text input area
text_input = st.text_area("Enter Text", "", height=300)

# Process button
if st.button('Process'):
    language = 'en'
    myobj = gTTS(text=text_input, lang=language, slow=False)
    myobj.save("welcome.mp3")
    st.success('Text processed and audio file saved.')

# Play button
if st.button('Play'):
    if os.path.exists("welcome.mp3"):
        audio_file = open("welcome.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.error("Please process the text first to generate the audio.")
