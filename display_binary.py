# Rodrigo Ferreira Maceno
# This program asks the user for an integer and converts it to binary.
def display_binary(num):
    binary = ""
    while num > 0:
        binary += str(num % 2)
        num = int(num / 2)
    binary = binary[::-1]
    return binary
