import re

def get_year_month_from_filename(filename):
    try:
        e = None
        match = re.search(r'(\d{4})-(\d{2})', filename)
        if match:
            year = match.group(1)
            month = match.group(2)
            return int(year), int(month)
    except Exception as e:
        pass
    raise Exception(f"Year, Month not found in filename {filename} {e}")

def create_new_pgn_filename(year, month, eco, source="lichess"):
    return source + "_" + str(year) + "_" + str(month) + "_" + eco + ".pgn"
