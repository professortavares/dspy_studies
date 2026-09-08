# dspy_studies

Estudos práticos do framework [DSPy](https://dspy.ai/) em notebooks Jupyter, organizados em ordem progressiva: básico → módulos → otimizadores.

## Instalação

Requisitos: Python 3.13+, [uv](https://docs.astral.sh/uv/), e opcionalmente [Ollama](https://ollama.com/) rodando local (alguns notebooks usam modelo local em vez de OpenAI).

```bash
# instalar dependências
uv sync

# criar .env na raiz com a chave da OpenAI (usada na maioria dos notebooks)
echo "OPENAI_API_KEY=sua-chave-aqui" > .env

# rodar jupyter lab
uv run jupyter lab

# ou rodar o script solto (usa Ollama local em localhost:11434)
uv run main.py
```

Notebooks que usam Ollama esperam um modelo `qwen3.5:4b` disponível via `ollama pull qwen3.5:4b` e o serviço rodando em `http://localhost:11434`.

## Notebooks

### 01 - Básico

Fundamentos de DSPy: configurar um LM, criar Signatures, inspecionar histórico de chamadas.

| Notebook | Conteúdo |
|---|---|
| `00 - Hello world - Ollama` | Primeira chamada a um LM local via Ollama; inspeção de resposta e histórico. |
| `01 - Hello world - OpenAI` | Mesma ideia usando OpenAI via `.env`. |
| `02 - Signature simples` | Signature definida como string (`entrada -> saida`); geração de poema a partir de pergunta. |
| `03 - Signature Classe` | Signature definida como classe Python (docstring + InputField/OutputField), mais estruturada. |
| `04 - Signature Multimodal` | Signature que recebe imagem como entrada. |

### 02 - Modules

Módulos de raciocínio e orquestração do DSPy.

| Notebook | Conteúdo |
|---|---|
| `01 - ChainOfThought` | Módulo que expõe raciocínio (`reasoning`) antes da resposta final. |
| `02 - BestOfN` | Executa o mesmo programa N vezes e seleciona a melhor resposta por `reward_fn`. |
| `03 - MultiChainComparison` | Gera várias soluções via ChainOfThought e compara/reconcilia numa chamada final. |
| `04 - Parallel` | Executa múltiplas chamadas DSPy independentes em paralelo (sem consolidar respostas). |
| `05 - ReAct` | Agente Reasoning+Acting com ferramentas externas (`yfinance`, API de piadas Chuck Norris). |
| `06 - ReActV2` | Nova implementação experimental do ReAct, com representação interna de trajetória diferente. |
| `07 - Avaliador Composto` | Pipeline: gera redação nos moldes ENEM e avalia por múltiplos critérios (relevância, gramática, estrutura, profundidade). |
| `08 - RLM` | Recursive Language Model: modelo explora programaticamente um texto grande (Dom Casmurro) sem RAG tradicional (sem chunks/embeddings/vetor). |

### 03 - Otimizadores

Todos usam o mesmo problema de classificação binária (dataset Kaggle "Disaster Tweets": tweet descreve desastre real ou não), comparando baseline zero-shot vs. programa otimizado por F1-score.

| Notebook | Otimizador | Estratégia |
|---|---|---|
| `01 - LabeledFewShot` | `LabeledFewShot` | Usa exemplos rotulados fixos como demonstrações few-shot. |
| `02 - BootstrapFewShot` | `BootstrapFewShot` | Gera demonstrações few-shot automaticamente a partir do próprio programa. |
| `03 - BootstrapFewShotWithRandomSearch` | `BootstrapFewShotWithRandomSearch` | Como acima, mas busca aleatória entre múltiplos conjuntos de demonstrações. |
| `04 - KNNFewShot` | `KNNFewShot` | Recupera dinamicamente exemplos semanticamente similares por entrada (KNN), em vez de um conjunto fixo. |
| `05 - COPRO` | `COPRO` | Otimiza a instrução textual da Signature via ascensão de coordenadas (não mexe em demonstrações). |
| `06 - GEPA` | `GEPA` (Genetic-Pareto) | Evolui a instrução reflexivamente a partir de traces de execução, feedback textual e fronteira de Pareto. |
| `07 - MIPROv2` | `MIPROv2` | Otimiza conjuntamente instrução e demonstrações few-shot via otimização Bayesiana. |
| `08 - SIMBA` | `SIMBA` (Stochastic Introspective Mini-Batch Ascent) | Amostra mini-batches, compara trajetórias, gera candidatos por demonstração ou regra de melhoria. |
| `09 - InferRules` | `InferRules` | Combina `BootstrapFewShot` com indução de regras explícitas em linguagem natural. |

Artefatos gerados por execuções passadas (`*.json`, `KNNFewShot_program/`) ficam ao lado de cada notebook — não editar manualmente, são outputs versionados.
