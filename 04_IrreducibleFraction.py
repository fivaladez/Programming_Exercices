def greater_number(number_1=0, number_2=0):
    if number_1 > number_2:
        return number_1
    else:
        return number_2


def irreducible_fraction(number=.25):
    numerator = 1
    denominator = 1
    exit = 1
    n = 1.0
    d = 1.0

    if number < 1 and number > 0:

        while exit != 0:
            while d < 10000:
                if number == n/d:
                    exit = 0
                    numerator = n
                    denominator = d
                d += 1
            d = 1
            n += 1

    return numerator, "/", denominator


if __name__ == "__main__":
    cases = input("\n\tEnter a the number of cases here: ")
    count = 0

    while count != cases:
        number = input("\n\tEnter a number a here: ")
        print number
        print "\n\tThe irreducible fraction is: ", irreducible_fraction(number)
        count += 1
