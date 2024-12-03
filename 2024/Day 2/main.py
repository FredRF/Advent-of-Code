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


def part1(test: bool = False):
    print("-"*15,"\nPart 1", "Test", test)
    if test:
        with open("input1.txt") as f:
            input = f.read()
    else:
        input = get_input(url="http://adventofcode.com/2024/day/2/input")
    _original_list = input.split("\n")
    safe = 0

    # remove the last line if exists
    if _original_list[-1] == '':
        _original_list = _original_list[:-1]

    for el in _original_list:
        _el = list(map(int, el.strip().split(" ")))
        if _aux_iter(_el=_el):
            safe += 1
            continue

    print("Safe: %s" % safe)

def _aux_valid(el: int, prev_el: int, dif: bool) -> bool:
    return el == prev_el or abs(el - prev_el) > 3 or bool(prev_el > el) != bool(dif)

def _aux_iter(_el: list):
    dif = _el[0] > _el[1]
    for idx, e in enumerate(_el[1:]):
        if _aux_valid(el=e, prev_el=_el[idx], dif=dif):
            return False
    return True

def part2(test: bool = False):
    print("-" * 15, "\nPart 2")
    if test:
        with open("input1.txt") as f:
            input = f.read()
    else:
        input = get_input(url="http://adventofcode.com/2024/day/2/input")
    _original_list = input.split("\n")
    safe = 0

    # remove the last line if exists
    if _original_list[-1] == '':
        _original_list = _original_list[:-1]

    for el in _original_list:
        _el = list(map(int, el.strip().split(" ")))
        if _aux_iter(_el=_el):
            safe += 1
            continue
        for idx, _ in enumerate(_el):
            if _aux_iter(_el=[x for i, x in enumerate(_el) if i != idx]):
                safe +=1
                break


    print("Safe: %s" % safe)


if __name__ == "__main__":
    part1(False)
    part2(False)