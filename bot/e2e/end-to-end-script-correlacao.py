"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_correlacao',
    'afirmar',
    'afirmar',
    'entender_correlacao',
    'negar',
    'entender_correlacao',
    'afirmar',
    'negar',
    'calcular_correlacao'
]

user_input = [
    'o que eh correlacao',
    'ok',
    'sim',
    'explicar correlação',
    'nop',
    'diga-me o que é correlação',
    'Ss',
    'Nn',
    'Como eu calculo a correlação'
    ]

utter = [
    'utter_entender_correlacao',
    'utter_matriz_correlacao',
    'utter_indice_correlacao',
    'utter_entender_correlacao',
    'utter_bons_estudos',
    'utter_entender_correlacao',
    'utter_matriz_correlacao'
    'utter_calcular_correlacao'
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
    E2E_FILE = './e2e_stories_correlacao.md'
    title = "## Stories Correlaction for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
