counter = 1
playerx_turn = True


square1 = ''
square2 = ''
square3 = ''
square4 = ''
square5 = ''
square6 = ''
square7 = ''
square8 = ''
square9 = ''

def mark_square(player_input, mark_img):
    global counter
    global playerx_turn
    if playerx_turn:
        mark_img = ximage
        mark_str = 'X'
    else:
        mark_img = oimage
        mark_str = 'O'

    if player_input == '1':
        canvas.create_image(5, 5, image=mark_img, anchor='nw')
        global square1
        square1 = mark_str
        print(square1)
    elif player_input == '2':
        canvas.create_image(150, 5, image=mark_img, anchor='n')
        global square2
        square2 = mark_str
        print(square2)
    elif player_input == '3':
        canvas.create_image(295, 5, image=mark_img, anchor='ne')
        global square3
        square3 = mark_str
        print(square3)
    elif player_input == '4':
        canvas.create_image(5, 150, image=mark_img, anchor='w')
        global square4
        square4 = mark_str
        print(square4)
    elif player_input == '5':
        canvas.create_image(150, 150, image=mark_img, anchor='c')
        global square5
        square5 = mark_str
        print(square5)
    elif player_input == '6':
        canvas.create_image(295, 150, image=mark_img, anchor='e')
        global square6
        square6 = mark_str
        print(square6)
    elif player_input == '7':
        canvas.create_image(5, 295, image=mark_img, anchor='sw')
        global square7
        square7 = mark_str
        print(square7)
    elif player_input == '8':
        canvas.create_image(150, 295, image=mark_img, anchor='s')
        global square8
        square8 = mark_str
        print(square8)
    elif player_input == '9':
        canvas.create_image(295, 295, image=mark_img, anchor='se')
        global square9
        square9 = mark_str
        print(square9)
    if counter % 2 != 0:
        counter += 1
        playerx_turn = False
        prompt = tkinter.Label(text="Player O - It's Your Turn")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10)
        prompt.grid(row=1, column=1)
    elif counter % 2 == 0:
        counter += 1
        playerx_turn = True
        prompt = tkinter.Label(text="Player X - It's Your Turn")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10)
        prompt.grid(row=1, column=1)
