"""
DAİ.MARS
Copyright (c) 2023 Your Name

Licensed under the MIT License (see LICENSE for details)
"""

from utilities import clear_screen, print_header, progress_bar, show_status
from locations import location_art, handle_location_action
from resources import consume_resource
from story import hikaye_giris
import sys

# Oyun durumlarını tutan global değişkenler
game_state = {
    "su": 75,
    "patates": 30,
    "gida": 15,
    "enerji": 65,
    "anten_parcasi": False,
    "iletisim_kuruldu": False,
    "current_room": "Kaza Alanı",
    "inventory": []
}

def start_game():
    hikaye_giris(game_state)
    
    while True:
        clear_screen()
        print_header(f"{game_state['current_room']} - ana menü")
        location_art(game_state['current_room'])
        
        print("\033[97m[1] Durum Raporu")
        print("[2] Haritayı Aç")
        print("[3] Kaynak Kullan")
        print("[4] Bölgeyi İncele")
        print("[5] İletişim Sistemini Dene")
        print("[0] Çıkış\033[0m")
        
        secim = input("\n\033[97m» Seçiminiz: \033[0m")
        
        if secim == "1":
            show_status(game_state)
        elif secim == "2":
            handle_map_navigation(game_state)
        elif secim == "3":
            consume_resource(game_state)
        elif secim == "4":
            handle_location_action(game_state)
        elif secim == "5":
            handle_communication(game_state)
        elif secim == "0":
            print("\n\033[97mGörev sonlandırılıyor...\033[0m")
            sys.exit()
        else:
            print("\033[91mGeçersiz seçim!\033[0m")
            time.sleep(1)
        
        update_resources(game_state)

def handle_map_navigation(state):
    from locations import show_map
    show_map(state)

def handle_communication(state):
    from communication import try_communication
    try_communication(state)

def update_resources(state):
    state['su'] = max(0, state['su']-2)
    state['enerji'] = max(0, state['enerji']-5)
    if state['su'] <=0 or state['enerji'] <=0:
        print("\033[91mHAYATİ KAYIP: Yaşam destek sistemleri durdu!\033[0m")
        sys.exit()