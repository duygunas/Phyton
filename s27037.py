#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:33:06 2023

@author: duygunas
no: s27037
"""

def sifre_kontrolu(sifre):
    if len(sifre) < 4:
        return "Şifre çok kısa", False
    elif len(sifre) > 8:
        return "Şifre en fazla 8 karakter olabilir", False
    
    kucuk_harf_var = any(c.islower() for c in sifre)
    buyuk_harf_var = any(c.isupper() for c in sifre)
    rakam_var = any(c.isdigit() for c in sifre)
    ozel_karakter_var = any(c in '()*+,-.' for c in sifre)
    gecersiz_karakter_var = any(c not in '()*+,-.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for c in sifre)

    if not kucuk_harf_var:
        return "Şifre en az bir küçük harf içermeli", False
    elif not buyuk_harf_var:
        return "Şifre en az bir büyük harf içermeli", False
    elif not rakam_var:
        return "Şifre en az bir rakam içermeli", False
    elif not ozel_karakter_var:
        return "Şifre izin verilen özel karakterlerden en az birini içermeli", False
    elif gecersiz_karakter_var:
        return "Şifre yalnızca sayı, harf ve izin verilen özel karakterlerden oluşmalı", False
    else:
        return "Geçerli Şifre", True

def sifre_gucluluk_skoru(sifre):
    kucuk_harf_sayisi = sum(c.islower() for c in sifre)
    buyuk_harf_sayisi = sum(c.isupper() for c in sifre)
    rakam_sayisi = sum(c.isdigit() for c in sifre)
    ozel_karakter_sayisi = sum(c in '()*+,-.' for c in sifre)

    skor = 3 * (kucuk_harf_sayisi + 1) * 5 * (buyuk_harf_sayisi + 1) * 2 * (rakam_sayisi + 1) * 4 * (ozel_karakter_sayisi + 1) - 120
    return skor

def sifre_gucluluk_degerlendirmesi(skor):
    if skor < 2000:
        return "Çok Zayıf Şifre"
    elif skor < 4000:
        return "Zayıf Şifre"
    elif skor < 6000:
        return "Ortalama Şifre"
    elif skor < 9000:
        return "Güçlü Şifre"
    else:
        return "Çok Güçlü Şifre"

# Kullanıcıdan şifre girdisi alınır
sifre = input("Bir şifre giriniz: ")
kontrol_sonucu, gecerli_mi = sifre_kontrolu(sifre)

if gecerli_mi:
    skor = sifre_gucluluk_skoru(sifre)
    print("Geçerli Şifre")
    print(sifre_gucluluk_degerlendirmesi(skor))
else:
    print("Geçersiz Şifre")
    print(kontrol_sonucu)

