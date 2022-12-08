import string
import os

#string.ascii_lowercase


def main():
    letters = organize_rugsacks()
    total_priority = convert_to_priority(letters=letters)
    print(f"The total priority value is: {sum(total_priority)}")

def organize_rugsacks() -> list:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    input_file = open(filename, 'r')
    priorities = []
    for line in input_file:
        l = [*line.strip()]
        half = int(len(l)/2)
        rugsack_1 = l[:half]
        rugsack_2 = l[half:]
        in_both = []
        for r1, r2 in zip(rugsack_1, rugsack_2):
            if r1 in rugsack_2:
                in_both.append(r1)

            if r2 in rugsack_1:
                in_both.append(r2)

        priorities.append(*list(dict.fromkeys(in_both)))

    return priorities

def convert_to_priority(letters: list) -> int:
    values = []
    for l in letters:
        if l.isupper():
            values.append(string.ascii_uppercase.index(l)+1 + 26)
            continue
        values.append(string.ascii_lowercase.index(l)+1)
    return values




if __name__ == "__main__":
    main()
