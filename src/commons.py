
RES_PATH = "C:\\Projects\\AdventOfCode2021\\res\\"
INPUT = "input"
EXAMPLE = "example"
TXT = ".txt"

def get_file(num):
	file_path = RES_PATH + INPUT + num + TXT
	return open(file_path, "r")

def get_example(num):
	file_path = RES_PATH + EXAMPLE + num + TXT
	return open(file_path, "r")

