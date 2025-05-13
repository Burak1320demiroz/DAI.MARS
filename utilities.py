"""
DAİ.MARS
Copyright (c) 2025 Burak Demiröz

Licensed under the MIT License (see LICENSE for details)
"""

def clear_screen():
    print("\033[H\033[J")

def print_header(title):
    print("\033[95m" + "═" * 60)
    print(f"■ {title.upper()} ■".center(60))
    print("═" * 60 + "\033[0m\n")

def progress_bar(value, max_value, color, label):
    bar_length = 30
    filled = int(round(bar_length * value / max_value))
    bar = f"{color}▓" * filled + "░" * (bar_length - filled)
    return f"\033[97m{label}: \033[0m{bar} {value}/{max_value}"

def show_status(state):
    clear_screen()
    print_header("astronot durum paneli")
    
    print(progress_bar(state['su'], 100, "\033[94m", "Su"))
    print(progress_bar(state['enerji'], 100, "\033[93m", "Enerji"))
    print(progress_bar(state['gida'], 30, "\033[92m", "Gıda"))
    print(progress_bar(state['patates'], 50, "\033[33m", "Patates"))
    
    print("\n\033[97mENVANTER:\033[0m")
    print(" ".join([f"[\033[96m{item}\033[0m]" for item in state['inventory']]) if state['inventory'] else "Boş")
    input("\nDevam etmek için Enter'a basın...")

def location_art(location):
    arts = {
        "Kaza Alanı": [
            r"   ___   ",
            r"  /   \  ",
            r" |  X  | ",
            r"  \___/  ",
            r"  /| |\  ",
            r" /_| |_\ "
        ],
        "İletişim Merkezi": [
            r"  ╔════╗ ",
            r"  ║ δ= ║ ",
            r"  ╚════╝ ",
            r"   /▲\   ",
            r"  /_■_\  "
        ],
        "Ana Yaşam Modülü": [
            r"  ░▒▓███ ",
            r" █▓▒░░▒▓█",
            r" █░░◯░░█ ",
            r" █▓▒░▒▓█ ",
            r"  ▀▀▀▀▀  "
        ]
    }
    print("\033[90m" + "\n".join(arts.get(location, [])) + "\033[0m")