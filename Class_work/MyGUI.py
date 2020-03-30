from guizero import App, Text, Picture, PushButton, MenuBar, Slider, CheckBox, Combo

app = App()
text = Text(app, align="bottom", text="This is GUI", color="blue", font="Times New Roman", size="70")


def do_somthing():
    print("you have a button")
    picture = Picture(app, image="Image.gif")
def do_something():
    print("you did something else")

menubar = MenuBar(app, toplevel=["file", "edit", "settings", "window"], options=[
    [["File Option 1", do_something], ["file Option 2", do_something]],
    [["edit Option 1", do_somthing], ["edit Option 2", do_somthing]],
    [["settings Option 1", do_somthing], ["settings Option 2", do_somthing]],
    [["Window Option 1", do_somthing], ["Window Option 2", do_somthing]],
])
button = PushButton(app, text="Push me!", align="right", width="3", height="2", command=do_somthing)
button.text_color = "blue"
button.text_size = "50"
slider = Slider(app, end="200")
checkbox = CheckBox(app, text="tick box")
combo = Combo(app, options=["first", "Second", "Third"])

app.display()
