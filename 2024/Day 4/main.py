def part1(test: bool = False):
    print("-" * 15, "\nPart 1", "Test", test)
    input_file = "input1.txt"
    if test:
        with open("test_" + input_file) as f:
            input = f.read()
    else:
        with open(input_file) as f:
            input = f.read()

    word = "XMAS"
    horizontal = ""
    vertical = ""
    diagonal_r = ""
    diagonal_l = ""
    h = 0
    v = 0
    dl = 0
    dr = 0
    lines = input.split("\n")
    for l_idx, line in enumerate(lines):
        for char_idx, _ in enumerate(line):
            for wrd_idx, _ in enumerate(word):
                try:
                    if len(line) - char_idx >= len(word):
                        horizontal += line[char_idx + wrd_idx]
                except IndexError:
                    pass

                try:
                    if len(lines) - l_idx >= len(word):
                        vertical += lines[l_idx + wrd_idx][char_idx]
                except IndexError:
                    pass

                try:
                    if len(lines) - l_idx >= len(word) and len(line) - char_idx >= len(
                        word
                    ):
                        diagonal_r += lines[l_idx + wrd_idx][char_idx + wrd_idx]
                except IndexError:
                    pass

                try:
                    if len(lines) - l_idx >= len(word) and char_idx >= len(word) - 1:
                        diagonal_l += lines[l_idx + wrd_idx][char_idx - wrd_idx]
                except IndexError:
                    pass

            if horizontal == word or horizontal == word[::-1]:
                h += 1
            if vertical == word or vertical == word[::-1]:
                v += 1
            if diagonal_r == word or diagonal_r == word[::-1]:
                dr += 1
            if diagonal_l == word or diagonal_l == word[::-1]:
                dl += 1

            horizontal = ""
            vertical = ""
            diagonal_r = ""
            diagonal_l = ""

    # print("Total XMAS: %s" % count)
    print("h: %s\nv: %s\ndl: %s\ndr: %s\nTotal: %s" % (h, v, dl, dr, (h + v + dl + dr)))


def part2(test: bool = False):
    print("-" * 15, "\nPart 2")
    input_file = "input1.txt"
    if test:
        with open("test_" + input_file) as f:
            lines = f.readlines()
    else:
        with open(input_file) as f:
            lines = f.readlines()

    count = 0
    for l_idx, line in enumerate(lines):
        line = line.replace("\n", "")
        for char_idx, _ in enumerate(line):
            if len(line) - char_idx < 3 or len(lines) - l_idx < 3:
                break

            d_r = (
                line[char_idx]
                + lines[l_idx + 1][char_idx + 1]
                + lines[l_idx + 2][char_idx + 2]
            )
            if d_r == "MAS" or d_r == "SAM":
                d_l = (
                    line[char_idx + 2]
                    + lines[l_idx + 1][char_idx + 1]
                    + lines[l_idx + 2][char_idx]
                )
                if d_l == "MAS" or d_l == "SAM":
                    count += 1

    print("Total XMAS: %s" % count)


if __name__ == "__main__":
    part1(False)
    part2(False)
