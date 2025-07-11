#!/usr/bin/python3
"""
Module containing function displaying all cities from a database.
"""
import sys
import MySQLdb


def main():
    """
    Lists all cities with linked state from a database.
    """
    if len(sys.argv) != 4:
        sys.exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id ASC
    """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
