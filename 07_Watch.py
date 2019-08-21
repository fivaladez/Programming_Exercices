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

display_7_Segments = [seven_segments_0, seven_segments_1, seven_segments_2, seven_segments_3,
                      seven_segments_4, seven_segments_5, seven_segments_6, seven_segments_7,
                      seven_segments_8, seven_segments_9]

# 1 minute = 60 seconds
# 1 hour = 3600 seconds


def watch(seconds=1):
    hours_first = 0
    hours_second = 0
    minutes_first = 0
    minutes_second = 0
    seconds_first = 0
    seconds_second = 0

    count = 0
    segment_count = 0

    # Get Hours, Minutes and seconds
    if seconds >= 3600:
        hours_first = int((seconds / 3600) / 10)
        hours_second = int((seconds / 3600) % 10)
        seconds %= 3600

    if seconds >= 60:
        minutes_first = int((seconds / 60) / 10)
        minutes_second = int((seconds / 60) % 10)
        seconds %= 60

    seconds_first = int(seconds / 10)
    seconds_second = int(seconds % 10)
    # Get number of segments by hour/minute/second
    while count <= hours_first:
        segment_count += display_7_Segments[count]
        count += 1
    count = 0
    while count <= hours_second:
        segment_count += display_7_Segments[count]
        count += 1
    count = 0
    while count <= minutes_first:
        segment_count += display_7_Segments[count]
        count += 1
    count = 0
    while count <= minutes_second:
        segment_count += display_7_Segments[count]
        count += 1
    count = 0
    while count <= seconds_first:
        segment_count += display_7_Segments[count]
        count += 1
    count = 0
    while count <= seconds_second:
        segment_count += display_7_Segments[count]
        count += 1
    count = 0

    return segment_count


if __name__ == "__main__":
    cases = int(input("\n\tEnter a the number of cases here: "))
    count = 0

    while count != cases:
        seconds = int(input("\n\tEnter a the seconds to calculate: "))
        print("\n\tThere are {} segments on afer {} seconds".format(watch(seconds), seconds))
        count += 1
