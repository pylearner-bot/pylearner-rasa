"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_gaussian_naive_bayes',
    'afirmar',
    'negar',
    'implementar_gaussian_nayve_bayes'
]

user_input = [
    'O que é naive bayes?',
    'Sim',
    'Não',
    'Como implementar naive bayes?'
]

utter = [
    'utter_entender_gaussian_naive_bayes',
    'utter_implementar_gaussian_nayve_bayes',
    'utter_bons_estudos',
    'utter_implementar_gaussian_nayve_bayes'
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
    E2E_FILE = './end-to-end-script-naive-bayes.md'
    title = "## Stories for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
