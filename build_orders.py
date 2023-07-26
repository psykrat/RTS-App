import tkinter as tk
from tkinter import ttk
import json

class RTSApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Set the title of the window
        self.title("RTS Build Order App")

        # Get screen width and height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Load build orders from file
        with open('builds.json') as f:
            self.build_orders = json.load(f)

        # Dropdown to select game
        self.game_var = tk.StringVar()
        self.game_dropdown = ttk.Combobox(self, textvariable=self.game_var)
        self.game_dropdown['values'] = ['--Select Game--'] + list(self.build_orders.keys())
        self.game_dropdown.set('--Select Game--')
        self.game_dropdown.bind('<<ComboboxSelected>>', self.update_race_dropdown)
        self.game_dropdown.grid(row=0, column=0, sticky='ew')

        # Dropdown to select race
        self.race_var = tk.StringVar()
        self.race_dropdown = ttk.Combobox(self, textvariable=self.race_var)

        # Dropdown to select build order
        self.build_var = tk.StringVar()
        self.build_dropdown = ttk.Combobox(self, textvariable=self.build_var)

        # Dropdown to select font size
        self.font_size_var = tk.StringVar()
        self.font_size_dropdown = ttk.Combobox(self, textvariable=self.font_size_var)
        self.font_size_dropdown['values'] = [10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40]
        self.font_size_dropdown.set(10)
        self.font_size_dropdown.bind('<<ComboboxSelected>>', self.update_font_size)
        self.font_size_dropdown.grid(row=4, column=0, sticky='ew')

        # Checkbutton to toggle overlay
        self.overlay_var = tk.IntVar()
        self.overlay_checkbutton = tk.Checkbutton(self, text="Overlay", variable=self.overlay_var, command=self.update_overlay)
        self.overlay_checkbutton.grid(row=5, column=0)

        # Checkbutton to lock overlay position
        self.lock_var = tk.IntVar()
        self.lock_checkbutton = tk.Checkbutton(self, text="Lock", variable=self.lock_var)
        self.lock_checkbutton.grid(row=6, column=0)

        # Listbox to display build order
        self.build_order_listbox = tk.Listbox(self, font=("TkDefaultFont", 10))
        self.build_order_listbox.grid(row=3, column=0, sticky='nsew')

        # Configure grid to resize with window
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        # Position on second monitor
        self.geometry('+%d+0' % (self.screen_width + 50))

        # Bind the drag function to the mouse motion event
        self.bind('<Button-1>', self.start_move_or_resize)
        self.bind('<B1-Motion>', self.move_or_resize)
        self.bind('<ButtonRelease-1>', self.end_move_or_resize)

        # Store the current x and y coordinates for the drag function
        self.x = 0
        self.y = 0

    def start_move_or_resize(self, event):
        self.x = self.winfo_pointerx() - self.winfo_rootx()
        self.y = self.winfo_pointery() - self.winfo_rooty()

    def move_or_resize(self, event):
        if self.overlay_var.get() == 1 and self.lock_var.get() == 0:
            self.geometry('+{0}+{1}'.format(event.x_root - self.x, event.y_root - self.y))
            
    def end_move_or_resize(self, event):
        self.x = 0
        self.y = 0

    def update_game_dropdown(self, event):
        game = self.game_var.get()
        if game != '--Select Game--':
            self.race_dropdown['values'] = ['--Select Race--'] + list(self.build_orders[game].keys())
        else:
            self.race_dropdown.set('--Select Race--')
            self.race_dropdown['values'] = ['--Select Race--']
        self.build_dropdown.set('--Select Build Order--')
        self.build_dropdown['values'] = ['--Select Build Order--']
        self.build_order_listbox.delete(0, 'end')

    def update_race_dropdown(self, event):
        game = self.game_var.get()
        if game != '--Select Game--':
            self.race_dropdown['values'] = ['--Select Race--'] + list(self.build_orders[game].keys())
            self.race_dropdown.set('--Select Race--')
            self.race_dropdown.bind('<<ComboboxSelected>>', self.update_build_dropdown)
            self.race_dropdown.grid(row=1, column=0, sticky='ew')
            self.game_dropdown.grid_forget()
            self.build_dropdown.grid_forget()
        else:
            self.race_dropdown.grid_forget()
            self.build_dropdown.grid_forget()
        self.build_order_listbox.delete(0, 'end')

    def update_build_dropdown(self, event):
        game = self.game_var.get()
        race = self.race_var.get()
        if race != '--Select Race--' and game != '--Select Game--':
            self.build_dropdown['values'] = ['--Select Build Order--'] + list(self.build_orders[game][race].keys())
            self.build_dropdown.set('--Select Build Order--')
            self.build_dropdown.bind('<<ComboboxSelected>>', self.update_build_order)
            self.build_dropdown.grid(row=2, column=0, sticky='ew')
            self.race_dropdown.grid_forget()
        else:
            self.build_dropdown.grid_forget()
        self.build_order_listbox.delete(0, 'end')

    def update_build_order(self, event):
        game = self.game_var.get()
        race = self.race_var.get()
        build = self.build_var.get()
        if race != '--Select Race--' and build != '--Select Build Order--' and game != '--Select Game--':
            self.build_order_listbox.delete(0, 'end')
            for order in self.build_orders[game][race][build]:
                self.build_order_listbox.insert('end', order)

    def update_font_size(self, event):
        new_size = int(self.font_size_var.get())
        self.build_order_listbox.config(font=("TkDefaultFont", new_size))

    def update_overlay(self):
        if self.overlay_var.get() == 1:
            self.overrideredirect(1)
            self.geometry('+0+0')
            self.attributes('-topmost', 1)
            # Remember the current x and y coordinates for dragging
            self.x = self.winfo_pointerx() - self.winfo_rootx()
            self.y = self.winfo_pointery() - self.winfo_rooty()
        else:
            self.overrideredirect(0)
            self.geometry('+%d+0' % (self.screen_width + 50))
            self.attributes('-topmost', 0)

if __name__ == "__main__":
    app = RTSApp()
    app.mainloop()
