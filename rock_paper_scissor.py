from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="yellow")



# Picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-user.jpg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor-user.png"))

# Insert picture
user_label = Label(root, image=scissor_img, bg="yellow")
comp_label = Label(root, image=scissor_img_comp, bg="yellow")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Player scores
playerScore = Label(root, text=0, font=100, bg="yellow", fg="red")
computerScore = Label(root, text=0, font=100, bg="yellow", fg="red")
playerScore.grid(row=1, column=3)
computerScore.grid(row=1, column=1)

# Indicators
user_indicator = Label(root, font=50, text="USER", bg="yellow", fg="red")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="yellow", fg="red")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Messages
msg = Label(root, font=50, bg="yellow", fg="red", text="")
msg.grid(row=3, column=2)

# Update message
def updateMessage(x):
    msg["text"] = x

# Update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

            

    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose")
            updateCompScore()

        else:
            updateMessage("You Win")
            updateUserScore()


# Update choices
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    # For computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # For user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E40", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="black", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

root.mainloop()
