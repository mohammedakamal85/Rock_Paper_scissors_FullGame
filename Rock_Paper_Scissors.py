# first import libraries tkinter, PIL, random
from tkinter import *
from PIL import Image,ImageTk
from random import randint

# main window
window = Tk()
window.title("Rock Paper & Scissor")
window.configure(background="#d3d3d3")

def start_game():
    # add pictures
    rock_image_comp = ImageTk.PhotoImage(Image.open("E:\AUC\Data Analysis\GoMyCode\Python\The Project\Left Rock.jpg"))
    Paper_image_comp = ImageTk.PhotoImage(Image.open("E:\AUC\Data Analysis\GoMyCode\Python\The Project\Left Paper.jpg"))
    scissor_image_comp = ImageTk.PhotoImage(Image.open("E:\AUC\Data Analysis\GoMyCode\Python\The Project\Left Scissor.jpg"))
    rock_image = ImageTk.PhotoImage(Image.open("E:\AUC\Data Analysis\GoMyCode\Python\The Project\Right Rock.jpg"))
    paper_image = ImageTk.PhotoImage(Image.open("E:\AUC\Data Analysis\GoMyCode\Python\The Project\Right Paper.jpg"))
    scissor_image = ImageTk.PhotoImage(Image.open("E:\AUC\Data Analysis\GoMyCode\Python\The Project\Right Scissor.jpg"))

    # insert picture
    user_label = Label(window, image=scissor_image, bg="#d3d3d3")
    comp_label = Label(window, image=scissor_image_comp, bg="#d3d3d3")
    comp_label.grid(row=0, column=0)
    user_label.grid(row=0, column=6)

    # scores
    playerscore = Label(window, text=0,font=("arial",30,"bold"),bg="#d3d3d3",fg="Black")
    computerscore = Label(window, text=0,font=("arial",30,"bold"),bg="#d3d3d3",fg="Black")
    computerscore.grid(row=2,column=2)
    playerscore.grid(row=2,column=4)

    # indicators
    user_indicator = Label(window, bg="#d3d3d3",fg="Black" ,font=("arial",20,"bold"), text="User").grid(row=1, column=4)
    comp_indicator = Label(window, bg="#d3d3d3",fg="Black" ,font=("arial",20,"bold"), text="Computer").grid(row=1, column=2)

    # message
    msg = Label(window, font=("arial",11,"bold"),bg="#d3d3d3",fg="Black")
    msg.grid(row=7,column=3)

    # update message
    def update_message(x):
        msg['text'] = x

    # update player score
    def update_player_score():
        score = int(playerscore["text"])
        score += 1
        playerscore["text"] = str(score)

    # update computer score
    def update_computer_score():
        score = int(computerscore["text"])
        score += 1
        computerscore["text"] = str(score)

    # check winner
    def check_winner(player,computer):
        if player == computer:
            update_message("It's a tie!!!")
        elif player == "rock":
            if computer == "paper":
                update_message("You Loose")
                update_computer_score()
            else:
                update_message("You Win")
                update_player_score()
        elif player == "paper":
            if computer == "scissor":
                update_message("You Loose")
                update_computer_score()
            else:
                update_message("You Win")
                update_player_score()
        elif player == "scissor":
            if computer == "rock":
                update_message("You Loose")
                update_computer_score()
            else:
                update_message("You Win")
                update_player_score()
        
        else:
            pass        

    # choices
    choices = ["rock", "paper", "scissor"]
    def choice(x):    
    # for computer    
        comp_choice = choices[randint(0,2)]
        if comp_choice == "rock":
            comp_label.configure(image=rock_image_comp)
        elif comp_choice == "paper":
            comp_label.configure(image=Paper_image_comp)
        else:
            comp_label.configure(image=scissor_image_comp)

    # for user    
        if x == "rock":
            user_label.configure(image=rock_image)
        elif x == "paper":
            user_label.configure(image=paper_image)
        else:
            user_label.configure(image=scissor_image)
        
        check_winner(x,comp_choice)    


    # Buttons
    rock = Button(window, width=20,height=2,text="Rock",bg="Dark Red",fg="Black",font=("arial",10,"bold"),command= lambda:choice("rock")).grid(row=5,column=2)
    paper = Button(window, width=20,height=2,text="Paper",bg="Dark Red",fg="Black",font=("arial",10,"bold"),command= lambda:choice("paper")).grid(row=5,column=3)
    scissor = Button(window, width=20,height=2,text="Scissor",bg="Dark Red",fg="Black",font=("arial",10,"bold"),command= lambda:choice("scissor")).grid(row=5,column=4)

    # Restart
    def restart():
        playerscore["text"] = "0"
        computerscore["text"] = "0"
        update_message("Score reset!")

    restart_button = Button(window, width=20,height=2,text="Restart",bg="Yellow",fg="Black",font=("arial",10,"bold"),command=restart).grid(row=9,column=2)

    # Button for closing
    exit_button = Button(window, width=20,height=2,text="Exit",bg="Red",fg="Black",font=("Arial",10,"bold"),command=window.destroy).grid(row=9,column=4)


# Create Play button to start the game
play_button = Button(window,text="Play",bg="Red",fg="Black",font=("arial",10,"bold"),command=start_game).grid(row=0,column=3)

window.mainloop()