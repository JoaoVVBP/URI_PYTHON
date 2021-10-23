# LANGUAGE	TIME	DATE
# Mine: Python 3	0.216	10/22/21, 11:53:16 PM
# Best: Python	0.048	2/9/18, 4:36:36 PM
range_value = int(input())

range_value = int(input())

for _ in range(range_value):
    output_string = ""
    input_string = input().split()
    big_string = ""
    small_string = ""

    if len(input_string[0]) != len(input_string[1]):
        if len(input_string[0]) > len(input_string[1]):
            big_string = input_string[0]
            small_string = input_string[1]

        elif len(input_string[0]) < len(input_string[1]):
            big_string = input_string[1]
            small_string = input_string[0]

        for i in range(len(small_string)):
            if input_string[0] == big_string:
                output_string += big_string[i] + small_string[i]
            elif input_string[1] == big_string:
                output_string += small_string[i] + big_string[i]

        output_string += big_string[len(small_string):]
        print(output_string)

    else:
        for i in range(len(input_string[0])):
            output_string += input_string[0][i] + input_string[1][i]
        print(output_string)