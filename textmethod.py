import combining
import unittest
import string
test_numwordlist = [3]
test_numlist = [3, 4]
test_string = "this is a test string. It contains various numbers, like three and 4. \nit also has paragraphs. and multiples sentences."
test_charstring  = "thisisateststringItcontainsvariousnumberslikethreeand4italsohasparagraphsandmultiplessentences"
test_string_reverse = "sentences multiples and paragraphs has also it 4 and three like numbers various contains It string test a is this"
test_char = ["t", "e", "s", "t", ".", "?"]
test_rev_char = ["t", "s", "e", "t"]
test_leftAcro_word = ["this", "it"]
test_leftAcro_char = ["t", "i"]


class testingdocuments(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(combining.fibList(10),[1,1,2,3,5,8,13,21,34,55])

    def test_prime(self):
        self.assertEqual(combining.prime(20), [2, 3, 5,7,11,13,17,19])

    def test_breakfile(self):
        self.assertEqual(combining.charactertext(test_string), list(test_charstring))

    def test_reversechar(self):
        self.assertEqual(combining.reversechar(combining.charactertext(test_char)), test_rev_char)

    def test_convertnumbers(self):
        self.assertEqual(combining.convertNumbers(test_string), [3])

    def test_reversetext(self):
        self.assertEqual(combining.reversetext(test_string), test_string_reverse.split(" "))

    def test_numerals(self):
        self.assertEqual(combining.numerals(test_string, test_string_reverse.split(" ")), ["numbers", "paragraphs", "test", "paragraphs", "and"])

    def test_charnumerals(self):
        self.assertEqual(combining.char_numerals(test_string, list(test_charstring), list(test_charstring[::-1])),
                         ["e", "l", "s", "n", "a"])

    def test_byWord(self):
        self.assertEqual(combining.byWord(test_numwordlist, test_string, test_string_reverse.split(" ")), ["a", "and", "it"])

    def test_byWordcharacters(self):
        self.assertEqual(combining.byWord_characters(test_string, list(test_charstring), list(test_charstring[::-1]), test_numwordlist),
                         ["i","c", "i"])

    def test_leftAcrostics(self):
        word, char = combining.leftAcrostics(test_string)
        self.assertEqual(sum(word, []), test_leftAcro_word)
        self.assertEqual(char, test_leftAcro_char)

    def test_rightAcrostics(self):
        word, char = combining.rightAcrostics(test_string)
        self.assertEqual(sum(word, []), ["4", "sentences"])
        self.assertEqual(sum(char, []), ["4", "s"])

    def test_fibCheck(self):
        word, char = combining.fibCheck(combining.fibList(10),test_string, test_charstring)
        self.assertEqual(word, ["this", "this", "is", "a", "string", "various", "4"])
        self.assertEqual(char, ["t", "t", "h", "i", "i", "t", "t", "o", "s", "i"])

    def test_primecheck(self):
        word, char = combining.primeCheck(combining.prime(20), test_string, test_charstring)
        self.assertEqual(word, ["is", "a", "string", "contains", "three", "4", "paragraphs", "multiples"])
        self.assertEqual(char, ["h", "i", "i", "a", "t", "t", "g", "t"])

    def test_numbers(self):
        self.assertEqual(combining.numbers(test_string, test_numwordlist), [4, 3])

    def test_crossdiscovery(self):
        self.assertEqual(combining.crossdiscovery(combining.fibList(10), test_string, test_numlist), ["a"])



if __name__ == 'main':
    unittest.main()