def nilai():
    nama = str(input('Masukkan Nama>> '))
    nile = int(input('Masukkan Nilai>> '))
    hasil = 'Halo, {nama}! Nilai anda setelah dikonversi adalah {nilai}'
    if nile < 60:
        print(hasil.format(nama = nama, nilai = 'E'))
    elif nile < 65:
        print(hasil.format(nama = nama, nilai = 'C'))
    elif nile < 70:
        print(hasil.format(nama = nama, nilai = 'C+'))
    elif nile < 75:
        print(hasil.format(nama = nama, nilai = 'B'))
    elif nile < 80:
        print(hasil.format(nama = nama, nilai = 'B+'))
    elif nile < 85:
        print(hasil.format(nama = nama, nilai = 'A-'))
    elif nile >= 65:
        print(hasil.format(nama = nama, nilai = 'A'))
    else:
        print('Masukkan ulang nilai')

nilai()