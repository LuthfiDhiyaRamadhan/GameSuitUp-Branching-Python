import random
komputer = random.choice (['G','K','B'])
#print(f"Komputer memilih{komputer}")
print("Komputer telah memilih. Sekarang giliran anda")
player = input(" Pilihan Anda {G,K,B}").upper()
#draw=0, komputer menang=1,player menang=2
if (komputer=="G") and (player=="G"):
    pemenang = 0
elif(komputer == "G") and (player == "k"):
    pemenang = 1
elif(komputer=="G") and (player=="B"):
    pemenang = 2
elif komputer =="K":
    if player == "G":
        pemenang = 2
    elif player == "K":
        pemenang=0
    elif player == "B":
        pemenang=1
elif komputer =="B":
    if player=="G":
        pemenang=1
    elif player=="K":
        pemenang=2
    elif player=="B":
        pemenang=0

if pemenang==0:
   print("Draw")
elif pemenang==1:
    print("Anda Kalah")
elif pemenang==2:
    print("Anda Menang")