"""
DAİ.MARS
Copyright (c) 2025 Burak Demiröz

Licensed under the MIT License (see LICENSE for details)
"""

from utilities import clear_screen, print_header, location_art
import time

def show_map(state):
    while True:
        clear_screen()
        print_header("mars üssü haritası")
        location_art(state['current_room'])
        print("\n\033[97m[1] Kaza Alanı\033[0m" + (" ← Şu anki konum" if state['current_room'] == "Kaza Alanı" else ""))
        print("\033[97m[2] Ana Yaşam Modülü\033[0m" + (" ← Şu anki konum" if state['current_room'] == "Ana Yaşam Modülü" else ""))
        print("\033[97m[3] İletişim Merkezi\033[0m" + (" ← Şu anki konum" if state['current_room'] == "İletişim Merkezi" else ""))
        print("\033[97m[4] Sera Alanı\033[0m" + (" ← Şu anki konum" if state['current_room'] == "Sera Alanı" else ""))
        print("\033[97m[5] Malzeme Deposu\033[0m" + (" ← Şu anki konum" if state['current_room'] == "Malzeme Deposu" else ""))
        print("\n\033[97m[0] Geri Dön\033[0m")

        try:
            hedef = int(input("\n\033[97m» Gitmek istediğiniz bölge: \033[0m"))
            odalar = ["", "Kaza Alanı", "Ana Yaşam Modülü", "İletişim Merkezi", "Sera Alanı", "Malzeme Deposu"]
            
            if hedef == 0:
                break
            elif 1 <= hedef <=5:
                state['current_room'] = odalar[hedef]
                state['enerji'] -= 15
                print(f"\n\033[97m{odalar[hedef]}'e gidiliyor...\033[0m")
                time.sleep(1)
                if state['enerji'] <=0:
                    print("\033[91mKRİTİK: Enerjiniz bitti! Hayatta kalamadınız!\033[0m")
                    sys.exit()
                break
            else:
                print("\033[91mGeçersiz bölge!\033[0m")
                time.sleep(1)
        except:
            print("\033[91mHatalı giriş!\033[0m")
            time.sleep(1)

def handle_location_action(state):
    if state['current_room'] == "Kaza Alanı" and not state['anten_parcasi']:
        print("\nEnkazın içinde parlayan bir metal görüyorsun...")
        time.sleep(1)
        print("1. Yakından incele")
        print("2. Göz ardı et")
        if input("Seçim: ") == "1":
            print("\nKırık iletişim anteni buldun! Envantere eklendi.")
            state['inventory'].append("Anten Parçası")
            state['anten_parcasi'] = True
    
    elif state['current_room'] == "İletişim Merkezi":
        print("\n\033[96mBOZUK İLETİŞİM KONSOLU: 'Anten bağlantısı yok' hatası veriyor.\033[0m")
        if "Anten Parçası" in state['inventory']:
            print("1. Anteni takmayı dene")
            if input("Seçim: ") == "1":
                print("\nAnteni yerleştiriyorsun...")
                time.sleep(2)
                print("Kıvılcımlar çakmaya başlıyor!")
                state['iletisim_kuruldu'] = True