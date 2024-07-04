import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Update Task", command=self.update_task).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=2, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter a new task:")
        if task:
            self.tasks.append(task)
            self.update_task_listbox()

    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            new_task = simpledialog.askstring("Input", "Update the selected task:", initialvalue=self.tasks[selected_task[0]])
            if new_task:
                self.tasks[selected_task[0]] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
