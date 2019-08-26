def words_inverter(sentence="hola mundo"):
    """Prints the words passed in reverse (last to first)"""
    inverted_list = []
    aux_sentence = ""
    count = 0
    while len(sentence) > count:
        while sentence[count].isalpha():
            aux_sentence += sentence[count]
            if len(sentence) == (count + 1):
                break
            else:
                count += 1
        inverted_list.append(aux_sentence)
        aux_sentence = ""

        count += 1

    print(inverted_list[-1:-(len(inverted_list)+1):-1])


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        sentence = input("\n\tWords to be inverted: ")
        print("\n\tCase#", count, " :")
        words_inverter(sentence)
        count += 1
