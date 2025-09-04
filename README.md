# Blockchain-Voting-System
A Python + Tkinter based Blockchain Voting System ensuring secure, transparent, and tamper-proof elections. Features user registration/login, one-vote-per-user, blockchain ledger with SHA-256 hashing, GUI for voting, and vote reset option. Ideal for learning blockchain and secure e-voting.

Overview

This project implements a Blockchain-based Voting System with a Graphical User Interface (GUI) using Python and Tkinter.
It ensures secure, transparent, and immutable voting, preventing tampering and enabling fair elections.

Votes are stored as blocks in a blockchain, making the system resistant to fraud and manipulation.

🚀 Features

-> User Registration & Login – Secure authentication via users.json.

-> One Voter, One Vote – Prevents multiple votes from the same user.

-> Blockchain Ledger – Every vote is stored as a block linked with cryptographic hashing.

-> Genesis Block – The chain starts with a special system-generated block.

-> GUI with Tkinter – Simple and interactive voting interface.

-> Reset Option – Admin can reset votes and restart the blockchain.

-> Transparency – Blockchain data can be viewed at any time.

📂 Project Structure
Blockchain voting/
│── main.py           # Main application (GUI + blockchain logic)
│── blockchain.json   # Stores blockchain ledger (all votes as blocks)
│── users.json        # Stores user details (username, password, vote status)

⚙️ How It Works

1)Initialization

2)Blockchain starts with a Genesis block.

3)User and blockchain files are created if missing.

4)User Registration

5)A new voter registers with username & password.

Stored in users.json.

Login

Registered users log in with credentials.

Voting

User selects a candidate.

A new block is created in blockchain.json:

{
  "index": 2,
  "timestamp": 1725522017.123,
  "voter_id": "User123",
  "candidate": "CandidateA",
  "previous_hash": "xyz...",
  "hash": "abc..."
}


The block is linked to the previous block.

Viewing Blockchain

Users can view the blockchain ledger in the GUI.

Resetting Votes

Clears blockchain and voter records.

Restarts from the Genesis block.

🖥️ Installation & Usage
1. Clone the Repository
git clone https://github.com/your-username/blockchain-voting.git
cd blockchain-voting

2. Install Dependencies

The project uses Tkinter (built-in with Python) and standard libraries:

json

hashlib

time

os

Make sure you have Python 3.8+ installed.

3. Run the Application
python main.py

4. Use the GUI

Register/Login as a voter.

Cast your vote.

View blockchain results.

Reset votes if needed.

🔒 Security

SHA-256 Hashing → Ensures data integrity.

Tamper Detection → Modifying a block invalidates the chain.

User Authentication → Prevents duplicate voting.

🌟 Future Enhancements

🌐 Web-based frontend for remote voting.

🔑 Public/Private key cryptography for stronger voter anonymity.

📡 Distributed blockchain instead of single JSON storage.

📊 Real-time results dashboard with candidate vote counts.
