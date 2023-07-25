import tkinter as tk
from tkinter import messagebox
import os

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def shutdown():
    global wait_time, remaining_time
    try:
        wait_time = int(entry.get())
        os.system(f"shutdown /s /f /t {wait_time}")
        remaining_time = wait_time
        update_countdown()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number of seconds.")

def cancel_shutdown():
    global remaining_time
    os.system("shutdown /a")
    messagebox.showinfo("Shutdown Canceled", "The shutdown process has been canceled.")
    countdown_label.config(text="")
    remaining_time = 0

def update_countdown():
    global remaining_time
    if remaining_time > 0:
        countdown_label.config(text=f"Time left: {format_time(remaining_time)}")
        remaining_time -= 1
        app.after(1000, update_countdown)
    else:
        countdown_label.config(text="")
        remaining_time = 0

def toggle_theme():
    current_theme = app.cget("bg")
    new_theme = "black" if current_theme == "white" else "white"
    app.config(bg=new_theme)
    frame.config(bg=new_theme)

    label.config(bg=new_theme, fg="white" if new_theme == "black" else "black")
    entry.config(bg=new_theme, fg="white" if new_theme == "black" else "black")
    shutdown_button.config(bg=new_theme, fg="white" if new_theme == "black" else "black")
    cancel_button.config(bg=new_theme, fg="white" if new_theme == "black" else "black")
    countdown_label.config(bg=new_theme, fg="white" if new_theme == "black" else "black")
    dark_theme_button.config(text="Light Theme" if new_theme == "black" else "Dark Theme")

def close_intro():
    intro_window.destroy()

# Create the introductory window
intro_window = tk.Tk()
intro_window.title("Welcome to Automatic Shutdown Timer")
intro_window.geometry("500x400")
intro_window.configure(bg="white")

intro_frame = tk.Frame(intro_window, bg="white")
intro_frame.pack(pady=50)

intro_label = tk.Label(intro_frame, text="Welcome to the Automatic Shutdown Timer!\n\n"
                                        "This program allows you to schedule an automatic shutdown\n"
                                        "of your computer after a specified number of seconds.\n\n"
                                        "Simply enter the number of seconds in the box below and click\n"
                                        "the 'Shutdown' button. You can cancel the shutdown anytime by\n"
                                        "clicking the 'Cancel Shutdown' button. Enjoy!", font=("Arial", 12), bg="white")
intro_label.pack(pady=20)

ok_button = tk.Button(intro_frame, text="OK!", font=("Arial", 12), command=close_intro)
ok_button.pack(pady=10)

# Create the main shutdown timer window
app = tk.Tk()
app.title("Automatic Shutdown Timer")
app.geometry("400x300")
app.configure(bg="white")

frame = tk.Frame(app, bg="white")
frame.pack(pady=10)

label = tk.Label(frame, text="Enter the number of seconds to shutdown after:", font=("Arial", 12), bg="white", fg="black")
label.pack(pady=10)

entry = tk.Entry(frame, width=10, font=("Arial", 12), fg="black")
entry.pack(pady=5)

shutdown_button = tk.Button(frame, text="Shutdown", font=("Arial", 12), command=shutdown, fg="black")
shutdown_button.pack(pady=10)

cancel_button = tk.Button(frame, text="Cancel Shutdown", font=("Arial", 12), command=cancel_shutdown, fg="black")
cancel_button.pack(pady=10)

countdown_label = tk.Label(app, text="", font=("Arial", 18), bg="white", fg="black")
countdown_label.pack(pady=10)

dark_theme_button = tk.Button(app, text="Dark Theme", font=("Arial", 12), command=toggle_theme, fg="black")
dark_theme_button.pack(pady=5)

wait_time = 0
remaining_time = 0

app.mainloop()