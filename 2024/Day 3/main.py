import requests
import re

def get_input(url: str):
    cookies = {
        'session': '53616c7465645f5fb63316243194789fb28f58dcb4bada055ea8bf8d5295ea8f29019a177d52696bdbc82b73b6dc2e12dff58034d812ce8f48821854289bd8db',
    }
    try:
        response = requests.get(url, headers=
        {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
         "Host": "adventofcode.com"}, cookies=cookies)
        response.raise_for_status()
    except Exception as e:
        raise Exception(e)

    return response.text


def part1(test: bool = False):
    print("-"*15,"\nPart 1", "Test", test)
    if test:
        with open("input1.txt") as f:
            input = f.read()
    else:
        input = get_input(url="http://adventofcode.com/2024/day/3/input")

    muls = re.findall(r"(mul[(])(\d{1,3},\d{1,3})([)])", input)
    total = 0
    for m in muls:
        num = list(map(int, m[1].split(",")))
        total += num[0] * num[1]

    print("Total: %s" % total)

def part2(test: bool = False):
    print("-" * 15, "\nPart 2")
    if test:
        with open("input2.txt") as f:
            input = f.read()
    else:
        input = get_input(url="http://adventofcode.com/2024/day/3/input")

    muls = re.findall(r"(don't[(][)]|do[(][)])|((mul[(])(\d{1,3},\d{1,3})([)]))", input)
    total = 0
    do = True

    for m in muls:
        if m[0] == "do()":
            do = True
            continue
        if m[0] == "don't()":
            do = False
            continue

        if do:
            num = list(map(int, m[3].split(",")))
            total += num[0] * num[1]

    print("Total: %s" % total)


if __name__ == "__main__":
    part1(False)
    part2(False)