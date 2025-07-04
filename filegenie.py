import os
import shutil

# ✅ Set the path to the test folder (change this to your actual test location)
TARGET_FOLDER = r'C:\Users\dell\Desktop\TestFiles'  # <- Update this path if needed

# ✅ Define file categories and associated extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

# ✅ Create folders for each category if they don't exist
def create_folders(base_path):
    for folder in FILE_CATEGORIES:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# ✅ Move files into their categorized folders
def organize_files(base_path):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(base_path, category)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"📁 Moved '{file}' → {category}")
                    moved = True
                    break
            if not moved:
                print(f"❌ Skipped '{file}' (Uncategorized)")

# ✅ Run the organizer
if __name__ == "__main__":
    print("📂 Organizing files in:", TARGET_FOLDER)
    create_folders(TARGET_FOLDER)
    organize_files(TARGET_FOLDER)
    print("✅ File organization complete.")
