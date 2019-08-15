def prime_factors(number=1):
    pf_list = []
    prime_factor = 2
    print "\n\t ", number, " = "
    if number == 1:
        print "1"
    while number >= prime_factor:
        if number % prime_factor == 0:
            pf_list.append(prime_factor)
            print "\t\t", prime_factor
            number /= prime_factor
            prime_factor = 2
        else:
            prime_factor += 1
    return pf_list


if __name__ == "__main__":
    cases = input("\n\tEnter a the number of cases here: ")
    count = 0

    while count != cases:
        number = input("\n\tEnter a number a here: ")
        print "\n\tThe prime factors are: ", prime_factors(number)
        count += 1
