import requests

def main():
    summary = {}
    elf = 1
    calories = []
    max = 0
    input_file = open('input.txt', 'r')

    for line in input_file:
        line = line.replace("\n", "")
        if line == '':
            total = sum(calories)
            summary[elf] = {
                'calories': calories,
                'total': total
            }

            if total > max:
                max = total

            calories = []
            elf += 1
            continue

        calories.append(int(line))

    print(f"The maximum calories is: {max}")

if __name__ == "__main__":
    main()