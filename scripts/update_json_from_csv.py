from copy import deepcopy
import json

score = {}

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

with open("score.csv", "r", encoding="utf-8") as f:
    csv = f.read()

csv_lines = csv.split("\n")[1:]

for line in csv_lines:
    data = line.split(",")
    if len(data) < 4:
        continue
    character_id = data[0]
    score[character_id] = deepcopy(init_json)
    index = 4
    for num in ["3", "4", "5", "6"]:
        for k in score[character_id]["main"][num]:
            if "." in data[index]:
                score[character_id]["main"][num][k] = float(data[index])
            else:
                score[character_id]["main"][num][k] = int(data[index])
            index += 1
    for k in score[character_id]["weight"]:
        if "." in data[index]:
            score[character_id]["weight"][k] = float(data[index])
        else:
            score[character_id]["weight"][k] = int(data[index])
        index += 1


for k, v in score.items():
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
    score[k]["max"] = max_score / 6.0
    if len(str(score[k]["max"])) > 6:
        score[k]["max"] = round(score[k]["max"], 3)


with open("score.json", "w", encoding="utf-8") as f:
    json.dump(score, f, ensure_ascii=False, indent=4)
