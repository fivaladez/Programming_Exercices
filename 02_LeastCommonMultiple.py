def greater_number(number_1=0, number_2=0):
    """Returns the bigger number from two numbers passed"""
    bigger_number = 0

    if number_1 > number_2:
        bigger_number = number_1
    else:
        bigger_number = number_2

    return bigger_number


def least_common_multiple(number_1=0, number_2=0):
    """Returns the least common multiple number"""
    # Get bigger number to start count from there
    lcm = greater_number(number_1, number_2)
    # Increment lcm up to make it divisible by both numbers and without remainder
    while lcm % number_1 != 0 or lcm % number_2 != 0:
        lcm += 1

    return lcm


if __name__ == "__main__":
    # For Python 3, function input returns a String, no matter if you enter a numeric value
    first_number = int(input("\n\tEnter a number a here: "))
    second_number = int(input("\n\tEnter a number a here: "))

    print("\n\tThe least common multiple is: ", least_common_multiple(first_number, second_number))
