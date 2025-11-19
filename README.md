# StarRailScore

_SRS_ scoring criteria for Honkai: Star Rail.

[English](README.md) | [中文](docs/README_zh-CN.md)

The project is still in development.

## Introduction

_SRS_ judges the number of effective affixes of the relic according to the typical positioning of the role, and calculates the score of the relic according to the weight of different affixes. _SRS_ provides the theoretical highest score to calculate the normalized final score. The main affix and sub affixes each account for 50% of the score.

## Calculation

### Main affix and sub affixes

The normalized score of the main affix is calculated by the level and weight, and the level 0 to 15 correspond to the base value 1/16 to 16/16 respectively. The weight is obtained by looking up the table, and the `main` field is the weight of the main affixes. For example: the weight of the main affixes at level 12 is 0.9, and the normalized score is (12+1)/16 \* 0.9 = 0.61.

The normalized score of the sub affixes is calculated by the count of each affix and the weight. The `weight` field is the weight of the sub affixes.

The `maxV2` field records the theoretical highest score (normalization denominator) for each specific part. The calculation logic differs by part to reflect difficulty and game mechanics:

1.  **Head (HEAD) / Hands (HAND)**:
    *   **Difficulty**: Low (Fixed main affix).
    *   **Model**: Assumes a 4-sub-affix initial relic, totaling 9 counts (4 initial + 5 enhancements).
    *   **Distribution**: Limit distribution `(6, 1, 1, 1)`.

2.  **Body (BODY) / Feet (FOOT) / Sphere (NECK) / Rope (OBJECT)**:
    *   **Difficulty**: High (Random main affix).
    *   **Model**: Assumes a 3-sub-affix initial relic, totaling 8 counts (3 initial + 4 enhancements + 1 fill).
    *   **Distribution**: Limit distribution `(5, 1, 1, 1)`.
    *   **Exclusion**: Automatically excludes sub-affixes that conflict with the optimal main affix for that part (e.g., Crit Rate Body cannot have Crit Rate sub-affix).

For example: sub affix 1 has 5 counts and 1 weight; sub affix 2 has 2 counts and 0.8 weight; sub affix 3 has 1 count and 0.5 weight; sub affix 4 has 1 count and 0.3 weight, and the original score is 5 \* 1 + 2 \* 0.8 + 1 \* 0.5 + 1 \* 0.3 = 7.4. If the `maxV2` field for this part is 9.0, then the normalized score is 7.4/9.0 = 0.82.

### Data Structure Compatibility

The `score.json` file contains two max fields for backward compatibility:

*   **`maxV2`** (object): Per-part theoretical maximum scores using the new algorithm with difficulty-adjusted counts. Use this field for accurate per-part normalization. Structure: `{"1": float, "2": float, "3": float, "4": float, "5": float, "6": float}`.
*   **`max`** (float): Legacy field, calculated using the old algorithm (all parts use 6-count distribution, then averaged). Maintained for backward compatibility with older implementations that expect a single `max` value.

**Recommendation**: New implementations should use `maxV2` for per-part scoring, as it provides more accurate normalization and better reflects the actual difficulty of obtaining perfect relics for different parts.

### _SRS-N_

_SRS-N_ uses the same weight to combine the scores of the main affix and the sub affixes. According to the example in the previous section, the total score is 0.61 \* 0.5 + 0.82 \* 0.5 = 0.72, which can be expressed as `0.72` `72%` `7.2/10`.

### _SRS-M_

_SRS-M_ takes the square root of the result of _SRS-N_, which has the characteristic that the improvement speed gradually slows down as the score increases. For example, if the result of _SRS-N_ is 0.72, then the result of _SRS-M_ is 0.72^0.5 = 0.85, which can be expressed as `0.85` `85%` `8.5/10`.
