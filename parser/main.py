from validation import *


PATH = "../data/3.xlsx"
# todo args_parser


def main():
    sheet = load_schedule(PATH)

    if sheet is not None:
        cleaned_schedule = clean_and_get_updated_rows(sheet)

        for updated_row in cleaned_schedule:
            print(updated_row)


if __name__ == "__main__":
    main()
