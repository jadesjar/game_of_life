# game_of_life

This repo contains the interview data for implementing Conway's Game of Life.

You will be implementing Conway's Game of Life. Your program will take the
path to a json data file as an argument. The data file contains an input state
and output state. Your program will then run Conway's Game of Life for one
step, and compare the output of your implementation against the output state in
the data file.

## Game Rules

Conway's Game of Life is a Cellular Automata. It's a function that operates on
a grid of "living" and "dead" cells (in the case of this repo, 1 is alive, and
0 is dead), and in each step of the function some cells will either live, or
die. 

Your implementation should follow these rules:
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

You can read more here: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


## Data Files

There is a list of json data files in the `data/` folder for you to use to test
your implementation. Each file has an input and output field containing MxN
arrays which represent the input state for your function, and the expected
resulting state of your function.

## life.py

I have provided a starting implementation in python in the file `life.py`, feel
free to use this. It handles the file reading and parsing, provides a stubbed
function `step_game_of_life_state` for you to implement, and checks the
output against the expected output.

You can run this file with the following command if python is in your path:
`$ python3 life.py <path_to_file>`