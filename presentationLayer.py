import StoryManager

story_bits = {
    "prologue": "Nomás terminas de poner la carta en el escritorio, un sabio te saluda. No sabes de dónde salió.\n\
Hasta donde te cobncierne, él se materializó desde el aire.\n\
¡Buenos días! - Grita el sabio.- Veo que llevas un poco de información para el rey de Terlaya.\n\
Si no te molesta, tomaré tu carta y le haré unos pequeños... Ajustes.\n\
Ya sabes cómo es con toda esta información. No te preocupes, de esto me\n\
encargaré yo.\n\
Tras darte una pequeña sonrisa, el sabio te da la carta de regreso. Más pesada que antes, pero no mucho cambio en su tamaño.\n\
Retornas la mirada para agradecerle, pero el sabio ya no está. Sin más preámbulos, decides tomar la única puerta en el cuarto\n\
que no estaba cerrada. Sin embargo, puedes decidir quedarte y esperar al sabio. ¿Lo esperas?",
}

failure_bits = {
    "prologue": "Te quedas esperando al sabio, pero este nunca regresa. La puerta que antes querías tomar, desaparece.\n\
Te quedas vagando en el cuarto para siempre.",
}


def main():
    story_structure = [
        [story_bits["prologue"], [False], failure_bits["prologue"]],
    ]

    return StoryManager.go_through_story(story_structure)
