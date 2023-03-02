# import PyPDF2
#
#
# input_file = 'documents/first.pdf'
# output_file = 'documents/firstOut.pdf'
# watermark_file = 'aproove.pdf'
#
# with open(input_file, 'rb') as file_input:
#     pypdf = PyPDF2.PdfReader(file_input)
#
#     with open(watermark_file, 'rb') as file_watermark:
#         watermark = PyPDF2.PdfReader(file_watermark)
#         first_page = pypdf.getPage(0)
#
#         first_page_watermark = watermark.getPage(0)
#
#         first_page.mergePage(first_page_watermark)
#
#         pdf_writer = PyPDF2.PdfWriter()
#
#         pdf_writer.add_page(first_page)
#
#         with open(output_file, 'wb') as file_output:
#             pdf_writer.write(file_output)


# Электронный документооборот для АлтынБулак

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.add_font('times', '', 'font/times.ttf', uni=True)
pdf.add_font('times', 'B', 'font/timesbd.ttf', uni=True)
pdf.add_font('times', 'BI', 'font/timesbi.ttf', uni=True)

pdf.set_text_color(0, 0, 0) # Задаем цвет в RGB все что будет снизу
pdf.set_font('times', '', size=14)

# Создаем шапку документа
pdf.image('logo.jpeg', x=10, y=10, w=50, h=20) # вставляем логотип
name = input('Введите имя от кого запускается служебка: ')
# name = 'Тен Владислав'

top_text = f'Директору\n' \
           f'ТОО "АлтынБулак-Атырау"\n'\
           f'г-же Таировой А.Р\n'\
           f'от {name}'

x = 130 # x - координата ячейки по горизонтали (от правого края страницы)
y = 15  # y - координата ячейки по вертикали (от верхнего края страницы)
pdf.set_xy(x, y)
pdf.multi_cell(w=70, h=7, txt=top_text, align = 'L',)

# Пишем в центре Служебная записка
pdf.set_font('times', 'B', size=18, )
pdf.text(x=85, y= 90, txt='Служебная записка')

# Записываем текст самой служебной записки
x = 15 # x - координата ячейки по горизонтали (от правого края страницы)
y = 100  # y - координата ячейки по вертикали (от верхнего края страницы)
body_text = 'Прошу вас согласовать командировку в город Майами, для посещения пляжей,' \
            ' питья крутых коктейлей и знакомства с латинками'
pdf.set_font('times', '', size=14)
pdf.set_xy(x, y)
pdf.multi_cell(w=190, h=7, txt='            ' + body_text, align = 'L')

# Footer документа (подписанты)
x = 15 # x - координата ячейки по горизонтали (от правого края страницы)
y = 230  # y - координата ячейки по вертикали (от верхнего края страницы)
body_text = f'Составил Супервайзер ________________________ {name}\n' \
            f'Не возражаю Коммерческий директор _______________________\n' \
            f'Изменения введены\n' \
            f'Ит Специалист ____________________________\n' \
            f'Директор по продажам __________________________ Ли Елена'
pdf.set_font('times', '', size=14)
pdf.set_xy(x, y)
pdf.multi_cell(w=190, h=7, txt=body_text, align = 'L')

pdf.image('aproove.png', x=140, y=270, w=50, h=20) # вставляем логотип

pdf.output("documents/First-signed.pdf")

pdf.close()








