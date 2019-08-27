def words_inverter(sentence="hola mundo"):
    """Prints the words passed in reverse (last to first)"""
    inverted_list = []
    aux_sentence = ""
    count = 0
    # Loop, to keep tracking the position in the array(sentence)
    while len(sentence) > count:
        # Check for a letter and keep there until find a non-alphanumeric character
        while sentence[count].isalpha():
            # Add letter by letter to a string
            aux_sentence += sentence[count]
            # To avoid exeed the size of the array
            if len(sentence) == (count + 1):
                break
            else:
                count += 1
        # Add the word learnt into a list
        inverted_list.append(aux_sentence)
        # Clean the variable to store the word
        aux_sentence = ""
        # Continue to the next position
        count += 1
    # Print in reverse the list learnt
    # [Begining position:End position:Increment of count]
    print(inverted_list[-1:-(len(inverted_list)+1):-1])


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        sentence = input("\n\tWords to be inverted: ")
        print("\n\tCase#", count, " :")
        words_inverter(sentence)
        count += 1
