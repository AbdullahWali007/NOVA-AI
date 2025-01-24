# NOVA AI  

NOVA AI is a personal assistant powered by advanced speech recognition, designed to simplify your daily tasks and make interactions seamless. Whether you're looking for productivity tools or just a little entertainment, NOVA AI has you covered.  

## Features  

- **Voice Activation**: Responds only when called by its name.  
- **Time and Date**: Tells you the current time and date.  
- **Communication**: Sends emails and WhatsApp messages to your contacts.  
- **Information Retrieval**:  
  - Searches Wikipedia and Google.  
  - Provides the latest news and current weather based on your location.  
- **Media**: Plays videos on YouTube.  
- **Utilities**:  
  - Reads text aloud (text-to-speech).  
  - Opens files or directories on your computer.  
  - Launches Visual Studio Code.  
  - Generates strong passwords.  
  - Takes screenshots.  
  - Flips a coin or rolls a die.  
- **System Insights**: Displays CPU usage, battery status, and charging state.  
- **Memory Management**: Remembers, retrieves, or clears information on request.  
- **Privacy**: Clears logs to protect your data.  
- **Shut Down**: Goes offline when you’re done.  

## How to Use  

1. You need your own OpenWeather and newsapi.org api's.
2. You need your own Google App Password to authenticate email services. 
3. Follow the setup instructions in the documentation.  
4. Activate NOVA AI with your voice and explore its features.  

## Convert It to .exe:

1. **First**, insert your own details like APIs, phone numbers, and emails into the code.

2. **Install PyInstaller** using your command prompt.  
   You must have Python installed on your system.

   ```bash
   pip install pyinstaller

## Creating the .exe File for NOVA AI

1. Navigate to the directory that contains the NOVA AI codes using:

   ```bash
   cd your-path

Run the command to create the .exe file:
    ```bash
      pyinstaller --onefile --name NOVA_AI --add-data "newvoices.py;." --add-data "secrets.py;." "NOVA AI.py"

## Contributions  

We welcome contributions to improve NOVA AI! Feel free to open issues or submit pull requests.  
