import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("400x450")
        master.config(bg="#f7f7fa")

        self.tasks = []

        # Heading
        tk.Label(master, text="What do you need to do today?", bg="#f7f7fa", font=("Arial", 12)).pack(pady=(10, 0))

        # Input box
        self.taskEntry = tk.Entry(master, font=("Arial", 12))
        self.taskEntry.pack(padx=10, pady=5, fill=tk.X)
        self.taskEntry.bind("<Return>", lambda event: self.add_task())

        # Add button
        tk.Button(master, text="Add", command=self.add_task,
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

        # Task list
        self.list_box = tk.Listbox(master, font=("Arial", 12),
                                   selectbackground="#cce5ff", activestyle='none')
        self.list_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Buttons at the bottom
        btn_frame = tk.Frame(master, bg="#f7f7fa")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Done", command=self.mark_done,
                  bg="#2196F3", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit", command=self.edit_task,
                  bg="#FFC107", fg="black", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_task,
                  bg="#f44336", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.taskEntry.get().strip()
        if not task:
            messagebox.showinfo("Hey!", "Type something before adding.")
            return
        self.tasks.append({"text": task, "done": False})
        self.taskEntry.delete(0, tk.END)
        self.refresh_list()

    def refresh_list(self):
        self.list_box.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "[✔]" if task["done"] else "[ ]"
            self.list_box.insert(tk.END, f"{i + 1}. {status} {task['text']}")
            self.list_box.itemconfig(i, fg="gray" if task["done"] else "black")

    def get_selected_index(self):
        selected = self.list_box.curselection()
        if not selected:
            messagebox.showwarning("Oops", "Pick a task first.")
            return None
        return selected[0]

    def mark_done(self):
        idx = self.get_selected_index()
        if idx is not None:
            self.tasks[idx]["done"] = not self.tasks[idx]["done"]
            self.refresh_list()

    def edit_task(self):
        idx = self.get_selected_index()
        if idx is not None:
            current = self.tasks[idx]["text"]
            updated = simpledialog.askstring("Edit", "Make your changes:", initialvalue=current)
            if updated and updated.strip():
                self.tasks[idx]["text"] = updated.strip()
                self.tasks[idx]["done"] = False
                self.refresh_list()

    def delete_task(self):
        idx = self.get_selected_index()
        if idx is not None:
            confirm = messagebox.askyesno("Sure?", "Delete this task?")
            if confirm:
                del self.tasks[idx]
                self.refresh_list()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
