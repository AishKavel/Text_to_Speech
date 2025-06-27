# Text to Speech Converter

## Description
This project is a simple Text to Speech Converter web application built using Streamlit and the Google Text-to-Speech (gTTS) library. It allows users to input text, convert it to speech, and play the generated audio directly within the app.

## Features
- User-friendly web interface for text input.
- Converts text to speech using gTTS.
- Saves the generated speech as an MP3 file (`welcome.mp3`).
- Plays the generated audio within the app.

## Installation

1. Clone the repository or download the project files.
2. Install the required Python packages:
   ```bash
   pip install streamlit gtts ipython
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run TTS.py
   ```
2. Enter the text you want to convert to speech in the text area.
3. Click the **Process** button to generate the speech audio.
4. Click the **Play** button to listen to the generated audio.

## Dependencies
- [Streamlit](https://streamlit.io/) - For building the web app interface.
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) - For converting text to speech.
- [IPython](https://ipython.org/) - For audio playback support.

## File Structure
- `TTS.py` - Main Streamlit application script.
- `welcome.mp3` - Generated audio file after processing text input.

## License
This project is licensed under the MIT License.

## Author
Created by the Text to Speech project team.
