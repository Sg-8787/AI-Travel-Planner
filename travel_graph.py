import ollama
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from weather_tool import get_weather
from places_tool import get_places
from hotel_tool import get_hotels

# STATE

class TravelState(TypedDict):
    destination: str
    days: str
    people: str
    budget: str
    interests: str
    weather: str
    places: str
    hotel: str
    budget_plan: str
    result: str


# WEATHER AGENT
def weather_agent(state: TravelState):

    weather_data = get_weather(
        state["destination"]
    )

    return {
        "weather": str(weather_data)
    }


# PLACES AGENT

def places_agent(state: TravelState):

    places = get_places(
        state["destination"]
    )

    return {
        "places": str(places)
    }

def hotel_agent(state: TravelState):

    hotels = get_hotels(state["destination"])

    print("\n🏨 AVAILABLE HOTELS:")

    if hotels:
        for i, hotel in enumerate(hotels, 1):
            print(f"{i}. {hotel}")
    else:
        print("No hotels found.")

    return {
        "hotel": str(hotels)
    }

# BUDGET AGENT

def budget_agent(state: TravelState):

    total_budget = float(state["budget"])
    days = int(state["days"])
    people = int(state["people"])

    hotel = total_budget * 0.35
    food = total_budget * 0.25
    transport = total_budget * 0.20
    activities = total_budget * 0.10
    miscellaneous = total_budget * 0.10

    budget_plan = f"""
Estimated Budget for {people} people / {days} days:

Hotel: ₹{hotel:.0f}
Food: ₹{food:.0f}
Local Transport: ₹{transport:.0f}
Activities: ₹{activities:.0f}
Miscellaneous: ₹{miscellaneous:.0f}

Total Budget: ₹{total_budget:.0f}
Estimated Total: ₹{total_budget:.0f}

All amounts are approximate estimates.
"""

    return {
        "budget_plan": budget_plan
    }



# WEATHER ROUTER

def weather_router(state: TravelState):

    weather = state["weather"].lower()

    if (
        "rain" in weather
        or "storm" in weather
        or "snow" in weather
        or "thunder" in weather
    ):
        return "indoor"

    return "outdoor"



# FINAL DECISION AGENT


def decision_agent(state: TravelState):

    route = weather_router(state)

    if route == "indoor":

        weather_instruction = """
Weather is unsuitable for outdoor activities.

Prefer:
- museums
- cafes
- indoor attractions
- shopping
- local food

Avoid long outdoor activities.
"""

    else:

        weather_instruction = """
Weather is suitable for outdoor activities.

Prefer:
- sightseeing
- nature
- photography
- trekking
- outdoor attractions
"""

    prompt = f"""
You are the final AI Travel Decision Agent.

Destination: {state['destination']}
Days: {state['days']}
People: {state['people']}
Total Budget: ₹{state['budget']}
Interests: {state['interests']}

Weather:
{state['weather']}

Available Places:
{state['places']}

Official Budget Allocation:
{state['budget_plan']}

{weather_instruction}

Create a clear day-by-day itinerary.

IMPORTANT COST RULES:

- Do NOT calculate individual activity costs.
- Do NOT assign ₹ amounts to Morning, Afternoon, or Evening activities.
- Do NOT create daily cost totals.
- Do NOT invent hotel, food, transport, or activity prices.
- Use the Official Budget Allocation exactly as provided.
- At the end, show only the official budget breakdown.
- The official total budget is ₹{state['budget']}.
- All prices in the budget section are estimates.

IMPORTANT:

- Use places from the available places when possible.
- Follow the weather.
- Follow the user's interests.
- Create a realistic {state['days']}-day itinerary.
- Include Morning, Afternoon and Evening where practical.

Return ONLY the final itinerary.
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "result": response["message"]["content"]
    }



# LANGGRAPH

graph = StateGraph(TravelState)

graph.add_node("weather", weather_agent)
graph.add_node("places", places_agent)
graph.add_node("hotel", hotel_agent)
graph.add_node("budget", budget_agent)
graph.add_node("decision", decision_agent)

graph.add_edge(START, "weather")
graph.add_edge("weather", "places")
graph.add_edge("places", "hotel")
graph.add_edge("hotel", "budget")

graph.add_conditional_edges(
    "budget",
    weather_router,
    {
        "indoor": "decision",
        "outdoor": "decision"
    }
)

graph.add_edge("decision", END)

travel_graph = graph.compile()
