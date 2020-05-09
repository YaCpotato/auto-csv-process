import sys


if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        if args[1].isdigit():
            fizzBuzz(int(args[1]))
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')
