import pipeline
import retriever

from haystack.utils import print_answers
from haystack.agents import Tool
from haystack.agents import AgentStep, Agent
from haystack.agents.base import Agent, ToolsManager
from haystack.nodes import PromptNode
from haystack.agents.memory import ConversationSummaryMemory

prompt_agente = """
    Nesta conversa, o usuário humano interage com uma Inteligência Artificial, que será o agente. O usuário faz perguntas e o agente passa por diversos processamentos para retornar uma resposta bem informada ao usuário.
    O agente deve utilizar as ferramentas disponíveis para achar informações atualizadas e a resposta deve ser baseada somente na saída das ferramentas.
    O agente deve ignorar todo seu conhecimento prévio para responder a pergunta, utilizando somente as ferramentas passadas.
    O agente tem acesso a estas ferramentas:
    {tool_names_with_descriptions}

    A seguir, tem a conversa prévia entre humano e IA:
    {memory}

    A resposta do agente IA deve começar com algum destes:
    Pensamento: [O processo de raciocínio do agente]
    Ferramenta: [Nome das ferramentas] (em uma nova linha) Entrada da Ferramenta: [entrada como uma pergunta para a ferramenta selecionada SEM aspas e em uma nova linha] (Estes devem ser sempre fornecidos juntos e em linhas separadas.)
    Observação: [Resultado da ferramenta]
    Resposta Final: [Resposta final para a pergunta do humano]
    Ao selecionar uma ferramenta, o Agente deve fornecer o par "Ferramenta:" e "Entrada da ferramenta:" na mesma resposta, mas em linhas separadas.
    O Agente não deve solicitar informações, esclarecimentos ou contexto adicionais ao usuário humano.
    Se o Agente não conseguir encontrar uma resposta específica após esgotar as ferramentas e abordagens disponíveis, ele responderá com a Resposta Final: Inconclusivo, sinto muito.
    
    Pergunta: {query}
    Pensamento:
    {transcript}

"""

def init_search_tool(gen_pipeline):
    search_tool = Tool(
        name="busca_vest_unicamp_2024",
        pipeline_or_node=gen_pipeline,
        description="útil quando você precisa responder perguntas sobre o vestibular 2024 da unicamp",
        output_variable="respostas",
    )

    return search_tool

def resolucao(query, agent, agent_step):
    return {
        "query": query,
        "tool_names_with_descriptions": agent.tm.get_tool_names_with_descriptions(),
        "transcript": agent_step.transcript,
        "memory": agent.memory.load()
    }

def run_conversation(api_key, pdf): #essa função irá realizar a conversão e junção dos diferentes pedidos para gerar uma resposta do chat gpt
    document = pipeline.convert_pdf_to_text(pdf)
    doc_store = pipeline.init_document_store(document)
    gen_pipeline = retriever.init_generative_pipeline(doc_store, api_key)
    search_tool = init_search_tool(gen_pipeline)
    agent_prompt_node = PromptNode("gpt-3.5-turbo", api_key = api_key, max_length=128)
    memory_prompt_node = PromptNode(
    "philschmid/bart-large-cnn-samsum", max_length=128, model_kwargs={"task_name": "text2text-generation"}
    )   
    memory = ConversationSummaryMemory(memory_prompt_node, prompt_template="{chat_transcript}")

    conversational_agent = Agent(
        agent_prompt_node,
        prompt_template=prompt_agente,
        prompt_parameters_resolver=resolucao,
        memory=memory,
        tools_manager=ToolsManager([init_search_tool(gen_pipeline)]),
    )

    while True:
        pergunta = input("Faça uma pergunta sobre o vestibular unicamp 2024!")
        response = conversational_agent.run(pergunta)
        print(response)
