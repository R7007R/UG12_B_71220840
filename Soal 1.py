print('SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG')

x = int(input('Masukkan Angka : '))

blank = x-1
for i in range(x):
    print(' '*blank,end='')
    print('*' if i == 0 else '**' if i !=0 and i != x-1 else '*'*(x*2-1))
    blank -= 1