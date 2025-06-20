
# 🤩 MazeForge - Full Game

**MazeForge** is a character-based maze game developed using Python and Pygame. Players can choose between Jerry 🐭, Spike 🐶, or Tom 🐱, and solve mazes of increasing difficulty. The game features real-time scoring, background music, a dynamic UI, and a difficulty-based leaderboard system powered by SQLite.

---

## 🎮 Features

- 🧠 Maze generation using DFS algorithm
- 🐭 Character selection: Jerry (Easy), Spike (Medium), Tom (Hard)
- 🎵 Integrated background music and sound effects
- 📊 Score tracking with **SQLite-based difficulty-wise leaderboard**
- 🖼️ Custom assets: images, sprites, and sounds
- 🌐 Dynamic menu, difficulty selection, and character screen
- 💾 Leaderboard shows top scores for each maze size (difficulty level)

---

## 📦 Requirements

- Python 3.6+
- Pygame
- SQLite3 (bundled with Python)

### Install dependencies

```bash
pip install pygame
```

---

## 🚀 How to Run

1. Clone this repository
2. Launch the game:

```bash
python app.py
```

3. In-game steps:
   - Click **Start** to begin
   - Choose your **maze size**:  
     - Easy (7x7)  
     - Medium (9x9, 11x11)  
     - Hard (13x13)
   - Select your **character**:  
     - Jerry 🐭  
     - Spike 🐶  
     - Tom 🐱
   - Navigate using arrow keys: `↑ ↓ ← →`
   - Reach the goal to finish and view your score + leaderboard!

---

## 📂 Project Structure

```
MazeForge/
├── assets/
│   ├── images/              # Maze tiles, characters, UI elements
│   └── sound/               # Background music and effects
├── game/
│   ├── maze_forge.py        # Main game loop and event handling
│   ├── assets_loader.py     # Loads image/sound assets
│   ├── constants.py         # Screen dimensions, colors, FPS
│   ├── player.py            # Player character logic
│   ├── renderer.py          # Responsible for UI/maze drawing
│   └── sound_manager.py     # Handles background music and effects
├── HighScoreDB.py           # SQLite3 DB interface with difficulty-based leaderboard
├── Mazegenerator.py         # Maze creation using DFS
├── app.py                   # Game entry point
└── README.md                # Project documentation
```

---

## 🛠️ Technical Highlights

### ✅ MazeGenerator (DFS)

- Depth-First Search algorithm for unique maze generation
- Random pathing ensures replayability
- Fixed entry (`x`) and goal (`y`) for each game

### ✅ Renderer

- Dynamically scales maze and assets based on size
- Displays maze, player, and game states (win/lose)
- Shows high score leaderboard after each round

### ✅ Player

- Controls mapped to arrow keys
- Handles movement, collision detection, and win condition

### ✅ SoundManager

- Plays different music for:
  - Menu
  - In-game
  - Game over screen
- Sound effects for movement and completion

### ✅ HighScoreDB

- Stores scores with player name, maze size, and time
- Shows **top scores per difficulty level**
- SQLite-backed and persistently stored in `HighScore.db`

---

## 📃 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💼 Author

Developed with 💻 and 🎮 by **Maharavan S**  
🔗 [LinkedIn](https://www.linkedin.com/in/maharavan-s/)
