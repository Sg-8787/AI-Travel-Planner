import requests


def get_places(city):

    # 1. City ka latitude/longitude
    geo_url = "https://nominatim.openstreetmap.org/search"

    geo_params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "AI-Travel-Agent/1.0"
    }

    geo_response = requests.get(
        geo_url,
        params=geo_params,
        headers=headers,
        timeout=10
    )

    geo_response.raise_for_status()

    geo_data = geo_response.json()

    if not geo_data:
        return []

    latitude = geo_data[0]["lat"]
    longitude = geo_data[0]["lon"]

    # 2. Overpass API
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json][timeout:6];
    node["tourism"="attraction"]
    (around:8000,{latitude},{longitude});
    node["tourism"="museum"](around:8000,{latitude},{longitude});
    out;
    """

    try:
        response = requests.post(
            overpass_url,
            data=query,
            headers=headers,
            timeout=15
        )
    except requests.exceptions.ReadTimeout:
        print("❌ Overpass server timeout")
        return []

    print("Overpass status:", response.status_code)

    if response.status_code != 200:
        print("API response:")
        print(response.text[:500])
        return []

    try:
        data = response.json()
    except ValueError:
        print("❌ API ne JSON return nahi kiya.")
        print(response.text[:500])
        return []

    # 3. Places extract
    places = []

    for element in data.get("elements", []):

        tags = element.get("tags", {})
        name = tags.get("name")

        if name and name not in places:
            places.append(name)

    return places[:10]