# -Speech-synthesis-


# Text to Speech Converter

## Overview

The Text to Speech Converter is a simple program that allows users to convert text into audio. The program utilizes the Google Text-to-Speech (gTTS) library and the translate library for language translation.

## Features

- **Multilingual Support:** Convert text to speech in various languages, including English, Arabic, Hebrew, Russian, German, Hindi, Korean, Japanese, Chinese, Italian, Spanish, French, and Portuguese.

- **Language Translation:** Translate input text from one language to another before converting it to speech.

- **Text Display Option:** Choose to display the output text along with the generated audio.

## Usage

1. Enter the text you want to convert in the provided text input field.

2. Select the input language from the dropdown menu.

3. Choose the desired output language for the converted audio.

4. Optionally, check the "Display output text" checkbox if you want to see the translated text.

5. Click the "Convert" button to generate the audio.

6. The generated audio will be displayed, and you can listen to it directly in the Streamlit interface.

## Dependencies

- Streamlit: `pip install streamlit`
- gTTS: `pip install gtts`
- translate: `pip install translate`

## Running the Program

1. Install the required dependencies using the provided commands.

2. Run the program by executing the following command in your terminal:

    ```bash
    streamlit run your_program_name.py
    ```

Replace `your_program_name.py` with the actual filename of your program.


##URL
https://speech-synthesis.streamlit.app/
