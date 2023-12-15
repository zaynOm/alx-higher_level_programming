#!/usr/bin/python3
"This script lists all cities in a state."

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM cities c JOIN states s \
                WHERE c.state_id = s.id and s.name = BINARY %s \
                ORDER BY c.id", (argv[4],))

    cities = cur.fetchall()
    print(*(c[0] for c in cities), sep=', ')

    cur.close()
    conn.close()
