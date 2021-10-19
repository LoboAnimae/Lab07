import StoryExecuter
import Utils
import os.path


def print_menu(hardmode):
    showHardmode = "\n3. Hardmode " if hardmode else ""
    print("1. Empezar el Juego\n2. Salir" + showHardmode)


if __name__ == "__main__":
    hardmode = os.path.isfile("hardmode")
    Utils.clear_screen()
    while True:
        try:
            print_menu(hardmode)
            opt = input(">>> ")
            if opt == "1":
                break
            elif opt == "2":
                exit(0)
            elif opt == "3":
                if hardmode:
                    Utils.clear_screen()
                    print(
                        "The XAMPP server stopped responding before you could begin your adventure. What a shame."
                    )
        except KeyboardInterrupt:
            Utils.clear_screen()
            print("Por favor utilice la tercera opción para salir.")
    StoryExecuter.main()
    try:
        open("hardmode", "x")
    except:
        pass
