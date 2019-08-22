#!python3
def digit_sum(number=1):
    """Retruns a list with all the digits of a number and the characers +/= to display it as a sum.
    Also, it returns the final sum of all digits of the desired value."""
    sum = 0
    # Control variable, it size determines the digits that can be read from a number
    count = 100000
    sum_list = []
    print ("\n")

    while count > 0:
        # Check that count is lower that the number passed.
        if number / count >= 1:
            # Check for last iteration
            if count < 10:
                sum_list.append(int(number/count))
                sum_list.append("=")
            # Otherwise, add the corresponding number and character "+"
            else:
                sum_list.append(int(number/count))
                sum_list.append("+")
            # Add new result to the sum, and substract the digit read from number
            sum += int(number/count)
            number -= int(number/count) * count
        # Decrease count
        count /= 10

    return sum_list, sum


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        number = int(input("\n\tEnter a number a here: "))
        print("\n\tThe sum of digits is: ", digit_sum(number))
        count += 1
