from tkinter import *
import time
import random


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, ball_position):
        paddle_position = self.canvas.coords(self.paddle.id)
        if ball_position[2] >= paddle_position[0] and ball_position[0] <= paddle_position[2]:
            if paddle_position[1] <= ball_position[3] <= paddle_position[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        ball_position = self.canvas.coords(self.id)
        if ball_position[0] <= 0:
            self.x = -self.x
        if ball_position[1] <= 0:
            self.y = -self.y
        if ball_position[2] >= self.canvas_width:
            self.x = - self.x
        if ball_position[3] >= self.canvas_height:
            self.y = -self.y
        if ball_position[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(ball_position):
            self.y = -self.y


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 20, fill=color)
        self.canvas.move(self.id, 600, 600)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = self.canvas.coords(self.id)
        if position[0] <= 0:
            self.x = 0
        if position[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -4

    def turn_right(self, evt):
        self.x = 4


class Block:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 40, 25, fill=color)

    def draw(self):
        block_1 = Block(canvas, "yellow")
        block_1.move


class Message:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.play = False
        self.id = canvas.create_text(550, 300,
                                     text="To begin press <space>.",
                                     fill=color,
                                     font=("Times", 26))
        self.canvas.bind_all("<KeyPress-space>", self.begin)

    def begin(self, evt):
        self.play = True


tk = Tk()
tk.title("RepulseIt")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1100, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update_idletasks()
tk.update()

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")
message = Message(canvas, "green")

while not message.play:
    tk.update_idletasks()
    tk.update()

canvas.delete(message.id)

while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
