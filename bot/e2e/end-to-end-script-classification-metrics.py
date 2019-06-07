"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_metricas_de_classificacao',
    'quais_as_metricas_de_classificacao',
    'usar_classificacao_f1',
    'recall'
]

user_input = [
    'o que são metricas de classificacao',
    'cite as metricas de classificação',
    'classificação f1',
    'o que eh recall'
    ]

utter = [
    'utter_entender_metricas_de_classificacao',
    'utter_quais_as_metricas_de_classificacao',
    'utter_usar_classificacao_f1',
    'utter_recall'
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
    E2E_FILE = './e2e_stories_classification_metrics.md'
    title = "## Stories for Metricas de Classificação\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
