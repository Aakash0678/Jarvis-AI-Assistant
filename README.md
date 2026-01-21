🤖 Jarvis AI Assistant
A voice-activated personal assistant built with Python that leverages advanced Large Language Models (LLMs) for intelligent conversations and task automation. 
This project integrates Google's Gemini 2.5 Flash for high-speed text processing , real-time image generation.

🚀 Features
Voice Interaction:

Wake Word Detection: Continuously listens for the wake word "Jarvis" to activate the system.

Speech-to-Text: Converts user speech into text commands using speech_recognition.

Text-to-Speech: Responds with a natural voice using pyttsx3.

Intelligent Conversation (The "Brain"):

Powered by the Google Gemini 2.5 Flash model via the google-genai library.

Capable of handling complex queries, writing code, and answering general knowledge questions with high accuracy.

Image Generation (The "Artist"):

Generates AI art based on voice descriptions 

Zero-Config: Uses a URL-based generation method that requires no extra API keys.

Auto-Display: Automatically saves the image locally and opens it on the user's screen.

System Automation:

App Control: Opens desktop applications (e.g., "Open Calculator", "Open VS Code") via voice commands.

Web Browsing: Performs Google searches automatically.

Utilities: Provides real-time date, time, and tells developer jokes.

🛠️ Tech Stack & Modules Used
Python 3.10+

Google GenAI SDK (google-genai): The core interface for communicating with Gemini models.

SpeechRecognition: For capturing and processing audio input.

Pyttsx3: Offline text-to-speech conversion library.

PyJokes: For generating random developer jokes.

Pillow (PIL): For image processing and saving.

OS & Webbrowser: Standard Python libraries for system interaction.

🔐 Security & API Key Management
This project requires a Google Cloud API Key to access the Gemini models.

Security Measure: To adhere to security best practices, the API key is NOT hardcoded in the main script.

The key is stored in a separate local file named api_key.py.

The main script imports the key securely using from api_key import api.

How to set up your keys

If you clone this repository, you must create your own key file:

Get a free API key from Google AI Studio.

Create a file named api_key.py in the project root folder.

Add the following function to that file:

Python
def api():
    return "YOUR_GOOGLE_API_KEY_HERE"
📦 Installation & Usage
Clone the Repository

Bash
git clone https://github.com/YOUR_USERNAME/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant
Create a Virtual Environment (Recommended)

Bash
conda create -n jarvis_env python=3.10
conda activate jarvis_env
Install Dependencies

Bash
pip install google-genai speechrecognition pyttsx3 pyjokes requests pillow
# Note: On Mac, you may also need: brew install portaudio
Run the Assistant

Bash
python main.py
Speak to Jarvis

Say "Jarvis" to wake him up.

Try commands like:

"Jarvis, what is the time?"

"Jarvis, open Google Chrome."

"Jarvis, create an image of a futuristic city."

"Jarvis, tell me a joke."

🔮 Future Improvements
Adding "Conversation Memory" so Jarvis remembers context from previous questions.

Integrating Spotify API for music control.

Building a simple GUI for a more visual experience.

Created by Aakash Pandey
