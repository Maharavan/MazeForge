
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
- 🔁 Multiple maze sizes (7x7, 9x9, 11x11, 13x13)
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

2. Click the **Start** button to begin.
3. Select your preferred **maze size**:  
   - `7x7` — Easy  
   - `9x9`,`11x11` — Medium  
   - `13x13` — Hard  

4. Use arrow keys (`↑ ↓ ← →`) to move Jerry through the maze.
5. Reach the cheese located at the bottom-right corner.
6. Score is calculated based on the time taken — lower is better!
7. View your current and best scores at the end screen.

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

- Adjust `cell_size` and `margin` in `MazeForge.py` to tweak spacing.
- Modify `MazeGenerator` to explore alternative algorithms like Prim's or Kruskal’s.
- Add new difficulty levels by simply introducing more grid sizes and corresponding images.

---

## ✨ Future Enhancements

- ⏲️ Timer countdown mode
- 🕹️ Character animations & effects
- 🗺️ Procedurally generated themed mazes (forest, dungeon, etc.)
---

## 📃 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**MazeForge** developed by Maharavan S  
🔗 [LinkedIn](https://www.linkedin.com/in/maharavan-s/)

