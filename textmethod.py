import combining
import unittest
import string

test_string = "this is a test string. It contains-various numbers, like three and 4." \
              "it also has paragraphs. and multiples sentences."
nohypen_test_string = "this is a test string It contains various numbers like three and 4" \
                      "it also has paragraphs and multiples sentences"


class testingdocuments(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(combining.fibList(10),[1,1,2,3,5,8,13,21,34,55])

    def test_prime(self):
        self.assertEqual(combining.prime(20), [2, 3, 5,7,11,13,17,19])

    def test_breakfile(self):
        self.assertEqual(combining.breaktext(test_string),
                         list(test_string.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")))

    def test_removepunctuation(self):
        self.assertEqual(combining.removePunctuation(test_string), nohypen_test_string.split())

    def test_reversechar(self):
        self.assertEqual(combining.reverseChar(test_string),
                         list(test_string[::-1].translate(str.maketrans("", "", string.punctuation)).replace(" ", "")))

    #NOT YET TESTED:
        #numeral lists
        #written numerals
        #acrostics

if __name__ == 'main':
    unittest.main()