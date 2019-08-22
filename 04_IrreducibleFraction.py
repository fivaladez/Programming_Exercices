def irreducible_fraction(number=.25):
    """Retruns the lower fraction possible that is equal to the number passed."""
    numerator, denominator = 1, 1
    # Control variable in the loop
    exit = 1
    n = 1.0
    d = 1.0
    # Check if the number is valid
    if number < 1 and number > 0:
        # Look for numerator
        while exit != 0:
            # Look for denominator
            while d < 10000:
                if number == n/d:
                    exit = 0
                    numerator = n
                    denominator = d
                d += 1
            # Clean denominator count to start again
            d = 1
            n += 1

    return numerator, "/", denominator


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        number = float(input("\n\tEnter a number a here: "))
        print(number)
        print("\n\tThe irreducible fraction is: ", irreducible_fraction(number))
        count += 1
