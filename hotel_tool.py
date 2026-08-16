
import requests


def get_hotels(city):

    headers = {
        "User-Agent": "AI-Travel-Planner/1.0"
    }

    # 1. City ka latitude/longitude
    nominatim_url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    try:
        response = requests.get(
            nominatim_url,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
        print("Geocoding error:", e)
        return []

    if not data:
        print("City not found.")
        return []

    lat = data[0]["lat"]
    lon = data[0]["lon"]

    # 2. Particular city ke around hotels search
    overpass_url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json][timeout:15];

    (
      node["tourism"="hotel"](around:10000,{lat},{lon});
      way["tourism"="hotel"](around:10000,{lat},{lon});
      relation["tourism"="hotel"](around:10000,{lat},{lon});
    );

    out center;
    """

    try:
        response = requests.post(
            overpass_url,
            data=query,
            headers=headers,
            timeout=25
        )

        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
        print("Overpass error:", e)
        return []

    hotels = []

    for element in data.get("elements", []):

        tags = element.get("tags", {})
        name = tags.get("name")

        if name and name not in hotels:
            hotels.append(name)

    print(f"\n🏨 Hotels near {city}:")

    if hotels:
        for i, hotel in enumerate(hotels[:10], 1):
            print(f"{i}. {hotel}")
    else:
        print("No hotels found.")

    return hotels[:10]
