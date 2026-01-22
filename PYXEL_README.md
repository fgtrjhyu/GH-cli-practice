# Pyxel Examples

This directory contains example games created with [Pyxel](https://github.com/kitao/pyxel), a retro game engine for Python.

## Files

### `pyxel_hello.py`
A simple "Hello World" example demonstrating:
- Basic window creation
- Text rendering
- Simple animation with circles
- Moving text across screen
- Rainbow background

**Controls:**
- Q: Quit

### `pyxel_example.py`
A more complete platformer game example demonstrating:
- Player movement with WASD or arrow keys
- Jumping mechanics with gravity
- Collision detection
- Game over/restart functionality
- Simple sprite drawing

**Controls:**
- WASD or Arrow Keys: Move player
- Space or Up: Jump
- Q: Quit
- R: Restart (when game over)

## Running the Examples

Make sure you have pyxel installed:
```bash
pip install pyxel
```

Then run either example:
```bash
python pyxel_hello.py
python pyxel_example.py
```

## About Pyxel

Pyxel is a retro game engine that supports:
- 160x120 display resolution
- 16 color palette
- 4 sound channels
- 256x256 sprite/tilemap
- Simple but powerful API for 2D games

Perfect for game jams, prototyping, and learning game development!