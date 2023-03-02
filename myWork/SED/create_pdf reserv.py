# Электронный документооборот для АлтынБулак

from fpdf import FPDF


with open('BD/numbers.txt', 'r') as f:
    counter = int(f.read())

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

x = 130  # x - координата ячейки по горизонтали (от правого края страницы)
y = 15   # y - координата ячейки по вертикали (от верхнего края страницы)
pdf.set_xy(x, y)
pdf.multi_cell(w=70, h=7, txt=top_text, align = 'L',)

# Пишем в центре Служебная записка
pdf.set_font('times', 'B', size=18, )
pdf.text(x=85, y=90, txt='Служебная записка')

# Записываем текст самой служебной записки
x = 15   # x - координата ячейки по горизонтали (от правого края страницы)
y = 100  # y - координата ячейки по вертикали (от верхнего края страницы)
body_text = input('Введите текст служебной записки: ')
pdf.set_font('times', '', size=14)
pdf.set_xy(x, y)
pdf.multi_cell(w=190, h=7, txt='            ' + body_text, align = 'L')

# Footer документа (подписанты)
x = 15   # x - координата ячейки по горизонтали (от правого края страницы)
y = 230  # y - координата ячейки по вертикали (от верхнего края страницы)
footer_text = f'Составил Супервайзер ________________________ {name}\n' \
            f'Не возражаю Коммерческий директор _______________________\n' \
            f'Изменения введены\n' \
            f'Ит Специалист ____________________________\n' \
            f'Директор по продажам __________________________ Ли Елена'
pdf.set_font('times', '', size=14)
pdf.set_xy(x, y)
pdf.multi_cell(w=190, h=7, txt=footer_text, align = 'L')

pdf.output("documents/First.pdf")

with open('BD/numbers.txt', 'w') as statistic:
    counter += 1
    statistic.write(str(counter))
    with open('BD/BD.txt', 'a', encoding='utf-8') as base_data:
        base_data.write(str(counter) + ' ' + name + ' ' + body_text + '\n')

pdf.close()









# from fpdf import FPDF
#
# # Создаем объект PDF-документа
# pdf = FPDF()
#
# # Добавляем страницу
# pdf.add_page()
#
# # Устанавливаем шрифт и размер
# pdf.set_font("Arial", size=12)
#
# # Устанавливаем координаты и размеры ячейки с таблицей
#
# x = 130 # x - координата ячейки по горизонтали (от правого края страницы)
# y = 15  # y - координата ячейки по вертикали (от верхнего края страницы)
# pdf.set_xy(x, y)
#
# # Создаем таблицу с одной строкой и одним столбцом
# pdf.multi_cell(50, 6, 'kddfkgj kjdfhgkd gkdhfgkdhgkdfhg', align= None)
#
# # Сохраняем PDF-файл
# pdf.output("example.pdf")




