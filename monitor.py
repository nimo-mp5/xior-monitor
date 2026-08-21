import requests

URL = "https://www.xiorstudenthousing.eu/netherlands/eindhoven/kronehoefstraat-student-accommodation/"

FULLY_BOOKED = "Kronehoefstraat is fully booked at the moment"

ROOM_TYPES = [
    "Comfy",
    "Comfy (Balcony)",
    "Comfy (Entresol)",
]

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 Safari/537.36"
    )
}

print("Checking Xior Kronehoefstraat...")

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

html = response.text

# Xiorの正しいページを取得できているか確認
if "Kronehoefstraat" not in html:
    raise RuntimeError("Xior page could not be read correctly.")

# 現在の満室表示を確認
if FULLY_BOOKED.lower() in html.lower():
    print("❌ FULLY BOOKED")
    print("No room is currently available.")

else:
    print("🚨 POSSIBLE AVAILABILITY!")
    print("The 'fully booked' message has disappeared.")
    print(URL)

print("\nRoom types being monitored:")
for room in ROOM_TYPES:
    print("-", room)
