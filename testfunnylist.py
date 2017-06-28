from funnylist import FunnyList
import unittest

class TestFunnyList(unittest.TestCase):
    def setUp(self):
        self.list1 = [1, 2, 3]
        self.list2 = [3, 2, 1]
        self.sclist = sorted(self.list1 + self.list2)
        self.fl1 = FunnyList(self.list1)
        self.fl2 = FunnyList(self.list2)
    
    def test_init(self):
        self.assertEqual(self.fl1, self.list1)
        self.assertEqual(self.fl2, self.list2)
        
    def test_equal(self):
        self.assertTrue(self.fl1 == self.fl2)

    def test_add_two(self):
        self.fl3 = self.fl1 + self.fl2
        self.assertEqual(sorted(self.fl3), self.sclist)

    def test_plus_equals_list(self):
        self.fl3 = self.fl1 + self.fl2
        self.fl1 += self.fl2
        self.assertEqual(self.fl3, self.fl1)
    
    def test_plus_equals_obj(self):
        self.list1.append(4)
        self.fl1 += 4
        self.assertTrue(self.list1 == self.fl1)
        
unittest.main()
