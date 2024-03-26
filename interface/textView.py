

# Import the required library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from interface.graphsView import GraphsView
from dataProcessing.budgetReader import budgetReader


class textView(object):
    def __init__(self, win):
        self.win = win
        self.win.state('zoomed')          
        height = self.win.winfo_screenheight()               
        # self.win.geometry("1000x850")
        self.win.title("Jessica Plot")

        # Create a frame to contain the text boxes and graphs
        content_frame = Frame(self.win)
        content_frame.pack(fill=BOTH, expand=True)

        text_height = height // 3
        # Add a Scrollbar(horizontal)
        v = Scrollbar(content_frame, orient='vertical')
        v.pack(side=RIGHT, fill='y')

        # Add a text widget on the top-left side
        self.text_left = Text(content_frame, font=("Georgia, 10"), yscrollcommand=v.set)

        # Add some text in the text widget
        for i in range(20):
            self.text_left.insert(END, "Welcome to Tutorialspoint...\n\n")

        # Attach the scrollbar with the text widget
        v.config(command=self.text_left.yview)
        self.text_left.pack(side=LEFT, padx=(0, 5), pady=(0, 5), fill=BOTH, expand=True)

        # Add another text widget on the top-right side
        self.text_right = Text(content_frame, font=("Georgia, 10"), yscrollcommand=v.set)

        # Add some text in the text widget
        for i in range(20):
            self.text_right.insert(END, "Additional text...\n\n")

        # Attach the scrollbar with the text widget
        v.config(command=self.text_right.yview)
        self.text_right.pack(side=LEFT, padx=(5, 0), pady=(0, 5), fill=BOTH, expand=True)

        # Create a plot button
        self.plot_button = Button(master=self.win, 
                                  command=self.plot,
                                  height=2, 
                                  width=10, 
                                  text="Plot") 
        self.plot_button.pack(side=BOTTOM, pady=10)

        # Initialize a list to hold GraphsView instances
        self.graph_views = []

    def plot(self):
        # Create a new GraphsView instance
        new_graph_view = GraphsView(self.win)
        self.graph_views.append(new_graph_view)

        # Create a button to remove the canvas
        def remove_canvas():
            new_graph_view.remove()
            button_remove.destroy()

        button_remove = Button(self.win, text="Remove Canvas", command=remove_canvas)
        button_remove.place(in_=new_graph_view.canvas.get_tk_widget(), relx=1.0, rely=0.0, anchor=NE)

        # Pack the new GraphsView instance within the content frame
        new_graph_view.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)

        # new_graph_view.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def addText_main(self, message):
        self.text_right.insert(END, ""+message)
        self.text_right.insert(END, "\n")
    
    def addText(self, message):
        self.text_left.insert(END, ""+message)
        self.text_left.insert(END, "\n")