def main():
    print("Ingenium ready.")

    while True:
        try:
            x = input("> ").strip()
        except EOFError:
            break

        if x == "exit":
            break

        if not x:
            continue

        print("Comando recibido:", x)


if __name__ == "__main__":
    main()