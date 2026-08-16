
import streamlit as st
from travel_graph import travel_graph


st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Planner")
st.write("Plan your trip using LLM + LangGraph + Weather + Places + Hotel + Budget")


# User inputs
destination = st.text_input(
    "📍 Destination",
    placeholder="e.g. Shimla"
)

days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=30,
    value=5
)

people = st.number_input(
    "👥 Number of People",
    min_value=1,
    max_value=20,
    value=2
)

budget = st.number_input(
    "💰 Budget (₹)",
    min_value=1000,
    value=20000,
    step=1000
)

interests = st.text_input(
    "❤️ Interests",
    placeholder="nature, museum, food, photography"
)


# Generate button
if st.button("🚀 Generate Travel Plan"):

    if not destination:
        st.warning("Please enter a destination.")
        st.stop()

    if not interests:
        st.warning("Please enter your interests.")
        st.stop()

    initial_state = {
        "destination": destination,
        "days": str(days),
        "people": str(people),
        "budget": str(budget),
        "interests": interests,
        "weather": "",
        "places": "",
        "hotel": "",
        "budget_plan": "",
        "result": ""
    }

    with st.spinner("🤖 AI is planning your trip..."):

        result = travel_graph.invoke(initial_state)

    st.success("✅ Travel plan generated!")


    # Weather
    st.subheader("🌦️ Weather")
    st.write(result["weather"])


    # Places
    st.subheader("📍 Places")
    st.write(result["places"])


    # Hotels
    st.subheader("🏨 Hotels")

    hotels = result.get("hotel", "")

    if hotels:
        st.write(hotels)
    else:
        st.write("No hotels found.")


    # Budget
    st.subheader("💰 Budget Analysis")
    st.write(result["budget_plan"])


    # Final itinerary
    st.subheader("🗓️ Final Travel Itinerary")
    st.write(result["result"])

