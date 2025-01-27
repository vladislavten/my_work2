import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import pandas as pd
import win32com.client as win32

class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FIRCaspian Email Sender")
        self.root.geometry("600x600")

        self.file_path = None
        self.attachment_path = None

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Add logo in the top-left corner
        try:
            logo_image = Image.open("logo.png")
            logo_image = logo_image.resize((100, 20), Image.Resampling.LANCZOS)
            logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = tk.Label(self.root, image=logo_photo)
            self.logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
            self.logo_label.place(x=10, y=10)
        except Exception as e:
            messagebox.showwarning("Предупреждение", f"Не удалось загрузить логотип: {e}")

        # Button to browse Excel file
        self.browse_button = tk.Button(self.root, text="Прикрепить файл рассылки", command=self.browse_file)
        self.browse_button.pack(pady=10)

        # Entry for email subject
        self.subject_label = tk.Label(self.root, text="Тема письма:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(self.root, width=70)
        self.subject_entry.pack(pady=10)

        # Text area for email body
        self.text_label = tk.Label(self.root, text="Текст письма:")
        self.text_label.pack()
        self.email_text = tk.Text(self.root, width=70, height=20)
        self.email_text.pack(pady=10)

        # Button to attach file
        self.attach_button = tk.Button(self.root, text="Прикрепить файл к письму", command=self.attach_file)
        self.attach_button.pack(pady=10)

        # Progress bar
        self.progress = Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        # Button to send emails
        self.send_button = tk.Button(self.root, bg="#A4152E", fg="white", text="Отправить письма", command=self.send_emails)
        self.send_button.pack(pady=10)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if self.file_path:
            messagebox.showinfo("Файл выбран", f"Выбран файл: {self.file_path}")

    def attach_file(self):
        self.attachment_path = filedialog.askopenfilename()
        if self.attachment_path:
            messagebox.showinfo("Файл прикреплен", f"Прикрепленный файл: {self.attachment_path}")

    def send_emails(self):
        if not self.file_path:
            messagebox.showwarning("Ошибка", "Пожалуйста, выберите файл Excel.")
            return

        # Read Excel file
        try:
            data = pd.read_excel(self.file_path)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")
            return

        # Validate required columns
        if not all(col in data.columns for col in ["Имя", "E-mail", "Компания"]):
            messagebox.showerror("Ошибка", "Файл должен содержать колонки: 'Имя', 'E-mail', 'Компания'.")
            return

        email_subject = self.subject_entry.get().strip()
        email_template = self.email_text.get("1.0", tk.END).strip()

        if not email_subject:
            messagebox.showwarning("Ошибка", "Введите тему письма.")
            return

        if not email_template:
            messagebox.showwarning("Ошибка", "Введите текст письма.")
            return

        # Initialize Outlook
        try:
            outlook = win32.Dispatch('outlook.application')
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при инициализации Outlook: {e}")
            return

        # Progress bar configuration
        total_emails = len(data)
        self.progress["maximum"] = total_emails
        self.progress["value"] = 0

        # Send emails
        for i, row in data.iterrows():
            try:
                # Check for required placeholders
                if "{name}" not in email_template and "{company}" not in email_template:
                    messagebox.showwarning("Ошибка", "В тексте письма должны быть указаны {name} и/или {company}.")
                    return

                personalized_email = email_template.format(name=row['Имя'], company=row['Компания'])

                mail = outlook.CreateItem(0)
                mail.To = row['E-mail']
                mail.Subject = email_subject

                # Preserve line breaks and exact formatting
                formatted_email_body = personalized_email.replace("\n", "<br>").replace("\t", "&emsp;")
                mail.HTMLBody = f"<div style='font-family: Arial; font-size: 11pt; white-space: pre-wrap;'>{formatted_email_body}</div>"

                if self.attachment_path:
                    mail.Attachments.Add(self.attachment_path)

                mail.Send()

                # Update progress bar
                self.progress["value"] = i + 1
                self.root.update_idletasks()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при отправке письма для {row['E-mail']}: {e}")
                return

        messagebox.showinfo("Успех", "Все письма успешно отправлены!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()