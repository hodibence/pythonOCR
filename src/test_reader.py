def read_scanner_test(filename):
    with open(filename) as testfile:
        lines = testfile.read().splitlines()
        testfile.close()
    return lines


def validate_scanner_result(lines):
    if len(lines) == 0:
        print('The file is empty')
        return False

    if len(lines) != 3:
        print(f'The file contains characters that are presented in {len(lines)} lines, but it has to be in the frist 3 lines')
        return False

    for line in lines:
        if len(line) % 3 != 0:
            print('The file contains at least 1 unnecessary characters')
            return False

    return True
