1. Open the conflicting README and overwrite it
nano Snake-Game/README.md


Delete everything in the file, then paste this content:

# Snake Game – COSC-3411

This project is a Snake Game implemented in Python using the built-in `turtle`
graphics library. It was developed as part of the COSC-3411 course.

---

## Requirements

- Python 3.8 or higher
- Tkinter support (needed for `turtle`)

### Install Tkinter on Debian/Kali/Ubuntu

```bash
sudo apt update
sudo apt install python3-tk

Installation & Configuration

Clone the course repository:

git clone https://github.com/MSAlateeq/COSC-3411.git
cd COSC-3411/Snake-Game


Make the game file executable (optional):

chmod +x snake_game.py


The game configuration (play area size, speed, colors) is defined at the top
of snake_game.py in constants.

How to Run

From the Snake-Game directory:

python3 snake_game.py


or, if you made it executable:

./snake_game.py

Controls

↑ – move up

↓ – move down

← – move left

→ – move right

Usage Example

Open a terminal:

cd COSC-3411/Snake-Game
python3 snake_game.py


Use the arrow keys to move the snake.

Eat the food (random shapes and colors):

Score increases by 10.

A new body segment is added.

The game speed slightly increases.

If the snake hits the wall or its own body, the game resets and the score
returns to 0 (high score for the session is kept).
