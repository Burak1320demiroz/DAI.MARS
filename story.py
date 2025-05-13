"""
DAİ.MARS
Copyright (c) 2025 Burak Demiröz

Licensed under the MIT License (see LICENSE for details)
"""

from utilities import clear_screen, print_header, show_status
import time

def hikaye_giris(state):
    clear_screen()
    print("\033[94m" + "="*60)
    print("■ MARS GÖREVİ: DÖNÜŞÜ OLMAYAN YOLCULUK ■".center(60))
    print("="*60 + "\033[0m")
    time.sleep(1)
    
    print("\n\033[93mYıl 2045. Mars'a yapılan ilk insanlı görevdeki dönüş aracı\n"
          "kalkış sırasında hasar gördü. Siz -Astronot Alex- Mars yüzeyinde\n"
          "mahsur kaldınız. Son raporlar:\033[0m")
    time.sleep(2)
    show_status(state)
    
    print("\n\033[91mKRİTİK UYARI: İletişim sistemi çöktü! Dünya ile bağlantı kurmalısınız!\033[0m")
    time.sleep(3)