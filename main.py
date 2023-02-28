from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo e treinar
myChatBot.createModel()

print("Bem vindo ao Chatbot\n\n")      
sinonimos_sim = ["sim", "claro", "óbvio", "yes"]

pergunta = input("como posso te ajudar?\n\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")

while (intencao[0]['intent']!="despedida"):
    if (resposta.__contains__("Iae, bem sim e vc?")):
        input("")
    if (resposta.__contains__("TCC?") and intencao[0]['intent'] == "questionamento_professor"):
        pergunta = input("")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")
    if(resposta.__contains__("TCC") and intencao[0]['intent'] == "questionamento_entregas"):
        resposta = input("")
        if resposta in sinonimos_sim:
            resposta, intencao = myChatBot.chatbot_response(resposta, 1)
            print(resposta + "   [" + intencao[0]['intent'] + "]")
    pergunta = input("Posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
