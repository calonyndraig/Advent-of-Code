import requests
from pathlib import Path

def download_input(day, year, session_cookie, save_to=None):
    """
    Download AOC input filve for the given day/year
    """

    print(f"Running code, session cookie = {session_cookie}...")
    url=f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}

    response = requests.get(url, cookies=cookies)
    response.raise_for_status()

    text = response.text.strip()

    base_dir = Path(__file__).resolve().parent

    if save_to is None:
        input_dir = base_dir / "input_files"
        input_dir.mkdir(parents=True, exist_ok=True)

        save_to = input_dir / f"aoc{year}_day{day}.txt"

    else:
        save_to = Path(save_to)
        save_to.parent.mkdir(parents=True, exist_ok=True)

    save_to.write_text(text, encoding="utf-8")
    print(f"Downloaded input for {year} Day {day} → {save_to}")

    return text


def string_convert_to_list(text):
    """
    Converts the .txt file to a simple list    
    """
    list_of_lines = [line.strip() for line in text.splitlines()]

    return list_of_lines


if __name__ == "__main__":
    SESSION = "53616c7465645f5fbb067603173994af2e21bebdd2b341a01395e2fb0cc53a062a148cdf70098ffec55fbfb023b471b283dc6403a774ae372c4614a32c682336"
    download_input(day=1, year=2025,session_cookie=SESSION)