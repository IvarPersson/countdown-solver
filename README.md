# Countdown solver
This repo provides code to solve the two minigames in the british TV-show Countdown. The same rule set can e used in the comedy version "8 out of 10 cats does Countdown". To get started, run

```bash
python run_game.py -h
```

## Numbers game
The numbers game consists of a player chosing to use 0-4 "high numbers" and the rest "small numbers" into a total of six numbers. The high numbers are drawn from the set [25, 50, 75, 100] and the small numbers are drawn from a set [1, 1, 2, 2, 3, ... , 9, 9, 10, 10], i.e. the numbers 1-10 with two copies of each. The six numbers are used together with the four basic arithmetic operations (+, -, *, /) to get as close to a target, in the range 100-999. You do not have to use all six numbers, each number may only be used once. The best player scores points; the correct answer is awarded ten, up to five away is awarded seven points and up to ten away is awarded five points.

To solve the numbers game, run run_game.py with numbers and target flags

## Word game

The word game is presented as a choice where the contestants can request vowels or consonants one after each other until they hit nine letters. Then the goal is to form the longest word possible using the letters, you may onlt use each letter once.

To solve the word game, run run_game.py with the letters flag.

## Analysis
Do any number combinations lack answers? What numbers are the hardest to find a solution? Analysis to much more will come...