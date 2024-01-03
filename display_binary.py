# Rodrigo Ferreira Maceno
# This program asks the user for an integer and converts it to binary.
def display_binary(num):
    binary = ""
    while num > 0:
        binary += str(num % 2)
        num = int(num / 2)
    binary = binary[::-1]
    return binary

def main():
    x = input("Enter a number to convert it to binary. ")

    while not x.strip("-").isnumeric():
        print("You didn't enter a valid integer!")
        x = input("Enter a number to convert it to binary. ")
    if x[0] == "-":
        x = x[1:]
        print("-" + display_binary_num(int(x)))
    else:
        print(display_binary_num(int(x)))

main()
