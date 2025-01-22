from gtts import gTTS
import os
import pygame

def speak(text):
    try:
        # Generate speech using gTTS
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("data.mp3")

        # Initialize pygame for audio playback
        pygame.init()
        pygame.mixer.init()

        # Load the generated speech file
        pygame.mixer.music.load("data.mp3")

        # Play the music
        pygame.mixer.music.play()

        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Stop music and quit pygame
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Clean up the generated file
        if os.path.exists("data.mp3"):
            os.remove("data.mp3")
            
