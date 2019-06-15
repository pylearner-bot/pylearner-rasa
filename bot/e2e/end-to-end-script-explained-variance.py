"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_explained_variance_score',
    'afirmar',
    'entender_explained_variance_score',
    'negar',
    'exemplo_funcao_explained_variance_score'
]

user_input = [
    'o que e explained variance?',
    'quero sim',
    'O que eh pontuação de variância?',
    'quero não, obrigado',
    'como implementar explained variance score'
    ]

utter = [
    'utter_entender_explained_variance_score',
    'utter_exemplo_funcao_explained_variance_score',
    'utter_entender_explained_variance_score',
    'utter_bons_estudos',
    'utter_exemplo_funcao_explained_variance_score'
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
    E2E_FILE = './e2e_stories_explained_variance_score.md'
    title = "## Stories Explained Variance for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
