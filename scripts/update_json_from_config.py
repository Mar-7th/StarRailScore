from copy import deepcopy
import json

init_json = {
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

with open("config/AvatarRelicRecommend.json", "r", encoding="utf-8") as f:
    relic_recommends = json.load(f)

with open("config/AvatarConfig.json", "r", encoding="utf-8") as f:
    characters = json.load(f)

with open("score.json", "r", encoding="utf-8") as f:
    score = json.load(f)

for character in characters:
    k = str(character.get("AvatarID"))
    if k not in score.keys():
        score[k] = deepcopy(init_json)
        v = None
        for relic_recommend in relic_recommends:
            if str(relic_recommend.get("AvatarID")) == k:
                v = relic_recommend
        if v:
            prop_set = set()
            for i in v["PropertyList"]:
                relic_part = type_map[i["RelicType"]]
                score[k]["main"][relic_part][i["PropertyType"]] = 1
                if i["PropertyType"] in {
                    "PhysicalAddedRatio",
                    "FireAddedRatio",
                    "IceAddedRatio",
                    "ThunderAddedRatio",
                    "WindAddedRatio",
                    "QuantumAddedRatio",
                    "ImaginaryAddedRatio",
                }:
                    score[k]["main"][relic_part]["AttackAddedRatio"] = 0.8
                if i["PropertyType"] == "AttackAddedRatio":
                    if (
                        f"{character['DamageType']}AddedRatio"
                        in score[k]["main"][relic_part]
                    ):
                        score[k]["main"][relic_part][
                            f"{character['DamageType']}AddedRatio"
                        ] = 1
                prop_set.add(i["PropertyType"])
            for i in prop_set:
                for kk, vv in score[k]["main"].items():
                    if i in vv and vv[i] == 0:
                        score[k]["main"][kk][i] = 0.8

score = {k: score[k] for k in sorted(score.keys())}


with open("score.json", "w", encoding="utf-8") as f:
    json.dump(score, f, ensure_ascii=False, indent=4)
