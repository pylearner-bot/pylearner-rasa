# ## end_to_end story 1
# * cumprimentar: oi
#     - utter_cumprimentar
# * importar_json: csv
#     - utter_importar_json_pandas
# * afirmar: aasdfasd
#     - utter_importar_json_pandas1
# * despedir: tchau
#     - utter_despedir

user_intent = [
    'cumprimentar',
    'importar_json',
]

user_input = [
    'oi',
    'csv',
]

utter = [
    'utter_cumprimentar',
    'utter_importar_json_pandas',
]

def create_stories(user_intent, user_input, utter):
    for intent, inp, utt in zip(user_intent, user_input, utter):
        yield "* {}: {}\n\t - {}".format(intent, inp, utt)


def write_file(stories):
    E2E_FILE = './e2e_stories.md'
    with open(E2E_FILE, "w") as f:
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)

stories = create_stories(user_intent, user_input, utter)
write_file(stories)
