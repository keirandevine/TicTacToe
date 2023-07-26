import tkinter

#_________________________________TKinter Window Set Up__________________________________#

window = tkinter.Tk()
window.title('Tic Tac Toe')
window.minsize(width=350, height=500)

window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=3)

#_________________________________Definition of Fuctions__________________________________#

counter = 1
playerx_turn = True
ximage = tkinter.PhotoImage(file='X.png')
oimage = tkinter.PhotoImage(file='O.png')
mark_img = ximage

square1 = ''
square2 = ''
square3 = ''
square4 = ''
square5 = ''
square6 = ''
square7 = ''
square8 = ''
square9 = ''

def mark_square():
    player_input = entry.get()
    global counter
    global playerx_turn
    global mark_img
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












#________________________________________Heading and Player Prompt__________________________#
heading_label = tkinter.Label(text="Tic Tac Toe")
heading_label.config(font=('Arial', 30, 'bold'))
heading_label.grid(row=0, column=1)

prompt = tkinter.Label(text="Player X - It's Your Turn")
prompt.config(font=('Georgia', 16, 'normal'), pady=10)
prompt.grid(row=1, column=1)



#_________________________________________Canvas / Game Interface_____________________________#
img1 = tkinter.PhotoImage(file='1.png')
img2 = tkinter.PhotoImage(file='2.png')
img3 = tkinter.PhotoImage(file='3.png')
img4 = tkinter.PhotoImage(file='4.png')
img5 = tkinter.PhotoImage(file='5.png')
img6 = tkinter.PhotoImage(file='6.png')
img7 = tkinter.PhotoImage(file='7.png')
img8 = tkinter.PhotoImage(file='8.png')
img9 = tkinter.PhotoImage(file='9.png')
canvas = tkinter.Canvas(width=300, height=300, bg='black', highlightthickness=0)
canvas.create_image(5, 5, image=img1, anchor='nw')
canvas.create_image(150, 5, image=img2, anchor='n')
canvas.create_image(295, 5, image=img3, anchor='ne')
canvas.create_image(5, 150, image=img4, anchor='w')
canvas.create_image(150, 150, image=img5, anchor='c')
canvas.create_image(295, 150, image=img6, anchor='e')
canvas.create_image(5, 295, image=img7, anchor='sw')
canvas.create_image(150, 295, image=img8, anchor='s')
canvas.create_image(295, 295, image=img9, anchor='se')
canvas.grid(row=2, column=1)


input_prompt = tkinter.Label(text="Choose a Square")
input_prompt.config(font=('Georgia', 16, 'normal'), pady=5)
input_prompt.grid(row=3, column=1)

entry = tkinter.Entry()
entry.grid(row=4, column=1)


submit_button = tkinter.Button(text='Submit', command=mark_square)
submit_button.grid(row=5, column=1)


window.mainloop()