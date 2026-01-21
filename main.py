import speech_recognition as sr 
import pyttsx3
import pyjokes
import webbrowser
import datetime
import time
import os
from google import genai
from google.genai import types
from PIL import Image
from api_key import api

# Configure the AI model
client = genai.Client(api_key=api())

def ask_ai(question):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=question
        )
        return response.text
    except Exception as e:
        print(f"AI Error: {e}")
        return "I am having trouble connecting to the internet."
    
def generate_image(prompt):
    print("🎨 Generating image..")
    #choose the ai models according to your api key
    try:
        response = client.models.generate_images(
            model='gemini-2.0-flash-exp-image-generation',
            prompt=prompt,
            config=types.GenerateImagesConfig(number_of_images=1)
        )
        
        if response.generated_images:
            image = response.generated_images[0].image
            filename = "generated_art.png"
            image.save(filename)
            print("✨ Image saved!")
            os.system(f"open {filename}")
            return "I have created the image and opened it for you."
        else:
            return "The image generation failed."
            
    except Exception as e:
        print(f"Image Error: {e}")
        # Fallback message if your API key doesn't have Imagen 3 access yet
        if "404" in str(e):
            return "My image model (Imagen 3) is currently not available for your API key."
        return "I am sorry, I encountered an error while painting that."
'''
it sets text to speech engine and stores the variable text
'''
def speak(text):

    print(f"🤖 Jarvis: {text}")
    try:
        engine = pyttsx3.init() #initialising the pyttsx3 module(one time)
        engine.setProperty('rate' , 190) #speed 
        engine.say(text) 
        engine.runAndWait()
    except Exception as e:
        print("Audio driver error, but continuing...")
'''
setting up the speech recognisition function and making it listen from my mac book microphone to check for the 
available microphone run this and copy the index no to the device_index = 
otherwise leave it empty it automatically sets to default

import speech_recognition as sr

print("🎤 Scanning audio devices...")
mics = sr.Microphone.list_microphone_names()

for i, mic_name in enumerate(mics):
    print(f"Index {i}: {mic_name}")
'''
def listen():
    r = sr.Recognizer()
    # Optional: Adjust these based on your room's background noise 300-400 is good for a closed room
    r.energy_threshold = 300 
    r.pause_threshold = 1.0 

    while True:
        print("🎤 Waiting for 'Jarvis'...")
        try:
            with sr.Microphone(device_index=1) as source:
                '''
                timeout = means how long jarvis waits for you to start speaking
                pharse_time_limit = This is the maximum time Jarvis will let you talk once you have started.
                summary:
                Jarvis, wait 5 seconds for me to start talking. 
                If I do talk, let me speak for up to 14 seconds, then cut me off and process the command.
                '''
                audio = r.listen(source, timeout=5, phrase_time_limit=14)
                
            print("⚡️ Processing...")
            query = r.recognize_google(audio, language='en-in').lower()
            print(f"👂 Heard: {query}")

            # SCENARIO 1: You said a full command (e.g., "Jarvis what is the time")
            if "jarvis" in query and len(query) > 6:
                # Remove the word "jarvis" and return the actual command
                command = query.replace("jarvis", "").strip()
                return command

            # SCENARIO 2: You just said "Jarvis" (e.g., to wake it up)
            elif query.strip() == "jarvis":
                speak("Yes?")
                # Now listen for the follow-up command
                with sr.Microphone(device_index=1) as source:
                    try:
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        print("🎤 Listening for command...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=10)
                        command = r.recognize_google(audio, language='en-in').lower()
                        return command
                    # if you stayed silent after saying jarvis
                    except Exception as e:
                        print(f"Ignored: '{query}' (Did not hear Jarvis)")
            # SCENARIO 3: You said something else (ignore it)
            else:
                print(f"Ignored: '{query}' (Did not hear Jarvis)")

        except sr.WaitTimeoutError:
            pass # Just keep listening silently
        except Exception as e:
            # print(f"Error: {e}") # Uncomment to debug
            pass

def main_brain():
    print("Testing Speaker...")
    speak("System online. Initializing audio drivers.")
    #speak("Hi! , I am Jarvis , What can i do for you today?")
    '''
    as i havent used AI based model so i created a few list of words and if they appeared in your 
    sentance the output will be according to that
    '''
    time_words = ["time" , 'clock' , 'watch']
    greet_words = ['hi' , 'hello' , 'hey' , 'wake up' , "Jarvis"]
    joke_words = ['joke' , 'make me laugh']


    while True:
        time.sleep(0.3) # small delay so that computer dont listen its own voice
        query = listen()

        if(query == "None"):
            continue
        flag = False

        if(any(word in query for word in greet_words)):
            speak("Hello Sir ")
            flag = True

        if(any(word in query for word in time_words)):
            current_time = datetime.datetime.now().strftime("%I:%M %p") # used to access current time from your pc
            speak(f"The time is {current_time}")
            flag = True

        if("date" in query):
            current_date = datetime.datetime.now().strftime("%B %d, %Y") # used to access current date from ur pc
            speak(f"Today is {current_date}")
            flag = True
            
        if(any(word in query for word in joke_words)): # using pyjokes to tell jokes
            joke = pyjokes.get_joke()
            speak(f"{joke}")
            flag = True

        if("open" in query): # it could be diffrent for your systems mine is mac m2 so i used to os module to open apps i tell 
            app_name = query.replace("open","").strip()
            if(app_name):
                speak(f"Opening {app_name}")
                os.system(f"open -a '{app_name}'")
            else:
                speak("which application should i open")
            flag = True
            
        if("search for" in query): # for searching something in google 
            topic = query.replace("search for"  , "").strip()
            if topic:
                speak(f"Searching for {topic}")

                search_url = f"https://www.google.com/search?q={topic}"

                webbrowser.open(search_url)
            else:
                speak("What should i search for")
            
            flag = True
        
        if("stop" in query or "exit" in query or "by" in query or 'bye' in query or 'shutdown' in query): # breaking condition from the loop
            speak("This is Jarvis signing off. Good Bye Sir")
            
            break

        if('create an image' in query or "generate an image" in query):
            prompt = query.replace('create image' , "").replace('generate image',"").strip()
            if prompt:
                speak("Generating your image, this may take a while")
                result = generate_image(prompt)
                speak(result)
                flag = True
            
            else:
                speak("what kind of image should i create")
            

        if (not flag):
            speak("Thinking...")
            answer = ask_ai(query)
            speak(answer)

if (__name__ == "__main__"):
    main_brain()

