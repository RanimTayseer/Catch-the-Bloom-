import tkinter as tk
import random
import math

WIDTH = 800
HEIGHT = 600


class FlowerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flower Vase Scene 🌸")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        self.btn = tk.Button(root, text="New Flower 🌼", command=self.draw_scene)
        self.btn.pack(pady=10)

        self.draw_scene()

    # 🌤️ Background (window + sky + sun + table with legs + tablecloth)
    def draw_background(self):
        # Sky
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT//2, fill="#87CEEB", outline="")

        # Floor / Room interior
        self.canvas.create_rectangle(0, HEIGHT//2, WIDTH, HEIGHT, fill="#eaeaea", outline="")

        # Sun
        self.canvas.create_oval(650, 50, 730, 130, fill="yellow", outline="orange")

        # 🌟 Window (clearly visible with glass reflection)
        self.canvas.create_rectangle(100, 80, 400, 300, fill="#b3e5fc", outline="brown", width=4)
        # Window frame
        self.canvas.create_line(250, 80, 250, 300, fill="brown", width=3)
        self.canvas.create_line(100, 190, 400, 190, fill="brown", width=3)
        # Window glass shine effect
        self.canvas.create_line(120, 100, 200, 100, fill="white", width=2)
        self.canvas.create_line(120, 120, 180, 120, fill="white", width=2)

        # 🪑 Table with legs + tablecloth
        # Table top
        self.canvas.create_rectangle(150, 420, 650, 450, fill="#CD853F", outline="black", width=2)
        # Table legs
        self.canvas.create_rectangle(180, 450, 210, 540, fill="#8B5A2B", outline="black", width=1)
        self.canvas.create_rectangle(590, 450, 620, 540, fill="#8B5A2B", outline="black", width=1)
        # Tablecloth (frilly style)
        self.canvas.create_rectangle(140, 420, 660, 450, fill="#FFB6C1", outline="pink", width=2)
        # Tablecloth hanging edge (scallop effect)
        for x in range(150, 660, 30):
            self.canvas.create_arc(x, 440, x+30, 470, start=0, extent=180, fill="#FFB6C1", outline="pink")

    # 🏺 Realistic Vase (curvy, elegant shape)
    def draw_vase(self):
        cx = WIDTH // 2

        # Vase body (curved polygon)
        self.canvas.create_polygon(
            cx - 70, 420,   # bottom left
            cx + 70, 420,   # bottom right
            cx + 50, 350,   # middle right
            cx + 30, 270,   # neck right
            cx - 30, 270,   # neck left
            cx - 50, 350,   # middle left
            fill="#4682B4",  # steel blue vase
            outline="darkblue",
            width=2
        )
        # Vase rim (opening)
        self.canvas.create_oval(cx - 35, 260, cx + 35, 280, fill="#5F9EA0", outline="darkblue", width=2)
        # Vase decorative line
        self.canvas.create_oval(cx - 55, 360, cx + 55, 380, fill="", outline="gold", width=2)
        # Vase base
        self.canvas.create_oval(cx - 70, 415, cx + 70, 430, fill="#4682B4", outline="darkblue", width=2)

    # 🌼 Flower (perfect center)
    def draw_flower(self, x, y):
        colors = ["red", "pink", "purple", "yellow", "orange", "magenta", "coral", "hotpink"]

        petal_color = random.choice(colors)
        center_color = "gold"

        # الزهرة تبدأ من فوق فوهة المزهرية
        flower_top = y - 80

        # Stem (يمتد من داخل المزهرية إلى الزهرة)
        self.canvas.create_line(x, y, x, flower_top, fill="green", width=3)

        # Petals around center
        for i in range(8):
            angle = i * (2 * math.pi / 8)
            px = x + 12 * math.cos(angle)
            py = flower_top + 12 * math.sin(angle)
            self.canvas.create_oval(
                px - 9, py - 9,
                px + 9, py + 9,
                fill=petal_color,
                outline=""
            )

        # Flower center
        self.canvas.create_oval(
            x - 8, flower_top - 8,
            x + 8, flower_top + 8,
            fill=center_color,
            outline="orange"
        )

        # Leaves (على الساق)
        self.canvas.create_oval(x - 12, y - 50, x + 20, y - 30, fill="darkgreen", outline="")
        self.canvas.create_oval(x - 22, y - 42, x + 8, y - 22, fill="darkgreen", outline="")

    # 🎨 Full scene
    def draw_scene(self):
        self.canvas.delete("all")

        self.draw_background()
        self.draw_vase()

        # 🌸 الزهور تخرج من فوهة المزهرية (من y = 270 إلى فوق)
        vase_opening_y = 270  # فوهة المزهرية
        base_x = WIDTH // 2

        for _ in range(random.randint(6, 10)):
            # ساق الزهرة يبدأ من داخل فوهة المزهرية
            x = base_x + random.randint(-30, 30)
            y = vase_opening_y + random.randint(5, 20)  # الساق يبدأ من الفوهة
            self.draw_flower(x, y)

        # Title
        self.canvas.create_text(
            WIDTH // 2,
            30,
            text="🌸 Flower Vase in Room Scene 🌸",
            font=("Arial", 18, "bold"),
            fill="darkblue"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = FlowerApp(root)
    root.mainloop()