import StoryManager

story_bits = {
    "prologue": "Te despiertas en un lugar extraño, donde la materia parece no tener influencia en lo que sucede a tu alrededor.\nUn ser extraño te muestra una carta y te señala hacia una salida.\n¿Aceptas la carta?",
    "act1": "Sientes una gran responsabilidad al tomar la carta.\nTe diriges hacia la puerta señalada y observas la carta una vez más, preguntándote qué hay dentro.\n¿Deseas abrirla?",
    "act2": "En la puerta te encuentras a un gigante. Sus manos están atadas frente a su torso, y su cara parece de piedra.\nSus ojos están detrás de un pequeño pañuelo gris. Aunque no puedas ver sus ojos, puedes sentir su mirada.\n\
Con cada paso que das hacia la puerta, su mirada se queda activa sobre ti.",
    "act3": "Mientras pasas por la puerta, alguien marca una pequeña pizarra con letras que no entiendes.\n\
Tu paso se acelera y llegas a un pequeño escritorio. Una luz parece desprenderse de este.\
Tu carta comienza a brillar.\n¿Deseas ponerla encima del escritorio?",
}

failure_bits = {
    "prologue": "Fallaste en agarrar la información y fuiste descartado. Así de temprano, ¿Enserio?",
    "act1": "Dentro de la carta puedes ver un montón de caracteres que no entiendes. Sin embargo, una alarma suena\ny la carta pierde integridad, desapareciendo en el aire. Te descartan. ¡No deberías de estar metiendo\nnarices!",
    "act2and3": "Decides pasar de largo el escritory y no ver hacia atrás. Tu carta es robada por el gigante, el cual la destruye. Te descartan.",
}


def main():
    story_structure = [
        [story_bits["prologue"], [True], failure_bits["prologue"]],
        [story_bits["act1"], [False], failure_bits["act1"]],
        [
            story_bits["act2"] + "\n" + story_bits["act3"],
            [True],
            failure_bits["act2and3"],
        ],
    ]

    return StoryManager.go_through_story(story_structure)
