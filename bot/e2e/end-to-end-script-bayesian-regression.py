"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_bayesian_regression',
    'afirmar',
    'afirmar',
    'despedir',
    'entender_bayesian_regression',
    'negar',
    'entender_bayesian_ridge_regression',
    'afirmar',
    'implementar_bayesian_ridge_regression'
]

user_input = [
    'o que eh bayesian_regression',
    'sim',
    'sim',
    'tchau',
    'fale sobre bayesian regression',
    'não',
    'bayesian regression',
    'ok',
    'como implementar o bayesian regression'
]

utter = [
    'utter_entender_bayesian_regression',
    'utter_entender_bayesian_ridge_regression',
    'utter_implementar_bayesian_ridge_regression',
    'utter_bons_estudos',
    'utter_entender_bayesian_regression',
    'utter_bons_estudos',
    'utter_entender_bayesian_ridge_regression',
    'utter_implementar_bayesian_ridge_regression'
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
    E2E_FILE = './e2e_stories_bayesian_regression.md'
    title = "## Stories for Bayesian Regression Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
