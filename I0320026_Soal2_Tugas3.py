#dict sebelum diubah
dict = {'Nama':'Dhea','Hobi_1':'Travelling','Hobi_2':'Menonton film',
        'Hobi_3':'Berenang','Sosmed_1':'line:dhproject','Sosmed_2':'ig:dheanaomii',
        'Sosmed_3':'WA : 082230074167','Lagu_1':'Monolog','Lagu_2':'If you could see me crying in my room',
        'Lagu_3':'paris in the rain','Makanan_1':'Lasagna','Makanan_2':'Pizza','Makanan_3':'Indomie'}
print(dict)
print("")
# Mengubah salah satu hobi dan sosmed, hapus 2 makanan, dan tambah 1 hobi
dict['Hobi_2'] = 'Menyanyi'
dict['Sosmed_3'] = 'twitter:@aryousirius'
del dict['Makanan_3']
del dict['Makanan_2']
dict['Hobi_4'] = 'Mendengarkan musik'
#dict setelah diubah
print(dict)