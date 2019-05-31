"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_feature_scaling',
    'afirmar',
    'entender_feature_scaling',
    'negar',
    'entender_normalizacao',
    'afirmar',
    'entender_normalizacao',
    'negar',
    'entender_padronizacao',
    'afirmar',
    'entender_padronizacao',
    'negar'
]

user_input = [
    'o que eh feature scaling?',
    'Sim',
    'Explicar feature scaling',
    'Não',
    'O que eh normalização?',
    'sim',
    'Explicar pra mim o que eh normalização',
    'não, valeu',
    'O que é padronização?',
    'quero sim valeu',
    'Padronização',
    'não quero'
    ]

utter = [
    'utter_entender_feature_scaling',
    'utter_tecnicas_feture_scaling',
    'utter_entender_feature_scaling',
    'utter_bons_estudos',
    'utter_entender_normalizacao',
    'utter_implementar_normalizacao',
    'utter_entender_normalizacao',
    'utter_bons_estudos',
    'utter_entender_padronizacao',
    'utter_implementar_padronizacao',
    'utter_entender_padronizacao',
    'utter_bons_estudos'
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
    E2E_FILE = './e2e_stories_feature_scaling.md'
    title = "## Stories Feature Scaling for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
