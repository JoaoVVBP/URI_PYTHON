# LANGUAGE	TIME	DATE
# Mine: Python 3.9	0.193	10/23/21, 12:58:51 AM
# Best: Python	0.048	2/9/18, 4:36:36 PM
range_value = int(input())

for _ in range(range_value):
    output_string = ""
    input_string = input().split()

    k = 0
    for i, j in zip(input_string[0], input_string[1]):
        output_string = output_string + i + j
        k += 1
    output_string = output_string + input_string[0][k:] + input_string[1][k:]
    print(output_string)

