"""
Portfolio: Simple Contact Book (in-memory)
Topic: lists, dictionaries, CRUD operations
"""


def add_contact(contacts: list[dict]) -> None:
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    if not name or not phone:
        print("Name and phone are required.")
        return
    contacts.append({"name": name, "phone": phone, "email": email or "-"})
    print("Contact added.")


def find_contacts(contacts: list[dict], query: str) -> list[dict]:
    query = query.lower()
    return [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"] or query in c["email"].lower()
    ]


def search_contact(contacts: list[dict]) -> None:
    query = input("Search (name, phone or email): ").strip()
    if not query:
        return
    found = find_contacts(contacts, query)
    if not found:
        print("No results.")
        return
    for i, c in enumerate(found, 1):
        print(f"  {i}. {c['name']} | {c['phone']} | {c['email']}")


def list_all(contacts: list[dict]) -> None:
    if not contacts:
        print("No contacts yet.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"  {i}. {c['name']} | {c['phone']} | {c['email']}")


def delete_contact(contacts: list[dict]) -> None:
    query = input("Enter name or phone to delete: ").strip()
    if not query:
        return
    found = find_contacts(contacts, query)
    if not found:
        print("Contact not found.")
        return
    if len(found) == 1:
        contacts.remove(found[0])
        print("Contact deleted.")
        return
    print("Multiple matches. Narrow your search.")


def main():
    contacts = []
    print("=== Contact Book ===\n")

    while True:
        print("1 - Add contact")
        print("2 - Search")
        print("3 - List all")
        print("4 - Delete contact")
        print("0 - Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            list_all(contacts)
        elif choice == "4":
            delete_contact(contacts)


if __name__ == "__main__":
    main()
