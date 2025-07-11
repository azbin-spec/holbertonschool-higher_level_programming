#!/usr/bin/python3
"""
Module containing function displaying specific states from a database.
"""
import sys
import MySQLdb


def main():
    """
    Lists all records safely with specific name from a database.
    """
    if len(sys.argv) != 5:
        sys.exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_state = sys.argv[4]

    if "'" in searched_state:
        sys.exit()

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM states
        WHERE name = '{}'
        ORDER BY id ASC
    """.format(searched_state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
