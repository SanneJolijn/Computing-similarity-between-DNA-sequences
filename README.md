# Advanced programming 8CC00 - Assignment 1
# Computing similarity between DNA sequences

Using advanced programming to elaborate complex DNA data to extract usefull information, this program calculates the DNA similarity using two sets of interval lists. It determines the degree of overlap between intervals in the two sets and computes a similarity score based on the overlapping intervals. 

The biggest challenges I faced during the construction of this code were extracting the data from the .txt files in a usefull way and correctly rounding the final metric.

In the future I hope to implement the possibility to give two input files of different length and a more clean way to round the final metric.

## Installation

1. Clone the repository: `git clone https://github.com/SanneJolijn/ass1_8cc00.git`
2. Navigate to the project directory: `cd ass1_8cc00`

## Usage

To calculate the similarity metric between two sets of interval lists, follow these steps:

1. Check your two .txt input files for the similarity function. Each file should contain the same amount of lines. Each list is in a separate line, with the intervals given as pairs of numbers enclosed in square brackets and separated by a comma [start, end].


2. Run the program by using a command in the format below, be sure to update the `set_1`, `set_2` and `outfile` variables in the `similarity` function call to point to the correct interval list files and the correct output file.

from main import similarity\
similarity(set_1='set1_name.txt', set_2='set2_name.txt', outfile='similarity.txt')


3. The program will calculate the similarity metric, round it to two decimals and store it in the specified output file.

## File Structure

- `main.py`: The main script that calculates the similarity metric.
- `utils.py`: Contains utility functions for reading the files and checking interval overlap.
- `README.md`: This file provides information about the program.

## Acknowledgments

- This program was inspired by the assignment created by Dr. Dragan Bosnacki.
- The following page was used in finding a fix for the rounding problem https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
- Thanks to the developers of the Python programming language and the open-source libraries used in this project.
