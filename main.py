import tkinter
from game_engine import GameEngine

engine = GameEngine()

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


    #Mark player's chosen square with their icon or prompt player to choose again if square already occupied
    if player_input == '1':
        global square1
        if square1 == '':
            canvas.create_image(5, 5, image=mark_img, anchor='nw')
            square1 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0

    elif player_input == '2':
        global square2
        if square2 == '':
            canvas.create_image(150, 5, image=mark_img, anchor='n')
            square2 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0


    elif player_input == '3':
        global square3
        if square3 == '':
            canvas.create_image(295, 5, image=mark_img, anchor='ne')
            square3 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0

    elif player_input == '4':
        global square4
        if square4 == '':
            canvas.create_image(5, 150, image=mark_img, anchor='w')
            square4 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0

    elif player_input == '5':
        global square5
        if square5 == '':
            canvas.create_image(150, 150, image=mark_img, anchor='c')
            square5 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0


    elif player_input == '6':
        global square6
        if square6 == '':
            canvas.create_image(295, 150, image=mark_img, anchor='e')
            square6 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0

    elif player_input == '7':
        global square7
        if square7 == '':
            canvas.create_image(5, 295, image=mark_img, anchor='sw')
            square7 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0

    elif player_input == '8':
        global square8
        if square8 == '':
            canvas.create_image(150, 295, image=mark_img, anchor='s')
            square8 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0

    elif player_input == '9':
        global square9
        if square9 == '':
            canvas.create_image(295, 295, image=mark_img, anchor='se')
            square9 = mark_str
        else:
            prompt = tkinter.Label(text=f"Player {mark_str} - Choose a free square")
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
            return 0


    #Check which player's turn it is and update the prompt label
    if counter % 2 != 0:
        counter += 1
        playerx_turn = False
        prompt = tkinter.Label(text="Player O - It's Your Turn")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=30)
        prompt.grid(row=1, column=1)
    elif counter % 2 == 0:
        counter += 1
        playerx_turn = True
        prompt = tkinter.Label(text="Player X - It's Your Turn")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=30)
        prompt.grid(row=1, column=1)



    #Check for the draw
    if square1 != "" and square2 != "" and square3 != "" and square4 != "" and square5 != "" and square6 != "" and square7 != "" and square8 != "" and square9 != "":
        prompt = tkinter.Label(text=f"It's a draw")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')

    #Check for the win
    if square1 == mark_str and square2 == mark_str and square3 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square4 == mark_str and square5 == mark_str and square6 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square7 == mark_str and square8 == mark_str and square9 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square1 == mark_str and square4 == mark_str and square7 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square2 == mark_str and square5 == mark_str and square8 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square3 == mark_str and square6 == mark_str and square9 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square1 == mark_str and square5 == mark_str and square9 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')
    elif square3 == mark_str and square5 == mark_str and square7 == mark_str:
        prompt = tkinter.Label(text=f"Player {mark_str} - You Win!")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10, width=20)
        prompt.grid(row=1, column=1)
        submit_button.config(state='disabled')



    entry.delete(0, 'end')













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
entry.config()
entry.grid(row=4, column=1)


submit_button = tkinter.Button(text='Submit', command=mark_square)
submit_button.grid(row=5, column=1)


window.mainloop()