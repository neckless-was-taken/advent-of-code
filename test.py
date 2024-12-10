# Set the length of the base-3 number
num_digits = 3

# Iterate through all base-3 numbers of the specified length
for i in range(3**num_digits):
    # Convert the number to a base-3 string with leading zeros
    base3_num = ''
    num = i
    for _ in range(num_digits):
        base3_num = str(num % 3) + base3_num  # Extract the least significant base-3 digit
        num //= 3  # Shift the number to the right in base-3
    
    print(f"Base-3 number: {base3_num}")
    
    # Iterate through each digit in the base-3 number
    # for digit in base3_num:
    #     if digit == '0':
    #         print("Found a 0!")
    #         # Perform some action for 0
    #     elif digit == '1':
    #         print("Found a 1!")
    #         # Perform some action for 1
    #     elif digit == '2':
    #         print("Found a 2!")
    #         # Perform some action for 2
    # print('-' * 20)  # Separator for better readability


