#!/usr/bin/python3
import unittest

def fib(n, memo={}):
    if n <= 2:
        return 1
    elif memo.get(str(n)):
        return memo[str(n)]
    else:
        memo[str(n)] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[str(n)]

def setUpModule():
    print("setup module")

def tearDownModule():
    print("teardown module")

class TestFib(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.n = 10
    def tearDown(self):
        print("tearDown")
        del self.n
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)
    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)

if __name__ == "__main__":
    unittest.main()
