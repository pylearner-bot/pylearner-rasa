"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'kmeans',
    'kmeans_conceito',
    'kmeans_centroide',
    'kmeans_mapeados',
]

user_input = [
    'Como implementar k-means?',
    'O que é K-means?',
    'Como implementar o centroide?',
    'Como visualizar os k-means mapeados?'
]

utter = [
    'utter_kmeans',
    'utter_kmeans_conceitual',
    'utter_kmeans_centroide',
    'utter_kmeans_mapeados'
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
    E2E_FILE = './end-to-end-script-k-means.md'
    title = "## Stories for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
