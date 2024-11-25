# Making Change: Coin Change Problem

This project is part of the ALX Specializations and focuses on solving the coin change problem, a classic algorithmic challenge. The goal is to determine the minimum number of coins needed to make up a given amount using a list of coin denominations.

### Concepts
- Greedy Algorithms: Quick solutions with limitations for specific scenarios.
- Dynamic Programming: Optimal substructure and overlapping subproblems.
- Algorithmic Complexity: Focus on runtime and space efficiency.
- Python Skills: List manipulation, efficient looping, and conditional programming.


## Requirements

1. Use editors like `vi`, `vim`, or `emacs`.
2. Compatible with Ubuntu 20.04 LTS and Python 3.4.3.
3. Adhere to PEP 8 style guide (version 1.7.x).
4. Ensure all files end with a new line and start with `#!/usr/bin/python3`.
5. All files must be executable.
6. A `README.md` file is mandatory at the root of the project.


## Task

### 0. Change Comes from Within
- Prototype: `def makeChange(coins, total)`
- Objective:
  - Find the minimum number of coins needed to make up a given `total`.
  - Return `0` if the `total` is `0` or less.
  - Return `-1` if the total cannot be achieved with the available coins.
- Parameters:
  - `coins`: List of integers representing coin denominations.
  - `total`: The amount to be made up.
- Constraints:
  - Infinite number of each coin is available.
  - Coin values are positive integers.
- Runtime Evaluation: Efficiency is a key criterion for this task.
