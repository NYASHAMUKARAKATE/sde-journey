import customtkinter as ctk
from tkinter import messagebox
from todo import ToDoList

# Set up the dark appearance and color theme for the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("800x540")
        self.todo_list = ToDoList()
        self.create_widgets()
        self.update_task_list()

    def create_widgets(self):
        # --- Top input area for adding tasks ---
        entry_frame = ctk.CTkFrame(self)
        entry_frame.pack(pady=16, padx=16, fill="x")

        self.task_entry = ctk.CTkEntry(entry_frame, width=220, placeholder_text="Task description")
        self.task_entry.pack(side="left", padx=8, pady=8)

        self.due_entry = ctk.CTkEntry(entry_frame, width=120, placeholder_text="YYYY-MM-DD")
        self.due_entry.pack(side="left", padx=8, pady=8)

        self.priority_var = ctk.StringVar(value="medium")
        self.priority_menu = ctk.CTkOptionMenu(entry_frame, variable=self.priority_var, values=["high", "medium", "low"], width=100)
        self.priority_menu.pack(side="left", padx=8, pady=8)

        add_button = ctk.CTkButton(entry_frame, text="Add Task", command=self.add_task)
        add_button.pack(side="left", padx=8, pady=8)

        # --- Search area ---
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=8, padx=16, fill="x")

        self.search_entry = ctk.CTkEntry(search_frame, width=220, placeholder_text="Search...")
        self.search_entry.pack(side="left", padx=8, pady=8)
        search_button = ctk.CTkButton(search_frame, text="Search", command=self.search_tasks, width=90)
        search_button.pack(side="left", padx=8, pady=8)
        show_all_button = ctk.CTkButton(search_frame, text="Show All", command=self.update_task_list, width=90)
        show_all_button.pack(side="left", padx=8, pady=8)

        # --- Where tasks will be displayed ---
        self.task_listbox = ctk.CTkFrame(self)
        self.task_listbox.pack(fill="both", expand=True, padx=16, pady=12)
        self.task_rows = []

        # --- Action buttons ---
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=12, padx=16, fill="x")

        ctk.CTkButton(button_frame, text="Mark Complete", command=self.mark_complete, width=120).pack(side="left", padx=8)
        ctk.CTkButton(button_frame, text="Mark Not Complete", command=self.mark_not_complete, width=140).pack(side="left", padx=8)
        ctk.CTkButton(button_frame, text="Edit Task", command=self.edit_task, width=100).pack(side="left", padx=8)
        ctk.CTkButton(button_frame, text="Delete Task", command=self.delete_task, width=110).pack(side="left", padx=8)
        ctk.CTkButton(button_frame, text="Archive Completed", command=self.archive_completed, width=160).pack(side="left", padx=8)

    def add_task(self):
        # Add a new task to the database
        task_text = self.task_entry.get().strip()
        due_date = self.due_entry.get().strip()
        priority = self.priority_var.get()
        if not task_text:
            messagebox.showwarning("Input Error", "Please enter a task description.")
            return
        self.todo_list.add_task(task_text, completed=False)
        if due_date:
            self.todo_list.set_due_date(task_text, due_date)
        if priority:
            self.todo_list.set_priority(task_text, priority)
        self.task_entry.delete(0, "end")
        self.due_entry.delete(0, "end")
        self.update_task_list()

    def mark_complete(self):
        # Mark the selected task as completed
        idx = self._get_selected_index()
        if idx is not None:
            task = self.current_tasks[idx][0]
            self.todo_list.mark_task_completed(task)
            self.update_task_list()

    def mark_not_complete(self):
        # Mark the selected task as not completed
        idx = self._get_selected_index()
        if idx is not None:
            task = self.current_tasks[idx][0]
            self.todo_list.mark_task_not_completed(task)
            self.update_task_list()

    def edit_task(self):
        # Edit the description of the selected task
        idx = self._get_selected_index()
        if idx is not None:
            old_task = self.current_tasks[idx][0]
            new_task = ctk.CTkInputDialog(text="Enter new description:", title="Edit Task").get_input()
            if new_task and new_task.strip():
                self.todo_list.edit_task(old_task, new_task.strip())
                self.update_task_list()

    def delete_task(self):
        # Delete the selected task
        idx = self._get_selected_index()
        if idx is not None:
            task = self.current_tasks[idx][0]
            self.todo_list.delete_task(task)
            self.update_task_list()

    def archive_completed(self):
        # Archive all completed tasks
        self.todo_list.archive_completed_tasks()
        self.update_task_list()

    def search_tasks(self):
        # Search for tasks containing the keyword
        keyword = self.search_entry.get().strip()
        if not keyword:
            self.update_task_list()
            return
        results = self.todo_list.search_tasks(keyword)
        self.display_tasks(results)

    def update_task_list(self):
        # Refresh the displayed list of tasks
        tasks = self.todo_list.list_active_tasks()
        self.display_tasks(tasks)

    def display_tasks(self, tasks):
        # Remove old rows from the display
        for row in self.task_rows:
            row.destroy()
        self.task_rows = []
        self.current_tasks = tasks

        # Header row
        header = ctk.CTkFrame(self.task_listbox)
        header.pack(fill="x")
        for i, col in enumerate(["Task", "Status", "Due Date", "Priority"]):
            ctk.CTkLabel(header, text=col, font=("Segoe UI", 13, "bold"), width=180, anchor="center").grid(row=0, column=i, padx=2, pady=2)
        self.task_rows.append(header)

        # Task rows
        for idx, (task, completed, due_date, priority) in enumerate(tasks):
            row = ctk.CTkFrame(self.task_listbox)
            row.pack(fill="x", pady=1)
            # Alternate row background color for readability
            bg = "#2a2d3e" if idx % 2 == 0 else "#232946"
            fg = "#6eeb83" if completed else "#eebbc3"
            status = "✓" if completed else "Pending"
            # Bind click for selection
            def select_row(event, idx=idx):
                self._select_row(idx)
            row.bind("<Button-1>", select_row)
            for i, val in enumerate([task, status, due_date or "", priority]):
                label = ctk.CTkLabel(row, text=val, font=("Segoe UI", 12), text_color=fg, width=180, anchor="center", bg_color=bg)
                label.grid(row=0, column=i, padx=2, pady=2)
                label.bind("<Button-1>", select_row)
            self.task_rows.append(row)
        self.selected_row = None

    def _select_row(self, idx):
        # Highlight the selected row
        for i, row in enumerate(self.task_rows[1:], start=0):
            color = "#393e46" if i == idx else "#2a2d3e" if i % 2 == 0 else "#232946"
            for widget in row.winfo_children():
                widget.configure(bg_color=color)
        self.selected_row = idx

    def _get_selected_index(self):
        # Return the index of the currently selected row
        return self.selected_row

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()