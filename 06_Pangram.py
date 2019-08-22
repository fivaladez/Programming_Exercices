def panagram(sentence="abc"):
    """Returns a string (Yes/No) to the question: Is those sentence a Panagram?"""
    answer = "No"
    sentence.lower()
    # List to contain the status of each word registered
    alfabet = [False for i in range(100)]
    # Counter to know when a not registered letter is read
    different_letters = 0
    for char in sentence:
        if char <= "z" and char >= "a":
            # Convert character into a numeric value a = 0 - z = 26
            number = ord(char) - 97
            # Check if the character was already seen and increment counter
            if alfabet[number] is False:
                alfabet[number] = True
                different_letters += 1
    # If all the 26 letters from abecedary were read, answer Yes. Otherwise, answer No
    if different_letters == 26:
        answer = "Yes"

    return answer


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        sentence = input("\n\tEnter a the sentence here: ")
        print("\n\tIs the sentence introduce a Pangram? ", panagram(sentence))
        count += 1
