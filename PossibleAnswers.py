affirmative = ['SÍ', 'Y', 'S', 'YES']
negative = ['NO', 'N']

def generate_false_answer():
    return {'success': False}

def generate_true_answer(answer): 
    return {'success': True, 'answer': answer}

def get_answer():
    opt = input('>>> ')
    return check_answer(opt)

def check_answer(answer):
    if answer.upper() in affirmative: return generate_true_answer(True)
    if answer.upper() in negative: return generate_true_answer(False)
    return generate_false_answer()