# ass1_8cc00
# Interval Similarity Calculation

This program calculates the similarity metric between two sets of interval lists. It determines the degree of overlap between intervals in the two sets and computes a similarity score based on the overlapping intervals.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/interval-similarity.git`
2. Navigate to the project directory: `cd interval-similarity`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To calculate the similarity between two interval sets, follow these steps:

1. Prepare two files, each containing interval lists. Each line in the file represents one interval, and each interval is represented as a tuple of two numbers (start, end).
2. Update the `set_1` and `set_2` variables in the `similarity` function call in the `main.py` file to point to the respective interval list files.
3. Run the program: `python main.py`
4. The program will calculate the similarity metric and store it in the specified output file.

## File Structure

- `main.py`: The main script that calculates the similarity metric.
- `utils.py`: Contains utility functions for reading files, checking interval overlap, and performing calculations.
- `README.md`: This file providing information about the program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## Acknowledgments

- This program was inspired by the need to compare interval data sets in various research fields.
- Thanks to the developers of the Python programming language and the open-source libraries used in this project.
