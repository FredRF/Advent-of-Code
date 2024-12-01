import requests

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


def part1():
    print("-"*15,"\nPart 1")
    input = get_input(url="http://adventofcode.com/2024/day/1/input")
    _original_list = input.split("\n")
    l1 = []
    l2 = []
    distance = 0
    for el in _original_list[:-1]:
        _el = el.strip().split("  ")
        l1.append(int(_el[0].strip()))
        l2.append(int(_el[1].strip()))
        l1.sort()
        l2.sort()

    for a, b in zip(l1,l2):
        distance += abs(a - b)

    print("Distance: %s"%distance)

def part2():
    print("-" * 15, "\nPart 2")
    input = get_input(url="http://adventofcode.com/2024/day/1/input")
    _original_list = input.split("\n")
    l1 = []
    l2 = {}
    gap = 0
    for el in _original_list[:-1]:
        _el = el.strip().split("  ")
        l1.append(int(_el[0].strip()))
        _le_el = int(_el[1].strip())
        if _le_el not in l2.keys():
            l2[_le_el] = 1
        else:
            l2[_le_el] +=1

        l1.sort()

    for l1_el in l1:
        if l1_el not in l2.keys():
            continue

        gap += l1_el * l2[l1_el]

    print("Gap :%s" % gap)


if __name__ == "__main__":
    part1()
    part2()