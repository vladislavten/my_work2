import os
import win32com.client as win32


def convert_excel_to_pdf(folder_path='results'):
    """
    Проходит по папке с Excel-файлами и конвертирует каждый в PDF.
    """

    # Да-да, вызываем Excel через COM, без этого никак.
    excel_app = win32.Dispatch("Excel.Application")
    excel_app.Visible = False  # Чтобы не пугало своими окошками

    # Пробегаемся по файлам в папке
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.xlsx', '.xls')):
            full_path = os.path.join(folder_path, file_name)

            # Открываем эту жалкую книжку
            wb = excel_app.Workbooks.Open(full_path)

            # Формируем PDF-файл с таким же именем, только на конце .pdf
            pdf_path = os.path.join(
                folder_path,
                os.path.splitext(file_name)[0] + ".pdf"
            )

            # ExportAsFixedFormat(0) - это тип экспорта в PDF
            wb.ExportAsFixedFormat(0, pdf_path)

            # Закрываем, чтобы Excel за нами потом не охотился
            wb.Close()

    # Вырубаем Excel, он нам больше не нужен
    excel_app.Quit()


if __name__ == "__main__":
    # Ну и вызовем нашу функцию; вдруг ты не догадаешься
    convert_excel_to_pdf('C:\\Users\\Admin\\PycharmProjects\\my_work2\\myWork\\сортировка ИИН и имен\\results')
    print("Работу за тебя сделал. Доволен?")
