# whelper
Wordle helper

This is a simple Python program to filter possible Wordle words based on known letter information from previous guesses.

Usage

Run the script from the command line, passing letter information as arguments. Each argument should be formatted as:

POSITION_TYPE_LETTER

POSITION - The zero-based position of the letter in the word.

TYPE - The classification of the letter:

g for green (correct letter in the correct position)

y for yellow (correct letter in the wrong position)

b for black (incorrect letter)

LETTER - The actual letter being classified.

Example

If your Wordle guess was TEARY and the feedback was:

T is green in position 0

E is black in position 1

A is green in position 2

R is yellow in position 3

Y is black in position 4

Run the script as follows:

python3 searchlist.py 0gT 1bE 2gA 3yR 4bY

The program will output a list of possible words that match the given conditions.

Requirements

Python 3.x

A word list file named wordlelist in the same directory as searchlist.py

Notes

The word list should contain valid five-letter words, one per line.

Black letters are ignored if they previously appeared as green in another position.

This tool helps narrow down possible Wordle solutions based on feedback from previous guesses. Happy solving!
