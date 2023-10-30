from haystack.nodes import PromptNode, PromptTemplate, AnswerParser, BM25Retriever
from haystack.pipelines import Pipeline

def init_prompt():
    prompt_template = PromptTemplate(
        prompt="""Responda a questão de forma precisa baseado apenas no documento que lhe foi passado. Caso a informação não esteja no documento, diga que uma resposta não pode ser gerada apenas com as informações dadas.
        Documento:{join(documents)}
        Pergunta:{query}
        stop_words=["Observação:"],
        Resposta:
        """,
        output_parser=AnswerParser()
    )

    return prompt_template


def init_prompt_node(api_key_openai: str, model_name):
    prompt_node = PromptNode(
        model_name_or_path = model_name,
        api_key=api_key_openai,
        default_prompt_template=init_prompt()
    )

    return prompt_node

def init_retriever(document_store):
    retriever = BM25Retriever(
        document_store = document_store
    )

    return retriever



def init_generative_pipeline(document_store, open_ai_key):
    generative_pipeline = Pipeline()
    generative_pipeline.add_node(
        component = init_retriever(document_store),
        name = "retriever",
        inputs=["Query"]
    )
    generative_pipeline.add_node(
        component=init_prompt_node(open_ai_key, "text-davinci-003"),
        name = "prompt_node",
        inputs = ["retriever"]
    )

    return generative_pipeline