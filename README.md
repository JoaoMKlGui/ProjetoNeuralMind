# ProjetoNeuralMind
Projeto para estágio de verão NeuralMind utilizando RAG para gerar respostas sobre o vestibular da unicamp de 2024

Temos 3 bibliotecas: Retriever, Conversation, Pipeline
Retriever: Constrói o init do retriever, prompt node e a pipeline generativa
Conversation: Possui o coração do código, a conversação com o usuário e mais a função que cria a ferramenta de busca
Pipeline: Possui funções para a conversão do documento em pdf sobre o vestibular para um documento do haystack

Para rodar, é necessária a execução dos seguintes comandos em um terminal linux:
  pip install --upgrade pip
  pip install farm-haystack
  wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.04.tar.gz
  tar -xvf xpdf-tools-linux-4.04.tar.gz && sudo cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin

Caso queira testar no colab, rode o seguinte trecho:
  pip install --upgrade pip
  pip install farm-haystack[colab]
  wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.04.tar.gz
  tar -xvf xpdf-tools-linux-4.04.tar.gz && sudo cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin

Ademais, para que a ferramenta funcione, você precisará de uma chave da API da OpenAI, uma vez que a ferramenta faz uso do GPT Turbo 3.5 para geração das respostas.
A implementação foi simples e rápida através da leitura da documentação do GPT e do framework Haystack. As funções foram testadas primariamente no colab devido a sua alta capacidade de processamento.
Principal dificuldade encontrada durante o desenvolvimento foi a escolha dos modelos, os quais eu não havia conhecimento prévio devido à falta de aprofundamento em NLP, e também a utilização do framework, uma vez que possui inúmeras ferramentas.
Realizar a procura daquilo que eu precisava e como utilizar foi difícil a princípio.
