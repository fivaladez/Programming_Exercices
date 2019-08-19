#!python3
def digit_sum(number=1):
    sum = 0
    count = 100000
    sum_list = []
    print ("\n")

    while count > 0:
        if number / count >= 1:
            if count < 10:
                sum_list.append(int(number/count))
                sum_list.append("=")
            else:
                sum_list.append(int(number/count))
                sum_list.append("+")
            sum += int(number/count)
            number -= int(number/count) * count

        count /= 10

    return sum_list, sum


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        number = int(input("\n\tEnter a number a here: "))
        print("\n\tThe sum of digits is: ", digit_sum(number))
        count += 1
