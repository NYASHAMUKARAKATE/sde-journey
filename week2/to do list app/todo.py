import sqlite3
from typing import List, Tuple

class ToDoList:
    def __init__(self):
        # Connect to the SQLite database (creates file if it doesn't exist)
        self.db_conn = sqlite3.connect('todo.db')
        self._create_table()
    
    def _create_table(self):
        # Create the tasks table if it doesn't exist
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                due_date TEXT,
                priority TEXT DEFAULT 'medium',
                archived INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db_conn.commit()

    def add_task(self, task: str, completed: bool = False) -> None:
        # Add a new task to the database
        cursor = self.db_conn.cursor()
        cursor.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, int(completed)))
        self.db_conn.commit()

    def delete_task(self, task: str) -> None:
        # Delete a task by its description
        cursor = self.db_conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE task=?', (task,))
        self.db_conn.commit()

    def mark_task_completed(self, task: str) -> None:
        # Mark a task as completed
        cursor = self.db_conn.cursor()
        cursor.execute('UPDATE tasks SET completed=1 WHERE task=?', (task,))
        self.db_conn.commit()

    def mark_task_not_completed(self, task: str) -> None:
        # Mark a task as not completed
        cursor = self.db_conn.cursor()
        cursor.execute('UPDATE tasks SET completed=0 WHERE task=?', (task,))
        self.db_conn.commit()

    def list_tasks(self) -> List[Tuple[str, bool, str, str]]:
        # Get all tasks (including archived ones)
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT task, completed, due_date, priority FROM tasks')
        return [(task, bool(completed), due_date, priority) for task, completed, due_date, priority in cursor.fetchall()]

    def edit_task(self, old_task: str, new_task: str) -> None:
        # Change the description of a task
        cursor = self.db_conn.cursor()
        cursor.execute('UPDATE tasks SET task=? WHERE task=?', (new_task, old_task))
        self.db_conn.commit()

    def set_due_date(self, task: str, due_date: str) -> None:
        # Set or update the due date for a task
        cursor = self.db_conn.cursor()
        cursor.execute('UPDATE tasks SET due_date=? WHERE task=?', (due_date, task))
        self.db_conn.commit()

    def set_priority(self, task: str, priority: str) -> None:
        # Set or update the priority for a task
        cursor = self.db_conn.cursor()
        cursor.execute('UPDATE tasks SET priority=? WHERE task=?', (priority, task))
        self.db_conn.commit()

    def search_tasks(self, keyword: str) -> List[Tuple[str, bool, str, str]]:
        # Search for tasks containing the keyword
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT task, completed, due_date, priority FROM tasks WHERE task LIKE ?', (f'%{keyword}%',))
        return [(task, bool(completed), due_date, priority) for task, completed, due_date, priority in cursor.fetchall()]

    def list_tasks_sorted(self, by: str = "due_date") -> List[Tuple[str, bool, str, str]]:
        # List tasks sorted by a given column (due_date, priority, or created_at)
        if by not in ("due_date", "priority", "created_at"):
            by = "due_date"
        cursor = self.db_conn.cursor()
        cursor.execute(f'SELECT task, completed, due_date, priority FROM tasks ORDER BY {by}')
        return [(task, bool(completed), due_date, priority) for task, completed, due_date, priority in cursor.fetchall()]

    def archive_completed_tasks(self) -> None:
        # Archive all tasks that are marked as completed
        cursor = self.db_conn.cursor()
        cursor.execute('UPDATE tasks SET archived=1 WHERE completed=1')
        self.db_conn.commit()

    def list_active_tasks(self) -> List[Tuple[str, bool, str, str]]:
        # List only tasks that are not archived
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT task, completed, due_date, priority FROM tasks WHERE archived=0')
        return [(task, bool(completed), due_date, priority) for task, completed, due_date, priority in cursor.fetchall()]