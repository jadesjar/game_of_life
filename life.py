import argparse
import json


def step_game_of_life_state(input):
	# TODO: Your implementation here
	return input


def parse_data_file(file_name):
	f = open(file_name)

	return json.load(f)


class GameState:

	def __init__(self, data):
		self.data = data

	def row_str(self, row):
		return "".join("X" if c == 1 else "0" for c in row)

	def __str__(self):
		return "\n".join(self.row_str(r) for r in self.data)

	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return false

		return self.data == other.data


if __name__ == "__main__":
	# parse json data file
	parser = argparse.ArgumentParser()
	parser.add_argument("file")
	args = parser.parse_args()
	data = parse_data_file(args.file)

	input_state = GameState(data["input"])
	expected_output_state = GameState(data["output"])

	print(f"Input State:\n{input_state}")

	output_state = step_game_of_life_state(input_state)

	print(f"Output State:\n{output_state}")

	print(f"Expected Output State:\n{expected_output_state}\n")

	print("Pass" if output_state == expected_output_state else "Fail")