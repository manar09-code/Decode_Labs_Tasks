from datetime import datetime

print("=" * 50)
print("🤖 DevMate AI - Programming Assistant")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}! I'm DevMate AI.")
print("Type 'help' to see available topics.")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print(f"DevMate: Hello {name}! How can I help you?")

    # Help
    elif user == "help":
        print("""
Available Topics:
- html
- css
- javascript
- python
- ai
- web development
- time
- exit
        """)

    # HTML
    elif "html" in user:
        print("DevMate: HTML is used to structure web pages.")

    # CSS
    elif "css" in user:
        print("DevMate: CSS is used to style web pages.")

    # JavaScript
    elif "javascript" in user or "js" in user:
        print("DevMate: JavaScript adds interactivity to websites.")

    # Python
    elif "python" in user:
        print("DevMate: Python is widely used in AI, automation, and web development.")

    # AI
    elif "ai" in user or "artificial intelligence" in user:
        print("DevMate: Artificial Intelligence enables computers to simulate human intelligence.")

    # Web Development
    elif "web development" in user:
        print("DevMate: Web development includes frontend and backend technologies.")

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"DevMate: Current time is {current_time}")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print(f"DevMate: Goodbye {name}! Keep coding!")
        break

    # Unknown input
    else:
        print("DevMate: Sorry, I don't understand that. Type 'help' for available commands.")