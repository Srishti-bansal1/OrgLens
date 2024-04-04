def set_msb_to_one(num):
    # Mask to set the two most significant bits to 1
    mask = 0b11000000
    result = num | mask  # Applying the mask using bitwise OR operation
    return result

def print_decimal_and_binary(num):
    print("Decimal:", num)
    print("Binary:", bin(num))

# consider for only 8 bits
number = int(input("Enter a number: "))
print_decimal_and_binary(number)
result = set_msb_to_one(number)
print_decimal_and_binary(result)
