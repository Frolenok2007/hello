box = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
chag = 0
result = ''

  #разложение матрицы по координатам
def vvodim(vvod):
    coordinate_x = (vvod - 1) // 3
    coordinate_y = (vvod - 1) % 3
    return [coordinate_x, coordinate_y]

# вывод матрицы
def out_box(matrix_for_printing, N=3, M=3):
     for i in range(N):
        for j in range(M):
            print(matrix_for_printing[i][j], end=" ")
        print()

out_box(box)

#проверка победил ли кто-то из игроков
def prover(win = '', linia = '', colomn = ''):
    for i in range (3):
        for j in range (3):
            linia += box[i][j]
            colomn += box[j][i]
        linia += ' '
        colomn += ' '
    linia += colomn
    if 'xxx' in linia:
        win = 'Игрок x  победил!'
    if 'ooo' in linia:
        win = 'Игрок o  победил!'

    if box[0][0] ==  box[1][1] == box[2][2] == 'x' or box[2][0] == box[1][1] == box[0][2] == 'x':
            win = 'Игрок x победил!!!'
    if box[0][0] ==  box[1][1] == box[2][2] == 'o' or box[2][0] == box[1][1] == box[0][2] == 'o':
            win = 'Игрок o победил!!!'

    print(win)
    return win


#сам х<од игры (ввод х или о в поле игры)
while not result:
    coordinate_x, coordinate_y = vvodim(int(input('введите цифру куда хотите поставить x')))
    while box[coordinate_x][coordinate_y] == 'x' or box[coordinate_x][coordinate_y] == 'o':
        print('Клетка занята. Введите повторно!')
        coordinate_x, coordinate_y = vvodim(int(input('введите цифру куда хотите поставить x')))
    box[coordinate_x][coordinate_y] = 'x'
    out_box(box)
    result = prover()
    chag += 1
    print(chag, 'итерация хода')
    if chag == 9:
        print('НИЧЬЯ')
        break

    if not result:
        coordinate_x, coordinate_y = vvodim(int(input('введите цифру куда хотите поставить o')))
        while box[coordinate_x][coordinate_y] == 'x' or box[coordinate_x][coordinate_y] == 'o':
            print('Клетка занята. Введите повторно!')
            coordinate_x, coordinate_y = vvodim(int(input('введите цифру куда хотите поставить o')))
        box[coordinate_x][coordinate_y] = 'o'
        out_box(box)
        result = prover()
        chag += 1
        print(chag, 'итерация хода')
