import retriever
import pipeline
import conversation

path = r'C:\Projeto NeuralMind\Procuradoria Geral - Normas - Vestibular 2024.pdf'
open_ai_key = "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"
conversation.run_conversation(open_ai_key, path)