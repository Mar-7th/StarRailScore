import json
import logging
from pathlib import Path
from copy import deepcopy


init_data = {
    "main": {
        "1": {"HPDelta": 1},
        "2": {"AttackDelta": 1},
        "3": {
            "HPAddedRatio": 0,
            "AttackAddedRatio": 0,
            "DefenceAddedRatio": 0,
            "CriticalChanceBase": 0,
            "CriticalDamageBase": 0,
            "HealRatioBase": 0,
            "StatusProbabilityBase": 0,
        },
        "4": {
            "HPAddedRatio": 0,
            "AttackAddedRatio": 0,
            "DefenceAddedRatio": 0,
            "SpeedDelta": 0,
        },
        "5": {
            "HPAddedRatio": 0,
            "AttackAddedRatio": 0,
            "DefenceAddedRatio": 0,
            "PhysicalAddedRatio": 0,
            "FireAddedRatio": 0,
            "IceAddedRatio": 0,
            "ThunderAddedRatio": 0,
            "WindAddedRatio": 0,
            "QuantumAddedRatio": 0,
            "ImaginaryAddedRatio": 0,
        },
        "6": {
            "BreakDamageAddedRatioBase": 0,
            "SPRatioBase": 0,
            "HPAddedRatio": 0,
            "AttackAddedRatio": 0,
            "DefenceAddedRatio": 0,
        },
    },
    "weight": {
        "HPDelta": 0,
        "AttackDelta": 0,
        "DefenceDelta": 0,
        "HPAddedRatio": 0,
        "AttackAddedRatio": 0,
        "DefenceAddedRatio": 0,
        "SpeedDelta": 0,
        "CriticalChanceBase": 0,
        "CriticalDamageBase": 0,
        "StatusProbabilityBase": 0,
        "StatusResistanceBase": 0,
        "BreakDamageAddedRatioBase": 0,
    },
    "max": 0,
}

type_map = {
    "HEAD": "1",
    "HAND": "2",
    "BODY": "3",
    "FOOT": "4",
    "NECK": "5",
    "OBJECT": "6",
}

character_map = json.loads(Path("config/AvatarConfig.json").read_text(encoding="utf-8"))
relic_recommend_map = json.loads(
    Path("config/AvatarRelicRecommend.json").read_text(encoding="utf-8")
)
main_recommend_map = json.loads(
    Path("config/RelicMainAffixAvatarValue.json").read_text(encoding="utf-8")
)
sub_recommend_map = json.loads(
    Path("config/RelicSubAffixAvatarValue.json").read_text(encoding="utf-8")
)

score_map = json.loads(Path("score.json").read_text(encoding="utf-8"))

for character_item in character_map:
    k = str(character_item.get("AvatarID"))
    logging.info(f"Processing {k}")
    score_map[k] = deepcopy(init_data)
    relic_recommend_item = next(
        (i for i in relic_recommend_map if str(i.get("AvatarID")) == k), None
    )
    main_recommend_item = next(
        (i for i in main_recommend_map if str(i.get("AvatarID")) == k), None
    )
    sub_recommend_item = next(
        (i for i in sub_recommend_map if str(i.get("AvatarID")) == k), None
    )
    # get main affix from character relic recommend
    if relic_recommend_item:
        property_set = set()
        for property in relic_recommend_item["PropertyList"]:
            relic_part = type_map[property["RelicType"]]
            score_map[k]["main"][relic_part][property["PropertyType"]] = 1
            property_set.add(property["PropertyType"])
    # get main affix from relic main affix character value
    if main_recommend_item:
        score_map[k]["main"]["3"] = {
            "HPAddedRatio": main_recommend_item.get("HP", 0),
            "AttackAddedRatio": main_recommend_item.get("Attack", 0),
            "DefenceAddedRatio": main_recommend_item.get("Defence", 0),
            "CriticalChanceBase": main_recommend_item.get("CriticalChance", 0),
            "CriticalDamageBase": main_recommend_item.get("CriticalDamage", 0),
            "HealRatioBase": main_recommend_item.get("HealRatio", 0),
            "StatusProbabilityBase": main_recommend_item.get("HP", 0),
        }
        score_map[k]["main"]["4"] = {
            "HPAddedRatio": main_recommend_item.get("HP", 0),
            "AttackAddedRatio": main_recommend_item.get("Attack", 0),
            "DefenceAddedRatio": main_recommend_item.get("Defence", 0),
            "SpeedDelta": main_recommend_item.get("Speed", 0),
        }
        score_map[k]["main"]["5"] = {
            "HPAddedRatio": main_recommend_item.get("HP", 0),
            "AttackAddedRatio": main_recommend_item.get("Attack", 0),
            "DefenceAddedRatio": main_recommend_item.get("Defence", 0),
            "PhysicalAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Physical"
                else 0
            ),
            "FireAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Fire"
                else 0
            ),
            "IceAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Ice"
                else 0
            ),
            "ThunderAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Thunder"
                else 0
            ),
            "WindAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Wind"
                else 0
            ),
            "QuantumAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Quantum"
                else 0
            ),
            "ImaginaryAddedRatio": (
                main_recommend_item.get("DamageAddedRatio", 0)
                if character_item["DamageType"] == "Imaginary"
                else 0
            ),
        }
        score_map[k]["main"]["6"] = {
            "BreakDamageAddedRatioBase": main_recommend_item.get("BreakDamage", 0),
            "SPRatioBase": main_recommend_item.get("SPRatio", 0),
            "HPAddedRatio": main_recommend_item.get("HP", 0),
            "AttackAddedRatio": main_recommend_item.get("Attack", 0),
            "DefenceAddedRatio": main_recommend_item.get("Defence", 0),
        }
        # fix highest value to 1
        for part in ["3", "4", "5", "6"]:
            if all(i != 1 for i in score_map[k]["main"][part].values()):
                highest = max(score_map[k]["main"][part].values())
                for i in score_map[k]["main"][part]:
                    if score_map[k]["main"][part][i] == highest:
                        score_map[k]["main"][part][i] = 1
        # some fix to attack and damage
        damage_add = main_recommend_item.get("DamageAddedRatio", 0)
        attack_add = main_recommend_item.get("Attack", 0)
        if damage_add > 0.1 and attack_add > 0.1:
            score_map[k]["main"]["5"]["AttackAddedRatio"] = max(
                min(1, round(damage_add * 0.8, 1)), attack_add
            )
    # get sub affix from relic main affix character value
    if sub_recommend_item:
        score_map[k]["weight"] = {
            "HPDelta": (
                round(sub_recommend_item.get("HP", 0) / 3, 1)
                if sub_recommend_item.get("HP", 0) > 0.1
                else 0
            ),
            "AttackDelta": (
                round(sub_recommend_item.get("Attack", 0) / 3, 1)
                if sub_recommend_item.get("Attack", 0) > 0.1
                else 0
            ),
            "DefenceDelta": (
                round(sub_recommend_item.get("Defence", 0) / 3, 1)
                if sub_recommend_item.get("Defence", 0) > 0.1
                else 0
            ),
            "HPAddedRatio": sub_recommend_item.get("HP", 0),
            "AttackAddedRatio": sub_recommend_item.get("Attack", 0),
            "DefenceAddedRatio": sub_recommend_item.get("Defence", 0),
            "SpeedDelta": sub_recommend_item.get("Speed", 0),
            "CriticalChanceBase": sub_recommend_item.get("CriticalChance", 0),
            "CriticalDamageBase": sub_recommend_item.get("CriticalDamage", 0),
            "StatusProbabilityBase": sub_recommend_item.get("StatusProbability", 0),
            "StatusResistanceBase": sub_recommend_item.get("StatusResistance", 0),
            "BreakDamageAddedRatioBase": sub_recommend_item.get("BreakDamage", 0),
        }


for k, v in score_map.items():
    sub_affix_weight_ordered = sorted(
        v["weight"].items(), key=lambda x: x[1], reverse=True
    )
    full_score_affix = []
    for i in sub_affix_weight_ordered:
        if i[1] == 1:
            full_score_affix.append(i[0])
    max_score = 0
    for i in ["3", "4", "5", "6"]:
        ordered_i = sorted(v["main"][i].items(), key=lambda x: x[1], reverse=True)
        sub_affix_weight_this = []
        for af in sub_affix_weight_ordered:
            if af[0] != ordered_i[0][0]:
                sub_affix_weight_this.append(af)
        max_score += 1.2 * (
            sub_affix_weight_this[0][1] * 6
            + sub_affix_weight_this[1][1]
            + sub_affix_weight_this[2][1]
            + sub_affix_weight_this[3][1]
        )
    # max 4+5 sub affix
    # origin 4 is different from each other
    max_score += (
        2
        * 1.2
        * (
            sub_affix_weight_ordered[0][1] * 6
            + sub_affix_weight_ordered[1][1]
            + sub_affix_weight_ordered[2][1]
            + sub_affix_weight_ordered[3][1]
        )
    )
    score_map[k]["max"] = max_score / 6.0
    if len(str(score_map[k]["max"])) > 6:
        score_map[k]["max"] = round(score_map[k]["max"], 3)


score_map = {k: score_map[k] for k in sorted(score_map.keys())}

logging.info("Writing to score.json")

Path("score.json").write_text(
    json.dumps(score_map, ensure_ascii=False, indent=4), encoding="utf-8"
)

csv_text = (
    "id,name,path,element,"
    + ",".join(f"3-{i}" for i in score_map["1001"]["main"]["3"].keys())
    + ","
    + ",".join(f"4-{i}" for i in score_map["1001"]["main"]["4"].keys())
    + ","
    + ",".join(f"5-{i}" for i in score_map["1001"]["main"]["5"].keys())
    + ","
    + ",".join(f"6-{i}" for i in score_map["1001"]["main"]["6"].keys())
    + ","
    + ",".join(score_map["1001"]["weight"].keys())
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
    "Memory": "Remembrance",
}

for k, v in score_map.items():
    for character_item in character_map:
        if str(character_item.get("AvatarID")) == k:
            csv_text += f"{k}, "
            csv_text += character_item["AvatarVOTag"] + ","
            csv_text += path_map[character_item["AvatarBaseType"]] + ","
            csv_text += character_item["DamageType"] + ","
            csv_text += ",".join(str(i) for i in v["main"]["3"].values()) + ","
            csv_text += ",".join(str(i) for i in v["main"]["4"].values()) + ","
            csv_text += ",".join(str(i) for i in v["main"]["5"].values()) + ","
            csv_text += ",".join(str(i) for i in v["main"]["6"].values()) + ","
            csv_text += ",".join(str(i) for i in v["weight"].values()) + "\n"
            break

logging.info("Writing to score.csv")

Path("score.csv").write_text(csv_text, encoding="utf-8")
