
def main():
    summary = elf_more_calories()
    get_top_elf_calories(summary, 3)

def elf_more_calories() -> dict:
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
    return summary

def get_top_elf_calories(elf_data: dict, top_num: int) -> dict:
    total = 0
    for i, elf in enumerate(sorted(elf_data, key=lambda x: elf_data[x]['total'], reverse=True), start=1):
        total += elf_data[elf]['total']
        if i == top_num:
            break

    print(f"The total calories of the top {top_num} is {total}")


if __name__ == "__main__":
    main()