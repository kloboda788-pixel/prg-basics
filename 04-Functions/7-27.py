# Returns True if the 4th digit is the remainder of dividing
# the sum of the first 3 digits by 7
def f(product_code):
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])
    return digits_sum % 7 == control_digit

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))