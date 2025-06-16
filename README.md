
# 🧩 MazeForge

**MazeForge** is a classic maze-solving game where 🐭 Jerry navigates through a maze to reach his delicious reward — 🧀 cheese!  
Built using **Pygame**, this interactive and visually engaging game challenges your reflexes, logic, and timing with real-time scoring and dynamic graphics.

---

## 🎮 Features

- 🧠 Intelligent maze generation using DFS
- 🐭 Character-based gameplay with Jerry and Cheese
- 📊 Real-time scoring and high-score tracking (SQLite)
- 🎵 Background music & sound effects (start, play, game over)
- 🖼️ Custom assets and images for immersive visuals
- 🔁 Multiple maze sizes supported (adjustable)
- 💾 High scores saved across sessions

---

## 📦 Requirements

- Python 3.6+
- Pygame
- SQLite3 (standard in Python)

Install dependencies using:

```bash
pip install pygame
```

---

## 🚀 How to Play

1. Run the game:
   ```bash
   python app.py
   ```

2. Click the **Start** button to generate a maze.
3. Use arrow keys (`↑ ↓ ← →`) to move Jerry through the maze.
4. Reach the cheese located at the bottom-right corner.
5. Score is calculated based on the time taken — lower is better!
6. View your current and best scores at the end screen.

---

## 🗂️ Project Structure

```
MazeForge/
│
├── assets/
│   ├── images/
│   │   ├── wall.png
│   │   ├── path.png
│   │   ├── jerry.png
│   │   ├── cheese.png
│   │   └── ...
│   ├── sound/
│       ├── game-intro.mp3
│       ├── game-begins.mp3
│       └── game-over.mp3
│
├── HighScoreDB.py        # SQLite score management
├── MazeGenerator.py      # DFS maze generator
├── MazeForge.py          # Main game logic
├── app.py                # Entry point
└── README.md             # This file
```

---

## 🛠️ Customization

- You can adjust the `cell_size` and `margin` in `MazeForge.py` to fit different grid sizes.
- Maze difficulty can be increased by increasing grid size in `MazeGenerator`.

---

## ✨ Future Enhancements

- Timer countdown mode
- Leaderboard across multiple sessions
- Character animations
- Multiple levels
---

## 📃 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**MazeForge** developed by Maharavan S  
🔗 [LinkedIn](https://www.linkedin.com/in/maharavan-s/)
