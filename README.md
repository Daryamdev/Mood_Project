# Mood Music Recommender 🎵

A simple web application that recommends songs based on the selected mood.  
Each time you click a mood button, a random track is shown with a link to listen on Spotify.

## 🚀 Features

- 9 moods to choose from (happy, sad, chill, angry, etc.)
- Each mood returns a random song from a preset list
- Frontend in HTML/CSS/JavaScript
- Backend built with FastAPI
- Live Spotify links

## 📸 Screenshot

![App Screenshot](/mood.png)
![App Screenshot](/mood1.png)


## 🧠 How it works

- Mood buttons trigger a fetch request to FastAPI
- FastAPI returns a random song from the mood’s list
- Frontend displays song title + Spotify link




## Future Plans 
- Integrate openAI (ChatGPT 3.5) to generate mood-based song suggestions using AI
- Add a database to track user-selected moods and song history 
- Allow users to submit their own songs for each mood 
- Add filters by genre ,energy level ,or language
- Improved UI/UX with transitions and animations
- Host the full app on Render or Railway 
- Implement login system (optional,for saving preferences )



## 🛠️ Installation

1. Clone the repo:
```bash
git clone https://github.com/Daryamdev/Mood_Project.git
cd Mood_Project


## How to run the app:

1.Create a virtual enviroment(optional but recommended )
python -m venv venv 
source venv/bin/activate ##Linux/Mac
venv\Scripts\activate    ##Windows

2.Install dependencies
pip install -r requirements.txt

3.Start the FastAPI backend
uvicorn backend.main:app --reload 


4.Open the app in your browser
Visit http://127.0.0.1:8000 to use the interface.


