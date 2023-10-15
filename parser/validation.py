import openpyxl


def load_schedule(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        return sheet
    except Exception as e:
        print(f"Error loading the Excel file: {e}")
        return None


def get_clean_data(sheet) -> list:
    temp_time = None
    temp_weekday = None
    updated_rows = []

    for row in sheet.iter_rows(min_row=6, max_row=7, max_col=6, values_only=True):
        updated_rows.append(row[0])

    for row in sheet.iter_rows(min_row=10, max_row=73, max_col=6, values_only=True):
        row_list = list(row)

        # Giving correct time for a class without time
        if row_list[2] is not None and row_list[1] is None:
            row_list[1] = temp_time
        elif row_list[1] is not None:
            temp_time = row_list[1]

        # Fill up weekday where None
        if row_list[0] is not None:
            temp_weekday = row_list[0]
        elif temp_weekday is not None:
            row_list[0] = temp_weekday

        updated_row = tuple(row_list)

        if updated_row[1] is not None and updated_row[2]:
            updated_rows.append(updated_row)

    return updated_rows


