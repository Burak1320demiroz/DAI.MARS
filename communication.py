"""
DAİ.MARS
Copyright (c) 2025 Burak Demiröz

Licensed under the MIT License (see LICENSE for details)
"""

import random
import time

def try_communication(state):
    if state['current_room'] == "İletişim Merkezi" and state['iletisim_kuruldu']:
        print("\n\033[92mSinyal gücü: %65... Frekans ayarlanıyor...\033[0m")
        time.sleep(1)
        print("1. SOS sinyali gönder")
        print("2. Manuel frekans dene")
        
        if input("Seçim: ") == "2":
            print("\nFrekans taraması başlıyor...")
            for i in range(3):
                print(f"{i+1}. Deneme...")
                time.sleep(1)
            if random.randint(1,10) >3:
                print("\033[92mDünya ile bağlantı kuruldu! Kurtarma ekibi yolda!\033[0m")
                print("=== OYUNU KAZANDINIZ ===")
                sys.exit()
            else:
                print("\033[91mBağlantı başarısız! Tekrar dene!\033[0m")
    else:
        print("\033[91mİletişim sistemi çalışmıyor!\033[0m")