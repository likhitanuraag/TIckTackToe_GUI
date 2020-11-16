from processing_py import *
dim = int(input())
grid = board = [["*" for x in range(dim)] for y in range(dim)]
w = 70
app = App(800, 800)

def draw():
    x, y = 0, 0
    for row in grid:
        for col in row:
            #if col == -1:
            app.fill(255, 0, 0)
            #else:
                #app.fill(255)
            app.rect(x, y, w, w)
            app.redraw()
            x = x + w
        y = y + w
        x = 0


draw()
