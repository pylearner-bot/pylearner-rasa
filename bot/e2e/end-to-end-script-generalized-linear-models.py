"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_modelos_lineares_generalizados',
    'afirmar',
    'afirmar',
    'entender_modelos_lineares_generalizados',
    'afirmar',
    'negar',
    'entender_modelos_lineares_generalizados',
    'negar',
    'entender_regressao_logistica',
    'afirmar',
    'entender_regressao_logistica',
    'negar'
]

user_input = [
    'o que são modelos lineares generalizados?',
    'Sim',
    'ok',
    'O que são generalized linear models',
    'sim',
    'não, valeu',
    'o que eh regressao logistica',
    'quero sim valeu',
    'me fale sobre regressão logiística',
    'não quero'
    ]

utter = [
    'utter_entender_modelos_lineares_generalizados',
    'utter_entender_regressao_logistica',
    'utter_implementar_regressao_logistica',
    'utter_entender_modelos_lineares_generalizados',
    'utter_entender_regressao_logistica',
    'utter_bons_estudos',
    'utter_entender_modelos_lineares_generalizados',
    'utter_bons_estudos',
    'utter_entender_regressao_logistica',
    'utter_implementar_regressao_logistica',
    'utter_entender_regressao_logistica',
    'utter_implementar_regressao_logistica'
    ]


def create_stories(user_intent, user_input, utter):
    """
    Zip through lists and return them in the e2e test format
    """
    for intent, inp, utt in zip(user_intent, user_input, utter):
        yield "* {}: {}\n\t - {}".format(intent, inp, utt)


def write_file(stories):
    """
    write story tests to file
    """
    E2E_FILE = './e2e_stories_generalized_linear_mode.md'
    title = "## Stories Generalized Linear Mode for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
