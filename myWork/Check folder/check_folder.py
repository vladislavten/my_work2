import os

folder_path = "general"  # замените на путь к вашей папке

while True:
    folder_size = sum(os.path.getsize(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
    if folder_size > 1024:
        print("Folder size exceeds 1KB. Deleting files...")
        for f in os.listdir(folder_path):
            file_path = os.path.join(folder_path, f)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    else:
        print(f"Folder size: {folder_size} bytes")