import requests

JSON_URL = "https://raw.githubusercontent.com/srhady/vipsports/refs/heads/main/alpha_live.json"

OUTPUT_FILE = "channels.m3u"

response = requests.get(JSON_URL)
data = response.json()

m3u = "#EXTM3U\n"

for channel in data:

    name = channel.get("name", "Unknown")
    logo = channel.get("logo", "")
    group = channel.get("group", "General")
    url = channel.get("url", "")

    # Optional DRM
    key = channel.get("key", "")
    keyid = channel.get("keyid", "")

    extinf = f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'

    # MPD + KEY support
    if ".mpd" in url and key:
        extinf += f'#KODIPROP:inputstream.adaptive.license_type=clearkey\n'
        extinf += f'#KODIPROP:inputstream.adaptive.license_key={keyid}:{key}\n'

    extinf += f"{url}\n"

    m3u += extinf

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(m3u)

print("M3U playlist updated successfully.")
