"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.

    :param line: A list if integers of length N to be merged

    :return: A list of merged integers padded at the end to be of length N
    """
    # initialize new line
    newline = [0] * len(line)

    # Our place in line
    i = 0
    # Out place in newline
    j = 0
    # Previously found tile that can be merged
    prev = None

    while i < len(line):
        if line[i] != 0:
            if prev is not None:
                if prev == line[i]:
                    # merge i and prev tile, write to newline
                    newline[j] = prev + line[i]
                    # Increment writing position of newline
                    j += 1
                    # Clear prev tile holder
                    prev = None
                else:
                    # Write old prev tile to newline
                    newline[j] = prev
                    # Increment writing position of newline
                    j += 1
                    # Store current tile for future
                    prev = line[i]
            else:
                prev = line[i]
        # else:
        #     Code not needed, but commented here for clarity.  If line[i] == 0, we move to the next element.
        #     pass
        i += 1

    # Store remaining prev tile
    if prev is not None:
        newline[j] = prev

    return newline

if __name__ == "__main__":
    """
    Sketchy test code for merge
    """
    tests = [
        ([2, 0, 2, 4], [4, 4, 0, 0]),
        ([0, 0, 2, 2], [4, 0, 0, 0]),
        ([2, 2, 0, 0], [4, 0, 0, 0]),
        ([2, 2, 2, 2, 2], [4, 4, 2, 0, 0]),
        ([8, 16, 16, 8], [8, 32, 8, 0]),
    ]

    for test in tests:
        print("Testing: " + str(test[0]) + "=>" + str(test[1]))
        result = merge(test[0])
        print("\tResult: ", result)
        if result == test[1]:
            print("\tPass")
        else:
            print("\tFail")