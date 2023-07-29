import tkinter
from game_engine import GameEngine



#_____________________TKinter Window Set Up / Creation of GameEngine Object____________________________#

window = tkinter.Tk()
window.title('Tic Tac Toe')
window.minsize(width=350, height=500)

window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=3)


engine = GameEngine()

x_img = tkinter.PhotoImage(file='X.png')
o_img = tkinter.PhotoImage(file='O.png')
mark_img = tkinter.PhotoImage(file='X.png')
#_________________________________Definition of Button Comman__________________________________#
def command():
    player_input = entry.get()
    global mark_img
    global x_img
    global o_img
    #______________Check player turn and set appropriate image_____________________#
    if engine.playerx_turn:
        mark_img = x_img
    else:
        mark_img = o_img

    #______________________Validate move or prompt player to move again_________________#
    if engine.validate_move(player_input):
        engine.mark_square(player_input)


        if player_input == '1':
            print('input is 1')
            canvas.create_image(5, 5, image=mark_img, anchor='nw')
        elif player_input == '2':
            canvas.create_image(150, 5, image=mark_img, anchor='n')
        elif player_input == '3':
            canvas.create_image(295, 5, image=mark_img, anchor='ne')
        elif player_input == '4':
            canvas.create_image(5, 150, image=mark_img, anchor='w')
        elif player_input == '5':
            canvas.create_image(150, 150, image=mark_img, anchor='c')
        elif player_input == '6':
            canvas.create_image(295, 150, image=mark_img, anchor='e')
        elif player_input == '7':
            canvas.create_image(5, 295, image=mark_img, anchor='sw')
        elif player_input == '8':
            canvas.create_image(150, 295, image=mark_img, anchor='s')
        elif player_input == '9':
            canvas.create_image(295, 295, image=mark_img, anchor='se')

        engine.check_result()
        if engine.game_over and engine.draw:
            prompt = tkinter.Label(text=f"It's a draw", width=30)
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
        elif engine.game_over and  engine.draw == False:
            prompt = tkinter.Label(text=f"Player {engine.mark_str} - You Win!", width=30)
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
        else:
            engine.set_turns()
    else:
        prompt = tkinter.Label(text=f"Player {engine.mark_str} - Choose a free square")
        prompt.config(font=('Georgia', 16, 'normal'), pady=10)
        prompt.grid(row=1, column=1)

    #_______________________________Disable button if game is over____________________________#
    if engine.game_over:
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


submit_button = tkinter.Button(text='Submit', command=command)
submit_button.grid(row=5, column=1)


window.mainloop()