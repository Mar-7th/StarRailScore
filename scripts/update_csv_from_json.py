import json

with open("config/AvatarConfig.json", "r", encoding="utf-8") as f:
    characters = json.load(f)

with open("score.json", "r", encoding="utf-8") as f:
    result = json.load(f)

csv_text = (
    "id,name,path,element,"
    + ",".join(f"3-{i}" for i in result["1001"]["main"]["3"].keys())
    + ","
    + ",".join(f"4-{i}" for i in result["1001"]["main"]["4"].keys())
    + ","
    + ",".join(f"5-{i}" for i in result["1001"]["main"]["5"].keys())
    + ","
    + ",".join(f"6-{i}" for i in result["1001"]["main"]["6"].keys())
    + ","
    + ",".join(result["1001"]["weight"].keys())
    + "\n"
)

path_map = {
    "Warrior": "Destruction",
    "Rogue": "The Hunt",
    "Mage": "Erudition",
    "Shaman": "Harmony",
    "Warlock": "Nihility",
    "Knight": "Preservation",
    "Priest": "Abundance",
}

for k, v in result.items():
    for character in characters:
        if str(character.get("AvatarID")) == k:
            csv_text += f"{k}, "
            csv_text += character["AvatarVOTag"] + ","
            csv_text += path_map[character["AvatarBaseType"]] + ","
            csv_text += character["DamageType"] + ","
            csv_text += ",".join(str(i) for i in v["main"]["3"].values()) + ","
            csv_text += ",".join(str(i) for i in v["main"]["4"].values()) + ","
            csv_text += ",".join(str(i) for i in v["main"]["5"].values()) + ","
            csv_text += ",".join(str(i) for i in v["main"]["6"].values()) + ","
            csv_text += ",".join(str(i) for i in v["weight"].values()) + "\n"
            break

with open("score.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)
