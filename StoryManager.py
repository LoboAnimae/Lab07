import PossibleAnswers
import Utils


def fail_here(reason):
    return {"passed": False, "reason": reason}


def story_interaction(story, correct_answer=[True], failure_message=""):
    unknown_answer = False
    while True:
        Utils.clear_screen()
        print(story)
        if unknown_answer:
            print("¡No entendí esa respuesta!")
        cont = PossibleAnswers.get_answer()
        if cont["success"]:
            if cont["answer"] in correct_answer:
                break
            else:
                return fail_here(failure_message)
        else:
            unknown_answer = True
    return True


def go_through_story(story_structure):
    story_length = len(story_structure)
    counter = 0
    for story_piece in story_structure:
        if story_length == counter:
            break
        story, correct_answer, failure_message = story_piece
        followedPath = story_interaction(story, correct_answer, failure_message)
        counter += 1
        if followedPath == True:
            continue
        return followedPath
    return {"passed": True}
