import streamlit as st
import os
import time
import glob
from gtts import gTTS
from translate import Translator

# Create 'temp' directory if it doesn't exist
try:
    os.mkdir("temp")
except FileExistsError:
    pass

st.write("Hello, my name is Mohamed Metwally")
st.write("and the first project")

st.title("Text to Speech")

def remove_old_files(n_days):
    mp3_files = glob.glob("temp/*.mp3")
    if mp3_files:
        now = time.time()
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days * 86400:
                os.remove(f)

def text_to_speech(input_language, output_language, text, tld):
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            translator = Translator(to_lang=output_language, from_lang=input_language)
            trans_text = translator.translate(text)
            break  # Break out of the loop if translation is successful
        except Exception as e:
            st.error(f"Translation failed on attempt {attempt}/{max_retries}. Error: {e}")
            if attempt < max_retries:
                st.info("Retrying...")
                time.sleep(1)  # Wait for a short time before retrying
            else:
                st.error("Failed to translate text after multiple retries.")
                raise RuntimeError("Failed to translate text after multiple retries.")

    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20] if text else "audio"
    except IndexError:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text

# GUI
text = st.text_input("Enter text")
in_lang = st.selectbox("Select your input language", ("English", "Arabic"))
out_lang = st.selectbox(
    "Select your output language",
    ("English", "Arabic", "Hebrew", "Russian", "German", "Hindi", "Korean", "Japanese", "Chinese", "Italian", "Spanish", "French", "Portuguese")
)
display_output_text = st.checkbox("Display output text")

# Language code mapping
lang_mapping = {
    "English": "en",
    "Arabic": "ar",
    "Hebrew": "iw",
    "Russian": "ru",
    "German": "de",
    "Hindi": "hi",
    "Korean": "ko",
    "Japanese": "ja",
    "Chinese": "zh-cn",
    "Italian": "it",
    "Spanish": "es",
    "French": "fr",
    "Portuguese": "pt",
}

input_language = lang_mapping.get(in_lang, "en")
output_language = lang_mapping.get(out_lang, "en")

# Text-to-Speech Conversion
if st.button("Convert"):
    try:
        result, output_text = text_to_speech(input_language, output_language, text, "com")
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown("## Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown("## Output text:")
            st.write(f" {output_text}")

    except RuntimeError as e:
        st.error(f"Error: {e}")

# Remove old audio files
remove_old_files(7)

