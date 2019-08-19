def greater_number(number_1=0, number_2=0):
    if number_1 > number_2:
        return number_1
    else:
        return number_2


def least_common_multiple(number_1=0, number_2=0):
    lcm = greater_number(number_1, number_2)

    while lcm % number_1 != 0 or lcm % number_2 != 0:
        lcm += 1

    return lcm


if __name__ == "__main__":
    first_number = input("\n\tEnter a number a here: ")
    second_number = input("\n\tEnter a number a here: ")

    print("\n\tThe least common multiple is: ", least_common_multiple(first_number, second_number))
