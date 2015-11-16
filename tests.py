import unittest    # Import the whole unittest module.
from Donor import DonorData    # Import DonorData class from the Donor file.


# Create definitions for each test case in the DonorTests class.
class DonorTests(unittest.TestCase):
    def test_get_sickness(self):
        self.assertEqual("Y", DonorData.get_sickness(self), "The answer should be Y or N.")

if __name__ == '__main__':
    unittest.main()
