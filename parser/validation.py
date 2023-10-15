import openpyxl


WEEK_DAYS = ("Понеділок", "Вівторок", "Середа", "Четвер", "П`ятниця", "Субота")


def load_schedule(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        return sheet
    except Exception as e:
        print(f"Error loading the Excel file: {e}")
        return None


def clean_and_get_updated_rows(sheet):
    temp_time = None
    updated_rows = []

    for row in sheet.iter_rows(min_row=10, max_row=73, max_col=6, values_only=True):
        if row[0] in WEEK_DAYS:
            print(row[0])

        row_list = list(row)

        # giving correct time for class without time
        if row_list[2] is not None and row_list[1] is None:
            row_list[1] = temp_time
        elif row_list[1] is not None:
            temp_time = row_list[1]
        updated_row = tuple(row_list)

        if updated_row[1] is not None and updated_row[2] is None:
            updated_rows.append(updated_row)

    return updated_rows
