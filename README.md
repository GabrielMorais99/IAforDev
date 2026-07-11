# IA for Dev — formação prática de 360 horas

Formação independente, gratuita e hands-on para desenvolvedores que querem projetar, construir, avaliar e publicar soluções com Machine Learning, visão computacional, NLP, LLMs, RAG, agentes, cloud e segurança.

> **Aviso:** este repositório não é material oficial da FIAP, não possui vínculo com a instituição e não reproduz aulas, vídeos, avaliações ou conteúdos proprietários. A organização temática foi inspirada somente na grade pública do curso “IA para Devs”, e todo o conteúdo deste repositório é original.

## Objetivo

Ao concluir a trilha, você será capaz de:

- preparar dados e construir pipelines de Machine Learning;
- resolver problemas de classificação, regressão, agrupamento e anomalias;
- desenvolver soluções de visão computacional, OCR, áudio e NLP;
- integrar LLMs a aplicações Python e ASP.NET Core;
- implementar RAG, busca vetorial, tools, workflows e agentes;
- usar serviços de IA da AWS e do Azure sem acoplar a arquitetura ao provedor;
- avaliar qualidade, custo, latência, segurança e privacidade;
- publicar um projeto completo de IA com documentação, testes e CI.

## Formato

- **Carga horária:** 360 horas
- **Duração sugerida:** 10 meses
- **Ritmo:** 9 horas por semana
- **Estrutura:** 5 fases de 72 horas
- **Metodologia:** teoria essencial, laboratório, checkpoint e Tech Challenge
- **Stack principal:** Python, scikit-learn, PyTorch, Hugging Face, FastAPI, ASP.NET Core, SQL, Docker e GitHub Actions
- **Integrações:** OpenAI API, modelos locais/open source, Azure AI e AWS AI Services

## Trilha completa

| Fase | Meses | Tema | Entrega principal |
|---|---:|---|---|
| [01](docs/FASE-01.md) | 1–2 | Fundamentos, ML e visão computacional | API de classificação e OCR |
| [02](docs/FASE-02.md) | 3–4 | NLP, cloud, algoritmos genéticos e LLMs | Classificador de documentos e chatbot |
| [03](docs/FASE-03.md) | 5–6 | Prompting, OpenAI, RAG, LangChain e LangGraph | Assistente corporativo com fontes |
| [04](docs/FASE-04.md) | 7–8 | Vídeo, áudio, texto, AWS e APIs multimodais | Pipeline multimodal assíncrono |
| [05](docs/FASE-05.md) | 9–10 | LGPD, segurança, Azure e anomalias | Produto final observável e seguro |

Consulte o [plano detalhado de 360 horas](docs/PLANO-360H.md), o [Tech Challenge](docs/TECH-CHALLENGE.md) e o [sistema de avaliação](docs/AVALIACAO.md).

## Projeto integrador

Durante as cinco fases você construirá o **Enterprise AI Hub**, uma plataforma que recebe documentos, imagens, áudio e dados tabulares, extrai informações, classifica conteúdo, responde perguntas com fontes, detecta anomalias e registra auditoria.

Arquitetura-alvo:

```text
Web/Client
   |
ASP.NET Core API ── Auth, regras, auditoria, orchestration
   |
   +── Python ML Service ── treino, inferência, OCR, NLP
   +── LLM Gateway ─────── OpenAI / Azure OpenAI / modelo local
   +── Vector Store ────── pgvector / Qdrant / Azure AI Search
   +── Queue/Worker ────── processamento assíncrono
   +── Object Storage ──── documentos, áudio e imagens
   +── Observability ───── logs, traces, métricas e avaliações
```

Cada fase adiciona um incremento utilizável ao mesmo produto. Ao final, o repositório do aluno deve conter código, arquitetura, ADRs, testes, relatório de avaliação, threat model e demonstração.

## Como estudar

Para cada semana:

1. Leia a unidade e registre um resumo curto.
2. Execute o laboratório sem copiar a solução.
3. Altere o experimento e compare métricas.
4. Escreva testes e documente decisões.
5. Faça um commit pequeno e explicativo.
6. Atualize o diário de aprendizagem.

A regra central é: **não basta chamar uma API; você deve saber medir, proteger, depurar e evoluir a solução.**

## Pré-requisitos

- lógica de programação;
- Git e GitHub básicos;
- HTTP/REST e JSON;
- noções de SQL;
- Python básico ou disposição para aprender;
- experiência com alguma linguagem de backend. Os exemplos de integração usam C# e ASP.NET Core.

## Ambiente

### Python

```bash
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate

pip install -r src/python/requirements.txt
```

### .NET

```bash
dotnet --info
dotnet restore src/dotnet/AiForDevs.Api
dotnet run --project src/dotnet/AiForDevs.Api
```

### Variáveis de ambiente

Nunca grave segredos no Git. Use variáveis locais, Secret Manager ou um cofre de segredos.

```bash
OPENAI_API_KEY=...
OPENAI_MODEL=...
```

O curso não exige um fornecedor específico. Laboratórios devem oferecer, sempre que viável, uma alternativa local ou mockada.

## Estrutura do repositório

```text
.
├── docs/                    # conteúdo, plano e avaliações
├── src/
│   ├── python/              # laboratórios de ML e RAG
│   └── dotnet/              # API de integração
├── .github/workflows/       # validação contínua
├── .gitignore
└── README.md
```

## Critérios de conclusão

Para considerar a formação concluída, entregue:

- 80% dos laboratórios;
- 5 checkpoints de fase;
- 1 projeto integrador com evolução registrada;
- testes automatizados para fluxos críticos;
- avaliação de modelos e prompts com dataset versionado;
- análise de privacidade e ameaças;
- pipeline de CI funcionando;
- README técnico com instruções reproduzíveis;
- demonstração final de 10 a 15 minutos.

## Princípios técnicos

1. **Baseline antes de complexidade:** compare com regras simples e modelos clássicos.
2. **Dados antes do modelo:** qualidade, cobertura e vazamento de dados dominam o resultado.
3. **Avaliação reproduzível:** métricas devem ser calculadas em datasets versionados.
4. **LLM não é banco de dados:** respostas críticas precisam de fonte, validação e fallback.
5. **Segurança por padrão:** mínimo privilégio, segredo fora do código e entradas não confiáveis.
6. **Observabilidade de ponta a ponta:** custo, latência, erros, tokens e qualidade.
7. **Arquitetura substituível:** domínio desacoplado de modelos e provedores.
8. **Humano no circuito:** decisões de alto impacto exigem revisão e contestação.

## Referências oficiais

A trilha usa documentação primária e projetos oficiais como fonte de atualização:

- OpenAI Developers e SDK oficial .NET;
- scikit-learn, PyTorch e Hugging Face;
- LangChain e LangGraph;
- Microsoft Learn para Azure AI;
- documentação AWS para Textract, Comprehend e SageMaker;
- documentação brasileira sobre LGPD e segurança da informação.

Veja a lista organizada em [Referências](docs/REFERENCIAS.md).

## Licença

O conteúdo original deste repositório é disponibilizado sob a licença MIT. Marcas, nomes de produtos e links externos pertencem aos respectivos titulares.