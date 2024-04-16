"""EXTRA CREDIT:   Write a unittest program that tests the program above (problem #5)."""
import unittest
import savings_account as sa

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_instances(self):
        name, pin, balance = account.createAccount()

        self.assertIsInstance(name, str)
        self.assertIsInstance(pin, int)
        self.assertIsInstance(balance, float)

if __name__ == "__main__":
    account = sa.SavingsAccount()
    unittest.main()