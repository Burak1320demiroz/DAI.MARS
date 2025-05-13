"""
DAİ.MARS
Copyright (c) 2023 Burak Demiröz

Licensed under the MIT License (see LICENSE for details)
"""

def consume_resource(state):
    print("\n\033[92m--- KAYNAKLAR ---")
    print("1. Su İç (-10L, +5% Enerji)")
    print("2. Patates Ye (-5kg, +10% Enerji)")
    print("3. Gıda Paketi Tüket (-2 paket, +15% Enerji)")
    print("0. Geri Dön\033[0m")
    
    kaynak = input("Seçiminiz: ")
    if kaynak == "1":
        if state['su'] >=10:
            state['su'] -=10
            state['enerji'] = min(100, state['enerji']+5)
            print("\nSoğuk suyu yudumluyorsun...")
        else:
            print("\033[91mYeterli su yok!\033[0m")
    elif kaynak == "2":
        if state['patates'] >=5:
            state['patates'] -=5
            state['enerji'] = min(100, state['enerji']+10)
            print("\nÇiğ patates çıtır çıtır...")
        else:
            print("\033[91mYeterli patates yok!\033[0m")
    elif kaynak == "3":
        if state['gida'] >=2:
            state['gida'] -=2
            state['enerji'] = min(100, state['enerji']+15)
            print("\nKonserve gıda mideni dolduruyor...")
        else:
            print("\033[91mYeterli gıda paketi yok!\033[0m")