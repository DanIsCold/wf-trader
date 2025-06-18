import pywmapi as wm
import os
import json

items = wm.items.list_items()

os.makedirs(os.path.dirname("../data/api_response.txt"), exist_ok=True)
with open("../data/api_response.txt", "w", encoding="utf-8") as file:
    json.dump(items, file, indent=4)