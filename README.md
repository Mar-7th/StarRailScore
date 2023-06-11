# StarRailScore

_SRS_ scoring criteria for Honkai: Star Rail.

崩坏：星穹铁道 _SRS_ 遗器评分标准。

The project is still in development.

该项目仍在开发中。

## Introduction

_SRS_ judges the number of effective affixes of the relic according to the typical positioning of the character, and calculates the score of the relic according to the weight of different affixes. _SRS_ provides a theoretical maximum score to calculate a normalized final score so that the distance from the upper limit can be easily seen. For relics with a non-fixed main affixes, use the main affixes rank and weight as 50% of the score; for relics with a fixed main affixes, the sub affixes score accounts for 100%.

_SRS_ 根据角色的典型定位判断遗器的有效词条数，根据不同词条的权重计算遗器分数。_SRS_ 提供理论最高分以计算归一化的最终得分，这样可以很容易看到与上限的差距。对于主词条非固定的遗器，使用主词条等级和权重作为 50% 的分数；对于主词条固定的遗器，副词条分数占比 100%。

For example, a relic has 5.3 weighted valid affixes, and if the highest relic score is 10.8, the final score is 5.3/10.8=0.49. If the main affix is not fixed, the coefficient is 0.9, and the grade is 12, the final score is ((12+1)/16) \* 0.9 \* 0.5 + 0.49 \* 0.5 = 0.61. Can be expressed as 61%, 6.1/10, etc.

例如，一个遗器有 5.3 个加权有效副词条，如果最高遗器分数为 10.8，最终得分为 5.3/10.8=0.49。如果主词条非固定，系数为 0.9，等级为 12，则最终分数为 ((12+1)/16) \* 0.9 \* 0.5 + 0.49 \* 0.5 = 0.61。可以表示为 61%，6.1/10 等。
