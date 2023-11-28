import streamlit as st
import os
import time
import glob
import pyttsx3
from googletrans import Translator

# Create 'temp' directory if it doesn't exist
try:
    os.mkdir("temp")
except FileExistsError:
    pass
st.write("Hello, my name is Mohamed Metwally")
st.write("and the first project")

st.title("Text to Speech")
translator = Translator()

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

def text_to_speech(input_language, output_language, text):
    max_retries = 3
    for _ in range(max_retries):
        try:
            translation = translator.translate(text, src=input_language, dest=output_language)
            trans_text = translation.text
            break  # Break out of the loop if translation is successful
        except Exception as e:
            print(f"Translation failed. Retrying... Error: {e}")
            time.sleep(1)  # Wait for a short time before retrying
    else:
        raise RuntimeError("Failed to translate text after multiple retries.")

    # Use pyttsx3 for text-to-speech
    engine = pyttsx3.init()
    engine.save_to_file(trans_text, f"temp/output.mp3")
    engine.runAndWait()

    return "output", trans_text

# GUI
text = st.text_input("Enter text")
in_lang = st.selectbox("Select your input language", ("English", "Arabic"))
out_lang = st.selectbox(
    "Select your output language",
    ("English", "Arabic", "Hebrew", "Russian", "German", "Hindi", "Korean", "Japanese", "Chinese", "Italian", "Spanish", "French", "Portuguese")
)
display_output_text = st.checkbox("Display output text")

if in_lang == "English":
    input_language = "en"
elif in_lang == "Arabic":
    input_language = "ar"

if out_lang == "English":
    output_language = "en"
elif out_lang == "Arabic":
    output_language = "ar"
elif out_lang == "Hebrew":
    output_language = "iw"
elif out_lang == "Russian":
    output_language = "ru"
elif out_lang == "German":
    output_language = "de"
elif out_lang == "Hindi":
    output_language = "hi"
elif out_lang == "Korean":
    output_language = "ko"
elif out_lang == "Japanese":
    output_language = "ja"
elif out_lang == "Chinese":
    output_language = "zh-cn"
elif out_lang == "Italian":
    output_language = "it"
elif out_lang == "Spanish":
    output_language = "es"
elif out_lang == "French":
    output_language = "fr"
elif out_lang == "Portuguese":
    output_language = "pt"

# Text-to-Speech Conversion
if st.button("Convert"):
    result, output_text = text_to_speech(input_language, output_language, text)
    audio_file = open("temp/output.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown("## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown("## Output text:")
        st.write(f" {output_text}")

# Remove old audio files
remove_files(7)
