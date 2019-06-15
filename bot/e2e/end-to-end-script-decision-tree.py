"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""
user_intent_tree = [
    'entender_decision_tree',
    'afirmar',
    'entender_decision_tree',
    'negar',
    'algoritmo_decision_tree',
    'despedir'
]
user_input_tree = [
    'o que eh decision tree?',
    'beleza',
    'explicar o que eh decision tree',
    'quero não, obrigado',
    'como implementar decision tree',
    'tchau'
    ]
utter_tree = [
    'utter_entender_decision_tree',
    'utter_algoritmo_decision_tree',
    'utter_entender_decision_tree',
    'utter_bons_estudos',
    'utter_algoritmo_decision_tree',
    'utter_despedir'
    ]
def create_stories(user_intent_tree, user_input_tree, utter_tree):
    """
    Zip through lists and return them in the e2e test format
    """
    for intent, inp, utt in zip(user_intent_tree, user_input_tree, utter_tree):
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


stories = create_stories(user_intent_tree, user_input_tree, utter_tree)
write_file(stories)
