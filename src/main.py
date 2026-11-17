from skills.status import status

def input_manager():
    try:
        x = input("> ").strip()
    except EOFError:
        x = None

    if x is None:
        return 1
    elif x == "":
        pass
        return 0
    elif x == "exit":
        return 1
    elif x == "status":
        status()
        return 0
    else:
        print(f"Comando desconhecido: {x}")
        return 0


def main():
    print("Ingenium ready.")

    while True:
        if input_manager():
            break


if __name__ == "__main__":
    main()