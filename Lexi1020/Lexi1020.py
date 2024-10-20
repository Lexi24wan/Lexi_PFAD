import streamlit as st
from pydub import AudioSegment
from pydub.generators import Sine
import io

# Streamlit title
st.title("Generate music based on your birthday!")

# user input
birthday = st.text_input("Please enter your birthday (YYYY-MM-DD):")

# function
def generate_music(birthday_str):
    try:
        # Convert each part of the birthday (year, month, day) into a frequency
        year, month, day = map(int, birthday_str.split('-'))
        
        # Generate audio frequencies for year, month, and day, and design them arbitrarily
        base_freq = year % 100 + 200
        month_freq = month * 20
        day_freq = day * 10
        
        # Generate three sine Boeing waves of different frequencies
        sound1 = Sine(base_freq).to_audio_segment(duration=1000) 
        sound2 = Sine(month_freq).to_audio_segment(duration=1000) 
        sound3 = Sine(day_freq).to_audio_segment(duration=1000) 
        
        # merge audio
        final_sound = sound1.append(sound2).append(sound3)
        
        # export audio
        audio_buffer = io.BytesIO()
        final_sound.export(audio_buffer, format="wav")
        return audio_buffer
    except Exception as e:
        st.error(f"False: {e}")
        return None

# Generate music when the user inputs their birthday
if birthday:
    audio_buffer = generate_music(birthday)
    
    if audio_buffer:
        # Display success message
        st.success("Music generation successful! Click the button below to play。")
        
        # Play the generated music
        st.audio(audio_buffer, format='audio/wav')

# 备注
st.write("Enter your birthday, AI will generate a short piece of music 🎵")



