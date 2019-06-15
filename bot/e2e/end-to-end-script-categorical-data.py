"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'cumprimentar',
    'transformar_dados_categoricos',
    'categoricos_rapidos',
    'categoricos_rapidos2',
    'categoricos_rapidos3',
    'categoricos_rapidos4',
    'categoricos_rapidos5',
    'despedir'
]

user_input = [
    'ola',
    'tratar dados categoricos',
    'scikit-learn',
    'label encoder',
    'fit transorform',
    'inverse transform',
    'instanciar',
    'bye'
    ]

utter = [
    'utter_cumprimentar',
    'utter_transformar_dados_categoricos',
    'utter_categoricos_rapidos',
    'utter_categoricos_rapidos2',
    'utter_categoricos_rapidos3',
    'utter_categoricos_rapidos4',
    'utter_categoricos_rapidos5',
    'utter_despedir'
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
    E2E_FILE = './e2e_stories_categorical_data.md'
    title = "## Stories for Categorical Data Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
