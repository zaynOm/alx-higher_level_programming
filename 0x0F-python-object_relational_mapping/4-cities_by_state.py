#!/usr/bin/python3
"This script lists all cities"

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c JOIN states s \
                WHERE c.state_id = s.id ORDER BY c.id")

    cities = cur.fetchall()
    for row in cities:
        print(row)

    cur.close()
    conn.close()
