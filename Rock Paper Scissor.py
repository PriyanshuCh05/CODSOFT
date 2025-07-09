import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissor') or \
         (user == 'scissor' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

# Function to play a round
def play_round(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissor"])
    result = determine_winner(user_choice, computer_choice)

    computer_label.config(text=f"Computer chose: {computer_choice}")
    
    if result == "tie":
        result_label.config(text="It's a tie!", fg="orange")
    elif result == "user":
        user_score += 1
        result_label.config(text="You win!", fg="green")
    else:
        computer_score += 1
        result_label.config(text="Computer wins!", fg="red")
    
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's Play!", fg="blue")
    score_label.config(text="You: 0 | Computer: 0")
    computer_label.config(text="Computer chose: ...")

# Setup GUI window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("300x350")
window.resizable(False, False)

# Widgets
title_label = tk.Label(window, text="🎮 Rock-Paper-Scissors", font=("Helvetica", 16), fg="blue")
title_label.pack(pady=10)

computer_label = tk.Label(window, text="Computer chose: ...", font=("Helvetica", 12))
computer_label.pack()

result_label = tk.Label(window, text="Let's Play!", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=10)

score_label = tk.Label(window, text="You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack()

# Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="🪨 Rock", width=10, command=lambda: play_round("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="📄 Paper", width=10, command=lambda: play_round("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(btn_frame, text="✂️ Scissor", width=10, command=lambda: play_round("scissor"))
scissor_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(window, text="🔄 Reset", command=reset_game)
reset_btn.pack(pady=10)

# Run the app
window.mainloop()