import Utils


def give_player_you_died(reason):
    Utils.clear_screen()
    print(
        f"¡Oh no! ¡Fallaste!\n{reason}\n¿Te gustaría volverlo a intentar desde un checkpoint?"
    )
    opt = input(">>> ")

    if opt.upper() in ["Y", "SÍ", "S", "YES"]:
        return True
    else:
        Utils.clear_screen()
        print("¡Hasta luego!")
        exit(0)
