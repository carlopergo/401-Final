import unittest
import main

class TestMain(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(main.fun(4),16)

    def test_fun2(self):
        self.assertEqual(main.fun(5),25)
    
    def test_fun3(self):
        self.assertEqual(main.fun(6),36)

    def test_fun4(self):
        self.assertEqual(main.fun(7),49)

    def test_fun5(self):
        self.assertEqual(main.fun(8),88)


if __name__ == '__main__':
    unittest.main()