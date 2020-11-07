import random

def main():
    print("Welcome to the Psych 'Sidekick Name Picker. '\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ("Baby Oil", "Bowel Noises", "Bad News", "Foncy", "Unko")
    last = ("CHIN", "Meshi", "Gohan", "Pasta", "Arisa")

    while True:
        firstName = random.choice(first)
        lastName = random.choice(last)

        print("\n\n")
        print(f"{firstName} {lastName}")
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower() == "n":
            break
        input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
