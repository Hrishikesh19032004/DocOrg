categories = {
    "Documents": [
        ".doc", ".docx", ".pdf", ".ppt", ".pptx", ".txt",
        ".xls", ".xlsx", ".csv", ".md", ".rtf", ".odt"
    ],

    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff",
        ".webp", ".svg", ".heic"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"
    ],

    "Music": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tar.gz"
    ],

    "Code": [
        ".py", ".cpp", ".c", ".h", ".java", ".js", ".jsx", ".ts", ".tsx",
        ".html", ".css", ".scss", ".yml", ".yaml",
        ".sql", ".ipynb", ".sh", ".bat"
    ],

    "Executables": [
        ".exe", ".msi", ".app", ".apk", ".deb", ".rpm"
    ],

    "Data": [
        ".json", ".xml", ".csv", ".parquet", ".avro", ".feather"
    ],

    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2"
    ],

    "Design": [
        ".psd", ".ai", ".fig", ".sketch", ".xd"
    ],

    "3D_Models": [
        ".obj", ".stl", ".fbx", ".blend", ".3ds"
    ],

    "Disk_Images": [
        ".iso", ".img", ".dmg"
    ],

    "Ebooks": [
        ".epub", ".mobi", ".azw3"
    ]
}


def categorise(file):
    for category, extensions in categories.items():
        if file.lower().endswith(tuple(extensions)):
            return category
    return "Others"