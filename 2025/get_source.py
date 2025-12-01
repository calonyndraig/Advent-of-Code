import requests
from pathlib import Path

def download_input(day, year, session_cookie="53616c7465645f5fbb067603173994af2e21bebdd2b341a01395e2fb0cc53a062a148cdf70098ffec55fbfb023b471b283dc6403a774ae372c4614a32c682336", save_to=None):
    """
    Download AOC input file for the given day/year; returns long string, which may include whitespace, line breaks, etc.
    """
    
    url=f"https://adventofcode.com/{year}/day/{day}/input" # creates URL for puzzle file
    cookies = {"session": session_cookie}

    response = requests.get(url, cookies=cookies)
    response.raise_for_status()

    text = response.text.strip()

    base_dir = Path(__file__).resolve().parent # used to correct pathing for saves within working files

    if save_to is None:
        input_dir = base_dir / "input_files"
        input_dir.mkdir(parents=True, exist_ok=True)

        save_to = input_dir / f"aoc{year}_day{day}.txt"

    else:
        save_to = Path(save_to)
        save_to.parent.mkdir(parents=True, exist_ok=True)

    save_to.write_text(text, encoding="utf-8")

    return text # returns long string, includes line breaks, white space, etc.


def string_convert_to_list(text):
    """
    Converts the .txt file to a simple list of strings    
    """
    list_of_lines = [line.strip() for line in text.splitlines()]

    return list_of_lines


if __name__ == "__main__":
    SESSION = "53616c7465645f5fbb067603173994af2e21bebdd2b341a01395e2fb0cc53a062a148cdf70098ffec55fbfb023b471b283dc6403a774ae372c4614a32c682336"
    download_input(day=1, year=2025,session_cookie=SESSION)