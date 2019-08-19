def greater_number(number_1=0, number_2=0):
    if number_1 > number_2:
        return number_1
    else:
        return number_2


if __name__ == "__main__":
    first_number = input("\n\tEnter a number a here: ")
    second_number = input("\n\tEnter a number a here: ")

    print("\n\tThe greater number is: ", greater_number(first_number, second_number))
