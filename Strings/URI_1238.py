range_value = int(input())

for _ in range(range_value):
    output_list = []
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
                output_list += big_string[i] + small_string[i]
            elif input_string[1] == big_string:
                output_list += small_string[i] + big_string[i]

        output_list += big_string[len(small_string):]
        print("".join(output_list))

    elif len(input_string[0]) == len(input_string[1]):
        for i in range(len(input_string[0])):
            output_list += input_string[0][i] + input_string[1][i]
        print("".join(output_list))