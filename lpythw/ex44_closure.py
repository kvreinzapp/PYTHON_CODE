def constructor(color, size):
    print(">>> constructor color:", color, "size:", size)

    def repeater():
        print("### repeater color:", color, "size:", size)

    print("<<< exit constructor")
    return repeater


blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")

for i in range(0, 4):
    blue_xl()
    green_sm()
