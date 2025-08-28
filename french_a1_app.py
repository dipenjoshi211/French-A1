import streamlit as st
import datetime
import json
import os

daily_activities = {
    "Monday": {
        "title": "Greetings and Introductions",
        "link": "https://www.youtube.com/watch?v=JkFQ8u2mI3E",
        "description": "Listen and repeat common greetings. Match audio to text."
    },
    "Tuesday": {
        "title": "Numbers & Time",
        "link": "https://stories.duolingo.com/",
        "description": "Practice listening with Duolingo Stories or TV5MONDE."
    },
    "Wednesday": {
        "title": "Family & Professions",
        "link": "https://www.youtube.com/c/EasyFrenchVideos",
        "description": "Watch Easy French interviews. Write down 5 new words."
    },
    "Thursday": {
        "title": "Daily Routine",
        "link": "https://www.podcastfrancaisfacile.com/",
        "description": "Listen to A1 dialogues. Answer 3 questions based on audio."
    },
    "Friday": {
        "title": "At the Caf\u00e9 / Ordering Food",
        "link": "https://www.lingq.com/en/learn-french-online/",
        "description": "Role-play ordering food. Listen and repeat."
    },
    "Saturday": {
        "title": "Mock Test Practice",
        "link": "#",
        "description": "Take a full listening mock test and review vocabulary."
    },
    "Sunday": {
        "title": "Speaking + Audio Diary",
        "link": "#",
        "description": "Practice dialogues and record a short audio diary."
    }
}

progress_file = 'progress.json'
if os.path.exists(progress_file):
    with open(progress_file, 'r') as f:
        progress = json.load(f)
else:
    progress = {day: False for day in daily_activities}

st.title('🇫🇷 French A1 Daily Practice App')
st.subheader('Your personalized DELF A1 preparation plan')

today = datetime.datetime.now().strftime('%A')
activity = daily_activities.get(today, {})

st.markdown(f'### 📅 Today is {today}')
st.markdown(f'**Activity:** {activity.get("title")}')
st.markdown(f'**Description:** {activity.get("description")}')
if activity.get("link") != '#':
    st.markdown(f'[Click here to start]({activity.get("link")})')

if st.checkbox('✅ Mark today\'s activity as completed'):
    progress[today] = True
    with open(progress_file, 'w') as f:
        json.dump(progress, f)
    st.success('Progress saved!')

st.markdown('### 📊 Weekly Progress')
for day, done in progress.items():
    st.write(f'{day}: {'✅' if done else '❌'}')

st.markdown('---')
st.markdown('🔔 **Notifications enabled for:** dipen.joshi211@gmail.com')
st.markdown('📬 Weekly summary will be sent every Sunday evening.')