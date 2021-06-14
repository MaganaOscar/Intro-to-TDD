import unittest

def reverse_list(a_list):
    if len(a_list) == 0 or len(a_list) == 1:
        return a_list
    for index in range(0,len(a_list)//2):
        a_list[index], a_list[len(a_list)-index-1] = a_list[len(a_list)-index-1], a_list[index]
    return a_list

def isPalindrome(a_string):
    if isinstance(a_string, str):
        for index in range(len(a_string)):
            if a_string[index] != a_string[len(a_string)-index-1]:
                return False
    else:
        return "Not a string"
    return True

def coins(coins):
    change=[0,0,0,0]
    while coins > 0:
        if coins >= 25:
            change[0] = coins // 25
            coins %= 25
        elif coins >= 10:
            change[1] = coins // 10
            coins %= 10
        elif coins >= 5:
            change[2] = coins // 5
            coins %= 5
        else:
            change[3] = coins
            coins = 0
    return change

def factorial(num):
    if num < 0:
        return 'No negative factorial'
    elif num == 0:
        return 1
    elif num == 1:
        return num
    else:
        return num*factorial(num-1)

def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

class tests(unittest.TestCase):
    def test_reverse_empty(self):
        self.assertEqual(reverse_list([]), [])
    def test_reverse_length_one(self):
        self.assertEqual(reverse_list([0]), [0])
    def test_reverse_even_length(self):
        self.assertEqual(reverse_list([10,45,2,8]), [8,2,45,10])
    def test_reverse_odd_length(self):
        self.assertEqual(reverse_list([10,45,2,8,76]), [76,8,2,45,10])

    def test_isPalindrome_type(self):
        self.assertEqual(isPalindrome(55), "Not a string")
    def test_isPalindrome_empty(self):
        self.assertTrue(isPalindrome(""))
    def test_isPalindrome_length_one(self):
        self.assertTrue(isPalindrome("a"))
    def test_isPalindrome_even_length(self):
        self.assertTrue("aa")
    def test_isPalindrome_odd_length(self):
        self.assertTrue("aba")

    def test_coins_empty(self):
        self.assertEqual(coins(0), [0,0,0,0])
    def test_coins_pennies(self):
        self.assertEqual(coins(4), [0,0,0,4])
    def test_coins_nickels(self):
        self.assertEqual(coins(8), [0,0,1,3])
    def test_coins_dimes(self):
        self.assertEqual(coins(19), [0,1,1,4])
    def test_coins_quarters(self):
        self.assertEqual(coins(99), [3,2,0,4])

    def test_factorial_zero(self):
        self.assertEqual(factorial(0),1)
    def test_factorial_negative(self):
        self.assertEqual(factorial(-5), 'No negative factorial')
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonnaci_zero(self):
        self.assertEqual(fibonacci(0), 0)
    def test_fibonnaci_one(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fibonnaci(self):
        self.assertEqual(fibonacci(5), 5)

    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()