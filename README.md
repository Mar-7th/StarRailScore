# StarRailScore

_SRS_ scoring criteria for Honkai: Star Rail.

崩坏：星穹铁道 _SRS_ 遗器评分标准。

The project is still in development.

该项目仍在开发中。

## Introduction

_SRS_ judges the number of effective affixes of the relic according to the typical positioning of the role, and calculates the score of the relic according to the weight of different affixes. _SRS_ provides the theoretical highest score to calculate the normalized final score. The main affix and sub affixes each account for 50% of the score.

_SRS_ 根据角色的典型定位判断遗器的有效词条数，根据不同词条的权重计算遗器分数。_SRS_ 提供理论最高分以计算归一化的最终得分。主词条和副词条各占 50% 的分数。

## Calculation

### Main affix and sub affixes

The normalized score of the main affix is calculated by the level and weight, and the level 0 to 15 correspond to the base value 1/16 to 16/16 respectively. The weight is obtained by looking up the table, and the `main` field is the weight of the main affixes. For example: the weight of the main affixes at level 12 is 0.9, and the normalized score is (12+1)/16 \* 0.9 = 0.61.

主词条归一化得分通过等级与权重计算，0 级到 15 级分别对应基础值 1/16 到 16/16，权重通过查表得到，`main` 字段中为各个部位主词条的权重。例如：12 级的主词条权重为 0.9，归一化得分为 (12+1)/16 \* 0.9 = 0.61。

The normalized score of the sub affixes is calculated by the number of base values, the number of boost values (x 0.1), and the weight. The `weight` field is the weight of the sub affixes. For example: sub affixes 1 has 3 base values, 2 boost values, and 1 weight; sub affixes 2 has 1 base value, 0.5 weight, and the original score is 3.2 \* 1 + 1.0 \* 0.5 = 3.7. If the `max` field is 8.0, then the normalized score is 3.7/8.0 = 0.46.

副词条归一化得分由各个词条的基础值次数、提升值次数（乘以 0.1）、权重计算得到，`weight` 字段中为各个部位副词条的权重。例如：副词条 1 为 3 个基础值、2 个提升值、1 权重；副词条 2 为 1 个基础值、0.5 权重，原始得分为 3.2 \* 1 + 1.0 \* 0.5 = 3.7。如果 `max` 字段为 8.0，那么归一化得分为 3.7/8.0 = 0.46。

### _SRS-N_

_SRS-N_ uses the same weight to combine the scores of the main affix and the sub affixes. According to the example in the previous section, the total score is 0.61 \* 0.5 + 0.46 \* 0.5 = 0.54, which can be expressed as `0.54` `54%` `5.4/10`.

_SRS-N_ 使用相同的权重合并主词条和副词条的得分，按照上一节的示例 ，总得分为 0.61 \* 0.5 + 0.46 \* 0.5 = 0.54，可表示为 `0.54` `54%` `5.4/10`。

### _SRS-M_

_SRS-M_ takes the square root of the result of _SRS-N_, which has the characteristic that the improvement speed gradually slows down as the score increases. For example, if the result of _SRS-N_ is 0.54, then the result of _SRS-M_ is 0.54^0.5 = 0.73, which can be expressed as `0.73` `73%` `7.3/10`.

_SRS-M_ 将 _SRS-N_ 的结果开平方根，该结果的特点是随着得分的提高，提升速度逐渐变慢。例如 _SRS-N_ 的结果为 0.54，那么 _SRS-M_ 的结果为 0.54^0.5 = 0.73，可表示为 `0.73` `73%` `7.3/10`。
