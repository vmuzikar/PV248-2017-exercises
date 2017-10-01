#!/usr/bin/env python3

import re
from collections import Counter
import logging

logging.basicConfig(level=logging.ERROR)  # change to see warnings
logger = logging.getLogger(__name__)


def aggregateScores(byKey, scores, **kWordParams):
    ctr = Counter()
    for score in scores:
        try:
            key = score[byKey]
        except KeyError:
            continue
        if "mapFunction" in kWordParams:
            key = kWordParams["mapFunction"](key)
        if key is None:
            continue
        ctr[key] += 1
    return ctr


def searchScores(key, value, scores):
    return list(filter((lambda s: key in s and s[key] is value), scores))


def loadScoresFromFile(filePath):
    f = open(filePath, "r", encoding="utf8")

    keyValuePattern = re.compile(r"^([^\s,:]+[^:]*): ([^\s].*)$")
    emptyPattern = re.compile(r"^\S*$")

    scores = [{}]

    for line in f:
        m = keyValuePattern.match(line)
        if m is None:
            if emptyPattern.match(line) is None:
                logger.warning("Couldn't parse following line: " + line)
                continue
            scores.append({})  # ok, new empty line ==> next record which is empty for now
            continue
        scores[-1][m.group(1)] = m.group(2).strip()

    f.close()

    return scores


def yearToCentury(year):
    try:
        year = re.compile(r".*(\d{4}).*").match(year).group(1)
        return "{}th century".format(int(year[0:2]) + 1)
    except AttributeError:
        logger.warning("Couldn't parse following year: " + year)


def main():
    scores = loadScoresFromFile("scorelib.txt")

    print(aggregateScores("Composer", scores))
    print(100 * "-")
    print(aggregateScores("Key", scores))
    print(100 * "-")
    print(aggregateScores("Composition Year", scores, mapFunction=yearToCentury))
    print(100 * "-")
    print(searchScores("Key", "C", scores))


if __name__ == "__main__":
    main()
