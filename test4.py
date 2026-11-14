import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 600
PLAYER_SPEED = 25
STAR_SPEED = 5

class StarCatcherGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Falling Stars!")
        self.root.resizable(False, False)

        # Create the game canvas (night sky)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1a1a2e")
        self.canvas.pack()

        # Score and lives tracking
        self.score = 0
        self.lives = 3
        self.game_over = False

        # Display score and lives at the top
        self.score_text = self.canvas.create_text(
            15, 20, anchor="nw", fill="white", font=("Arial", 16, "bold"),
            text=f"Score: {self.score}"
        )
        self.lives_text = self.canvas.create_text(
            WIDTH - 15, 20, anchor="ne", fill="#ff6b6b", font=("Arial", 16, "bold"),
            text=f"Lives: {'❤️' * self.lives}"
        )

        # Create the player's basket at the bottom
        self.basket = self.canvas.create_rectangle(
            210, HEIGHT - 40, 290, HEIGHT - 20, fill="#f39c12", outline="white", width=2
        )

        # Create the first falling star
        self.star = None
        self.spawn_star()

        # Bind keyboard arrow keys
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # Start the game loop
        self.update_game()

    def spawn_star(self):
        if self.star:
            self.canvas.delete(self.star)
        x = random.randint(30, WIDTH - 30)
        self.star = self.canvas.create_oval(
            x - 15, 40, x + 15, 70, fill="#f1c40f", outline="#fff200", width=2
        )

    def move_left(self, event):
        if not self.game_over:
            coords = self.canvas.coords(self.basket)
            if coords[0] > 10:
                self.canvas.move(self.basket, -PLAYER_SPEED, 0)

    def move_right(self, event):
        if not self.game_over:
            coords = self.canvas.coords(self.basket)
            if coords[2] < WIDTH - 10:
                self.canvas.move(self.basket, PLAYER_SPEED, 0)

    def update_game(self):
        if self.game_over:
            return

        # Move the star downward
        self.canvas.move(self.star, 0, STAR_SPEED)
        star_coords = self.canvas.coords(self.star)
        basket_coords = self.canvas.coords(self.basket)

        # Check if the basket caught the star
        if (star_coords[2] >= basket_coords[0] and
            star_coords[0] <= basket_coords[2] and
            star_coords[3] >= basket_coords[1] and
            star_coords[1] <= basket_coords[3]):
            self.score += 10
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.spawn_star()

        # Check if the star hit the bottom of the screen
        elif star_coords[3] >= HEIGHT:
            self.lives -= 1
            self.canvas.itemconfig(self.lives_text, text=f"Lives: {'❤️' * self.lives}")
            if self.lives <= 0:
                self.end_game()
                return
            self.spawn_star()

        # Repeat every 30 milliseconds
        self.root.after(30, self.update_game)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2, fill="#ff6b6b", font=("Arial", 32, "bold"),
            text="GAME OVER!"
        )
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 + 45, fill="white", font=("Arial", 18),
            text=f"Final Score: {self.score}"
        )

if __name__ == "__main__":
    window = tk.Tk()
    game = StarCatcherGame(window)
    window.mainloop()
