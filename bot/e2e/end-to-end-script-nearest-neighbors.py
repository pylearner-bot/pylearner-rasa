"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_nearest_neighbors'
    'afirmar'
    'afirmar'
    'entender_classificador_k_neighbors_classifier'
    'classificadores_nearest_neighbors'
    'entender_classificador_radius_neighbors_classifier'
    'afirmar'
    'classificadores_nearest_neighbors'
    'entender_classificador_k_neighbors_classifier'
    'afirmar'
    'implementar_classificadores_nearest_neighbors'
    'RadiusNeighborsClassifier'
    'KNeighborsClassifier'
    'entender_classificacao_nearest_neighbors'
]

user_input = [
    
]

utter = [
    'utter_entender_nearest_neighbors'
    'utter_entender_classificacao_nearest_neighbors'
    'utter_classificadores_nearest_neighbors'
    'utter_entender_classificador_k_neighbors_classifier'
    'utter_classificadores_nearest_neighbors'
    'utter_entender_classificador_radius_neighbors_classifier'
    'utter_RadiusNeighborsClassifier'
    'utter_classificadores_nearest_neighbors'
    'utter_entender_classificador_k_neighbors_classifier'
    'utter_KNeighborsClassifier'
    'utter_implementar_classificadores_nearest_neighbor'
    'utter_RadiusNeighborsClassifier'
    'utter_KNeighborsClassifier'
    'utter_entender_classificacao_nearest_neighbors'
    
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
