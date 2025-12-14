# Bolt's Journal

## 2024-05-22 - Initial Exploration
**Learning:** The `ProjectOZ` codebase seems to be a skeleton or an instructional kernel where most implementation files in `BasicOZ` are empty or just include headers. The real implementation might be in `SPACE` or it is expected to be filled in. `WRK-V1.2` contains the Windows Research Kernel, which is a massive and complex codebase.
**Action:** Focus exploration on `ProjectOZ/SPACE` for a manageable C codebase, or dive into specific parts of `WRK-V1.2` like `RTL` (Runtime Library) or `EX` (Executive) for potential algorithmic improvements.

## 2024-05-22 - Hashing Strategy
**Learning:** Simple modulo hashing `(val % size)` is perfect for sequential keys (0 collisions) and "coprime strides" (like 512 % 511 = 1, which acts as stride 1). However, it fails catastrophically for "resonant strides" (Stride = k * Size), resulting in 100% collisions.
Mixing functions like `XOR` shifts (`val ^ (val >> k)`) fix the resonant stride case but degrade the sequential case (introducing small collisions) and degrade "coprime strides" significantly (e.g., Stride 512 on 511 with XOR3 gives 296 collisions vs 0 for Old).
**Action:** Since `mastertoken` and `nextportalid` are sequential counters, and `NTThreadHash` (handles) are likely aligned but essentially sequential (or stride 8), the **Old Modulo Hash is actually optimal for the most common cases** in this specific codebase. Changing it to a generic "better" hash (like Knuth or XOR-Shift) actually hurts performance for the primary use cases here.
**Correction:** I should look for a different optimization. Modulo is fast and correct for these counters. Maybe `NTThreadHash` collision on 4-byte aligned handles is the real issue (stride 4 vs `HANDLEVALUE` >> 3).
