import unittest

from lclib import lichess

class TestLichessLib(unittest.TestCase):
    def test_year_month(self):
        year, month = lichess.get_year_month_from_filename("lichess_db_standard_rated_2024-10.pgn")
        assert year == 2024
        assert month == 10

        try:
            year, month = lichess.get_year_month_from_filename("lichess_db_standard_rated_xxx.pgn")
        except Exception as e:            
            assert str(e).startswith("Year, Month not found in filename") == True


if __name__ == '__main__':
    unittest.main()