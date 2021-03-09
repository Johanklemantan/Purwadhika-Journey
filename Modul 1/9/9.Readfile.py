data = open('./9/katadalam.txt', 'r') # r = read
print(data.read())

text = data.read()
print(text)

lines = data.readlines(6)
print(lines)
for line in lines:
    print(line)


# data2 = open('./9/kata2.txt','w') #w = write #paling luar
# data2.write('Ini dibuat di Python') #./9/ itu tempat lokasi folder (pake titik)

# data3 = open('./9/kata3.py','w') #w = write
# data3.write('print(''Ini dibuat di Python)')# kalo polosan, otomatis di create paling luar.

# abc = open('./9/nama.txt','r')
# # text = (abc.read()).replace(',',' ') # dalam string biasa

# # print(text)
# text_list = (abc.read()).split(',') # dalam list
# print(text_list)

# list_nama = open('./9/list_nama.txt','w')
# for i in text_list:
#     list_nama.write(f'{i}\n')

data_diri = open('./9/daftar_nama.csv','r')
x = data_diri.read().split('\n')
# print('x awal :', x)

header_list = x[0]
# print('header list :', header_list)
header_element = header_list.split(',')
# print('header element : ', header_element)

value_list = x[1:]
# print('value list: ', value_list)

data = []
for i in value_list: #['Andi,21,Jakarta', 'Budi,22,Bandung', 'Caca,23,Semarang']
    a = i.split(',')
    header_value = dict(zip(header_element, a))
    data.append(header_value)
    # print(header_value)
# print('hasil akhir jadi dict :', data)

#MULAI KACAO 


json = open('./9/daftar_nama.json','r') 
print(json.read())
print()
print(type(json.read()))

import json #PAKE SHIFT + ALT + F biar lebih rapi bentukannya.

with open('./9/daftar_nama.json',mode='r') as daftar:
    output = json.load(daftar)

print(output[0])
print()
print(type(output))
for i in range(len(output)):
    print(output[i])

print()
print('untuk append :')
output.append({'nama':'Dede', 'usia': 24, 'kota' : 'Bekasi'})
print(output)
with open('./9/daftar_nama_update.json',mode='w') as update:
    json.dump(output, update)

import csv

list_data = []
with open('./9/daftar_nama.csv','r') as nama:
    read = csv.DictReader(nama)
    for data in read:
        list_data.append(dict(data))

print(list_data)
list_data.append({'nama':'Dede', 'usia': 24, 'kota' : 'Bekasi'})
print(list_data)

with open('./9/daftar_nama_update.csv','w') as update:
    colums = list_data[2].keys()
    write = csv.DictWriter(update,fieldnames=colums) #harus pake fieldnames.
    write.writeheader() #write headernya
    write.writerows(list_data) #write rowsnya.


'''
Import data dari JSON ke CSV ==> json_to_csv.csv

Import data dari CSV ke JSON ==> csv_to_json.json

'''

dari_json = open('./9/daftar_nama_update.json','r')
ke_csv = open('./9/json_to_csv.csv','w')

# colums = list_data[0].keys()
write = csv.DictWriter(ke_csv,fieldnames=colums) #harus pake fieldnames.
write.writeheader() #write headernya
write.writerows(list_data) #write rowsnya.




dari_csv = open('./9/daftar_nama_update.csv','r')
ke_json = open('./9/csv_to_json.json','w')
json.dump(output,ke_json)
# csvReader = csv.DictReader(dari_csv)
# for csvRow in csvReader:
#     nama = csvRow['nama']
#     data[nama] = csvRow


# ke_json.write(json.dumps(data,indent=5))

