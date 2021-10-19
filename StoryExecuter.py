import Errors
import applicationLayer
import presentationLayer
import sessionLayer
import networkLayer

functions = [applicationLayer, presentationLayer, sessionLayer, networkLayer]


def main():
    for checkpoint in functions:
        while True:
            passed = checkpoint.main()
            if passed["passed"]:
                break
            elif not passed["passed"]:
                Errors.give_player_you_died(passed["reason"])
            else:
                raise "BUG!"


if __name__ == "__main__":
    print("ARCHIVO A EJECUTAR: main.py")
