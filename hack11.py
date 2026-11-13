'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
'''
def split_and_join(line):
    new1 = line.split(" ")
    new2 = "-".join(new1)
    return new2
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
