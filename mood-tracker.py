def add_entry(entries):
    day_note = input("How was your day? ")
    if not day_note:
        print("You must write something about your day.")
        return
    mood = input("How were you feeling? happy/sad/neutral ").lower()
    if mood not in ["happy", "sad", "neutral"]:
        print("Invalid mood, we'll use 'neutral'.")
        mood = "neutral"
    entries.append({"note": day_note, "mood": mood})
    print("Successfully added your entry!\n")

def show_entries(entries):
    if not entries:
        print("No entries yet.")
        return
    mood_filter = input("Which moods would you like to see? happy/sad/neutral/all ").lower()
    if mood_filter not in ["happy", "sad", "neutral", "all"]:
        print("Invalid choice, showing all entries.")
        mood_filter = "all"
    print("\n---Entries---")
    for entry in entries:

        if mood_filter == "all" or entry["mood"] == mood_filter:
            print(f"[{entry['mood']}] {entry['note']}")
    print("--------------\n")

def main():
    entries = []
    while True:
        print("1 - Add entry")
        print("2 - Show entries")
        print("3 - Exit")
        choice = input("Choose an option: ")
        if not choice.isdigit():
            print("Invalid input, please enter a valid number.")
            continue
        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            show_entries(entries)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please enter a valid number.")

if __name__ == "__main__":
    main()
