"""
Portfolio: Task Queue with Undo (deque, Counter)
Topic: collections.deque, collections.Counter, FIFO/LIFO
"""

from collections import deque, Counter


def main():
    task_queue: deque[str] = deque()
    undo_stack: deque[str] = deque()
    completed: list[str] = []
    print("=== Task Queue (collections) ===\n")
    print("Commands: add, do, undo, list, stats, clear, quit")

    while True:
        cmd = input("\nCommand: ").strip().lower()
        if not cmd:
            continue

        if cmd == "quit":
            print("Bye.")
            break

        if cmd == "add":
            task = input("Task name: ").strip()
            if task:
                task_queue.append(task)
                print(f"Added: {task}. Queue size: {len(task_queue)}")
            else:
                print("Empty task ignored.")

        elif cmd == "do":
            if not task_queue:
                print("Queue is empty.")
                continue
            task = task_queue.popleft()
            completed.append(task)
            undo_stack.append(task)
            print(f"Done: {task}")

        elif cmd == "undo":
            if not undo_stack:
                print("Nothing to undo.")
                continue
            task = undo_stack.pop()
            task_queue.appendleft(task)
            if completed and completed[-1] == task:
                completed.pop()
            print(f"Undone: {task}")

        elif cmd == "list":
            print("Queue:", list(task_queue))
            print("Completed:", completed[-10:])

        elif cmd == "stats":
            if completed:
                counts = Counter(completed)
                print("Completed (count):", dict(counts))
            else:
                print("No completed tasks yet.")
            print("Queue length:", len(task_queue))

        elif cmd == "clear":
            task_queue.clear()
            undo_stack.clear()
            completed.clear()
            print("All cleared.")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
