import tkinter as tk
from tkinter import messagebox
import random

class RPS:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        self.setui()

    def setui(self):
        tk.Label(self.root, text="Your Choice:").pack(pady=5)

        self.user_choice_var = tk.StringVar(value="Rock")
        for choice in self.choices:
            tk.Radiobutton(self.root, text=choice, variable=self.user_choice_var, value=choice).pack(pady=5)

        tk.Button(self.root, text="Play", command=self.play).pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=self.get_score(), font=("Arial", 12))
        self.score_label.pack(pady=10)

        tk.Button(self.root, text="Play Again", command=self.play_again).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def play(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.score_label.config(text=self.get_score())

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def get_score(self):
        return f"User: {self.user_score}  Computer: {self.computer_score}"

    def play_again(self):
        self.result_label.config(text="")
        self.user_choice_var.set("Rock")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=self.get_score())

if __name__ == "__main__":
    root = tk.Tk()
    app = RPS(root)
    root.mainloop()
