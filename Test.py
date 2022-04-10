def oct_to_bin(octal):
    sum = 0
    for index, char in enumerate(octal):
        sum = sum + (int(char) * 8**index)
    return bin(sum)



print(oct_to_bin("1000"))