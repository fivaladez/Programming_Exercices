def prime_factors(number=1):
    """Returns a list with all the prime factors from the number passed."""
    pf_list = []
    prime_factor = 2
    print ("\n\t ", number, " = ")
    # Check first known prime factor from 1
    if number == 1:
        print ("\t\t 1")
    # Look for all prime factors from number
    while number >= prime_factor:
        # Check for divisible numbers
        if number % prime_factor == 0:
            pf_list.append(prime_factor)
            print ("\t\t", prime_factor)
            number /= prime_factor
            # Restart prime_factor value
            prime_factor = 2
        else:
            prime_factor += 1

    return pf_list


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        number = int(input("\n\tEnter a number a here: "))
        print("\n\tThe prime factors are: ", prime_factors(number))
        count += 1
