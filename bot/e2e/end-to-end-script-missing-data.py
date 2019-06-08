"""
End to end test script
To add new test cases add the:
    - user_intent
    - user_input
    - utter
"""

user_intent = [
    'entender_dados_faltantes'
    'afirmar'
    'afirmar'
    'afirmar'
    'afirmar'
    'afirmar'
    'afirmar'
    'negar'
    'iniciar_a_deteccao'
    'corrigir_a_deteccao'
    'substituicao_constante'
    'substituicao_imputacao'
    'substituicao_mediana'
]

user_input = [
    'O que são dados faltantes?'
    'sim'
    'sim'
    'sim'
    'sim'
    'sim'
    'sim'
    'Não'
    'Como detectar dados faltantes?'
    'Como corrigir dados faltanteS?'
    'Substituição por constante'
    'Substituição por imputação'
    'Substituição por mediana'
]

utter = [
    'utter_entender_dados_faltantes'
    'utter_causa_dados_faltantes'
    'utter_iniciar_a_deteccao'
    'utter_visualizar_dados_faltantes'
    'utter_dados_faltantes_padronizados'
    'utter_Dados_faltantes_nao_padronizados'
    'utter_corrigir_a_deteccao'
    'utter_bons_estudos'
    'utter_iniciar_a_deteccao'
    'utter_corrigir_a_deteccao'
    'utter_substituicao_constante'
    'utter_substituicao_imputacao'
    'utter_substituicao_mediana'
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
    E2E_FILE = './end-to-end-script-missing-data.md'
    title = "## Stories for Pyter Test\n"

    with open(E2E_FILE, "w") as f:
        f.write(title)
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)


stories = create_stories(user_intent, user_input, utter)
write_file(stories)
