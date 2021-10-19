import StoryManager

story_bits = {
    "prologue": 'Le das tu carta al pequeño hombre que te recibió, el cual sale corriendo\n\
hacia un pequeño kiosko al lado de la estación, retornando con una caja mucho más grande, pero igual\n\
de pesada que la carta. Encima hay una dirección e instrucciones sobre a dónde ir y qué hacer allí.\n\
Sin embargo, también te entrega una banda que tiene toda la información que "necesitarás" en tu viaje.\n\
Te informa sobre tu destinatario y cómo llegar hacia él también.\n',
    "act1": "Al llegar a la única puerta en el edificio, sales a un pequeño puerto con un pequeño barco al\n\
final. Te diriges hacia él, pero no hay nadie. Detrás, escuchas a alguien que te saluda.\n\
¡Hola amigo! ¿Planeas zarpar hoy? -Te pregunta el extraño, vestido con un traje que asimila a aquel de un\n\
capitán.- Soy Contrarius, pero mis amigos me dicen el Control. Te vi salir del edificio.\n\
¿Te dio algo Mac?",
    "act2": "Sin esperar tu respuesta, toma el paquete de tus manos y lo lee.\n\
¡Ya veo! -Grita, tirando el paquete a bordo.- Sube ya, que zarpamos enseguida.\n\
Este paquete es de extremada importancia, y nos tomará un buen rato el llegar\n\
a su destino, por medio de todas las islas. Tomaremos la ruta principal de ruteo\n\
trasoceánico y nos encontraremos del otro lado en un santiamén.\n\
¿Continuar?",
    "fin": 'Pasamos por muchas islas. Encontramos monstruos marinos, piratas, entre otros. Logramos salir\n\
victoriosos gracias al barco y el saber a dónde íbamos. Siempre que llegábamos a una isla, nos marcaban\n\
en qué dirección seguir nuestro camino, hasta eventualmente llegar al otro lado, hacia donde el rey estaba.\n\
Allí, entregué el paquete, e hice todo en perfecto reverso, como si de un aeropuerto se tratase.\n\
Sin embargo, al llegar a la sala del rey, entregué el mensaje y lo leyó en voz alta:\n\
"u up?"\n\
\n\nHas completado la historia. Modo difícil desbloqueado. ¿Continuar?',
}

failure_bits = {"prologue": "¡Decidiste abandonar! ¡Eres un paquete caído!", "act1": ""}


def main():
    story_structure = [
        [story_bits["prologue"], [True], failure_bits["prologue"]],
        [story_bits["act1"], [True, False], ""],
        [story_bits["act2"], [True], ""],
        [story_bits["fin"], [True], ""],
    ]

    return StoryManager.go_through_story(story_structure)
