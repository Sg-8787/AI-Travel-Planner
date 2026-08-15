# ✈️ AI Travel Planner

An AI-powered travel planning application that generates personalized, weather-aware travel itineraries using **LangGraph, Ollama/Gemma, Streamlit, Weather APIs, and OpenStreetMap**.

## 🚀 Features

* 🌍 Single-destination travel planning
* 🌦️ Fetches weather information
* 📍 Finds nearby tourist attractions and museums
* 💰 Generates an estimated trip budget
* 🧠 Uses **Ollama + Gemma 3 4B** for itinerary generation
* 🔀 Uses LangGraph for agent workflow
* 🎯 Considers user's interests
* ☔ Adapts activities according to weather
* 📅 Generates day-by-day itineraries
* 🖥️ Interactive Streamlit interface

## 🏗️ Workflow

```text
User Input
    ↓
Streamlit UI
    ↓
Weather Agent
    ↓
Places Agent
    ↓
Budget Agent
    ↓
Weather Router
    ↓
Decision Agent
    ↓
Final Travel Itinerary
```

## 🤖 Agents

### 🌦️ Weather Agent

Fetches weather information for the selected destination.

### 📍 Places Agent

Uses **OpenStreetMap/Overpass API** to find nearby attractions and museums.

### 💰 Budget Agent

Creates an estimated budget allocation:

* Hotel — 35%
* Food — 25%
* Local Transport — 20%
* Activities — 10%
* Miscellaneous — 10%

### 🔀 Weather Router

Checks the weather and determines whether the itinerary should prefer indoor or outdoor activities.

### 🧠 Decision Agent

Uses **Gemma 3 4B through Ollama** to generate the final itinerary using:

* Destination
* Number of days
* Number of people
* Budget
* Interests
* Weather
* Available places

## 🛠️ Tech Stack

* Python
* Streamlit
* LangGraph
* Ollama
* Gemma 3 4B
* Requests
* OpenStreetMap
* Overpass API
```
```
## 🔮 Future Improvements

* Hotel and flight API integration
* Live travel costs
* Distance and route optimization
* Google Maps integration
* Multiple destination support
* Automatic budget verification
* PDF itinerary export
* User authentication
* Saved travel plans


