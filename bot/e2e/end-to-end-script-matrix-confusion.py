"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_matriz_confusao',
    'afirmar',
    'afirmar',
    'implementar_matriz_confusao_sklearn',
    'afirmar',
    'entender_verdadeiro_positivo'

]

user_input = [
    'o que eh matriz de confusão?',
    'sim',
    'sim',
    'como implementar matriz de confusão?',
    'sim',
    'verdadeiro positivo'
    ]

utter = [
    'utter_entender_matriz_confusao',
    'utter_implementar_matriz_confusao_sklearn',
    'utter_implementar_matriz_confusao_pandas',
    'utter_implementar_matriz_confusao_sklearn',
    'utter_implementar_matriz_confusao_pandas',
    'utter_entender_verdadeiro_positivo'
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
    E2E_FILE = './e2e_matrix_confusion.md'
    title = "## Stories for Matrix Confusion Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
