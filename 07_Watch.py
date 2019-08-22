# Variable to contain number of segments that are required to display the number
seven_segments_0 = 6
seven_segments_1 = 2
seven_segments_2 = 5
seven_segments_3 = 5
seven_segments_4 = 4
seven_segments_5 = 5
seven_segments_6 = 6
seven_segments_7 = 4
seven_segments_8 = 7
seven_segments_9 = 6
# List with info about number of segment required added in order 0 - 9
display_7_Segments = [seven_segments_0, seven_segments_1, seven_segments_2, seven_segments_3,
                      seven_segments_4, seven_segments_5, seven_segments_6, seven_segments_7,
                      seven_segments_8, seven_segments_9]

# 1 minute = 60 seconds
# 1 hour = 3600 seconds


def watch(seconds=1):
    """ Retruns the sum of all segments turned on up to get the desired time.
    It starts from 00:00:00 = 32 segments on."""
    # Store digit by digit in the list 01:23:45
    time = [0 for x in range(6)]
    # Control variable
    count = 0
    # Sum of all segments on
    total_segments = 0

    # Get Hours, Minutes and seconds
    if seconds >= 3600:
        time[0] = int((seconds / 3600) / 10)
        time[1] = int((seconds / 3600) % 10)
        seconds %= 3600

    if seconds >= 60:
        time[2] = int((seconds / 60) / 10)
        time[3] = int((seconds / 60) % 10)
        seconds %= 60

    time[4] = int(seconds / 10)
    time[5] = int(seconds % 10)

    # Get number of segments by hour/minute/second
    for digit in time:
        while count <= digit:
            total_segments += display_7_Segments[count]
            count += 1
        count = 0

    return total_segments


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        seconds = int(input("\n\tEnter a the seconds to calculate: "))
        print("\n\tThere are {} segments on afer {} seconds".format(watch(seconds), seconds))
        count += 1
