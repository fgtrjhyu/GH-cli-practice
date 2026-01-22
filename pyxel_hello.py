import pyxel

class SimpleExample:
    def __init__(self):
        pyxel.init(160, 120, title="Hello Pyxel")
        self.x = 0
        self.y = 60
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        # Move the text horizontally
        self.x = (self.x + 1) % (pyxel.width + 50)

    def draw(self):
        pyxel.cls(0)  # Clear screen with black
        
        # Draw rainbow background
        for i in range(8):
            pyxel.rect(0, i * 15, pyxel.width, 15, i + 8)
        
        # Draw moving text
        pyxel.text(self.x - 50, self.y, "Hello Pyxel!", 7)
        
        # Draw a simple animation
        for i in range(5):
            pyxel.circb(80 + i * 20, 30, 
                       5 + 3 * abs((pyxel.frame_count + i * 10) % 60 - 30) // 15, 
                       (pyxel.frame_count // 10 + i) % 16)

if __name__ == "__main__":
    SimpleExample()