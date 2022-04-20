import sys


def read_scanner_result():
    try:
        with open(sys.argv[1]) as file:
            lines = file.read().splitlines()
            file.close()
        return lines
    except IOError as err:
        print('File does not exist')
        raise err
    except IndexError as err:
        print('File was not named (Try: python main.py folder/filename.txt)')
        raise err
