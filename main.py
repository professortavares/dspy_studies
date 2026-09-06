import dspy


lm = dspy.LM(
    "ollama_chat/qwen3.5:4b",
    api_base="http://localhost:11434",
    api_key="",
)

dspy.configure(lm=lm)


class PerguntaResposta(dspy.Signature):
    """Responda à pergunta de maneira clara e didática."""

    pergunta: str = dspy.InputField()
    resposta: str = dspy.OutputField()


responder = dspy.Predict(PerguntaResposta)


resultado = responder(
    pergunta="O que é uma árvore binária?"
)

print(resultado.resposta)
