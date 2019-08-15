def greater_number(number_1=0, number_2=0):
    if number_1 > number_2:
        return number_1
    else:
        return number_2


def prime_factors(number=1):
    pf_list = []
    print "\n\t ", number, " = "


if __name__ == "__main__":
    cases = input("\n\tEnter a the number of cases here: ")
    count = 0

    while count != cases:
        number = input("\n\tEnter a number a here: ")
        print "\n\tThe prime factors are: ", prime_factors(number)
        count += 1
