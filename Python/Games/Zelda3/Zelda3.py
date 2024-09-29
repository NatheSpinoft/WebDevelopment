import tkinter as tk
import time

class Game:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.canvas = tk.Canvas(root, bg='white', width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack()

        # Player (blue box)
        self.player = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue")
        self.sword = self.canvas.create_line(100, 75, 150, 75, fill="yellow", width=5)
        self.sword_angle = 0

        # Enemy (red box)
        self.enemy = self.canvas.create_rectangle(600, 50, 650, 100, fill="red")
        self.enemy_direction = 0  # 0=down, 1=right, 2=up, 3=left
        self.enemy_moving = True

        # Player stats
        self.health = 3
        self.hearts = [self.canvas.create_text(1200 + i * 30, 30, text='!', font=('Arial', 20)) for i in range(self.health)]
        
        # Player movement
        self.root.bind("<Up>", self.move_player)
        self.root.bind("<Down>", self.move_player)
        self.root.bind("<Left>", self.move_player)
        self.root.bind("<Right>", self.move_player)
        self.root.bind("p", self.swing_sword)

        self.enemy_move()
        self.check_collisions()

    def move_player(self, event):
        if event.keysym == 'Up':
            self.canvas.move(self.player, 0, -10)
            self.canvas.move(self.sword, 0, -10)
        elif event.keysym == 'Down':
            self.canvas.move(self.player, 0, 10)
            self.canvas.move(self.sword, 0, 10)
        elif event.keysym == 'Left':
            self.canvas.move(self.player, -10, 0)
            self.canvas.move(self.sword, -10, 0)
        elif event.keysym == 'Right':
            self.canvas.move(self.player, 10, 0)
            self.canvas.move(self.sword, 10, 0)

    def swing_sword(self, event):
        if self.sword_angle == 0:
            self.canvas.rotate(self.sword, 45)
            self.sword_angle = 45
        else:
            self.canvas.rotate(self.sword, -45)
            self.sword_angle = 0
        self.check_sword_collision()

    def check_sword_collision(self):
        sword_coords = self.canvas.coords(self.sword)
        enemy_coords = self.canvas.coords(self.enemy)

        if (enemy_coords[0] < sword_coords[2] < enemy_coords[2] and
            enemy_coords[1] < sword_coords[3] < enemy_coords[3]):
            self.flash_enemy()

    def flash_enemy(self):
        for _ in range(2):
            self.canvas.itemconfig(self.enemy, fill="white")
            self.root.update()
            time.sleep(0.1)
            self.canvas.itemconfig(self.enemy, fill="red")
            self.root.update()
            time.sleep(0.1)
        self.canvas.delete(self.enemy)

    def enemy_move(self):
        if self.enemy_moving:
            if self.enemy_direction == 0:  # Move down
                self.canvas.move(self.enemy, 0, 10)
            elif self.enemy_direction == 1:  # Move right
                self.canvas.move(self.enemy, 10, 0)
            elif self.enemy_direction == 2:  # Move up
                self.canvas.move(self.enemy, 0, -10)
            elif self.enemy_direction == 3:  # Move left
                self.canvas.move(self.enemy, -10, 0)

            # Get enemy position and update direction when necessary
            x1, y1, x2, y2 = self.canvas.coords(self.enemy)
            if y2 >= 600:  # Reached bottom
                self.enemy_direction = 1
            elif x2 >= 1200:  # Reached right side
                self.enemy_direction = 2
            elif y1 <= 50:  # Reached top
                self.enemy_direction = 3
            elif x1 <= 600:  # Reached left side
                self.enemy_direction = 0

            self.root.after(100, self.enemy_move)

    def check_collisions(self):
        player_coords = self.canvas.coords(self.player)
        enemy_coords = self.canvas.coords(self.enemy)

        if (enemy_coords[0] < player_coords[2] < enemy_coords[2] and
            enemy_coords[1] < player_coords[3] < enemy_coords[3]):
            self.player_hit()

        self.root.after(50, self.check_collisions)

    def player_hit(self):
        if self.health > 0:
            self.health -= 1
            self.canvas.delete(self.hearts[self.health])
            if self.health == 0:
                self.game_over()

    def game_over(self):
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height()//2,
                                text="Game Over", font=('Arial', 50), fill="red")
        self.enemy_moving = False

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
