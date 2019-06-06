<p align="center">
    <img src="https://raw.githubusercontent.com/fga-eps-mds/2019.1-PyLearner/master/docs/img/Logo_text.jpg" alt="Logo" height=300 width=400>
</p>

<h1 align="center">
  <a href="https://fga-eps-mds.github.io/2019.1-PyLearner">
    Machine Learning Chatbot Assistant
  </a>
</h1>

<!--<p align="center">
    <a href="https://fga-eps-mds.github.io/2019.1-PyLearner"><strong>Read the Docs &raquo;</strong></a>
    <br>
</p>
//-->

[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.com/pylearner-bot/pylearner-rasa.svg?branch=master)](https://travis-ci.com/pylearner-bot/pylearner-rasa)<a href="https://codeclimate.com/github/pylearner-bot/pylearner-rasa/maintainability"><img src="https://api.codeclimate.com/v1/badges/8d809e9a3afb53be6deb/maintainability" /></a>
![GitHub watchers](https://img.shields.io/github/watchers/fga-eps-mds/2019.1-PyLearner.svg?style=social)

<p align="justify">
O PyLearner surge com a ideia de ter um ambiente web que traga a comodidade de utilizar Jupyter Notebook sem instalar localmente na máquina e que possua também artifícios para ajudar iniciantes em Machine Learning. Para isso, desenvolvemos o chatbot <i>Pyter</i> que tira dúvidas recomenda conteúdos para o usuário estudar e faz demonstrações usando tutoriais.

- **Aprendizado.** Com o uso frequente do pyter para auxiliar em atividades de machine learning ou até mesmo para recomendar exercícios, você pode aprender muito!
- **Praticidade.** A junção do chat no jupyter torna muito mais tranquilo tirar as duvidas no ambiente em que já esta aprendendo.
- **Ajuda.** O Pyter não só te ajuda com dúvidas mas também com possíveis erros nas células do jupyter.
- **Tutoriais.** Os tutoriais são os exemplos mais clássicos em machine learning, para que o aluno possa ter uma experiencia de solucionar o seu primeiro problema de forma completa.


## Conteudos

- [Documentação](#-documentação)
- [Como usar?](#-como-usar)
- [Funções já implementadas](#-funções-implementadas)
- [Roadmap do projeto](#-roadmap-do-projeto)
- [Codigo de Conduta](#-código-de-conduta)
- [Licença](#-licença)

</p>

## Funções implementadas

As principais habilidades do _Pyter_ são:

* Pré-processamento de dados.
    - [x] Importação de dados [(Pandas)](https://pandas.pydata.org/)
    - [x] Tratamento de dados [(Pandas)](https://pandas.pydata.org/), [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
* Modelagem.
    - [x] Aprendizado supervisionado [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
        - Generalized Linear Models
            - Logistic regression
        - Support Vector Machines
            - Classification
        - Stochastic Gradient Descent
            - Classification
        - Nearest Neighbors
            - Nearest Neighbors Classification
        - Naive Bayes
            - Gaussian Naive Bayes
        - Decision Trees
            - Classification
    - [ ] Aprendizado não-supervisionado [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
* Visualização.
    - [x] Visualização de dados [(Matplotlib)](https://matplotlib.org/), [(Seaborn)](https://seaborn.pydata.org/)
    - [x] Visualização de resultados [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
* Tutorial.
    - [x] Iris Flower [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
    - [x] MNIST [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
    - [x] Titanic [(SciKit Learn)](https://scikit-learn.org/stable/modules/preprocessing.html)
* Sugestões de conteúdo.
    - [ ] Espaços de conteúdos [(Medium)](https://medium.com/), [(TowardsDataScience)](https://towardsdatascience.com/), [(Kaggle)](https://kaggle.com)
    - [ ] Fórum [(Cross Validated)](https://stats.stackexchange.com/), [(Artificial Intelligence StackExchange)](https://ai.stackexchange.com/)

## Como usar

Clone o repositório:

```sh
git clone https://github.com/fga-eps-mds/2019.1-PyLearner.git
```

Suba o contêiner. (`sudo` pode ser necessário)

```sh
docker-compose up --build
```

Acesse o jupyter notebook em http://localhost:8888/

## Roadmap do projeto

Você pode aprender mais sobre nossa visão dando uma olhada no nosso [Roadmap](https://fga-eps-mds.github.io/2019.1-PyLearner/roadmap/Roadmap-Projeto/)

## Código de Conduta
Nós adotamos um [Código de Conduta](https://github.com/pylearner-bot/pylearner-rasa/blob/master/.github/CODE_OF_CONDUCT.md) que esperamos que os participantes do projeto sigam. Por favor, leia o texto completo para que você possa entender quais ações serão e quais não serão toleradas.

## Licença

Este projeto está licenciado sob a [Licença](https://github.com/pylearner-bot/pylearner-rasa/blob/master/LICENSE) MIT. 

Os direitos autorais nos arquivos de definição são respectivos de cada colaborador listado no início de cada arquivo de definição

## Ferramentas utilizadas em desenvolvimento

<p float="left">
  <img src="https://telegram.org/img/t_logo.png" width="60"/>
  <img src="https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png" width="60"/>
  <img src="https://koenig-media.raywenderlich.com/uploads/2015/07/Featured4.png" width="60"/>
  <img src="https://jupyter.org/assets/main-logo.svg" width="60"/>
  <img src="https://www.ericholscher.com/_static/img/readthedocs-logo.png" width="60"/>
  <img src="https://png.pngtree.com/svg/20170622/3e5b63be8b.svg" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png" width="60"/>
  <img src="https://www.completecontrol.co.uk/wp-content/uploads/2017/01/HTML5_Badge_512.png" width="60"/>
  <img src="http://lifehackdev.xsrv.jp/ZakkiBlog/images/thumb/css3_logo.svg" width="60"/>
  <img src="https://www.docker.com/sites/default/files/social/docker_facebook_share.png" width="60"/>
  <img src="https://pbs.twimg.com/profile_images/866319063261356033/UoI86ZDX.jpg" width="60"/>
  <img src="https://cdn.worldvectorlogo.com/logos/rocket-chat.svg" width="60"/>
  <img src="https://github.githubassets.com/images/modules/logos_page/Octocat.png" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Google_Drive_logo.png" width="60"/>
  <img src="https://pbs.twimg.com/profile_images/1101641643193561088/YSp2QvBm.png" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Vimlogo.svg" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Visual_Studio_Code_1.18_icon.svg/1200px-Visual_Studio_Code_1.18_icon.svg.png" width="60"/>
  <img src="https://cdn.freebiesupply.com/logos/large/2x/atom-4-logo-png-transparent.png" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Tux.png/220px-Tux.png" width="60"/>
  <img src="https://www.notebookcheck.net/fileadmin/Notebooks/News/_nc3/20170817_Google_Chrome_logo_vector_download.png" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Firefox_Logo%2C_2017.svg/1200px-Firefox_Logo%2C_2017.svg.png" width="60"/>
  <img src="https://avatars3.githubusercontent.com/u/46843839?v=4" width="60"/>
</p>


## Ferramentas ensinadas pelo <i>Pyter</i>

<p float="left">
  <img src="https://i0.wp.com/www.numfocus.org/wp-content/uploads/2016/07/pandas-logo-300.png?w=1080&ssl=1" width="60"/>
  <img src="https://matplotlib.org/_static/logo2.svg" width="60"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" width="60"/>
  <img src="https://www.seabornnetworks.com/wp-content/uploads/2017/05/seaborn-498x280.jpg" width="60"/>
</p>

## Conteúdos recomendados por <i>Pyter</i>

<p float="left">
  <img src="https://cdn-images-1.medium.com/max/1600/1*emiGsBgJu2KHWyjluhKXQw.png" width="60"/>
  <img src="https://cdn-images-1.medium.com/max/1200/1*F0LADxTtsKOgmPa-_7iUEQ.jpeg" width="60"/>
  <img src="https://cdn.sstatic.net/Sites/stats/img/apple-touch-icon@2.png?v=344f57aa10cc" width="60"/>
  <img src="https://storage.googleapis.com/kaggle-organizations/4/thumbnail.png" width="60"/>
  <img src="https://cdn.sstatic.net/Sites/ai/img/logo.svg?v=99838c31f823" width="60"/>
</p>

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="https://www.linkedin.com/in/gabriel-ziegler-323121106/"><img src="https://avatars2.githubusercontent.com/u/18370133?v=4" width="100px;" alt="Gabriel Ziegler"/><br /><sub><b>Gabriel Ziegler</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=gabrielziegler3" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/davialvb"><img src="https://avatars3.githubusercontent.com/u/34287081?v=4" width="100px;" alt="Davi Alves"/><br /><sub><b>Davi Alves</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=davialvb" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/Mexazonic"><img src="https://avatars1.githubusercontent.com/u/48650663?v=4" width="100px;" alt="Bruno Duarte"/><br /><sub><b>Bruno Duarte</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=Mexazonic" title="Documentation">📖</a></td><td align="center"><a href="https://www.linkedin.com/in/eug%C3%AAnio-sales-siqueira-19533213b/"><img src="https://avatars0.githubusercontent.com/u/42457772?v=4" width="100px;" alt="Eugenio Sales Siqueira"/><br /><sub><b>Eugenio Sales Siqueira</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=Eugeniosales" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/thiagoiferreira"><img src="https://avatars2.githubusercontent.com/u/26505480?v=4" width="100px;" alt="Thiago Ferreira"/><br /><sub><b>Thiago Ferreira</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=thiagoiferreira" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/ZarathosDeath"><img src="https://avatars0.githubusercontent.com/u/39169676?v=4" width="100px;" alt="Ernando Braga"/><br /><sub><b>Ernando Braga</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=ZarathosDeath" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/alexportof"><img src="https://avatars0.githubusercontent.com/u/45185346?v=4" width="100px;" alt="Álex Porto"/><br /><sub><b>Álex Porto</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=alexportof" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/joao15victor08"><img src="https://avatars2.githubusercontent.com/u/32016154?v=4" width="100px;" alt="Joao Victor de Oliveira Matos"/><br /><sub><b>Joao Victor de Oliveira Matos</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=joao15victor08" title="Documentation">📖</a></td><td align="center"><a href="https://www.linkedin.com/in/carlos-enrique-rodrigues-aragon-084b47b5"><img src="https://avatars2.githubusercontent.com/u/18129918?v=4" width="100px;" alt="Carlos Aragon"/><br /><sub><b>Carlos Aragon</b></sub></a><br /><a href="https://github.com/fga-eps-mds/2019.1-PyLearner/commits?author=carlosaragon" title="Documentation">📖</a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
