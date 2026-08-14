import pygame
import math

pygame.init()

boyut = 100
pencere = pygame.display.set_mode((boyut*8,boyut*8))
clock = pygame.time.Clock()

sprite_sheet = pygame.image.load("Chess_Pieces_Sprite.png").convert_alpha()
sprite_genislik = sprite_sheet.get_width() // 6
sprite_yukseklik = sprite_sheet.get_height() // 2

hareket_sesi = pygame.mixer.Sound("move.mp3")
illegal_sesi = pygame.mixer.Sound("illegal.mp3")
check_sesi = pygame.mixer.Sound("check.mp3")

taslar = {
    "beyaz_sah": pygame.transform.scale(sprite_sheet.subsurface((0*sprite_genislik, 0, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "beyaz_vezir": pygame.transform.scale(sprite_sheet.subsurface((1*sprite_genislik, 0, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "beyaz_fil": pygame.transform.scale(sprite_sheet.subsurface((2*sprite_genislik, 0, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "beyaz_at": pygame.transform.scale(sprite_sheet.subsurface((3*sprite_genislik, 0, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "beyaz_kale": pygame.transform.scale(sprite_sheet.subsurface((4*sprite_genislik, 0, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "beyaz_piyon": pygame.transform.scale(sprite_sheet.subsurface((5*sprite_genislik, 0, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "siyah_sah": pygame.transform.scale(sprite_sheet.subsurface((0*sprite_genislik, sprite_yukseklik, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "siyah_vezir": pygame.transform.scale(sprite_sheet.subsurface((1*sprite_genislik, sprite_yukseklik, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "siyah_fil": pygame.transform.scale(sprite_sheet.subsurface((2*sprite_genislik, sprite_yukseklik, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "siyah_at": pygame.transform.scale(sprite_sheet.subsurface((3*sprite_genislik, sprite_yukseklik, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "siyah_kale": pygame.transform.scale(sprite_sheet.subsurface((4*sprite_genislik, sprite_yukseklik, sprite_genislik, sprite_yukseklik)), (boyut, boyut)),
    "siyah_piyon": pygame.transform.scale(sprite_sheet.subsurface((5*sprite_genislik, sprite_yukseklik, sprite_genislik, sprite_yukseklik)), (boyut, boyut)) 
}

tahta = [
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1]
]

tas = [
    ["siyah_kale", "siyah_at", "siyah_fil", "siyah_vezir", "siyah_sah", "siyah_fil", "siyah_at", "siyah_kale"],
    ["siyah_piyon"]*8,
    [None]*8,
    [None]*8,
    [None]*8,
    [None]*8,
    ["beyaz_piyon"]*8,
    ["beyaz_kale", "beyaz_at", "beyaz_fil", "beyaz_vezir", "beyaz_sah", "beyaz_fil", "beyaz_at", "beyaz_kale"]
]

beyazlar = ["beyaz_piyon", "beyaz_kale", "beyaz_at", "beyaz_fil", "beyaz_vezir", "beyaz_sah"]
siyahlar = ["siyah_piyon", "siyah_kale", "siyah_at", "siyah_fil", "siyah_vezir", "siyah_sah"]

renkler = {
    0: (59, 2, 112),
    1: (111, 0, 255)
}

duz_yonler = [(-1,0), (1,0), (0,-1), (0,1)]
capraz_yonler = [(-1,1), (-1,-1), (1,-1), (1,1)]
tum_yonler = [(-1,0), (1,0), (0,-1), (0,1), (-1,1), (-1,-1), (1,-1), (1,1)]
secili_kare = None
sira = True
yol_acik = True
click_satir = None
click_sutun = None

def beyaz_hamle():
    global secili_kare, sira, tas
    eski_tas = tas[click_satir][click_sutun]
    tas[click_satir][click_sutun] = tas[eski_satir][eski_sutun]
    tas[eski_satir][eski_sutun] = None
    secili_kare = None
    if beyaz_sah_tehdit():
        tas[eski_satir][eski_sutun] = tas[click_satir][click_sutun]
        tas[click_satir][click_sutun] = eski_tas
        secili_kare = None
        illegal_sesi.play()
    else:
        sira = False
        if siyah_sah_tehdit():
            print("Şah!")
            check_sesi.play()
        else:
            hareket_sesi.play()
def siyah_hamle():
    global secili_kare, sira, tas
    eski_tas = tas[click_satir][click_sutun]
    tas[click_satir][click_sutun] = tas[eski_satir][eski_sutun]
    tas[eski_satir][eski_sutun] = None
    secili_kare = None
    if siyah_sah_tehdit():
        tas[eski_satir][eski_sutun] = tas[click_satir][click_sutun]
        tas[click_satir][click_sutun] = eski_tas
        secili_kare = None
        illegal_sesi.play()
    else:
        sira = True
        if beyaz_sah_tehdit():
            print("Şah!")
            check_sesi.play()
        else:
            hareket_sesi.play()
    
def gecerli(satir, sutun):
    return 0 <= satir <= 7 and 0 <= sutun <= 7

def beyaz_sah_tehdit():
    for satir_idx, satir in enumerate(tahta):
        for sutun_idx, kare in enumerate(satir):
            if tas[satir_idx][sutun_idx] == "beyaz_sah":
                for satir_yon, sutun_yon in duz_yonler:
                    i = 1
                    while gecerli(satir_idx + satir_yon*i, sutun_idx + sutun_yon*i):
                        hedef = tas[satir_idx + satir_yon*i][sutun_idx + sutun_yon*i]
                        if hedef == "siyah_kale" or hedef == "siyah_vezir":
                            return True
                        elif hedef is not None:
                            break
                        i += 1
                for satir_yon, sutun_yon in capraz_yonler:
                    i = 1
                    while gecerli(satir_idx + satir_yon*i, sutun_idx + sutun_yon*i):
                        hedef = tas[satir_idx + satir_yon*i][sutun_idx + sutun_yon*i]
                        if hedef == "siyah_fil" or hedef == "siyah_vezir":
                            return True
                        elif hedef is not None:
                            break
                        i += 1
                for satir_yon, sutun_yon in tum_yonler:
                    if gecerli(satir_idx + satir_yon, sutun_idx + sutun_yon):
                        if tas[satir_idx + satir_yon][sutun_idx + sutun_yon] == "siyah_sah":
                            return True
                if (gecerli(satir_idx-1, sutun_idx-2) and tas[satir_idx-1][sutun_idx-2] == "siyah_at") or (gecerli(satir_idx-1, sutun_idx+2) and tas[satir_idx-1][sutun_idx+2] == "siyah_at") or (gecerli(satir_idx+1, sutun_idx-2) and tas[satir_idx+1][sutun_idx-2] == "siyah_at") or (gecerli(satir_idx+1, sutun_idx+2) and tas[satir_idx+1][sutun_idx+2] == "siyah_at") or (gecerli(satir_idx-2, sutun_idx-1) and tas[satir_idx-2][sutun_idx-1] == "siyah_at") or (gecerli(satir_idx-2, sutun_idx+1) and tas[satir_idx-2][sutun_idx+1] == "siyah_at") or (gecerli(satir_idx+2, sutun_idx-1) and tas[satir_idx+2][sutun_idx-1] == "siyah_at") or (gecerli(satir_idx+2, sutun_idx+1) and tas[satir_idx+2][sutun_idx+1] == "siyah_at"):
                    return True
                elif (gecerli(satir_idx-1, sutun_idx-1) and tas[satir_idx-1][sutun_idx-1] == "siyah_piyon") or (gecerli(satir_idx-1, sutun_idx+1) and tas[satir_idx-1][sutun_idx+1] == "siyah_piyon"):
                    return True
                else:
                    return False

def siyah_sah_tehdit():
    for satir_idx, satir in enumerate(tahta):
        for sutun_idx, kare in enumerate(satir):
            if tas[satir_idx][sutun_idx] == "siyah_sah":
                for satir_yon, sutun_yon in duz_yonler:
                    i = 1
                    while gecerli(satir_idx + satir_yon*i, sutun_idx + sutun_yon*i):
                        hedef = tas[satir_idx + satir_yon*i][sutun_idx + sutun_yon*i]
                        if hedef == "beyaz_kale" or hedef == "beyaz_vezir":
                            return True
                        elif hedef is not None:
                            break
                        i += 1
                for satir_yon, sutun_yon in capraz_yonler:
                    i = 1
                    while gecerli(satir_idx + satir_yon*i, sutun_idx + sutun_yon*i):
                        hedef = tas[satir_idx + satir_yon*i][sutun_idx + sutun_yon*i]
                        if hedef == "beyaz_fil" or hedef == "beyaz_vezir":
                            return True
                        elif hedef is not None:
                            break
                        i += 1
                for satir_yon, sutun_yon in tum_yonler:
                    if gecerli(satir_idx + satir_yon, sutun_idx + sutun_yon):
                        if tas[satir_idx + satir_yon][sutun_idx + sutun_yon] == "beyaz_sah":
                            return True
                if (gecerli(satir_idx-1, sutun_idx-2) and tas[satir_idx-1][sutun_idx-2] == "beyaz_at") or (gecerli(satir_idx-1, sutun_idx+2) and tas[satir_idx-1][sutun_idx+2] == "beyaz_at") or (gecerli(satir_idx+1, sutun_idx-2) and tas[satir_idx+1][sutun_idx-2] == "beyaz_at") or (gecerli(satir_idx+1, sutun_idx+2) and tas[satir_idx+1][sutun_idx+2] == "beyaz_at") or (gecerli(satir_idx-2, sutun_idx-1) and tas[satir_idx-2][sutun_idx-1] == "beyaz_at") or (gecerli(satir_idx-2, sutun_idx+1) and tas[satir_idx-2][sutun_idx+1] == "beyaz_at") or (gecerli(satir_idx+2, sutun_idx-1) and tas[satir_idx+2][sutun_idx-1] == "beyaz_at") or (gecerli(satir_idx+2, sutun_idx+1) and tas[satir_idx+2][sutun_idx+1] == "beyaz_at"):
                    return True
                elif (gecerli(satir_idx+1, sutun_idx-1) and tas[satir_idx+1][sutun_idx-1] == "beyaz_piyon") or (gecerli(satir_idx+1, sutun_idx+1) and tas[satir_idx+1][sutun_idx+1] == "beyaz_piyon"):
                    return True
                else:
                    return False
                
                
                    
                            
    
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickx, clicky = pygame.mouse.get_pos()
            click_satir = clicky // boyut
            click_sutun = clickx // boyut
            if secili_kare is None:
                if tas[click_satir][click_sutun] is not None and tas[click_satir][click_sutun] in beyazlar and sira == True:
                        secili_kare = (click_satir, click_sutun)
                        print(tas[click_satir][click_sutun], " seçildi")
                if tas[click_satir][click_sutun] is not None and tas[click_satir][click_sutun] in siyahlar and sira == False:
                        secili_kare = (click_satir, click_sutun)
                        print(tas[click_satir][click_sutun], " seçildi")
            else:
                if tas[eski_satir][eski_sutun] == "beyaz_piyon":
                    if (eski_satir == 6) and (eski_sutun == click_sutun) and (eski_satir - click_satir == 2) and (tas[click_satir][click_sutun] == None) and (tas[click_satir + 1][click_sutun] == None):
                        beyaz_hamle()
                    elif (tas[click_satir][click_sutun] == None) and (eski_sutun == click_sutun and eski_satir - click_satir == 1):
                        if click_satir == 0:
                            tas[click_satir][click_sutun] = "beyaz_vezir"
                            tas[eski_satir][eski_sutun] = None
                            secili_kare = None
                            sira = False
                            hareket_sesi.play()
                        else:
                            beyaz_hamle()
                    elif (tas[click_satir][click_sutun] in siyahlar) and ((eski_sutun - click_sutun == 1 and eski_satir - click_satir == 1) or (eski_sutun - click_sutun == -1 and eski_satir - click_satir == 1)):
                        if click_satir == 0:
                            tas[click_satir][click_sutun] = "beyaz_vezir"
                            tas[eski_satir][eski_sutun] = None
                            secili_kare = None
                            sira = False
                            hareket_sesi.play()
                        else:
                            beyaz_hamle()
                    else:
                        secili_kare = None  
                        
                if tas[eski_satir][eski_sutun] == "beyaz_kale":
                    if (eski_satir == click_satir or eski_sutun == click_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in siyahlar):
                        yol_acik = True
                        if eski_satir == click_satir:
                            for sutun in range(min(eski_sutun, click_sutun) + 1, max(eski_sutun, click_sutun)):
                                if tas[eski_satir][sutun] is not None:
                                    yol_acik = False
                                    break
                        else:
                            for satir in range(min(eski_satir, click_satir) + 1, max(eski_satir, click_satir)):
                                if tas[satir][eski_sutun] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            beyaz_hamle()
                        else:
                            secili_kare = None
                    else:
                        secili_kare = None
                        
                if tas[eski_satir][eski_sutun] == "beyaz_fil":
                    if (eski_satir-click_satir == eski_sutun-click_sutun or eski_satir-click_satir == click_sutun-eski_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in siyahlar):
                        yol_acik = True
                        if eski_satir-click_satir > 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir > 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            beyaz_hamle()
                        else:
                            secili_kare = None
                    else:
                        secili_kare = None
                        
                if tas[eski_satir][eski_sutun] == "beyaz_at":
                    if ((abs(eski_satir-click_satir) == 2 and abs(eski_sutun-click_sutun) == 1) or (abs(eski_satir-click_satir) == 1 and abs(eski_sutun-click_sutun) == 2)) and ((tas[click_satir][click_sutun] in siyahlar) or (tas[click_satir][click_sutun] is None)):
                        beyaz_hamle()
                    else:
                        secili_kare = None 
                        
                if tas[eski_satir][eski_sutun] == "beyaz_vezir":
                    if (eski_satir-click_satir == eski_sutun-click_sutun or eski_satir-click_satir == click_sutun-eski_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in siyahlar):
                        yol_acik = True
                        if eski_satir-click_satir > 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir > 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            beyaz_hamle()
                        else:
                            secili_kare = None
                    elif (eski_satir == click_satir or eski_sutun == click_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in siyahlar):
                        yol_acik = True
                        if eski_satir == click_satir:
                            for sutun in range(min(eski_sutun, click_sutun) + 1, max(eski_sutun, click_sutun)):
                                if tas[eski_satir][sutun] is not None:
                                    yol_acik = False
                                    break
                        else:
                            for satir in range(min(eski_satir, click_satir) + 1, max(eski_satir, click_satir)):
                                if tas[satir][eski_sutun] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            beyaz_hamle()
                        else:
                            secili_kare = None
                    else:
                        secili_kare = None
                               
                if tas[eski_satir][eski_sutun] == "beyaz_sah":
                    sahsutun = abs(eski_sutun-click_sutun)
                    sahsatir = abs(eski_satir-click_satir)
                    if (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in siyahlar) and ((sahsutun == 1 and sahsatir == 0) or (sahsutun == 1 and sahsatir == 1) or (sahsutun == 0 and sahsatir == 1)):
                        beyaz_hamle()
                    else:
                        secili_kare = None 
                    
                if tas[eski_satir][eski_sutun] == "siyah_piyon":
                    if (eski_satir == 1) and (eski_sutun == click_sutun) and (eski_satir - click_satir == -2) and (tas[click_satir][click_sutun] == None) and (tas[click_satir - 1][click_sutun] == None):
                        siyah_hamle()
                    elif (tas[click_satir][click_sutun] == None) and (eski_sutun == click_sutun and eski_satir - click_satir == -1):
                        if click_satir == 7:
                            tas[click_satir][click_sutun] = "siyah_vezir"
                            tas[eski_satir][eski_sutun] = None
                            secili_kare = None
                            sira = True 
                            hareket_sesi.play()
                        else: 
                            siyah_hamle()
                    elif (tas[click_satir][click_sutun] in beyazlar) and ((eski_sutun - click_sutun == 1 and eski_satir - click_satir == -1) or (eski_sutun - click_sutun == -1 and eski_satir - click_satir == -1)):
                        if click_satir == 7:
                            tas[click_satir][click_sutun] = "siyah_vezir"
                            tas[eski_satir][eski_sutun] = None
                            secili_kare = None
                            sira = True 
                            hareket_sesi.play()
                        else: 
                            siyah_hamle()
                    else:
                        secili_kare = None
                        
                if tas[eski_satir][eski_sutun] == "siyah_kale":
                    if (eski_satir == click_satir or eski_sutun == click_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in beyazlar):
                        yol_acik = True
                        if eski_satir == click_satir:
                            for sutun in range(min(eski_sutun, click_sutun) + 1, max(eski_sutun, click_sutun)):
                                if tas[eski_satir][sutun] is not None:
                                    yol_acik = False
                                    break
                        else:
                            for satir in range(min(eski_satir, click_satir) + 1, max(eski_satir, click_satir)):
                                if tas[satir][eski_sutun] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            siyah_hamle()
                        else:
                            secili_kare = None
                    else:
                        secili_kare = None
                        
                if tas[eski_satir][eski_sutun] == "siyah_fil":
                    if (eski_satir-click_satir == eski_sutun-click_sutun or eski_satir-click_satir == click_sutun-eski_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in beyazlar):
                        yol_acik = True
                        if eski_satir-click_satir > 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir > 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            siyah_hamle()
                        else:
                            secili_kare = None
                    else:
                        secili_kare = None
                        
                if tas[eski_satir][eski_sutun] == "siyah_at":
                    if ((abs(eski_satir-click_satir) == 2 and abs(eski_sutun-click_sutun) == 1) or (abs(eski_satir-click_satir) == 1 and abs(eski_sutun-click_sutun) == 2)) and ((tas[click_satir][click_sutun] in beyazlar) or (tas[click_satir][click_sutun] is None)):
                        siyah_hamle()
                    else:
                        secili_kare = None  
                        
                if tas[eski_satir][eski_sutun] == "siyah_vezir":
                    if (eski_satir-click_satir == eski_sutun-click_sutun or eski_satir-click_satir == click_sutun-eski_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in beyazlar):
                        yol_acik = True
                        if eski_satir-click_satir > 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun > 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun-i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir < 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, click_satir-eski_satir):
                                if tas[eski_satir+i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        elif eski_satir-click_satir > 0 and eski_sutun-click_sutun < 0:
                            for i in range(1, eski_satir-click_satir):
                                if tas[eski_satir-i][eski_sutun+i] is not None:
                                    yol_acik = False
                                    break
                        else:
                            secili_kare = None
                        if yol_acik:
                            siyah_hamle()
                    elif (eski_satir == click_satir or eski_sutun == click_sutun) and (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in beyazlar):
                        yol_acik = True
                        if eski_satir == click_satir:
                            for sutun in range(min(eski_sutun, click_sutun) + 1, max(eski_sutun, click_sutun)):
                                if tas[eski_satir][sutun] is not None:
                                    yol_acik = False
                                    break
                        else:
                            for satir in range(min(eski_satir, click_satir) + 1, max(eski_satir, click_satir)):
                                if tas[satir][eski_sutun] is not None:
                                    yol_acik = False
                                    break
                        if yol_acik:
                            siyah_hamle()
                        else:
                            secili_kare = None
                    else:
                        secili_kare = None
                        
                if tas[eski_satir][eski_sutun] == "siyah_sah":
                    sahsutun = abs(eski_sutun-click_sutun)
                    sahsatir = abs(eski_satir-click_satir)
                    if (tas[click_satir][click_sutun] == None or tas[click_satir][click_sutun] in beyazlar) and ((sahsutun == 1 and sahsatir == 0) or (sahsutun == 1 and sahsatir == 1) or (sahsutun == 0 and sahsatir == 1)):
                        siyah_hamle()
                    else:
                        secili_kare = None 
                    
                        
    # Do logical updates here.
    # ...
    
    imlecx, imlecy = pygame.mouse.get_pos()
    imlec_satir = imlecy // boyut
    imlec_sutun = imlecx // boyut

    #Render graphics
    for satir_idx, satir in enumerate(tahta):
        for sutun_idx, kare in enumerate(satir):
            x = sutun_idx * boyut
            y = satir_idx * boyut
            if pygame.mouse.get_focused() and sutun_idx == imlec_sutun and satir_idx == imlec_satir:
                pygame.draw.rect(pencere, (150, 41, 241), (x, y, boyut, boyut))
            else:
                renk = renkler.get(kare, (0,0,0))
                pygame.draw.rect(pencere, renk, (x, y, boyut, boyut))
            if secili_kare is not None:
                eski_satir, eski_sutun = secili_kare
                if tas[eski_satir][eski_sutun] == "beyaz_piyon" and eski_satir == 6:
                    if (tas[satir_idx][sutun_idx] is None) and (satir_idx == eski_satir - 1) and sutun_idx == eski_sutun:
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                    if (tas[satir_idx][sutun_idx] is None) and (satir_idx == eski_satir - 2) and sutun_idx == eski_sutun:
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                    if (tas[satir_idx][sutun_idx] in siyahlar) and ((satir_idx-eski_satir == -1 and sutun_idx-eski_sutun == -1) or (satir_idx-eski_satir == -1 and sutun_idx-eski_sutun == 1)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                elif tas[eski_satir][eski_sutun] == "beyaz_piyon":
                    if (tas[satir_idx][sutun_idx] is None) and (satir_idx == eski_satir - 1) and sutun_idx == eski_sutun:
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                    if (tas[satir_idx][sutun_idx] in siyahlar) and ((satir_idx-eski_satir == -1 and sutun_idx-eski_sutun == -1) or (satir_idx-eski_satir == -1 and sutun_idx-eski_sutun == 1)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                if tas[eski_satir][eski_sutun] == "siyah_piyon" and eski_satir == 1:
                    if (tas[satir_idx][sutun_idx] is None) and (satir_idx == eski_satir + 1) and sutun_idx == eski_sutun:
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                    if (tas[satir_idx][sutun_idx] is None) and (satir_idx == eski_satir + 2) and sutun_idx == eski_sutun:
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                    if (tas[satir_idx][sutun_idx] in beyazlar) and ((satir_idx-eski_satir == 1 and sutun_idx-eski_sutun == -1) or (satir_idx-eski_satir == 1 and sutun_idx-eski_sutun == 1)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                elif tas[eski_satir][eski_sutun] == "siyah_piyon":
                    if (tas[satir_idx][sutun_idx] is None) and (satir_idx == eski_satir + 1) and sutun_idx == eski_sutun:
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                    if (tas[satir_idx][sutun_idx] in beyazlar) and ((satir_idx-eski_satir == 1 and sutun_idx-eski_sutun == -1) or (satir_idx-eski_satir == 1 and sutun_idx-eski_sutun == 1)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)
                if tas[eski_satir][eski_sutun] == "beyaz_at":
                    if (tas[satir_idx][sutun_idx] is None or tas[satir_idx][sutun_idx] in siyahlar) and ((abs(sutun_idx-eski_sutun) == 2 and abs(satir_idx-eski_satir) == 1) or (abs(sutun_idx-eski_sutun) == 1 and abs(satir_idx-eski_satir) == 2)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5)   
                if tas[eski_satir][eski_sutun] == "siyah_at":
                    if (tas[satir_idx][sutun_idx] is None or tas[satir_idx][sutun_idx] in beyazlar) and ((abs(sutun_idx-eski_sutun) == 2 and abs(satir_idx-eski_satir) == 1) or (abs(sutun_idx-eski_sutun) == 1 and abs(satir_idx-eski_satir) == 2)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5) 
                if tas[eski_satir][eski_sutun] == "beyaz_sah":
                    sahsutun = abs(eski_sutun-sutun_idx)
                    sahsatir = abs(eski_satir-satir_idx)
                    if (tas[satir_idx][sutun_idx] == None or tas[satir_idx][sutun_idx] in siyahlar) and ((sahsutun == 1 and sahsatir == 0) or (sahsutun == 1 and sahsatir == 1) or (sahsutun == 0 and sahsatir == 1)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5) 
                if tas[eski_satir][eski_sutun] == "siyah_sah":
                    sahsutun = abs(eski_sutun-sutun_idx)
                    sahsatir = abs(eski_satir-satir_idx)
                    if (tas[satir_idx][sutun_idx] == None or tas[satir_idx][sutun_idx] in beyazlar) and ((sahsutun == 1 and sahsatir == 0) or (sahsutun == 1 and sahsatir == 1) or (sahsutun == 0 and sahsatir == 1)):
                        pygame.draw.rect(pencere,(255,255,255), (x, y, boyut, boyut), 5) 
            tas_adi = tas[satir_idx][sutun_idx]
            if tas_adi is not None:
                pencere.blit(taslar[tas_adi], (x, y))
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)