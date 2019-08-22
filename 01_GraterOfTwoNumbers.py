def greater_number(number_1=0, number_2=0):
    """Returns the bigger number from two numbers passed"""
    bigger_number = 0

    if number_1 > number_2:
        bigger_number = number_1
    else:
        bigger_number = number_2

    return bigger_number


if __name__ == "__main__":
    first_number = float(input("\n\tEnter a number a here: "))
    second_number = float(input("\n\tEnter a number a here: "))

    print("\n\tThe greater number is: ", greater_number(first_number, second_number))
