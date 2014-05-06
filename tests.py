import unittest
from src import stringReverse
class Test_String_Operation(unittest.TestCase):
    def test_string(self):
		result = stringReverse('today is my birthday')
		assert "birthday my is today" == result
		assert isinstance(result,str)
		print "Test case 1 executed fine"

    def test_string_punctuation(self):
        result = stringReverse("today's is my b'day")
        assert "b'day my is today's" == result
        assert isinstance(result,str)
        print "Test case 2 executed fine"
        
    def test_single_word(self):
        result = stringReverse("show")
        assert "show" == result
        assert isinstance(result,str)
        print "Test case 3 executed fine"
        
if __name__ == "__main__":
    unittest.main()
