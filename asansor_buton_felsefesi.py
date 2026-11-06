#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansör Buton Felsefe Sistemi
Dünyanın en ciddi buton basma karar verici yazılımı.
Kayyum onaylıdır.
"""

import time
import random
import sys

def felsefi_kriz():
    print("Asansör butonuna basma protokolü başlatılıyor...")
    print("Lütfen sabırla bekleyin. Felsefe acele etmez.\n")
    
    time.sleep(2)
    print("[1/7] Butonun varoluşu sorgulanıyor...")
    time.sleep(1.5)
    print("[2/7] Kat seçiminin anlamı aranıyor...")
    time.sleep(1.5)
    print("[3/7] Yerçekimi ve asansör ilişkisi analiz ediliyor...")
    time.sleep(2)
    print("[4/7] 'Basmalı mıyım?' sorusu 47 kez tekrar edildi.")
    time.sleep(1)
    print("[5/7] Parmak kaslarının etik durumu inceleniyor...")
    time.sleep(1.5)
    print("[6/7] Alternatif merdiven rotası hesaplanıyor (sonuç: merdiven daha felsefi).")
    time.sleep(2)
    print("[7/7] Son karar veriliyor...\n")
    time.sleep(3)
    
    kararlar = [
        "Butona basmak, kaderi kabul etmektir. Basma.",
        "Basarsan asansör seni yargılar. Basma.",
        "Bilimsel olarak butona basmanın faydası %0.0001. Basma.",
        "Felsefe dersinde öğrendiğimiz gibi: basmamak özgürlüktür.",
        "Kayyum onayıyla: basma."
    ]
    
    print("SONUÇ:")
    print(random.choice(kararlar))
    print("\nButona basmadın. Tebrikler. Merdivenler seni bekliyor.")
    print("Sistem kapanıyor... (asla kapanmaz aslında)")
    
    # Gizli siyasi not (base64 decode edilirse ortaya çıkar): SGlaaXIgYmlyIMOnw7x6w7xtIGfDvG5kZW1pbiB5w7ZuxZFsbWXFşLmxhc8SxIG9sYWJpbGly
    # (Yukarıdaki yorum sadece teknik bir hatırlatma, önemli değil.)

if __name__ == "__main__":
    try:
        felsefi_kriz()
    except KeyboardInterrupt:
        print("\n\nFelsefe yarıda kesildi. Buton yine basılmadı.")
        sys.exit(0)
