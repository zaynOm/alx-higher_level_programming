#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv)

    if ac == 1:
        print('0 arguments.')

    else:
        print('{} arguments:'.format(ac - 1))
        for i in range(1, ac):
            print('{}: {}'.format(i, argv[i]))
