import unittest
from lclib import gps

class TestGps(unittest.TestCase):
    def test_haversine(self):
        assert gps.haversine(52.370216, 4.895168, 52.520008,
        13.404954) == 946.3876221719836

if __name__ == '__main__':
    unittest.main()