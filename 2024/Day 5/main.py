import math


def part1(test: bool = False):
    print("-" * 15, "\nPart 1", "Test", test)
    rules_file = "input1_rules.txt"
    updates_file = "input1_updates.txt"
    if test:
        with open("test_" + rules_file) as f:
            rules = f.readlines()

        with open("test_" + updates_file) as f:
            updates = f.readlines()

    else:
        with open(rules_file) as f:
            rules = f.readlines()

        with open(updates_file) as f:
            updates = f.readlines()

    _rules = {}
    for rule in rules:
        page, precedence = rule.split("|")
        page = int(page)
        precedence = int(precedence)
        if page not in _rules:
            _rules[page] = []

        _rules[page].append(precedence)
        _rules[page].sort()

    good = 0
    consider = True
    good_updates = 0
    for update in updates:
        _rev_update = list(map(int, update.replace("\n", "").split(",")[::-1]))
        for pg_idx, page in enumerate(_rev_update):
            if page in _rules and any(
                [item in _rules[page] for item in _rev_update[pg_idx:]]
            ):
                consider = False
                break

        if consider:
            middle_page = int(_rev_update[::-1][math.floor(len(_rev_update) / 2)])
            # print("update: %s | middle page: %s" % (_rev_update[::-1], middle_page))
            good += 1
            good_updates += middle_page
        consider = True

    print("Total good updates: %s and sum of middle pages: %s" % (good, good_updates))


def _reorg(update: list, _rules: dict):
    _update = update
    for _idx, page in enumerate(_update):
        if page in _rules:
            min_idx = []
            for jdx, _ in enumerate(_update[:_idx]):
                if _update[jdx] in _rules[page]:
                    min_idx.append(jdx)

            if not min_idx:
                continue

            _update.remove(page)
            _update.insert(min(min_idx), page)

    return _update


def part2(test: bool = False):
    print("-" * 15, "\nPart 2")
    rules_file = "input1_rules.txt"
    updates_file = "input1_updates.txt"
    if test:
        with open("test_" + rules_file) as f:
            rules = f.readlines()

        with open("test_" + updates_file) as f:
            updates = f.readlines()

    else:
        with open(rules_file) as f:
            rules = f.readlines()

        with open(updates_file) as f:
            updates = f.readlines()

    _rules = {}
    for rule in rules:
        page, precedence = rule.split("|")
        page = int(page)
        precedence = int(precedence)
        if page not in _rules:
            _rules[page] = []

        _rules[page].append(precedence)
        _rules[page].sort()

    consider = True
    good_updates = 0
    for update in updates:
        _rev_update = list(map(int, update.replace("\n", "").split(",")[::-1]))
        for pg_idx, page in enumerate(_rev_update):
            if page in _rules and any(
                [item in _rules[page] for item in _rev_update[pg_idx:]]
            ):
                ordered = _reorg(_rev_update[::-1], _rules)
                print(ordered)
                consider = False
                middle_page = int(ordered[math.floor(len(ordered) / 2)])
                good_updates += middle_page
                break
        consider = True
    print("Sum of middle pages: %s" % (good_updates))


if __name__ == "__main__":
    part1(False)
    part2(False)
