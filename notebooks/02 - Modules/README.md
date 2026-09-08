# 02 - Modules

Módulos de raciocínio e orquestração do DSPy: chain-of-thought, votação/seleção entre tentativas, execução paralela, agentes com ferramentas e contexto longo.

## Notebooks

### 01 - ChainOfThought

`dspy.ChainOfThought` em vez de `dspy.Predict`. DSPy injeta campo `reasoning` (pensamento passo-a-passo) além da saída final. Útil pra tarefas multi-etapa, matemática, decisões que exigem justificativa.

### 02 - BestOfN

`dspy.BestOfN` executa um programa base N vezes (N=3 no exemplo) e seleciona a resposta de maior score, segundo `reward_fn` (0-1) e `threshold` mínimo de aceitação. Notebook mostra as N tentativas, notas e justificativas de seleção.

### 03 - MultiChainComparison

Duas etapas: `ChainOfThought` gera várias soluções independentes pro mesmo problema; `MultiChainComparison` faz nova chamada ao LLM comparando raciocínios, identificando inconsistências, corrigindo erros e produzindo resposta final consolidada.

### 04 - Parallel

`dspy.Parallel` executa múltiplas chamadas DSPy independentes simultaneamente, reduzindo tempo total. Diferente do MultiChainComparison: não compara nem consolida respostas, só paraleliza execução.

### 05 - ReAct

Agente Reasoning+Acting (`dspy.ReAct`) com acesso a ferramentas externas: `consultar_acao` (dados financeiros via `yfinance`) e `obter_piada_chuck_norris` (API `chucknorris.io`). O agente decide sozinho qual ferramenta usar e quando, com base na pergunta — ciclo de pensar → escolher ferramenta → executar → observar → repetir ou responder.

### 06 - ReActV2

Implementação experimental mais nova do ReAct. Mesmo princípio (reasoning + acting), mas muda como a trajetória é representada internamente: `ReAct` tradicional guarda passos em `resultado.trajectory` com campos tipo `thought_0`; `ReActV2` altera essa estrutura interna.

### 07 - Avaliador Composto

Pipeline de geração e avaliação de redações estilo ENEM:

```
TEMA → GerarRedacaoENEM → REDAÇÃO → [Relevância, Gramática, Estrutura, Profundidade] → nota composta
```

Um módulo gera a redação, quatro avaliadores independentes julgam critérios diferentes em paralelo, resultado é composto. Não define `temperature` no LM (evita parâmetro desnecessário).

### 08 - RLM

`dspy.RLM` (Recursive Language Model): usa texto integral de *Dom Casmurro* como contexto pra responder perguntas que exigem análise de partes distintas da obra. Diferente de RAG tradicional (sem chunks, embeddings ou banco vetorial pré-construídos) — o modelo explora o contexto programaticamente, escrevendo e executando código pra buscar palavras/expressões, localizar posições, extrair trechos, usar regex, dividir o texto etc.

## Padrão comum

Notebooks (exceto ReAct/RLM que puxam dados externos) seguem: `load_dotenv()` → configurar LM via OpenAI → definir Signature → instanciar módulo → executar → inspecionar campos extras do resultado (`reasoning`, `trajectory`, scores) e `lm.history`.
