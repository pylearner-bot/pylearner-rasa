## caminho feliz
* cumprimentar
    - utter_cumprimentar
* bom_humor
    - utter_bom_humor

## caminho triste 1
* cumprimentar
    - utter_cumprimentar
* mau_humor
    - utter_oferecer_ajuda
    - utter_animar
* afirmar
    - utter_bom_humor

## caminho triste 2
* cumprimentar
    - utter_cumprimentar
* mau_humor
    - utter_oferecer_ajuda
    - utter_animar
* negar
    - utter_despedir


## Despedir
* despedir
    - utter_despedir    

## Apresentacao
* cumprimentar
    - utter_cumprimentar

## Nao entendi
* diga_mais
    - utter_diga_mais  

## fallback
* fora_do_escopo
    - utter_default

## negar sem contexto
* negar
    - utter_despedir

## Apresentacao e despedida
* cumprimentar
    - utter_cumprimentar
* despedir
    - utter_despedir

## Dados Json Convencional
 * importar_json
    - utter_importar_json
 * negar
    - utter_despedir

## Dados Json Completo
  * importar_json
    - utter_importar_json
  * afirmar
    - utter_importar_json_pandas
  * afirmar
    - utter_importar_json_pandas1

## Dados Json Completo2
  * importar_json
    - utter_importar_json
  * afirmar
    - utter_importar_json_pandas
  * negar
    - utter_importar_json_pandas2
