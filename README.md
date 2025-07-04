# 📁 FileGenie: Python File Organizer

**FileGenie** is a lightweight Python automation script that organizes messy folders by sorting files into categories like Documents, Images, Videos, Archives, and more — all based on file extensions.

---

## 🚀 Features

- Automatically moves files into categorized folders
- Supports common file types: `.pdf`, `.jpg`, `.mp4`, `.zip`, `.py`, and more
- Easy to customize and extend (add new categories or rules)
- Built with core Python modules: `os`, `shutil`, and `datetime`

---

## 🛠️ How It Works

The script scans a target folder and:
1. Identifies the file type using its extension
2. Creates folders for each file type (if they don’t exist)
3. Moves each file into the appropriate folder

---

## 📂 File Categories Handled

| Category     | Extensions                           |
|--------------|---------------------------------------|
| Documents    | `.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx` |
| Images       | `.jpg`, `.jpeg`, `.png`, `.gif`       |
| Videos       | `.mp4`, `.mkv`, `.avi`                |
| Music        | `.mp3`, `.wav`                        |
| Archives     | `.zip`, `.rar`, `.tar`, `.gz`         |
| Executables  | `.exe`, `.msi`                        |
| Scripts      | `.py`, `.js`, `.html`, `.css`         |

---

## ✅ How to Use

1. Clone or download the repo.
2. Modify the `TARGET_FOLDER` path in `filegenie.py` to the folder you want to organize.
3. Run the script:

```bash
python filegenie.py
Before running the script-
TestFiles/
├── resume.pdf
├── image.png
├── song.mp3
After running the script-
TestFiles/
├── Documents/
│   └── resume.pdf
├── Images/
│   └── image.png
├── Music/
│   └── song.mp3
