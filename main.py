import libs/retriever
import libs/pipeline
import libs/conversation

path = r'insira o path'
open_ai_key = "insira a chave da api aqui"

if __name__ == "__main__":
    conversation.run_conversation(open_ai_key, path)