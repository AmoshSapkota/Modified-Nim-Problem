
## Overview

This repository contains the implementation of the red-blue nim game. The game involves a modified version of nim where a computer and a human player take turns to remove marbles from two piles (red and blue).

## Description

Your task is to build an agent to play a modified version of nim (called red-blue nim) against a human player. The game consists of two piles of marbles (red and blue). On each player's turn, they pick a pile and remove one marble from it. If, on their turn, either pile is empty, they win. The amount they win is dependent on the number of marbles left (2 for every red marble and 3 for every blue marble).

## Objectives

- **Implement the red-blue nim game.**
- **Use MinMax with Alpha Beta Pruning** to determine the best move for the computer.
- **Prompt the human player for their move.**
- **Alternate turns between the computer and human** until the game ends.
- **Calculate and display the final score and winner.**

## Command Line Invocation

red_blue_nim.py <num-red> <num-blue> <first-player> <depth>

- `<num-red>`: Number of red marbles.
- `<num-blue>`: Number of blue marbles.
- `<first-player>`: `computer` or `human` (default: `computer`).
- `<depth>`: Depth for depth-limited search (optional for extra credit).

## Example Usage

red_blue_nim.py 5 7 computer


