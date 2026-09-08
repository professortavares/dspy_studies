# 03 - Otimizadores

Otimizadores de programas DSPy (prompt/demonstrações/instruções), todos aplicados ao mesmo problema: classificação binária de tweets — dataset Kaggle **Natural Language Processing with Disaster Tweets** (`disaster_tweets.csv`).

* `0`: tweet **não** descreve desastre real.
* `1`: tweet descreve desastre real.

Padrão comum a quase todos: avaliar baseline (zero-shot ou instrução original) → aplicar otimizador → reavaliar → comparar por **F1-score** (também Accuracy, Precision, Recall, confusion matrix). `load_dotenv()` + LM via OpenAI, split treino/validação/teste com `sklearn`.

## Notebooks

### 01 - LabeledFewShot

`LabeledFewShot`: usa exemplos rotulados fixos do treino como demonstrações few-shot. Mais simples dos otimizadores — não gera nem busca nada, só injeta exemplos escolhidos.

### 02 - BootstrapFewShot

`BootstrapFewShot`: gera demonstrações few-shot automaticamente, executando o próprio programa no treino e guardando execuções bem-sucedidas como exemplos.

### 03 - BootstrapFewShotWithRandomSearch

Igual ao anterior, mas com busca aleatória entre múltiplos conjuntos de demonstrações candidatas, mantendo o de melhor desempenho.

### 04 - KNNFewShot

`KNNFewShot`: em vez de um conjunto fixo de demonstrações, recupera dinamicamente (via KNN sobre embeddings) exemplos semanticamente parecidos com cada tweet a classificar. Gera artefato `KNNFewShot_program/` ao lado do notebook.

### 05 - COPRO

`COPRO` (Coordinate Ascent Prompt Optimization): não mexe em demonstrações, otimiza a **instrução textual** da Signature. Gera variações de instrução, avalia cada uma pela métrica, usa resultados pra propor novas candidatas, mantém a melhor.

### 06 - GEPA

`GEPA` (Genetic-Pareto): otimizador evolutivo e reflexivo. Usa um LM separado (`prompt_lm`) pra analisar traces de execução, erros e feedback textual, evoluindo a instrução via seleção por fronteira de Pareto. Dados separados em treino (atualizações reflexivas) / validação (seleção do candidato) / teste (avaliação final).

### 07 - MIPROv2

`MIPROv2` (Multiprompt Instruction PRoposal Optimizer v2): otimiza **conjuntamente** instrução e demonstrações few-shot. Três etapas — gera candidatos de demonstrações, propõe instruções considerando tarefa/dados/demonstrações, usa **otimização Bayesiana** pra achar melhor combinação. Também usa `prompt_lm` separado (com `temperature=1.0`, compatível com GPT-5) além do LM do classificador.

### 08 - SIMBA

`SIMBA` (Stochastic Introspective Mini-Batch Ascent): amostra mini-batches do treino, executa trajetórias diferentes pros mesmos exemplos, identifica onde há maior diferença de desempenho entre trajetórias, e gera candidatos por duas estratégias — adicionar demonstração bem-sucedida ou gerar regra de melhoria por reflexão comparando trajetória boa vs. ruim. Retorna melhor programa e também `candidate_programs`. Como `SIMBA.compile()` não recebe `valset`, validação por F1 é feita **externamente**, após a compilação (métrica interna do SIMBA é por exemplo, F1 é global).

### 09 - InferRules

`InferRules`: baseado em `BootstrapFewShot`, combina demonstrações few-shot com indução de **regras explícitas em linguagem natural**. Fluxo:

```
trainset → BootstrapFewShot → demonstrações few-shot → indução de regras
→ múltiplos programas candidatos → avaliação no valset → melhor programa → testset
```

## Artefatos

Cada notebook (exceto os que não persistem programa) gera `*.json` (ou pasta, no caso do KNN) com o programa otimizado ao lado do notebook — são outputs de execuções passadas, não editar manualmente.
