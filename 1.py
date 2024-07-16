import argparse
from pathlib import Path
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для піддиректорії
                copy_files(item, dst)
            else:
                # Копіювання файлу
                extension = item.suffix[1:] # Видаляємо крапку перед розширенням
                if extension:
                    new_dir = dst / extension
                    new_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, new_dir / item.name)
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    args = parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)  # Створюємо директорію призначення, якщо вона не існує
    copy_files(args.source, args.dest)

if __name__ == "__main__":
    main()
