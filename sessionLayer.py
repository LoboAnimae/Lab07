import StoryManager

story_bits = {
    "prologue": "Llegas a un nuevo cuarto. A diferencia del anterior, este es enorme y poblado.\nVes a muchos otros\
como tú, cada uno con su propia carta. En el centro hay un escritorio circular con miles de otros atendiendo.\n\
Te diriges hacia él y te encuentras con una mujer que te pide la carta.\n¿Se la das?",  # True
    "act1": "La mujer lee la carta con infinitésimo detalle, y escribe datos en una computadora a su lado.\n\
Sin ninguna palabra, levanta la mirada para verte varias veces.",
    "act2": "Tras una pequeña introspección, se levanta, te da la carta, y te señala una puerta.\n\
Hicimos conexión con el reino hace algunos nanosegundos. Ya vas tarde. Ya negociamos paso seguro\n\
entre nosotros y ellos. -Dice la mujer casi monótonamente.- Asegúrate de no perder esta carta.\n\
Puedes tomar la puerta número 3000 a la derecha. Puedes tomar el tren, no te preocupes.\n\
La carta ahora es tu llave, te espera un paquete del otro lado de la ciudad. El tren te llevará.",
    "act3": "Sin más preámbulos, te diriges hacia el tren señalado. Allí, un señor te espera y recibe\n\
tu carta como pasaje.\n\
¡Buen día! -Grita él.- Hoy nos dirigimos a la sección del puerto. El código de su carta es 860ee3fd-1eaf-4cbb-a54c-d5b325b99971.\n\
En el tren, hay otros iguales a ti. Apenas con una carta cada uno. Sin embargo, cada uno se baja en diferentes estaciones.\n\
Al llegar a la estación 3000, solamente tú te bajas.",
    "act4": "Al bajarte, un pequeño señor te pide tu código y señala tu carta.\n\
¿Se la das? ",
}

failure_bits = {
    "prologue": "Al no darle la carta, te encuentras con una mirada cautiva y enojada. Con su dedo, te señala y un dron\n\
te toma de los brazos y te enseña la salida hacia un cuarto oscuro. No sabes dónde estás, ni por cuánto tiempo estarás allí.",
    "act1234": "Decides no darle la carta y sigues de largo. A la distancia, ves una puerta sin abrirse, y un hombre te patea de regreso.\n\
No tienes autorización -Te dice.- No puedes pasar.",
}


def main():
    story_structure = [
        [story_bits["prologue"], [True], failure_bits["prologue"]],
        [
            story_bits["act1"]
            + "\n"
            + story_bits["act2"]
            + "\n"
            + story_bits["act3"]
            + "\n"
            + story_bits["act4"],
            [True],
            failure_bits["act1234"],
        ],
    ]

    return StoryManager.go_through_story(story_structure)
