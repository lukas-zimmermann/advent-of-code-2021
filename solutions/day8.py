from input.day8 import input_signal_patterns


def solve_day8():
    count = count_1478_in_output(input_signal_patterns)
    print('Solution for day 8 puzzle 1:')
    print(f'count: {count}')

    print()

    result = sum_decoded_output(input_signal_patterns)
    print('Solution for day 8 puzzle 2:')
    print(f'decoded sum: {result}')


def count_1478_in_output(patterns):
    count = 0
    for line in patterns:
        line = line.split()
        for i in range(-4, 0):
            if len(line[i]) in [2, 3, 4, 7]:
                count += 1

    return count


def sum_decoded_output(patterns):
    result = 0
    for pattern in patterns:
        result += decode_result(pattern.split())

    return result


def decode_result(pattern):
    pattern = list(map(sort_string, pattern))
    decoded_pattern = decode_pattern(pattern[0:10])

    return (decoded_pattern[pattern[-4]] * 1000 +
            decoded_pattern[pattern[-3]] * 100 +
            decoded_pattern[pattern[-2]] * 10 +
            decoded_pattern[pattern[-1]])


def sort_string(string):
    return "".join(sorted(string))


def decode_pattern(pattern):
    # 1, 4, 7 and 8 are obvious from the amount of segments
    pattern.sort(key=len)
    decoded_pattern = {
        1: pattern[0],
        4: pattern[2],
        7: pattern[1],
        8: pattern[9],
    }

    # 9 is the 6 segment digit that includes 4
    for code in pattern[6:9]:
        if segments_in_pattern(decoded_pattern[4], code):
            decoded_pattern[9] = code
            break

    # 6 is the 6 segment digit that doesn't include 1
    for code in pattern[6:9]:
        if not segments_in_pattern(decoded_pattern[1], code):
            decoded_pattern[6] = code
            break

    # 0 is the 6 segment digit that' left
    for code in pattern[6:9]:
        if code not in decoded_pattern.values():
            decoded_pattern[0] = code
            break

    # 3 is the 5 segment digit that includes 1
    for code in pattern[3:6]:
        if segments_in_pattern(decoded_pattern[1], code):
            decoded_pattern[3] = code
            break

    # 5 is the 5 segment digit that's included in 6
    for code in pattern[3:6]:
        if segments_in_pattern(code, decoded_pattern[6]):
            decoded_pattern[5] = code
            break

    # 2 is the 5 segment digit that's left
    for code in pattern[3:6]:
        if code not in decoded_pattern.values():
            decoded_pattern[2] = code
            break

    return {
        decoded_pattern[0]: 0,
        decoded_pattern[1]: 1,
        decoded_pattern[2]: 2,
        decoded_pattern[3]: 3,
        decoded_pattern[4]: 4,
        decoded_pattern[5]: 5,
        decoded_pattern[6]: 6,
        decoded_pattern[7]: 7,
        decoded_pattern[8]: 8,
        decoded_pattern[9]: 9,
    }


def segments_in_pattern(segments, pattern):
    for char in segments:
        if char not in pattern:
            return False

    return True
