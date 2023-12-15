#!/usr/bin/python3
"This script lists all states that has a matching name to the given one"

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id"
                .format(argv[4]))

    states = cur.fetchall()
    for row in states:
        print(row)

    cur.close()
    conn.close()
