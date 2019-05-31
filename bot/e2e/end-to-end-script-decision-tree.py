"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_decision_tree',
    'afirmar',
    'entender_decision_tree',
    'negar',
    'algoritmo_decision_tree'
]

user_input = [
    'o que eh decision tree?',
    'beleza',
    'explicar o que eh decision tree',
    'quero não, obrigado',
    'como implementar decision tree'
    ]

utter = [
    'utter_entender_decision_tree',
    'utter_algoritmo_decision_tree',
    'utter_entender_decision_tree',
    'utter_bons_estudos',
    'utter_algoritmo_decision_tree'
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
    E2E_FILE = './e2e_stories_decision_tree.md'
    title = "## Stories Decision Tree for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
