import pyttsx3  # type: ignore #pip install pyttsx3 == text to speech
import datetime
import speech_recognition as sr  # type: ignore # pip install SpeechRecognition == speech from mic to text
import smtplib  #for emails
from secrets import senderemail, epwd # type: ignore
from email.message import EmailMessage
import pyautogui # type: ignore
from time import sleep
import webbrowser as wb
import pywhatkit # type: ignore
import wikipedia
import pywhatkit
import requests
import clipboard # type: ignore 
import os
import time as tt
import string
import random
import psutil
import re
import pygetwindow as gw
from newvoices import speak
    
def time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    

    # Convert to 12-hour format
    meridian = "AM"
    if hour >= 12:
        meridian = "PM"
        if hour > 12:
            hour -= 12
    elif hour == 0:
        hour = 12

    speak("The current time is:")
    speak(f"{hour}:{minute:02d} {meridian}")

def date():
    now = datetime.datetime.now()
    year = now.year
    month_name = now.strftime("%B")  # Gets the full name of the month
    day = now.day

    speak("The current date is:")
    speak(f"{day} {month_name} {year}")

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("and Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("and Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("and Good evening sir!")
    else:
        speak("and Good night sir!")


def wishme():
    speak("Hello I am nova , Welcome back")
    greeting()  # for good morning, afternoon etc
    speak(" What I can do for you?")

def takecommandCMD():
    query = input("Tell me what to do: ")
    
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language = "en-US")
        print(query)
    except Exception as e:
        print(e)
        
        return "None"
    return query

def sendEmail(reciever, subject, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(senderemail, epwd)

        email = EmailMessage()
        email['From'] = senderemail
        email['To'] = reciever
        email['Subject'] = subject
        email.set_content(content)
        server.send_message(email)

        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        server.close()
    
import pygetwindow as gw
import pywhatkit
import pyautogui
from time import sleep

def sendwhatsapp(phone_number, message):
    """
    Sends a WhatsApp message using an existing tab if one is open; otherwise, it opens a new tab.
    
    Args:
    phone_number (str): The recipient's phone number (should start with '+').
    message (str): The message to be sent.
    """
    def is_whatsapp_tab_open():
        windows = gw.getAllTitles()
        for title in windows:
            if "WhatsApp" in title:  # Checks if "WhatsApp" is in any window title
                return True
        return False

    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    if is_whatsapp_tab_open():
        print("WhatsApp tab is already open.")
        
        pyautogui.hotkey('ctrl', 't')  
        sleep(2)
        pyautogui.typewrite(message)
        sleep(1)
        pyautogui.press('enter')
    else:
        print("Opening a new WhatsApp tab.")
        # Open a new WhatsApp tab and send the message
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        sleep(11)  # Wait for WhatsApp web to load the message box
        pyautogui.press('enter')


def searchgoogle():
    speak("what do you want to search on google")
    search =takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


def get_weather(api_key):
    try:
        # Get current location
        location_url = "http://ip-api.com/json/"
        location_data = requests.get(location_url).json()
        city = location_data.get('city', None)

        if not city:
            speak("Sorry, I couldn't determine your location.")
            return

        # fetch weather data
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(weather_url)
        weather_data = response.json()

        # debug logs
        print(f"Location Data: {location_data}")
        print(f"Weather Data: {weather_data}")

        if weather_data.get("cod") == 200:
            temp = weather_data['main']['temp']
            weather_desc = weather_data['weather'][0]['description']
            weather_info = f"The current temperature in {city} is {temp} degrees Celsius with {weather_desc}."
            speak(weather_info)
        else:
            error_message = weather_data.get("message", "Unknown error")
            speak(f"Couldn't fetch the weather information. API response: {error_message}")
    except Exception as e:
        speak("An error occurred while fetching the weather.")
        print(f"Error: {e}")

#news function
def get_news(api_key):
    try:
        speak("Do you have a specific topic in mind for the news?")
        topic = takeCommandMic().lower()

        if "random" in topic:
            # Fetch top random headlines
            news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
            speak("Fetching random news...")
        else:
            # Fetch news for the specific topic
            news_url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
            speak(f"Fetching news about {topic}...")

        # Fetch news data
        response = requests.get(news_url)
        news_data = response.json()


        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])
            if not articles:
                speak(f"Sorry, I couldn't find any news about {topic}.")
                return

            # Speak the top 5 valid news headlines
            speak("Here are the top news headlines:")
            count = 0
            for article in articles:
                title = article.get("title", "").strip()
                # Skip articles with "removed" or empty titles
                if title and "removed" not in title.lower():
                    count += 1
                    speak(f"News {count}: {title}")
                    # Stop after 5 valid headlines
                    if count == 5:
                        break

            if count == 0:
                speak(f"Sorry, I couldn't find any valid news about {topic}.")
        else:
            error_message = news_data.get("message", "Unknown error")
            speak(f"Couldn't fetch the news. API response: {error_message}")
    except Exception as e:
        speak("An error occurred while fetching the news.")
        print(f"Error: {e}")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def tell_joke():
    try:
        
        joke_url = "https://v2.jokeapi.dev/joke/Any?type=single"  # You can also specify 'Programming', 'Miscellaneous', etc.
        
       
        response = requests.get(joke_url)
        joke_data = response.json()
        
        if joke_data.get("error"):
            speak("Sorry, I couldn't fetch a joke at the moment.")
            return

        
        if "joke" in joke_data:
            joke = joke_data["joke"]
            speak(joke)
        elif "setup" in joke_data and "delivery" in joke_data:
            setup = joke_data["setup"]
            delivery = joke_data["delivery"]
            speak(f"{setup}... {delivery}")
        else:
            speak("Sorry, I couldn't understand the joke format.")
    except Exception as e:
        speak("An error occurred while fetching the joke.")
        print(f"Error: {e}")
        
def screenshot():
    img_name = tt.time()
    img_name =f'C:\\Users\\Dell\\Desktop\\NOVA AI\\screenshots\\{img_name}.png'
    sleep(4)
    img = pyautogui.screenshot(img_name)
    speak("The screenshot has been successfully taken")
    img.show()

def passwordgen(length=12):  
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    print(password)

def flip_coin():
    
    result = random.choice(["Heads", "Tails"])
    
    
    speak(f"The coin landed on: {result}")

def roll_die():
    
    result = random.randint(1, 6)
    
    
    speak(f"The die landed on: {result}")


def cpu():
    # get CPU usage percentage
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage + " percent")
    
    # get battery information
    battery = psutil.sensors_battery()
    if battery is not None:
        battery_percent = str(battery.percent)
        speak("Battery is at " + battery_percent + " percent")
        
        # check if the battery is charging or discharging
        if battery.power_plugged:
            speak("The battery is charging.")
        else:
            speak("The battery is not charging.")
    else:
        speak("Sorry, I could not retrieve battery information.")
def tokenize_query(query):
    # use regex to find all words (ignores punctuation and special characters)
    tokens = re.findall(r'\b\w+\b', query.lower())
    return tokens


#all tasks added
def what_can_i_do():
    tasks = """
    Sir, I can do the following for you:
    1. Tell you the current time.
    2. Provide the current date.
    3. Tell you about yourself (basic details).
    4. Send emails to your contacts.
    5. Send WhatsApp messages to your contacts.
    6. Search on Wikipedia.
    7. Search on Google.
    8. Play videos on YouTube.
    9. Get the current weather.
    10. Get the latest news.
    11. Read out a text (convert text to speech).
    12. Open a file or directory on your computer.
    13. Open Visual Studio Code.
    14. Tell you a joke.
    15. Take a screenshot.
    16. Remember something for you.
    17. Tell you what I remember.
    18. Forget everything you've asked me to remember.
    19. Generate strong passwords.
    20. Flip a coin for you.
    21. Roll a die for you.
    22. Show CPU usage.
    23. Go offline (shut down).
    """
    speak(tasks)

def clear_console():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for macOS and Linux
    else:
        os.system('clear')

if __name__ =="__main__":
    clear_console()
    wishme()
    while True:
        wake_word = "nova"
        query = takeCommandMic().lower()
        tokens = tokenize_query(query)

        if wake_word in query:

            if 'time' in query:
                time()

            elif 'date' in query:
                date()
            
            elif 'know about me' in query:
                speak("sir your name is (your-name), your other details ")
            
            elif 'shut up' in query:
                speak("sorry sir!, If i offended you, tell me what else can i do for you? ")
            
            elif 'email' in query:
                email_list = {
                    'david':'david-email@gmail.com', #email of david
                    'anna': 'anna-email@gmail.com' #email of anna
                }
                try:
                    speak("to whom you want to send an email, sir")
                    name = takeCommandMic().lower()
                    receiver = email_list[name]
                    speak("what is the subject of the email")
                    subject = takeCommandMic()
                    speak("What is the content for the e mail?")
                    content = takeCommandMic()
                    sendEmail(receiver,subject,content)
                    speak("Email has been sent successfully! ")
                except Exception as e:
                    print(e)
                    speak("unable to end the e mail")

            elif 'Whatsapp' in query or 'whatsapp' in query:
                user_name = {
                    'david':'+92xxxxxxxx',
                    'anna':'+92xxxxxxxxx', 'iris':'+92xxxxxxxx' #add as much needed, you can change country code like +41,+91 etc
                    

                }
                try:
                    speak("to whom you want to send the whatsapp message, sir")
                    name = takeCommandMic().lower()
                    phone_number = user_name[name]
                    speak("what message you want to send?")
                    message = takeCommandMic()
                    sendwhatsapp(phone_number,message)
                    speak("message has been sent successfully! ")
                except Exception as e:
                    print(e)
                    speak("unable to end the message")
                
            elif 'wikipedia' in query:
                try:
                    speak("searching on wikipedia...")
                    query = query.replace("wikipedia","")
                    result = wikipedia.summary(query,sentences = 2)
                    print(result)
                    speak(result)
                except Exception as e:
                    print("Unable to search wikipedia..")
                    speak("Unable to search wikipedia..")

            elif 'search' in query:
                try:
                    searchgoogle()
                except Exception as e:
                    speak("There was an error searching google")

            elif 'youtube' in query:
                speak("what i have to search on youtube sir?")
                try:
                    topic = takeCommandMic()
                    pywhatkit.playonyt(topic)
                except Exception as e:
                    speak("an error occured playing on youtube")

            elif 'weather' in query:
                api_key = 'your-openweathermap-api key'
                get_weather(api_key)

            elif 'news' in query:
                news_api_key = 'your-newsapi.org-api key'
                get_news(news_api_key)
            
            elif 'read' in query:
                text2speech()

            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('Open','')))

            elif 'open code' in query:
                code_path = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(code_path)
            
            elif 'joke' in query:
                tell_joke()

            elif 'screenshot' in query:
                screenshot()


            elif 'remember' in query:
                speak("What do you want me to remember, sir?")
                data = takeCommandMic()

                
                if data:
                    speak("Okay, sir, I will remember that: " + data)

                    
                    with open('data.txt', 'a') as remember:  
                        remember.write(data + "\n")  
                else:
                    speak("Sorry, sir, I didn't catch that. Could you please repeat?")


            elif 'do you know anything' in query or 'what do you know' in query:
                try:
                    
                    with open('data.txt', 'r') as remember:
                        data = remember.read()
                        if data:
                            speak("You told me to remember: " + data)
                        else:
                            speak("I don't remember anything yet.")
                except FileNotFoundError:
                    speak("I don't remember anything yet.")

            elif 'forget' in query or 'delete' in query:
                speak("Okay, sir, I will forget everything.")
                
                # clear the contents of the file
                with open('data.txt', 'w') as forget:
                    forget.truncate(0)  

                
                speak("I have forgotten everything, sir.")

            

            elif 'password' in query:
                speak("here is a secure and strong password for you")
                try:
                    passwordgen()

                except Exception as e:
                    speak("there was an error in generating password")

            elif 'flip a coin' in query:
                try:
                    flip_coin()
                except Exception as e:
                    speak("sorry sir,i am unable to flip the coin")

            elif 'roll a die' in query or 'roll' in query:
                try:
                    roll_die()
                except Exception as e:
                    speak("sorry sir,i am unable to roll the die")
            
            elif 'cpu' in query or 'CPU' in query:
                try:
                    cpu()
                except Exception as e:
                    speak("i am unable to get cpu usage sir")

            elif 'what can you do' in query:
                what_can_i_do()

            elif 'clear' in query:
                clear_console()

            elif 'offline' in query or 'off' in query or 'goa' in query:
                speak("going offline sir, good bye!")
                quit()