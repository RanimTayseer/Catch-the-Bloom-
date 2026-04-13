import tkinter as tk
import random
import os

WIDTH = 800
HEIGHT = 600


class FlowerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Flower Game 🌸🎮")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#87CEEB")
        self.canvas.pack()

        # 🧍 اللاعب
        self.player_x = WIDTH // 2
        self.player = self.canvas.create_rectangle(
            self.player_x - 40, HEIGHT - 50,
            self.player_x + 40, HEIGHT - 20,
            fill="brown"
        )

        # 🎮 عناصر اللعبة
        self.flowers = []
        self.particles = []

        # 🏆 النقاط
        self.score = 0
        self.level = 1

        # 🏆 High Score
        self.high_score = self.load_high_score()

        self.score_text = self.canvas.create_text(100, 30, text="Score: 0", font=("Arial", 14))
        self.level_text = self.canvas.create_text(350, 30, text="Level: 1", font=("Arial", 14))
        self.high_text = self.canvas.create_text(650, 30, text=f"Best: {self.high_score}", font=("Arial", 14))

        # ⏱️ الوقت
        self.time_left = 60
        self.timer_text = self.canvas.create_text(400, 60, text="Time: 60", font=("Arial", 16, "bold"))

        # التحكم
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # تشغيل
        self.spawn_flower()
        self.update_game()
        self.update_timer()

    # 🌼 زهور بأنواع مختلفة
    def spawn_flower(self):
        x = random.randint(50, WIDTH - 50)
        y = 0

        colors = ["red", "pink", "yellow", "orange", "purple"]
        color = random.choice(colors)

        size = random.randint(10, 20)

        flower = self.canvas.create_oval(
            x - size, y - size,
            x + size, y + size,
            fill=color
        )

        self.flowers.append([flower, x, y, color, size])

        # 🧠 صعوبة متزايدة
        speed = max(300, 900 - self.level * 80)
        self.root.after(speed, self.spawn_flower)

    # 🧍 حركة اللاعب
    def move_left(self, event):
        self.player_x -= 30
        self.update_player()

    def move_right(self, event):
        self.player_x += 30
        self.update_player()

    def update_player(self):
        self.canvas.coords(
            self.player,
            self.player_x - 40, HEIGHT - 50,
            self.player_x + 40, HEIGHT - 20
        )

    # 💥 مؤثرات Particles
    def create_particles(self, x, y, color):
        for _ in range(6):
            px = self.canvas.create_oval(x, y, x+5, y+5, fill=color, outline="")
            self.particles.append([px, random.randint(-3, 3), random.randint(-6, -1)])

    def update_particles(self):
        new_particles = []
        for p, dx, dy in self.particles:
            self.canvas.move(p, dx, dy)
            coords = self.canvas.coords(p)

            if coords[1] < HEIGHT:
                new_particles.append([p, dx, dy])
            else:
                self.canvas.delete(p)

        self.particles = new_particles

    # 🎮 تحديث اللعبة
    def update_game(self):
        new_flowers = []

        for flower, x, y, color, size in self.flowers:
            y += 5 + self.level  # ذكاء صعوبة

            self.canvas.coords(
                flower,
                x - size, y - size,
                x + size, y + size
            )

            # 🎯 التقاط
            if HEIGHT - 80 < y < HEIGHT - 20 and abs(x - self.player_x) < 50:
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

                # 🔊 صوت
                self.root.bell()

                # 💥 particles
                self.create_particles(x, HEIGHT - 60, color)

                self.canvas.delete(flower)
                continue

            # ❌ خارج الشاشة
            if y < HEIGHT:
                new_flowers.append([flower, x, y, color, size])
            else:
                self.canvas.delete(flower)

        self.flowers = new_flowers

        self.update_particles()
        self.update_level()

        if self.time_left > 0:
            self.root.after(40, self.update_game)
        else:
            self.end_game()

    # ⏱️ Timer
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.canvas.itemconfig(self.timer_text, text=f"Time: {self.time_left}")
            self.root.after(1000, self.update_timer)

    # 🧠 Level System
    def update_level(self):
        new_level = self.score // 5 + 1

        if new_level != self.level:
            self.level = new_level
            self.canvas.itemconfig(self.level_text, text=f"Level: {self.level}")

    # 🏆 High Score
    def load_high_score(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as f:
                return int(f.read())
        return 0

    def save_high_score(self):
        if self.score > self.high_score:
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))

    # 🛑 نهاية اللعبة
    def end_game(self):
        self.save_high_score()

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text=f"Game Over 🎮\nScore: {self.score}",
            font=("Arial", 28, "bold"),
            fill="red"
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = FlowerGame(root)
    root.mainloop()