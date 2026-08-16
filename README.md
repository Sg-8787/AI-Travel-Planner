# ✈️ AI Travel Planner

An AI-powered travel planning application that generates personalized, weather-aware travel itineraries using **LangGraph, Ollama/Gemma, Streamlit, Weather APIs, and OpenStreetMap**.

## 🚀 Features

* 🌍 Single-destination travel planning
* 🌦️ Fetches weather information
* 📍 Finds nearby tourist attractions and museums
* 🏨 Finds nearby hotels for the selected destination
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
Hotel Agent
    ↓
Budget Agent
    ↓
Weather Router
    ↓
Decision Agent
    ↓
Ollama + Gemma 3 4B
    ↓
Final Travel Itinerary
```

## 🤖 Agents

### 🌦️ Weather Agent

Fetches weather information for the selected destination using a weather API.

### 📍 Places Agent

Uses **OpenStreetMap/Overpass API** to find nearby tourist attractions, museums and other points of interest.

### 🏨 Hotel Agent

Finds hotels near the selected destination using **OpenStreetMap**.

The agent uses:

* **Nominatim API** — to find the destination's latitude and longitude
* **Overpass API** — to search for nearby hotels

The hotel search uses a radius around the selected destination and returns available hotel names mapped in OpenStreetMap.
Hotel availability and prices are not real-time.

### 💰 Budget Agent

The Budget Agent uses **Python-based calculations** to divide the user's total budget into estimated categories:

* Hotel — 35%
* Food — 25%
* Local Transport — 20%
* Activities — 10%
* Miscellaneous — 10%

The total allocation equals the user's entered budget.

### 🔀 Weather Router

Checks the weather conditions and determines whether the itinerary should focus on indoor or outdoor activities.

### 🧠 Decision Agent

Uses **Ollama + Gemma 3 4B** to generate the final personalized day-by-day itinerary.

The Decision Agent considers:

* Destination
* Number of days
* Number of people
* Budget allocation
* User interests
* Weather
* Available places
* Available hotels

The LLM is responsible for **travel planning and itinerary generation**, while budget calculations are handled by Python.

## 🛠️ Tech Stack

* Python
* Streamlit
* LangGraph
* Ollama
* OpenStreetMap
* Nominatim API
* Overpass API

## 🔮Future Improvements

* ✈️ Flight API integration
* 💵 Live hotel and flight prices
* 🗺️ Distance and route optimization
* 📍 Google Maps integration
* 🌍 Multiple destination support
* 📊 Automatic budget verification
* 📄 PDF itinerary export
* 🔐 User authentication
* 💾 Saved travel plans

