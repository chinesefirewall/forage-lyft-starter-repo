import unittest
from engine.engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class TestEngine(unittest.TestCase):

    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(1000, 6000)
        self.assertTrue(engine.needs_service())

        engine = CapuletEngine(1000, 4000)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        engine = WilloughbyEngine(1000, 8000)
        self.assertTrue(engine.needs_service())

        engine = WilloughbyEngine(1000, 7000)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
