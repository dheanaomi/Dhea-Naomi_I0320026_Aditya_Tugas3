print("===LIST TEMAN DHEA===")
nama_teman = ['Alip', 'Audi', 'Ambon', 'Ayak', 'Echa', 'Rizal', 'Duha', 'Vika', 'Riki', 'Nina']
#isi indeks 4,6, dan 7
print("\n",nama_teman[4],"\n", nama_teman[6],"\n", nama_teman[7])
#mengganti nama teman di list 3,5, dan 9
nama_teman[3] = 'Alyn'
nama_teman[5] = 'Hasna'
nama_teman[9] = 'Nadiya'
print ('')

nama_teman.append('Hani')
nama_teman.append('Rafika')
#iteration
for x in nama_teman :
    print(x)

print(len(nama_teman))