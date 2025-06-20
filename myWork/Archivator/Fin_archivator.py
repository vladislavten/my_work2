import os
import time
import subprocess
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === НАСТРОЙКИ ===
SEVEN_ZIP_PATH = "C:\\Program Files\\7-Zip\\7z.exe"
WATCH_FOLDER = "E:\\Shared\\Finance Department\\Password protect\\Original files"
RESULTS_FOLDER = "E:\\Shared\\Finance Department\\Password protect\\Protected files"
ARCHIVE_PASSWORD = "Firfin2025" # Устанавливаем пароль
ARCHIVE_FORMAT = "zip"  # можно изменить на "7z"

# === ОБРАБОТЧИК СОБЫТИЙ ===
class ArchiveHandler(FileSystemEventHandler):
    def on_created(self, event):
        # подождём чуть-чуть, чтобы файлы догрузились
        time.sleep(4)

        if event.is_directory:
            self.process_directory(event.src_path)
        else:
            self.process_file(event.src_path)

    def process_file(self, filepath):
        filename = os.path.basename(filepath)
        zip_path = os.path.join(RESULTS_FOLDER, filename + ".zip")

        print(f"[Файл] Архивируем: {filename}")
        cmd = [SEVEN_ZIP_PATH, 'a', f'-t{ARCHIVE_FORMAT}', f'-p{ARCHIVE_PASSWORD}', zip_path, filepath]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        try:
            os.remove(filepath)
            print(f"[Файл] Удалён: {filename}")
        except Exception as e:
            print(f"❌ Не удалось удалить файл {filename}: {e}")

    def process_directory(self, dirpath):
        dirname = os.path.basename(dirpath.rstrip(os.sep))
        zip_path = os.path.join(RESULTS_FOLDER, dirname + ".zip")

        print(f"[Папка] Архивируем: {dirname}")
        cmd = [SEVEN_ZIP_PATH, 'a', f'-t{ARCHIVE_FORMAT}', f'-p{ARCHIVE_PASSWORD}', zip_path, dirpath]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # подождём, чтобы 7zip точно всё закончил
        time.sleep(5)

        try:
            os.remove(dirpath)
            # shutil.rmtree(dirpath)
            print(f"[Папка] Удалена: {dirname}")
        except Exception as e:
            print(f"❌ Не удалось удалить папку {dirname}: {e}")

# === ОСНОВНОЙ БЛОК ===
if __name__ == "__main__":
    os.makedirs(WATCH_FOLDER, exist_ok=True)
    os.makedirs(RESULTS_FOLDER, exist_ok=True)

    event_handler = ArchiveHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    print("Следим за папкой, как ФСБ за интернетом...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Останавливаемся по CTRL+C.")
    observer.join()
