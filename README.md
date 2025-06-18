# 🤩 MazeForge - Full Game

**MazeForge** is a character-based maze game developed using Python and Pygame. Players can choose between Jerry 🐭, Spike 🐶, or Tom 🐱, and solve mazes of increasing difficulty. The game features real-time scoring, background music, high score tracking, and intelligent maze generation.

---

## 🎮 Features

* 🧠 Maze generation using DFS algorithm
* 🐭 Character selection: Jerry (Easy), Spike (Medium), Tom (Hard)
* 🎵 Integrated background music and sound effects
* 📊 Score tracking and SQLite-based high score saving
* 🖼️ Custom assets (images and audio)
* 🌐 Dynamic menu, difficulty, and character selection screens

---

## 📦 Requirements

* Python 3.6+
* Pygame
* SQLite3 (comes with Python)

Install Pygame:

```bash
pip install pygame
```

---

## 🚀 How to Run

1. Launch the game using:

```bash
python app.py
```

2. On the menu:

   * Click **Start** to play
   * Choose a maze size: Easy (7x7), Medium (9x9, 11x11), Hard (13x13)
   * Select a character: Jerry, Spike, or Tom
3. Navigate the maze using arrow keys: `↑ ↓ ← →`
4. Reach the goal to win and see your score!

---

## 📂 Project Structure

```
MazeForge/
├── assets/
│   ├── images/          # Game visuals (maze, characters, UI)
│   ├── sound/           # Sound effects and background music
├── game/
│   ├── maze_forge.py    # Main game loop and logic
│   ├── assets_loader.py # Loads images and sounds
│   ├── constants.py     # Screen dimensions, FPS
│   ├── player.py        # Player control and movement
│   ├── renderer.py      # Handles drawing the game
│   └── sound_manager.py # Music/sound control
├── HighScoreDB.py       # SQLite high score handler
├── Mazegenerator.py     # DFS-based maze generator
├── app.py               # Game entry point
└── README.md            # This file
```

---

## 🛠️ Technical Highlights

### MazeGenerator (DFS)

* Carves out random paths from the top-left to bottom-right.
* Ensures maze solvability.
* Marks player start (`'x'`) and end (`'y'`) positions.

### Renderer

* Renders menus, characters, maze, game over screen.
* Dynamically scales images based on maze size.

### Player

* Handles key input and collision detection.
* Knows when the goal is reached.

### SoundManager

* Plays/stops looping music for intro, in-game, and game over.

### HighScoreDB

* Stores scores in `HighScore.db`.
* Tracks and displays best scores by maze size.

---

## ✨ Planned Enhancements

* ⏲️ Timer countdown mode
* 🕹️ Animated character sprites
* 🌳 Themed mazes: forest, desert, space, etc.
* 🌐 Web version (using Pyodide or Pygbag)

---

## 📃 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for full details.

---

## 👨‍💼 Author

Developed by **Maharavan S**
🔗 [LinkedIn](https://www.linkedin.com/in/maharavan-s/)
