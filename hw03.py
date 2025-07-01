#!/usr/bin/env python
"""
Виводить дерево директорії у кольорах:
- каталоги – синій
- файли     – зелений

Використання:
    python hw03.py <path>
"""
import sys
from pathlib import Path
from colorama import init, Fore, Style


def walk(directory: Path, depth: int = 0) -> None:
    """
    Рекурсивно обходить дерево директорії та друкує його зміст.

    directory : Path  – каталог, що обробляється
    depth     : int   – поточний рівень вкладеності (для відступу)
    """
    indent = "    " * depth
    # Сортуємо: спочатку каталоги, потім файли – для стабільного виводу
    for entry in sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower())):
        if entry.is_dir():
            print(f"{indent}{Fore.BLUE}{entry.name}/ {Style.RESET_ALL}")
            walk(entry, depth + 1)
        else:
            print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main() -> None:
    # Перевірка аргументів
    if len(sys.argv) != 2:
        print("Usage: python hw03.py <directory_path>")
        sys.exit(1)

    target = Path(sys.argv[1]).expanduser().resolve()

    if not target.exists():
        print(f"Error: path '{target}' does not exist")
        sys.exit(1)
    if not target.is_dir():
        print(f"Error: path '{target}' is not a directory")
        sys.exit(1)

    init()  # ініціалізація colorama
    walk(target)


if __name__ == "__main__":
    main()
