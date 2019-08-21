def watch(seconds=1):
    pass


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        seconds = int(input("\n\tEnter a the seconds to calculate: "))
        print("\n\tThere are {} segments on afer {} seconds".format(watch(seconds), seconds))
        count += 1
