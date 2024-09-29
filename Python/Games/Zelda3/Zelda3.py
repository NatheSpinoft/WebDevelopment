import tkinter as tk
import time
import math

class Game:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()-40}")  # Avoid taskbar
        self.canvas = tk.Canvas(root, bg='white', width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()-40)
        self.canvas.pack()

        self.running = True  # Game state variable
        self.grace_period = False  # To track grace period after losing a life
        self.setup_game()

    def setup_game(self):
        # Player (blue box)
        self.player = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue")
        self.sword = self.canvas.create_line(100, 50, 100, 10, fill="yellow", width=5)  # Starts upright
        self.sword_angle = 0  # Initial angle is 0 degrees

        # Enemy (red box)
        self.enemy = self.canvas.create_rectangle(600, 50, 650, 100, fill="red")
        self.enemy_direction = 0  # 0=down, 1=right, 2=up, 3=left
        self.enemy_moving = True

        # Player stats
        self.health = 3
        self.hearts = [self.canvas.create_text(1200 + i * 30, 30, text='❤️', font=('Arial', 20)) for i in range(self.health)]
        
        # Player movement
        self.root.bind("<Up>", self.move_player)
        self.root.bind("<Down>", self.move_player)
        self.root.bind("<Left>", self.move_player)
        self.root.bind("<Right>", self.move_player)
        self.root.bind("p", self.rotate_sword)

        self.enemy_move()
        self.check_collisions()

    def move_player(self, event):
        if not self.running:
            return

        player_coords = self.canvas.coords(self.player)
        player_x1, player_y1, player_x2, player_y2 = player_coords
        move_x, move_y = 0, 0

        if event.keysym == 'Up' and player_y1 > 0:
            move_y = -10
        elif event.keysym == 'Down' and player_y2 < self.canvas.winfo_height():
            move_y = 10
        elif event.keysym == 'Left' and player_x1 > 0:
            move_x = -10
        elif event.keysym == 'Right' and player_x2 < self.canvas.winfo_width():
            move_x = 10

        self.canvas.move(self.player, move_x, move_y)
        self.canvas.move(self.sword, move_x, move_y)

    def rotate_sword(self, event):
        if not self.running:
            return
        # Rotate by 30 degrees each time, then reset after 90 degrees
        self.sword_angle = (self.sword_angle + 30) % 120
        self.update_sword_position()
        self.check_sword_collision()

    def update_sword_position(self):
        # Get the player's current position (center)
        player_coords = self.canvas.coords(self.player)
        player_x = (player_coords[0] + player_coords[2]) / 2
        player_y = (player_coords[1] + player_coords[3]) / 2

        # Calculate new sword coordinates based on the angle
        sword_length = 50  # Length of the sword
        angle_radians = math.radians(self.sword_angle)
        sword_x = player_x + sword_length * math.cos(angle_radians)
        sword_y = player_y - sword_length * math.sin(angle_radians)

        # Move the sword
        self.canvas.coords(self.sword, player_x, player_y, sword_x, sword_y)

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
        if self.enemy_moving and self.running:
            if self.enemy_direction == 0:  # Move down
                self.canvas.move(self.enemy, 0, 10)
            elif self.enemy_direction == 1:  # Move right
                self.canvas.move(self.enemy, 10, 0)
            elif self.enemy_direction == 2:  # Move up
                self.canvas.move(self.enemy, 0, -10)
            elif self.enemy_direction == 3:  # Move left
                self.canvas.move(self.enemy, -10, 0)

            # Get enemy position and update direction when necessary (for square path)
            x1, y1, x2, y2 = self.canvas.coords(self.enemy)
            if y2 >= self.canvas.winfo_height():  # Reached bottom
                self.enemy_direction = 1
            elif x2 >= self.canvas.winfo_width():  # Reached right side
                self.enemy_direction = 2
            elif y1 <= 0:  # Reached top
                self.enemy_direction = 3
            elif x1 <= self.canvas.winfo_width() // 2:  # Reached left side
                self.enemy_direction = 0

            self.root.after(100, self.enemy_move)

    def check_collisions(self):
        if not self.running or self.grace_period:
            return
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

            # Activate grace period
            self.grace_period = True
            self.root.after(10000, self.end_grace_period)  # 10-second grace period

            if self.health == 0:
                self.game_over()

    def end_grace_period(self):
        self.grace_period = False

    def game_over(self):
        self.running = False
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height()//2 - 30,
                                text="Game Over", font=('Arial', 50), fill="red")
        self.try_again_button = tk.Button(self.root, text="Try Again", font=('Arial', 20), command=self.restart_game)
        self.try_again_button.place(x=self.canvas.winfo_width()//2 - 75, y=self.canvas.winfo_height()//2 + 20)

    def restart_game(self):
        self.try_again_button.destroy()
        self.canvas.delete("all")
        self.running = True
        self.setup_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
