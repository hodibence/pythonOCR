import ocr_parser
import reader
import os


def main():
    data = reader.read_scanner_result()
    ocr_characters = ocr_parser.parse(data)
    account_number = str(ocr_parser.translate(ocr_characters))
    f = open("result.txt", "a")
    if (os.path.getsize("result.txt") > 0):
        f.write("\n" + account_number)
    else:
        f.write(account_number)

    f.close()


if __name__ == '__main__':
    main()
