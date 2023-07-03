from tkinter import *
from tkinter import messagebox
import os
import random
os.system('clear')

root = Tk()
root.title('Lines')
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
image_list = []

for i in range(1, 9):
    image = PhotoImage(file='images/' + str(i) + '.png')
    image_list.append(image)

canvas = Canvas(root, width=300, height=350)
canvas.pack(expand=TRUE, anchor=CENTER, side=TOP)

score_label = Label(root, text="Score: 0")
score_label.pack()
steps_label = Label(root, text="Steps: 0")
steps_label.pack()

score = 0
steps = 0
ball_click = 0
tmpx = 0
tmpy = 0
tmpz = 0

cols = 9
rows = 9
a = [[0 for _ in range(cols)] for _ in range(rows)]
b = [[0 for _ in range(cols)] for _ in range(rows)]


def delete_ball():
    del_b = False
    # horizontal
    for i in range(5):
        for j in range(9):
            if (a[i][j] == a[i+1][j]) and (a[i][j] == a[i+2][j]) and (a[i][j] == a[i+3][j]) and (a[i][j] == a[i+4][j]) \
                    and (a[i][j] > 0):
                b[i][j] = -20
                b[i+1][j] = -20
                b[i+2][j] = -20
                b[i+3][j] = -20
                b[i+4][j] = -20
    # vertical
    for i in range(9):
        for j in range(5):
            if (a[i][j] == a[i][j+1]) and (a[i][j] == a[i][j+2]) and (a[i][j] == a[i][j+3]) and (a[i][j] == a[i][j+4]) \
                    and (a[i][j] > 0):
                b[i][j] = -20
                b[i][j+1] = -20
                b[i][j+2] = -20
                b[i][j+3] = -20
                b[i][j+4] = -20
    # diagonals
    for i in range(5):
        for j in range(5):
            if (a[i][j] == a[i+1][j+1]) and (a[i][j] == a[i+2][j+2]) and (a[i][j] == a[i+3][j+3]) \
                    and (a[i][j] == a[i+4][j+4]) and (a[i][j] > 0):
                b[i][j] = -20
                b[i+1][j+1] = -20
                b[i+2][j+2] = -20
                b[i+3][j+3] = -20
                b[i+4][j+4] = -20
    for i in range(8, 5, -1):
        for j in range(5):
            if (a[i][j] == a[i-1][j+1]) and (a[i][j] == a[i-2][j+2]) and (a[i][j] == a[i-3][j+3]) \
                    and (a[i][j] == a[i-4][j+4]) and (a[i][j] > 0):
                b[i][j] = -20
                b[i-1][j+1] = -20
                b[i-2][j+2] = -20
                b[i-3][j+3] = -20
                b[i-4][j+4] = -20
    for i in range(5):
        for j in range(8, 5, -1):
            if (a[i][j] == a[i+1][j-1]) and (a[i][j] == a[i+2][j-2]) and (a[i][j] == a[i+3][j-3]) \
                    and (a[i][j] == a[i+4][j-4]) and (a[i][j] > 0):
                b[i][j] = -20
                b[i+1][j-1] = -20
                b[i+2][j-2] = -20
                b[i+3][j-3] = -20
                b[i+4][j-4] = -20
    for i in range(5):
        for j in range(5, -1, -1):
            if (a[i][j] == a[i+1][j-1]) and (a[i][j] == a[i+2][j-2]) and (a[i][j] == a[i+3][j-3]) \
                    and (a[i][j] == a[i+4][j-4]) and (a[i][j] > 0):
                b[i][j] = -20
                b[i+1][j-1] = -20
                b[i+2][j-2] = -20
                b[i+3][j-3] = -20
                b[i+4][j-4] = -20

    # deletion
    for i in range(9):
        for j in range(9):
            if b[i][j] == -20:
                canvas.create_image(i * 32, j * 32, image=image_list[6], anchor=NW)
                del_b = True
                global steps, score
                steps -= 1
                score += 20
                a[i][j] = 0
                b[i][j] = 0

    score_label["text"] = 'Score: ' + str(score)
    steps_label["text"] = 'Steps: ' + str(steps)

    return del_b


def random_ball():
    if not delete_ball():
        num_ball = 0
        global steps
        while num_ball != 3 and steps != 81:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            z = random.randint(0, 4)+1
            if a[x][y] == 0:
                a[x][y] = z
                canvas.create_image(x * 32, y * 32, image=image_list[z], anchor=NW)
                num_ball = num_ball + 1
                steps = steps + 1
        delete_ball()
    if steps == 81:
        messagebox.showerror('Game Over!', 'Game Over!')


def new_game():
    score_label["text"] = "Score: 0"
    score_label.pack()
    global ball_click, steps, score
    ball_click = 0
    steps = 0
    score = 0
    for x in range(9):
        for y in range(9):
            a[x][y] = 0
            b[x][y] = 0
            canvas.create_image(x*32, y*32, image=image_list[6], anchor=NW)
    random_ball()


# find free squares
def find_zero(x1, y1):
    for row in range(x1-1, x1+2):
        for column in range(y1-1, y1+2):
            if (row >= 0) and (row < 9) and (column >= 0) and (column < 9) and (b[row][column] == 0) \
                    and (a[row][column] == 0):
                if (row == x1-1) and (column == y1-1):
                    continue
                if (row == x1+1) and (column == y1-1):
                    continue
                if (row == x1+1) and (column == y1+1):
                    continue
                if (row == x1-1) and (column == y1+1):
                    continue

                b[row][column] = 1
                find_zero(row, column)


# button click
def move(event):
    x = event.x // 32
    y = event.y // 32

    global ball_click, tmpx, tmpy, tmpz
    if a[x][y] > 0:
        for i in range(9):
            for j in range(9):
                b[i][j] = 0
        tmpx = x
        tmpy = y
        tmpz = a[x][y]
        ball_click = True
        find_zero(x, y)

    if a[x][y] == 0 and ball_click and b[x][y] == 1:
        canvas.create_image(tmpx*32, tmpy*32, image=image_list[6], anchor=NW)
        canvas.create_image(x*32, y*32, image=image_list[tmpz], anchor=NW)
        ball_click = False
        a[tmpx][tmpy] = 0
        a[x][y] = tmpz
        random_ball()


root.bind('<Button-1>', move)
new_game()


root.mainloop()
