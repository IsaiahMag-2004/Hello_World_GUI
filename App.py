import tkinter
from tkinter import BOTH, END, StringVar



#Define main window
root = tkinter.Tk()
root.title("Hello GUI World")
root.iconbitmap("wave.ico")
root.geometry("400x400")
root.resizable(0, 0)

#Define fonts and colors
root_color = "#231f20"
input_color = "#bb4430"
output_color = "#7ebdc2"
root.config(bg=root_color)

#Define Functions
def submit():
    """Submits the name, and outputs a hello message to the user"""
    global submit
    username = name.get()
    if capitalization.get() == "normal":
        output_label = tkinter.Label(output_frame, text=(f"Hello {username.title()}! Keep learning Tkinter!"), bg=output_color)
    else:
        output_label = tkinter.Label(output_frame, text=(f"HELLO {username.upper()}! KEEP LEARNING TKINTER!"), bg=output_color)
    
    #pack label onto screen
    output_label.pack()

    #Clear entry box on button press
    name.delete(0, END)

#Define Frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10) #Using pady so that nothing is right up against the top of the window
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

#Create Widgets
name = tkinter.Entry(input_frame, text="Enter your name", width=15)
submit_button = tkinter.Button(input_frame, text="Submit", command=submit)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10)

#Create radio buttons for text display
capitalization = StringVar()
capitalization.set("normal")
normal_button = tkinter.Radiobutton(input_frame, text="Normal Case", variable=capitalization, value="normal", bg=input_color).grid(row=1, column=0, pady=(0, 5))
Upper_button = tkinter.Radiobutton(input_frame, text="Upper Case", variable=capitalization, value="upper", bg=input_color).grid(row=1, column=1, pady=(0, 5))

#Create image
smile_image = tkinter.PhotoImage(file="smile.png")
image_label = tkinter.Label(output_frame, image=smile_image, bg=output_color).pack()

#Run root main loop
root.mainloop()
