import openpyxl

class OpenExel:
    def __init__(self, file_name):
        self.file_obj = openpyxl.load_workbook(file_name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with OpenExel('Task3.xlsx') as file:
    print(file.sheetnames)
    sheet = file.active
    print(sheet['A2'].value, sheet['B2'].value)
    sheet['A4'] = 13
    print(sheet['A4'].value)
    file.save('Task3_update.xlsx')