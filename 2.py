
import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)
            
           
def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    order = 3
    size = 300

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    screen.mainloop()

if __name__ == "__main__":
    main()