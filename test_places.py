from places_tool import get_places

places = get_places("Manali, Himachal Pradesh, India")

print("\n📍 Places found:")

for place in places:
    print("-", place)