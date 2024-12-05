import tkinter as tk
root = tk.Tk()
root.title("Profile Information")
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)
name_label = tk.Label(top_frame, text="Name: Oluwatobi Olajide")
name_label.pack(side=tk.TOP)
middle_frame = tk.Frame(root)
middle_frame.pack(side=tk.TOP, fill=tk.X)
classification_label = tk.Label(middle_frame, text="Classification: Freshman")
classification_label.pack(side=tk.TOP)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.TOP, fill=tk.X)
hobby_label = tk.Label(bottom_frame, text="Favorite Hobby: Coding and Building projects")
hobby_label.pack(side=tk.TOP)
color_label = tk.Label(bottom_frame, text="Favorite Color: black")
color_label.pack(side=tk.TOP)
holiday_label = tk.Label(bottom_frame, text="Favorite Holiday: New Years")
holiday_label.pack(side=tk.TOP)
season_label = tk.Label(bottom_frame, text="Favorite Season: Winter")
season_label.pack(side=tk.TOP)
root.mainloop()