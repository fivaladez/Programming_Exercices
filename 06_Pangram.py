def panagram(sentence="abc"):
    answer = "No"
    sentence.lower()
    alfabet = [False for i in range(100)]
    different_letters = 0
    for char in sentence:
        if char <= "z" and char >= "a":
            number = ord(char) - 97
            # print char
            if alfabet[number] is False:
                alfabet[number] = True
                different_letters += 1
    if different_letters == 26:
        answer = "Yes"
    return answer


if __name__ == "__main__":
    cases = input("\n\tEnter a the number of cases here: ")
    count = 0

    while count != cases:
        sentence = raw_input("\n\tEnter a the sentence here: ")
        print "\n\tIs the sentence introduce a Pangram? ", panagram(sentence)
        count += 1
