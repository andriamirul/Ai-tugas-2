# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

def gaji(inp):
    rendah = 0
    tinggi = 0
    if inp < 0.747:
        rendah = (inp-0)/(0.747-0)
    elif inp ==0.747:
        rendah = 0.9035
    elif (inp > 0.747) and (inp <1.06): 
        rendah = (1.06-inp)/(0.747-1.06)
        tinggi = (inp-0.747)/(0.747-1.06)
    elif inp >= 1.06:
        tinggi = 1
    return rendah,tinggi

def deFuzzy(iya,tidak):
    if (iya > 0 and tidak > 0):
        return ((iya*75)+(tidak*35))/(iya+tidak)
    elif iya > 0:
        return (iya*75)/iya
    elif tidak > 0:
        return (tidak*35)/tidak
    else:
        return 0

def hutang(hut):
    rendah = 0
    tinggi = 0
    if hut <= 25:
        rendah = 1
    elif (hut <= 40 and hut>=25):
        rendah = (40-hut)/(40-25)
        tinggi = (hut-25)/(40-25)
    elif (hut >= 40):
        tinggi=1
    return rendah,tinggi

def Fuzzy(PendapatanRendah,PendapatanTinggi,HutangRendah,HuangTinggi):
    tidak = [0,0]
    iya = [0,0]
    if (PendapatanRendah > 0 and HutangRendah > 0):
        iya[0] = min(PendapatanRendah,HutangRendah)
    if (PendapatanRendah > 0 and HutangTinggi > 0):
        iya[1] = min(PendapatanRendah,HutangTinggi)
    if (PendapatanTinggi > 0 and HutangRendah > 0):
        tidak[0] = min(PendapatanTinggi,HutangRendah)
    if (PendapatanTinggi > 0 and HutangTinggi > 0):
        tidak[1] = min(PendapatanTinggi,HutangTinggi)
    return max(iya),max(tidak)
       

hasilnyaeuy = []
with open('C:/Users/andri/Desktop/DataTugas2.csv') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',') 
    next(csv_reader)
    for row in csv_reader:
        PendapatanRendah,PendapatanTinggi = gaji(float(row[1]))
        HutangRendah,HutangTinggi = hutang(float(row[2]))
        iya,tidak = Fuzzy(PendapatanRendah,PendapatanTinggi,HutangRendah,HutangTinggi)
        layak = deFuzzy(iya,tidak)
        print(layak)
        if layak>=75:
            hasilnyaeuy.append(row[0])
    

        
with open('TebakanTugas2.csv','w',newline='') as f:
    csv_writer = csv.writer(f)
    for row in hasilnyaeuy :
        csv_writer.writerow([row])
        
    
        