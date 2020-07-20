import tkinter as tk


class Window:
    def __init__(self, toplevel):
        # create a frame that is a conteiner to widgets
        self.frame = tk.Frame(toplevel)
        # 'pack' is a geometry manager. there are 3 types:
        # 1.pack: tk places the widgets for you, but you can manage a few parameters
        # 2.place: you can explicitly define position of the widget in window
        # 3.grid: you can place widgets on window in a grid
        self.frame.pack()
        # create a widget, in this case a label
        self.lbl1 = tk.Label(self.frame, text='Click to turn green')
        self.lbl1['width'] = 26
        self.lbl1['height'] = 3
        # paint background color
        self.lbl1['bg'] = 'yellow'
        self.lbl1.pack(fill=tk.X, padx=10, pady=5)
        # create another widget, a button
        self.btn = tk.Button(self.frame, text='Click here!')
        # a handler that trigger a event 'change_color' when btn is clicked
        self.btn.bind("<Button-1>", self.change_color)
        self.btn.pack(fill=tk.X, padx=10, pady=5)

    def change_color(self, event):
        if self.lbl1['bg'] == 'yellow':
            self.lbl1['bg'] = 'green'
            self.lbl1['text'] = 'Click to turn yellow'
        else:
            self.lbl1['bg'] = 'yellow'
            self.lbl1['text'] = 'Click to turn green'


root = tk.Tk()
Window(root)
root.mainloop()
