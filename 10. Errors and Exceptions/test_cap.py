import unittest # the library we need
import cap # the file we wish to test

# A test class
class TestCap(unittest.TestCase):

    # separate methods for each test we want
    # assertEqual() tests whether what we get is what we are expecting
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

# This isn't strictly necessary but is good practice as
# it prevents the test being run if we're importing this script
if __name__ == '__main__':
    # finally, we perform the test itself
    unittest.main()