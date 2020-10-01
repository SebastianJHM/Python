import sys
import re
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        test_case = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(test_case), expected)
    def test_empty(self):
        test_case = ""
        expected = ""
        self.assertEqual(rearrange_name(test_case), expected)
    def test_double_name(self):
        test_case = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(test_case), expected)
    def test_one_name(self):
        test_case = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(test_case), expected)
        
def rearrange_name(name):
    x = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if x is None:
        return name
    return "{} {}".format(x[2], x[1])

def principal( argv ):
    unittest.main() 
    #rint(rearrange_name("Lovelace, Ada"))
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi

# Method	                  Checks that	         New in
# assertEqual(a, b)	          a == b	
# assertNotEqual(a, b)    	  a != b	
# assertTrue(x)         	  bool(x) is True	
# assertFalse(x)	          bool(x) is False	
# assertIs(a, b)	          a is b	             3.1
# assertIsNot(a, b)	          a is not b	         3.1
# assertIsNone(x)	          x is None	             3.1
# assertIsNotNone(x)	      x is not None	         3.1
# assertIn(a, b)	          a in b	             3.1
# assertNotIn(a, b)	          a not in b	         3.1
# assertIsInstance(a, b)	  isinstance(a, b)	     3.2
# assertNotIsInstance(a, b)	  not isinstance(a, b)   3.2