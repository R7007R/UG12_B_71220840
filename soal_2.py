print('~~~ Selamat Datang di Kalkulator Sederhana ~~~')


def add(a,b):
    return f'{a} + {b} = {a+b}'

def subtract(a,b):
    return f'{a} - {b} = {a-b}'

def multiply(a,b):
    return f'{a} * {b} = {a*b}'

def divide(a,b):
    return f'{a} / {b} = {a/b}'

kalkulasi = {
    '+':[add,'penjumlahan'],
    '-':[subtract,'pengurangan'],
    'x':[multiply,'perkalian'],
    ':':[divide,'pembagian']
}




oprtr = input('Masukan operator matematika yang ingin anda hitung: ').lower()

if oprtr in kalkulasi:
    ngitunglgi = True

    while ngitunglgi:
        jmlproses = int(input(f'Mau {kalkulasi[oprtr][1]} berapa: '))
        jmlprint = int(input('Print berapa banyak: '))
        oprspertama = {x:y for x,y in zip(range(1,jmlproses+1),range(jmlproses,0,-1))}
        for i in range(1,jmlprint+1):
            print(kalkulasi[oprtr][0](i,oprspertama[i]))
        print('')

        novalid = True

        while novalid:
            tryagain = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ').upper()
            if tryagain == 'Y':
                novalid = False
            elif tryagain == 'T':
                novalid = False
                ngitunglgi = False
            else:
                print('Input Tidak Valid\n')
                continue
    print('Terima Kasih dan Sampai Jumpa Lagi!')
else:
    print('Maaf, Operator Matematika yang anda cari belum tersedia.')