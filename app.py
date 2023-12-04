import streamlit as st
import os
import time
import glob
from gtts import gTTS
from mtranslate import translate

# Create 'temp' directory if it doesn't exist
try:
    os.mkdir("temp")
except FileExistsError:
    pass

st.write("Hello, my name is Mohamed Metwally")
st.write("and the first project")

st.title("Text to Speech")

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

def text_to_speech(input_language, output_language, text):
    try:
        trans_text = translate(text, output_language, input_language)
    except Exception as e:
        raise RuntimeError(f"Failed to translate text: {e}")

    tts = gTTS(trans_text, lang=output_language, slow=False)
    try:
        my_file_name = text[0:20]
    except IndexError:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text

# GUI
text = st.text_input("Enter text")
in_lang = st.selectbox("Select your input language", ("English", "Arabic"))
out_lang = st.selectbox(
    "Select your output language",
    ("English", "Arabic", "French", "German", "Spanish", "Italian", "Portuguese", "Russian", "Chinese", "Japanese", "Korean", "Hindi", "Hebrew")
)
display_output_text = st.checkbox("Display output text")

language_codes = {
    "English": "en",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Hebrew": "he"
}

input_language = language_codes.get(in_lang, "en")
output_language = language_codes.get(out_lang, "en")

# Text-to-Speech Conversion
if st.button("Convert"):
    result, output_text = text_to_speech(input_language, output_language, text)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown("## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown("## Output text:")
        st.write(f" {output_text}")

# Remove old audio files
remove_files(7)
