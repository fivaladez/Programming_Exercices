def panagram(sentence="abc"):


if __name__ == "__main__":
    cases = input("\n\tEnter a the number of cases here: ")
    count = 0

    while count != cases:
        sentence = raw_input("\n\tEnter a the sentence here: ")
        print("\n\tIs the sentence introduce a Pangram? ", panagram(sentence))
        count += 1
