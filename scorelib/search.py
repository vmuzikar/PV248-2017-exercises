import json
import sqlite3
import sys


def search_person(name, cursor):
    data = {}
    for record in cursor.execute("SELECT person.name AS person_name, score.name AS score_name, print.id AS print "
                                 "FROM person "
                                 "LEFT OUTER JOIN score_author ON person.id = score_author.composer "
                                 "JOIN score ON score.id = score_author.score "
                                 "JOIN edition ON score.id = edition.score "
                                 "JOIN print ON edition.id = print.edition "
                                 "WHERE person.name LIKE ?", ("%{}%".format(name),)):

        if record[0] not in data:
            data[record[0]] = []

        data[record[0]].append({
            "print": record[2],
            "score_name": record[1]
        })

    return data


def main():
    if len(sys.argv) is 2:
        name = sys.argv[1]
    else:
        name = ""

    cursor = sqlite3.connect("scorelib.dat").cursor()
    print(json.dumps(search_person(name, cursor), sort_keys=True, indent=4))


if __name__ == "__main__":
    main()
