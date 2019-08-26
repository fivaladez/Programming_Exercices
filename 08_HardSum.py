def hard_sum(sum_sentence="1 2 3"):
    """Returns the sum of all numbers introduced in the standar input (string) format.
    The numbers can be negative and positive, they have to be separated by a space."""
    result = 0
    count = 0
    while len(sum_sentence) > count:
        # Check for a negative number and make sure it is not at the end of the sentence
        if sum_sentence[count] == "-" and len(sum_sentence) != count + 1:
            aux_result = ""
            # Check that the inmediate next character is a number
            while sum_sentence[count+1].isdigit():
                # Add the digit as a string into another componed string
                aux_result += sum_sentence[count+1]
                # When the string is close to finish, exit of the loop
                if len(sum_sentence) == count + 2:
                    count += 1
                    break
                # Keep in the loop
                else:
                    count += 1
            # It checks for the end of the number introduced and substract it from the result
            if sum_sentence[count].isdigit():
                result = result - int(aux_result)

        elif sum_sentence[count].isdigit():
            aux_result = ""
            while sum_sentence[count].isdigit():
                aux_result += sum_sentence[count]
                if len(sum_sentence) == count + 1:
                    count += 1
                    break
                else:
                    count += 1
            result = result + int(aux_result)

        count += 1

    return result


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        sum_sentence = input("\n\tEnter a the numbers to calculate: ")
        print("\n\tThe sum of {} is equal to {}".format(sum_sentence, hard_sum(sum_sentence)))
        count += 1
