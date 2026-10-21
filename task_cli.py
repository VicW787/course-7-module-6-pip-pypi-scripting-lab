import argparse
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {"title": self.title, "completed": self.completed}

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.title}"


class User:
    def __init__(self, username, tasks=None):
        self.username = username
        self.tasks = tasks or []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        return task

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return task
        return None

    def to_dict(self):
        return {"tasks": [t.to_dict() for t in self.tasks]}


class TaskStore:
    def __init__(self, path=DATA_FILE):
        self.path = Path(path)

    def get_user(self, username):
        data = json.loads(self.path.read_text()) if self.path.exists() else {}
        tasks = [Task(**t) for t in data.get(username, {}).get("tasks", [])]
        return User(username, tasks)

    def save_user(self, user):
        data = json.loads(self.path.read_text()) if self.path.exists() else {}
        data[user.username] = user.to_dict()
        self.path.write_text(json.dumps(data, indent=2))


def build_parser():
    parser = argparse.ArgumentParser(description="Simple task manager")
    sub = parser.add_subparsers(dest="command", required=True)

    for name, help_text in [
        ("add-task", "Add a task to a user"),
        ("complete-task", "Mark a task as complete"),
    ]:
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--user", required=True)
        p.add_argument("title")

    lst = sub.add_parser("list-tasks", help="List a user's tasks")
    lst.add_argument("--user", required=True)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    store = TaskStore()
    user = store.get_user(args.user)

    if args.command == "add-task":
        task = user.add_task(args.title)
        print(f"Added task for {user.username}: {task.title}")
    elif args.command == "complete-task":
        task = user.complete_task(args.title)
        if task:
            print(f"Completed task for {user.username}: {task.title}")
        else:
            print(f"Task not found: {args.title}")
            return
    elif args.command == "list-tasks":
        for task in user.tasks:
            print(task)
        return

    store.save_user(user)


if __name__ == "__main__":
    main()

