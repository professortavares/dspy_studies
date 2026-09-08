# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é

Repo de estudos do framework DSPy (Python). Não é biblioteca/app — coleção de Jupyter notebooks numerados, progressivos, cobrindo básico -> Modules -> Otimizadores. `main.py` é só um script de teste solto (Predict simples via Ollama), não entrypoint da aplicação.

## Setup e execução

- Gerenciado com `uv` (tem `uv.lock`, `.venv`). Python >=3.13.
- Instalar deps: `uv sync`
- Rodar script solto: `uv run main.py`
- Notebooks: `uv run jupyter lab` (jupyterlab está em dependency-group `dev`)
- Sem testes, sem lint configurado, sem CI.

## Modelos / LMs

Notebooks alternam entre dois providers DSPy:
- **Ollama local**: `dspy.LM("ollama_chat/<modelo>", api_base="http://localhost:11434", api_key="")` — requer Ollama rodando localmente.
- **OpenAI**: `dspy.LM("openai/<modelo>", api_key=os.getenv("OPENAI_API_KEY"))` — chave em `.env` (via `python-dotenv`, `load_dotenv()`), variável `OPENAI_API_KEY`.

Padrão em notebooks de otimizadores: dois LMs separados — um para o programa/classificador (`lm`), outro para o otimizador gerar instruções/candidatos (`prompt_lm`), configurados via `dspy.configure(lm=lm)`.

## Estrutura dos notebooks

- `notebooks/01 - Básico/` — Signatures (simples, classe, multimodal), hello world Ollama/OpenAI.
- `notebooks/02 - Modules/` — ChainOfThought, BestOfN, MultiChainComparison, Parallel, ReAct/ReActV2, avaliador composto, RLM.
- `notebooks/03 - Otimizadores/` — LabeledFewShot, BootstrapFewShot(+RandomSearch), KNNFewShot, COPRO, GEPA, MIPROv2, SIMBA, InferRules.

Cada subpasta de otimizadores gera artefatos ao lado do notebook (`*.json` com programas otimizados, `KNNFewShot_program/`) — são outputs versionados de execuções passadas, não editar manualmente.

Notebooks usam datasets locais quando aplicável (ex.: `disaster_tweets.csv`, `dom_casmurro.txt`) — caminhos relativos à própria subpasta.

## Convenções

- Comentários e texto explicativo nos notebooks em português.
- Cada notebook é auto-contido (própria célula de imports, load_dotenv, configuração de LM) — não há módulo compartilhado entre notebooks.
