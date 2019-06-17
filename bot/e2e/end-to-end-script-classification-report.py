"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_relatorio_classificacao',
    'gerar_relatorio_classificacao'
]

user_input = [
    'o que eh relatorio de classificacao',
    'como gerar relatorios de classificação'
    ]

utter = [
    'utter_entender_relatorio_classificacao',
    'utter_gerar_relatorio_classificacao'
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
    E2E_FILE = './e2e_stories_classification_report.md'
    title = "## Stories for Classification Report Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
