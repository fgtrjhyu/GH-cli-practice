import pyxel

class Game:
    def __init__(self):
        pyxel.init(160, 120, title="Pyxel Example Game")
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0
        self.player_alive = True
        
        # Simple obstacles
        self.obstacles = []
        for i in range(4):
            self.obstacles.append({
                "x": i * 40,
                "y": 96,
                "w": 8,
                "h": 8
            })
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.player_alive:
            # Player movement
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
                self.player_x = max(self.player_x - 2, 0)
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
                self.player_x = min(self.player_x + 2, pyxel.width - 16)
            
            # Jump mechanics
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                if self.player_y == 104:  # On ground
                    self.player_vy = -4
            
            # Apply gravity
            self.player_vy += 0.25
            self.player_y += self.player_vy
            
            # Ground collision
            if self.player_y > 104:
                self.player_y = 104
                self.player_vy = 0
            
            # Check collision with obstacles
            for obstacle in self.obstacles:
                if (self.player_x < obstacle["x"] + obstacle["w"] and
                    self.player_x + 16 > obstacle["x"] and
                    self.player_y < obstacle["y"] + obstacle["h"] and
                    self.player_y + 16 > obstacle["y"]):
                    self.player_alive = False
        else:
            # Restart game
            if pyxel.btnp(pyxel.KEY_R):
                self.player_x = 72
                self.player_y = 104
                self.player_vy = 0
                self.player_alive = True

    def draw(self):
        pyxel.cls(1)  # Clear screen with dark blue
        
        # Draw ground
        pyxel.rect(0, 120, pyxel.width, 8, 11)
        
        # Draw obstacles
        for obstacle in self.obstacles:
            pyxel.rect(obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"], 8)
        
        # Draw player
        if self.player_alive:
            pyxel.rect(self.player_x, self.player_y, 16, 16, 9)
            # Simple face
            pyxel.pset(self.player_x + 4, self.player_y + 4, 7)
            pyxel.pset(self.player_x + 11, self.player_y + 4, 7)
            pyxel.line(self.player_x + 4, self.player_y + 10, self.player_x + 11, self.player_y + 10, 7)
        else:
            # Draw dead player
            pyxel.rect(self.player_x, self.player_y, 16, 16, 8)
            pyxel.line(self.player_x + 4, self.player_y + 4, self.player_x + 7, self.player_y + 7, 7)
            pyxel.line(self.player_x + 7, self.player_y + 4, self.player_x + 4, self.player_y + 7, 7)
            pyxel.line(self.player_x + 9, self.player_y + 4, self.player_x + 12, self.player_y + 7, 7)
            pyxel.line(self.player_x + 12, self.player_y + 4, self.player_x + 9, self.player_y + 7, 7)
            
            # Game over text
            pyxel.text(50, 40, "GAME OVER", 8)
            pyxel.text(45, 50, "Press R to restart", 7)
        
        # Instructions
        pyxel.text(5, 5, "WASD/Arrows: Move", 7)
        pyxel.text(5, 12, "Space/Up: Jump", 7)
        pyxel.text(5, 19, "Q: Quit", 7)

if __name__ == "__main__":
    Game()