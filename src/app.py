import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import Label
from PIL import ImageTk, Image
import cv2

# Import the standalone image processing service logic module cleanly
from processing import process_cavity_image

root = tk.Tk()
root.title('Air Pocket Detection System')
root.resizable(True, True)
root.geometry('450x450')

is_dark_mode = False
test1, test2, test3, test4 = None, None, None, None
loc = ""

# --- UI Element Layout Definitions ---
label1 = Label(root)
label2 = Label(root)
label3 = Label(root)
label4 = Label(root)

title_label = Label(text="CAVITY  DETECTION  SYSTEM", font=("Futura 50 bold"))
orig_img_label = Label(text="Original Image", font=("Futura 25"))
proc_img_label = Label(text="Processed Image", font=("Futura 25"))
label_gui = Label(root) 

def update_theme():
    global is_dark_mode, test1, test2, test3, test4
    
    bg_color = 'black' if is_dark_mode else 'white'
    fg_color = 'white' if is_dark_mode else 'black'
    suffix = "_dark.jpg" if is_dark_mode else ".jpg"
    
    root.configure(bg=bg_color)
    
    img1 = Image.open(r'.\icons\NUST_dark.jpg' if is_dark_mode else r'.\icons\logo.jpg')
    img1 = img1.resize((180, 180)) if is_dark_mode else img1
    test1 = ImageTk.PhotoImage(img1)
    label1.configure(image=test1, bg=bg_color)
    label1.image = test1
    
    img2 = Image.open(f'.\\icons\\open{suffix}').resize((50, 50))
    test2 = ImageTk.PhotoImage(img2)
    label2.configure(image=test2, bg=bg_color)
    
    img3 = Image.open(f'.\\icons\\run{suffix}').resize((65, 65))
    test3 = ImageTk.PhotoImage(img3)
    label3.configure(image=test3, bg=bg_color)
    
    img4 = Image.open(f'.\\icons\\exit{suffix}').resize((60, 60))
    test4 = ImageTk.PhotoImage(img4)
    label4.configure(image=test4, bg=bg_color)
    
    title_label.configure(bg=bg_color, fg=fg_color)
    orig_img_label.configure(bg=bg_color, fg=fg_color)
    proc_img_label.configure(bg=bg_color, fg=fg_color)
    
    toggle_button.configure(text="SWITCH TO LIGHT MODE" if is_dark_mode else "SWITCH TO DARK MODE")

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    update_theme()

def select_file():
    global loc
    filetypes = (('Image files', '*.jpg'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Select a file', initialdir='/', filetypes=filetypes)
    if filename:
        loc = filename.replace("/", "\\")
        showinfo(title='Selected File', message=loc)

def live_stream():
    global loc
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Live Video Feed", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:  
            break
        elif k % 256 == 32:  
            img_name = f"opencv_frame_{img_counter}.jpg"
            cv2.imwrite(img_name, frame)
            loc = f".\\opencv_frame_{img_counter}.jpg"
            img_counter += 1
            print(f"Frame saved to target location: {loc}")

    cam.release()
    cv2.destroyAllWindows()

def immask():
    global loc
    if not loc:
        showinfo(title="Error", message="Please select an image or use live capture first.")
        return

    # Call the functional matrix pipeline located in processing.py
    processed_rgb = process_cavity_image(loc, is_dark_mode=is_dark_mode)
    
    if processed_rgb is None:
        showinfo(title="Error", message="Could not read or parse the image file.")
        return

    image_gui = Image.fromarray(processed_rgb)
    photo = ImageTk.PhotoImage(image_gui)

    label_gui.photo = photo
    label_gui.configure(image=photo)
    label_gui.place(x=350, y=250)
    
    orig_img_label.place(x=520, y=200)
    proc_img_label.place(x=960, y=200)

# --- Components Placement Engine ---
open_button = ttk.Button(root, text='OPEN FILE', command=select_file)
run_button = ttk.Button(root, text='RUN Pipeline', command=immask)
live_button = ttk.Button(root, text='LIVE STREAM', command=live_stream)
toggle_button = ttk.Button(root, text='TOGGLE THEME', command=toggle_theme)
exit_button = ttk.Button(root, text='EXIT', command=root.destroy)

label1.place(x=0, y=0)
label2.place(x=62, y=196)
label3.place(x=53, y=432)
label4.place(x=62, y=690)

title_label.place(x=350, y=65)
root.attributes("-transparentcolor", "grey")

open_button.place(x=50, y=250)
live_button.place(x=150, y=250)
run_button.place(x=50, y=500)
toggle_button.place(x=150, y=500)
exit_button.place(x=50, y=750)

update_theme()
root.state('zoomed')
root.mainloop()