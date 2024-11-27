import unittest

from  lclib.twic import get_highest_twic_issue, download_twic_file

class TestLichessLib(unittest.TestCase):
    def test_get_highest_twic_issue(self):
        highest = 1560
        base_url = "https://theweekinchess.com/zips/"
        twic_pattern = "twic<<number>>g.zip"

        high = get_highest_twic_issue(highest, base_url, twic_pattern)
        assert high > highest

    def test_download_twic_file(self):
        download_dir = "/Volumes/FRITZ.NAS/HERSELCLOUD/TWIC/download"
        unzip_dir = "/Volumes/FRITZ.NAS/HERSELCLOUD/TWIC/unzipped"
        issue_number = 1560
        base_url = "https://theweekinchess.com/zips/"
        twic_pattern = "twic<<number>>g.zip"
        download_twic_file(base_url, issue_number, download_dir, unzip_dir, twic_pattern)
        assert 1 == 1

if __name__ == '__main__':
    unittest.main()