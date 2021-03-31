def menyapa():
    nama = str(input('Masukkan Nama>> '))
    kelamin = str(input('Masukkan Jenis kelamin (Pria/Wanita)>> '))
    sapa = 'Selamat datang, '
    if kelamin == 'Pria':
        print(sapa, 'Pak', nama)
    elif kelamin == 'Wanita': 
        print(sapa, 'Nyonya', nama)
    else:
        pass

menyapa()