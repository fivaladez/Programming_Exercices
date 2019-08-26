def hard_sum(sum_sentence="1 2 3"):
    """Returns the sum of all numbers introduced in the standar input (string) format"""
    result = 0
    count = 0
    while len(sum_sentence) > count:

        if sum_sentence[count] == "-" and len(sum_sentence) != count + 1:
            aux_result = ""
            while sum_sentence[count+1].isdigit():
                aux_result += sum_sentence[count+1]
                if len(sum_sentence) == count + 2:
                    count += 1
                    break
                else:
                    count += 1
            # print("-" + aux_result)
            if sum_sentence[count].isdigit():
                result = result - int(aux_result)
            # else:
            #     print("Error")

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
            # print(aux_result)

        count += 1

    return result


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        sum_sentence = input("\n\tEnter a the numbers to calculate: ")
        print("\n\tThe sum of {} is equal to {}".format(sum_sentence, hard_sum(sum_sentence)))
        count += 1
