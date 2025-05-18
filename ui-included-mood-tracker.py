import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import json
from datetime import datetime

FILENAME = "diary.json"

def load_entries():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_entries(entries):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=4)

class DiaryApp:
    def __init__(self, root):
        self.root = root
        root.title("My Diary App")

        self.entries = load_entries()

        self.note_label = tk.Label(root, text="Write about your day:")
        self.note_label.pack()

        self.note_text = tk.Text(root, height=5, width=40)
        self.note_text.pack()

        self.mood_label = tk.Label(root, text="Select your mood:")
        self.mood_label.pack()

        self.mood_var = tk.StringVar(value="neutral")
        moods = [("Happy", "happy"), ("Sad", "sad"), ("Neutral", "neutral")]
        for text, mood in moods:
            tk.Radiobutton(root, text=text, variable=self.mood_var, value=mood).pack(anchor=tk.W)

        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Show Entries", command=self.show_entries)
        self.show_button.pack(pady=5)

        self.entries_text = scrolledtext.ScrolledText(root, height=10, width=50)
        self.entries_text.pack()

    def add_entry(self):
        note = self.note_text.get("1.0", tk.END).strip()
        if not note:
            messagebox.showwarning("Warning", "Please write something about your day!")
            return
        mood = self.mood_var.get()
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.entries.append({"note": note, "mood": mood, "date": date_str})
        save_entries(self.entries)
        messagebox.showinfo("Success", "Entry added successfully!")
        self.note_text.delete("1.0", tk.END)

    def show_entries(self):
        self.entries_text.delete("1.0", tk.END)
        mood_filter = simpledialog.askstring("Filter", "Which moods to show? happy/sad/neutral/all", initialvalue="all")
        if mood_filter is None:
            return
        mood_filter = mood_filter.lower()
        if mood_filter not in ["happy", "sad", "neutral", "all"]:
            messagebox.showinfo("Info", "Invalid mood filter, showing all entries.")
            mood_filter = "all"
        filtered = [e for e in self.entries if mood_filter == "all" or e["mood"] == mood_filter]
        if not filtered:
            self.entries_text.insert(tk.END, "No entries to show.\n")
            return
        for entry in filtered:
            self.entries_text.insert(tk.END, f"[{entry['date']}] [{entry['mood']}] {entry['note']}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
