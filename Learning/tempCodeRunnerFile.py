
filename = '1.txt'
def count_file_stats(filename):
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)
    return num_lines, num_words, num_chars
num_lines, num_words, num_chars = count_file_stats(filename)