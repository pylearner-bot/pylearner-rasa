"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'fluxo_inicio',
    'afirmar',
    'preprocessamento_topicos',
    'afirmar',
    'preprocessamento_topicos',
    'negar',
    'modelagem_topicos',
    'afirmar',
    'modelagem_topicos',
    'negar',
    'visualizacao_topicos'
]

user_input = [
    'Como iniciar?',
    'Sim',
    'Pre-processamento',
    'Sim',
    'Pré-processamento',
    'Não',
    'Modelagem de dados'
    'sim',
    'Modelagem'
    'Nao',
    'Visualização de dados'
]

utter = [
    'utter_listagem_conteudos'
    'utter_preprocessamento_topicos',
    'utter_preprocessamento_topicos',
    'utter_modelagem_topicos',
    'utter_preprocessamento_topicos',
    'utter_bons_estudos',
    'utter_modelagem_topicos',
    'utter_visualizacao_topicos'
    'utter_modelagem_topicos',
    'utter_bons_estudos',
    'utter_visualizacao_topicos'

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
    E2E_FILE = './e2e_stories_begin.md'
    title = "## Stories for Pyter Test - 176\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
