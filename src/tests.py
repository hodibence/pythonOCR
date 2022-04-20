import unittest
import test_reader
import ocr_parser


class FileInputTest(unittest.TestCase):

    def test_read_empty_file(self):
        '''Empty file test'''
        data = test_reader.read_scanner_test('../data/empty.txt')
        self.assertFalse(test_reader.validate_scanner_result(data))

    def test_read_more_char(self):
        '''Line is contains more characters test'''
        data = test_reader.read_scanner_test('../data/morechar.txt')
        self.assertFalse(test_reader.validate_scanner_result(data))

    def test_read_long_file(self):
        '''4 lines instead of 3 test'''
        data = test_reader.read_scanner_test('../data/long.txt')
        self.assertFalse(test_reader.validate_scanner_result(data))

    def test_read_short_file(self):
        '''2 lines instead of 3 test'''
        data = test_reader.read_scanner_test('../data/short.txt')
        self.assertFalse(test_reader.validate_scanner_result(data))


class FileParserTest(unittest.TestCase):
    def test_parse_zeros(self):
        '''000000000 test'''
        data = test_reader.read_scanner_test('../data/nine-zeroes.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('000000000', str(account_number))

    def test_parse_ones(self):
        '''111111111 test'''
        data = test_reader.read_scanner_test('../data/nine_ones.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('111111111 ERR', str(account_number))

    def test_parse_123456789(self):
        '''123456789 test '''
        data = test_reader.read_scanner_test('../data/one_to_9.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('123456789', str(account_number))


    def test_parse_ill(self):
        '''12?456709 ILL test'''
        data = test_reader.read_scanner_test('../data/misspelled.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('12?456709 ILL', str(account_number))


    def test_parse_checksum_ok(self):
        '''checksum 123456789 test'''
        data = test_reader.read_scanner_test('../data/one_to_9.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual(0, account_number.calculate_checksum())

    def test_parse_checksum_err(self):
        '''checksum 664371495 test '''
        data = test_reader.read_scanner_test('../data/wrong_checksum.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual(2, account_number.calculate_checksum())
        self.assertEqual('664371495 ERR', str(account_number))


if __name__ == '__main__':
    unittest.main()
