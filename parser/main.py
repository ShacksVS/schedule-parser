import argparse

from convertation import *
from validation import *


def parse_args():
    parser = argparse.ArgumentParser(description="Process an Excel file.")
    parser.add_argument("path", help="Path to the Excel file")
    return parser.parse_args()


def main():
    args = parse_args()
    sheet = load_schedule(args.path)
    cleaned_schedule = None

    if sheet is not None:
        cleaned_schedule = get_clean_data(sheet)
        # to look for cleaned data uncomment this

        # for el in cleaned_schedule:
        #     print(el)

    if cleaned_schedule:
        convert_to_json(cleaned_schedule)


# to run write in terminal 'python main.py "../data/3.xlsx"'
if __name__ == "__main__":
    main()
