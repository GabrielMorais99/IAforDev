# Fase 3 — Prompt engineering, RAG, LangChain e agentes

**Carga:** 72 horas  
**Período:** meses 5 e 6  
**Entrega:** assistente corporativo com respostas fundamentadas e fontes.

## Competências

- criar e versionar prompts;
- usar saídas estruturadas e ferramentas;
- projetar pipelines RAG;
- medir recuperação e geração separadamente;
- implementar workflows com estado;
- construir agentes com limites, aprovação e auditoria;
- integrar Python e ASP.NET Core.

## Unidade 1 — Prompt engineering de produção

Estude instruções, contexto, exemplos, delimitadores, critérios de resposta, decomposição, few-shot, structured output e tratamento de ambiguidade.

### Laboratório

Crie um catálogo de prompts versionados com:

- objetivo;
- entradas e saídas;
- schema esperado;
- exemplos positivos e negativos;
- modelo testado;
- dataset de avaliação;
- métricas;
- histórico de alterações.

Nunca trate “pareceu bom” como avaliação suficiente.

## Unidade 2 — APIs de LLM e tool calling

Implemente chamadas com timeout, cancelamento, retry seguro, rate limit, idempotência quando aplicável, logging de tokens, custo e latência.

### Laboratório

Crie tools para:

- consultar pedido por ID;
- buscar produto;
- calcular prazo;
- abrir solicitação simulada.

Valide todos os argumentos no backend. O modelo não deve executar SQL, shell ou HTTP arbitrário.

## Unidade 3 — RAG

Pipeline:

```text
fonte -> extração -> limpeza -> chunking -> metadados
      -> embedding -> índice -> recuperação -> reranking
      -> contexto -> geração -> citação -> avaliação
```

Estude chunking, overlap, metadados, filtros, busca híbrida, top-k, reranking, contexto perdido e atualização de índice.

### Laboratório — Base documental

- ingira PDF, Markdown e texto;
- preserve origem, versão e página;
- implemente busca lexical e vetorial;
- gere resposta com citações;
- permita “não encontrei evidência suficiente”;
- teste documentos conflitantes e desatualizados.

## Unidade 4 — Avaliação de RAG

Meça:

- Recall@k e MRR da recuperação;
- precisão das citações;
- groundedness;
- completude;
- taxa de abstention correta;
- latência e custo;
- falhas por categoria.

Crie pelo menos 50 perguntas com resposta esperada, documento-fonte e dificuldade.

## Unidade 5 — LangChain e composição

Use abstrações somente quando reduzirem complexidade. Compare implementação direta com framework.

Pratique:

- loaders;
- splitters;
- retrievers;
- chains;
- tools;
- callbacks;
- memória explícita;
- tracing.

## Unidade 6 — LangGraph e workflows com estado

Modele fluxos como grafo:

```text
classificar -> recuperar -> responder -> validar
                    |             |
                    v             v
               pedir contexto   revisão humana
```

Inclua estado tipado, limites de iteração, checkpoints, retries e caminhos de erro.

## Unidade 7 — Agentes e multiagentes

Agentes são adequados quando o caminho precisa ser escolhido dinamicamente. Para processos previsíveis, prefira workflows determinísticos.

### Riscos

- loops;
- custo explosivo;
- tool misuse;
- prompt injection;
- ações irreversíveis;
- perda de contexto;
- delegação sem rastreabilidade.

### Laboratório

Construa um agente de suporte com três papéis lógicos: triagem, pesquisa e resposta. Mantenha ferramentas restritas e aprovação humana antes de qualquer escrita externa.

## Checkpoint — Enterprise Knowledge Assistant

### Requisitos

- ingestão incremental;
- busca híbrida;
- respostas com fonte e página;
- output estruturado;
- tool calling restrito;
- fluxo LangGraph ou equivalente;
- dataset de avaliação;
- proteção contra prompt injection;
- observabilidade;
- provider mock;
- integração ASP.NET Core.

## Critérios de aceite

- recuperação medida antes da geração;
- citações apontam para trechos existentes;
- ausência de fonte causa abstention;
- documentos não autorizados são filtrados;
- ações exigem validação do backend;
- testes cobrem injection, documento malicioso e falha de provider.