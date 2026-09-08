# 01 - Básico

Fundamentos de DSPy: configurar um LM (local ou remoto), definir Signatures e inspecionar histórico de chamadas.

## Notebooks

### 00 - Hello world - Ollama

Configura `dspy.LM` apontando pra Ollama local (`ollama_chat/qwen3.5:4b`, `http://localhost:11434`, sem API key). Faz chamada direta ao modelo (sem Signature), explora campos da resposta (`text`, `reasoning_content`) e inspeciona `lm.history` pra debug (prompt, resposta, latência, tokens).

Requer Ollama rodando local com modelo `qwen3.5:4b` (`ollama pull qwen3.5:4b`).

### 01 - Hello world - OpenAI

Mesma ideia do notebook anterior, mas com OpenAI. Carrega `OPENAI_API_KEY` via `.env`/`load_dotenv()`. Chamada direta ao LM, inspeção de resposta e histórico (incluindo custos, exclusivo da OpenAI).

### 02 - Signature simples

Introduz Signature em formato string: `entrada -> saida` (ex.: `pergunta -> poema`). Executa predição e extrai campo de saída do `Prediction`. Mostra prompt gerado internamente e histórico de chamada.

### 03 - Signature Classe

Mesma tarefa, mas Signature definida como classe Python (docstring como instrução geral, `InputField`/`OutputField` com descrições opcionais). Mais estruturado que string, indicado pra tarefas complexas.

### 04 - Signature Multimodal

Signature que recebe imagem como entrada (arquivo local `pexels-kristin-morgan-1853468-29636799.jpg`), mostrando suporte multimodal do DSPy.

## Padrão comum

Todo notebook (exceto o de Ollama) começa com `load_dotenv()` lendo `.env` na raiz do projeto pra pegar `OPENAI_API_KEY`. Notebooks terminam inspecionando `lm.history` — útil pra entender prompt gerado, custo, latência e tokens de cada chamada.
