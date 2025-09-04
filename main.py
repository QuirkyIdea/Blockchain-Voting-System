import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import hashlib
import time


# Blockchain Class #
class Blockchain:
    def __init__(self):
        self.clear_blockchain()
        self.chain = []
        self.create_block(voter_id="System", candidate="Genesis", previous_hash="0")  # Genesis Block

    def create_block(self, voter_id, candidate, previous_hash):
        """Create a new block and add it to the chain"""
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "voter_id": voter_id,
            "candidate": candidate,
            "previous_hash": previous_hash,
            "hash": ""
        }
        block["hash"] = self.hash_block(block)
        self.chain.append(block)
        self.save_blockchain()
        return block

    def hash_block(self, block):
        """Generate hash of a block"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_last_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]
    
    def save_blockchain(self):
        """Save the blockchain to a JSON file"""
        with open("blockchain.json", "w", encoding="utf-8") as file:
            json.dump(self.chain, file, indent=4)
    
    def clear_blockchain(self):
        with open("blockchain.json", "w", encoding="utf-8") as file:
            pass


def reset_votes():
    """Reset all users' voting status at the start of a new session"""
    global users
    if os.path.exists(users_file):
        # Check if the file is empty before loading
        if os.path.getsize(users_file) == 0:
            users = {}
        else:
            with open(users_file, "r", encoding="utf-8") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = {}

        for user_id in users:
            users[user_id]["voted"] = False  # Reset all users

        save_users()
    else:
        messagebox.showerror("Error", "No users are registered!")
        users = {}


def save_users():
    """Save user data to JSON file"""
    with open(users_file, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def authenticate_user():
    """Ask for user ID and check if they have voted"""
    user_id = simpledialog.askstring("Login", "Enter your voter ID:")

    if user_id not in users:
        messagebox.showerror("Error", "This ID is not registered!")
        return None
    
    if users[user_id]["voted"]:
        messagebox.showerror("Error", "You have already voted!")
        return None
    
    return user_id


def vote(candidate):
    """Cast a vote and store it in the blockchain"""
    user_id = authenticate_user()
    if user_id:
        users[user_id]["voted"] = True
        previous_hash = blockchain.get_last_block()["hash"]
        new_block = blockchain.create_block(voter_id=user_id, candidate=candidate, previous_hash=previous_hash)
        save_users()
        messagebox.showinfo("Vote Confirmed", f"You voted for {candidate}!\n\nBlock Index: {new_block['index']}\nHash: {new_block['hash']}")


def show_result():
    """Display the election results based on blockchain data"""
    red_count = sum([1 for block in blockchain.chain if block["candidate"] == "Red"])
    blue_count = sum([1 for block in blockchain.chain if block["candidate"] == "Blue"])

    result_text = f"Red: {red_count} votes \nBlue: {blue_count} votes\n"
    if red_count > blue_count:
        result_text += f"Red wins by {red_count - blue_count} votes!"
    elif blue_count > red_count:
        result_text += f"Blue wins by {blue_count - red_count} votes!"
    else:
        result_text += "It's a tie! 🏳"

    messagebox.showinfo("Result", result_text)


def register_user():
    """Ask for user name"""
    while True:
        user_name = simpledialog.askstring("register", "Enter your name:")
        if user_name and not any(char.isdigit() for char in user_name):
            break
        else:
            messagebox.showerror("Error", "Name cannot be empty or contain numbers!")
    
    if users == {}:
        user_id = 100
    else:
        user_id = max([int(i) for i in users])
    
    user = {
        "name": user_name,
        "voted": False
    }
    
    users.update({str(user_id + 1): user})
    messagebox.showinfo("Registration Confirmed", f"Your voter ID is {user_id + 1}")
    save_users()


root = tk.Tk()
root.title("Blockchain Voting System")
root.attributes('-fullscreen', True)
root.configure(bg="#f0f0f0")

# UI Layout
frame = tk.Frame(root, bg="#ffffff", padx=50, pady=50)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(frame, text="Vote for Your Preferred Candidate", font=("Arial", 24, "bold"), bg="#ffffff")
title_label.pack(pady=20)

# Vote Buttons
red_button = tk.Button(frame, text="Vote for Red 🔴", font=("Arial", 18, "bold"), command=lambda: vote("Red"), bg="red", fg="white", padx=20, pady=10)
red_button.pack(pady=10)

blue_button = tk.Button(frame, text="Vote for Blue 🔵", font=("Arial", 18, "bold"), command=lambda: vote("Blue"), bg="blue", fg="white", padx=20, pady=10)
blue_button.pack(pady=10)

# Result Button
result_button = tk.Button(frame, text="View Results", font=("Arial", 18, "bold"), command=show_result, bg="#28a745", fg="white", padx=20, pady=10)
result_button.pack(pady=20)

# Exit Button
exit_button = tk.Button(root, text="Close", font=("Arial", 16), command=root.quit, bg="red", fg="white", padx=10, pady=5)
exit_button.place(relx=0.9, rely=0.05)

register_button = tk.Button(root, text="Register", font=("Arial", 16), command=register_user, bg="green", fg="white", padx=10, pady=5)
register_button.place(relx=0.05, rely=0.05)

# File Handling #
users_file = "users.json"

# Initialize Blockchain & Reset Votes
blockchain = Blockchain()
users = {}
reset_votes()

root.mainloop()
