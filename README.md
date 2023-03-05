# ChatBot
## Introdução
O projeto tem por objetivo o desenvolvimento de um chat-bot com a capacidade de auxiliar um usuário com suas dúvidas em relação à aula de introdução da disciplina Trabalho Final de Curso. 

## Execução 
Verifique se o Python 3 está instalado na máquina, após isso basta utilizar o comando abaixo para instalar os pacotes necessários:
```
pip install
```

Já com os pacotes em sua máquina realize o código abaixo na pasta do projeto para executá-lo:
```
python3 main.py
```
## Funcionamento
<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/execucao.jpg" alt="Telnet"/>
</p>

[Vídeo para visualização do Funcionamento](https://youtu.be/uGjqAtd-Www)

## Intenções
### Questionamento da Dinâmica

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/QuestionamentoDinamica.png" alt="Telnet"/>
</p>

"questionamento_dinamica": Essa Intent é acionada quando o usuário faz uma pergunta sobre a dinâmica da disciplina. As frases de entrada que disparam essa Intent incluem "vai ter dinamica?", "como será feita a dinamica?" e "haverá dinamica?". As respostas do chat-bot para essa Intent explicam como a dinâmica será composta por meio de apresentações e discussões em aula.

### Saudação

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/Saudacao.png" alt="Telnet"/>
</p>

"saudacao": Essa Intent é acionada quando o usuário faz uma saudação para o chat-bot, como "Oi" ou "tudo bem?". As respostas do chat-bot para essa Intent incluem saudações como "Oi" e "Olá", bem como uma resposta de "tudo bem?" para algumas saudações específicas.

### Despedida

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/Despedida.png" alt="Telnet"/>
</p>

"despedida": Essa Intent é acionada quando o usuário faz uma despedida, como "tchau" ou "até mais". As respostas do chat-bot para essa Intent incluem despedidas como "Até breve" e "Falou".

### Questionamento do Conteúdo

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/QuestionamentoConteudo.png" alt="Telnet"/>
</p>

"questionamento_conteudo": Essa Intent é acionada quando o usuário pergunta sobre o conteúdo que será abordado na disciplina. As frases de entrada que disparam essa Intent incluem "O que será abordado?" e "qual o conteúdo?". As respostas do chat-bot para essa Intent explicam brevemente os tópicos que serão abordados na disciplina.

### Questionamento do Professor

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/QuestionamentoProfessor.png" alt="Telnet"/>
</p>

"questionamento_professor": Essa Intent é acionada quando o usuário pergunta sobre o professor que irá ministrar a disciplina. As frases de entrada que disparam essa Intent incluem "Qual o professor?" e "Qual professor dará a matéria?". As respostas do chat-bot para essa Intent incluem o nome do professor e uma descrição de como ele irá conduzir a disciplina.


### Questionamento da Formação de Grupos

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/QuestionamentoGrupos.png" alt="Telnet"/>
</p>

"questionamento_grupos": Essa Intent é acionada quando o usuário pergunta sobre como serão formados os grupos para o trabalho de conclusão de curso. As frases de entrada que disparam essa Intent incluem "Será em grupo?" e "Quantas pessoas pode no grupo?". As respostas do chat-bot para essa Intent explicam que o trabalho será desenvolvido em grupos de até 4 integrantes.

### Questionamento de Entregas

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/QuestionamentoEntrega.png" alt="Telnet"/>
</p>

"questionamento_entregas": Essa Intent é acionada quando o usuário pergunta sobre a entrega do trabalho de conclusão de curso. As frases de entrada que disparam essa Intent incluem "Como será feita a entrega?" e "Quanto tempo para a entrega?". As respostas do chat-bot para essa Intent explicam como será feita a entrega, a data limite para a entrega e o que se espera como resultado final do TCC.

## Interação

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/interacoes.png" alt="Telnet"/>
</p>
Para a Interação do usuário com o chat-bot, foi feita a alteração no “main.py”. Resumidamente, no laço que aguarda a despedida do usuário, colocamos algumas condições que levariam a alguns questionamentos com possíveis interações do chat-bot de acordo com a resposta do usuário.

<p align="center">
  <img src="https://github.com/LacThales/ChatBot/blob/main/Imagens/chatbotresponse.png" alt="Telnet"/>
</p>

Na classe chatbot_response, localizada no “chatbot.py” podemos reparar que em alguns casos usamos um parâmetro adicional “cont”. Pois, partindo deste parâmetro, nós podemos saber o questionamento e qual a interação que será realizada pelo chat.

## Autores
[Vítor M. Oliveira](https://github.com/vihmar)  
[Thales Lacerda](https://github.com/LacThales)
