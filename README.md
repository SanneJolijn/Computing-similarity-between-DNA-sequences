# Advanced programming 8CC00 - Assignment 1
# Computing similarity between DNA sequences

Using advanced programming to elaborate complex DNA data to extract usefull information, this program calculates the similarity metric between two sets of interval lists. It determines the degree of overlap between intervals in the two sets and computes a similarity score based on the overlapping intervals. 

We used the technologies we used

Some of the challenges you faced and features you hope to implement in the future.

## Installation

1. Clone the repository: `git clone https://github.com/SanneJolijn/ass1_8cc00.git`
2. Navigate to the project directory: `cd ass1_8cc00`

## Usage

To calculate the similarity metric between two sets of interval lists, follow these steps:

1. Check your two files. Each file should contain lists of intervals. Each line in the file represents a list of intervals, and each interval is represented as a list of two numbers [start, end]
2. Update the `set_1` and `set_2` variables in the `similarity` function call in the `main.py` file to point to the correct interval list files.
3. Run the program: `python main.py`
4. The program will calculate the similarity metric and store it in the specified output file.

## File Structure

- `main.py`: The main script that calculates the similarity metric.
- `utils.py`: Contains utility functions for reading files and checking interval overlap.
- `README.md`: This file provides information about the program.

## Acknowledgments

- This program was inspired by the need to compare interval data sets in various research fields.
- Thanks to the developers of the Python programming language and the open-source libraries used in this project.
