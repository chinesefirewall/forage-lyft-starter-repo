
import unittest
from tires import CarriganTires, OctoprimeTires


class TestTires(unittest.TestCase):

    def test_carrigan_tires(self):
        # Initialize object
        tire = CarriganTires()

        # Test cases where service is not needed
        self.assertFalse(tire.needs_service([0.1, 0.2, 0.3, 0.4]))
        self.assertFalse(tire.needs_service([0.8, 0.8, 0.8, 0.8]))

        # Test cases where service is needed
        self.assertTrue(tire.needs_service([0.9, 0.1, 0.1, 0.1]))
        self.assertTrue(tire.needs_service([1, 0.1, 0.1, 0.1]))

    def test_octoprime_tires(self):
        # Initialize object
        tire = OctoprimeTires()

        # Test cases where service is not needed
        self.assertFalse(tire.needs_service([0.5, 0.5, 0.5, 0.5]))

        # Test cases where service is needed
        self.assertTrue(tire.needs_service([1, 1, 1, 0.1]))
        self.assertTrue(tire.needs_service([1, 1, 1, 1]))


if __name__ == "__main__":
    unittest.main()
