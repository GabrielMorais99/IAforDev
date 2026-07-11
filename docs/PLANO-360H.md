# Plano completo — 360 horas em 10 meses

Este plano organiza a formação em **40 semanas de 9 horas**, totalizando 360 horas. Cada fase possui 8 semanas e 72 horas.

## Distribuição semanal sugerida

- 2h — fundamentos e leitura técnica;
- 3h — laboratório guiado;
- 2h — exercício sem solução pronta;
- 1h — testes, documentação e refatoração;
- 1h — evolução do Tech Challenge.

## Fase 1 — Fundamentos, Machine Learning e visão computacional

### Semana 1 — Como sistemas de IA aprendem

**Conteúdo:** IA simbólica e estatística, aprendizado supervisionado/não supervisionado, features, labels, treino, validação, teste, inferência, generalização e overfitting.

**Laboratório:** construir um classificador por regras e compará-lo com um modelo treinado.

**Entrega:** glossário próprio e ADR explicando quando não usar IA.

### Semana 2 — Python para ciência de dados

**Conteúdo:** ambientes virtuais, módulos, typing, NumPy, pandas, notebooks versus scripts, leitura de CSV/JSON, tratamento de nulos e testes.

**Laboratório:** pipeline reproduzível de limpeza e análise exploratória.

**Entrega:** pacote Python instalável localmente com testes.

### Semana 3 — Regressão e classificação

**Conteúdo:** regressão linear/logística, KNN, SVM, separação treino/teste, normalização, variáveis categóricas e baseline.

**Laboratório:** previsão de valor e classificação binária.

**Entrega:** relatório comparando pelo menos três modelos.

### Semana 4 — Árvores, ensembles e pipelines

**Conteúdo:** decision tree, random forest, gradient boosting, feature importance, ColumnTransformer e Pipeline do scikit-learn.

**Laboratório:** pipeline completo sem vazamento entre treino e teste.

**Entrega:** endpoint de inferência com contrato versionado.

### Semana 5 — Métricas e validação

**Conteúdo:** matriz de confusão, precision, recall, F1, ROC-AUC, PR-AUC, MAE, RMSE, validação cruzada, desbalanceamento e threshold.

**Laboratório:** otimizar limiar com base em custo de negócio.

**Entrega:** model card inicial.

### Semana 6 — Agrupamento e redução de dimensionalidade

**Conteúdo:** K-Means, DBSCAN, PCA, escalonamento, distância, escolha de número de clusters e limitações interpretativas.

**Laboratório:** segmentação exploratória de registros.

**Entrega:** análise de estabilidade dos clusters.

### Semana 7 — Visão computacional e OCR

**Conteúdo:** imagem como tensor, filtros, detecção, segmentação, OCR, CNNs, transfer learning, YOLO, riscos de reconhecimento facial e GANs.

**Laboratório:** extrair texto de imagens e detectar objetos em um conjunto pequeno.

**Entrega:** API de OCR com score de confiança e fallback manual.

### Semana 8 — Checkpoint da fase 1

**Desafio:** receber um documento ou imagem, extrair conteúdo, classificar o tipo e devolver resultado estruturado.

**Evidências:** dataset, notebook exploratório, pipeline de treino, API, testes, métricas e README.

## Fase 2 — NLP, cloud, algoritmos genéticos, GenAI e LLMs

### Semana 9 — Fundamentos de NLP

Tokenização, normalização, stop words, stemming, lematização, n-gramas e problemas específicos do português.

### Semana 10 — Representação de texto

Bag of Words, TF-IDF, similaridade, embeddings clássicos, Word2Vec, GloVe e comparação com embeddings modernos.

### Semana 11 — Informação linguística

Part-of-speech, parsing, dependências, NER, classificação de sentimento, tópicos e avaliação de NLP.

### Semana 12 — Transformers e LLMs

Attention, tokenização subword, pretraining, instruction tuning, contexto, temperatura, amostragem, alucinação e limites.

### Semana 13 — Cloud para ML

Treino versus inferência, CPU/GPU, batch versus online, containers, autoscaling, storage, filas, registry, custo e arquitetura portátil entre AWS, Azure e GCP.

### Semana 14 — Algoritmos genéticos

Representação de indivíduos, fitness, seleção, crossover, mutação, elitismo, convergência, exploração versus explotação e casos adequados.

### Semana 15 — GenAI aplicada

Geração de texto, imagem, áudio e vídeo; controle de entrada/saída; procedência; direitos autorais; riscos de deepfake; revisão humana.

### Semana 16 — Checkpoint da fase 2

**Desafio:** classificador de documentos em português com busca semântica e chatbot básico, publicável em container.

## Fase 3 — OpenAI, prompting, RAG, LangChain e LangGraph

### Semana 17 — APIs de modelos

Autenticação, modelos, mensagens, Responses API, streaming, structured output, function calling, retries, rate limits, idempotência e custos.

### Semana 18 — Engenharia de prompts

Instruções, contexto, exemplos, delimitadores, formatos, decomposição, autoavaliação, testes adversariais e versionamento.

> O curso trabalha com raciocínio verificável e decomposição de tarefas, mas não depende de solicitar ou armazenar raciocínio privado do modelo.

### Semana 19 — Evals para prompts e LLMs

Golden dataset, critérios, graders determinísticos e por modelo, regressão de prompt, factualidade, groundedness, relevância, segurança e custo.

### Semana 20 — Embeddings e recuperação

Chunking, overlap, metadados, busca vetorial, híbrida, filtros, reranking, recall da recuperação e atualização de índice.

### Semana 21 — RAG de ponta a ponta

Ingestão, parsing, deduplicação, indexação, consulta, geração com citações, abstention, cache, avaliação e observabilidade.

### Semana 22 — Fine-tuning e alternativas

Quando usar prompting, RAG, tool calling ou fine-tuning; preparação de dataset; splits; qualidade; privacidade; avaliação pré/pós; rollback.

### Semana 23 — LangChain e LangGraph

Loaders, splitters, retrievers, tools, chains, estado, nós, arestas, persistência, interrupção humana, retry e multiagentes.

### Semana 24 — Checkpoint da fase 3

**Desafio:** assistente corporativo com RAG, referências, tools autorizadas, avaliação automatizada e API ASP.NET Core.

## Fase 4 — Multimodalidade, AWS e APIs de produção

### Semana 25 — Vídeo e visão temporal

Frames, tracking, detecção de atividade, eventos, custo computacional, privacidade e amostragem.

### Semana 26 — Áudio e fala

Speech-to-text, diarização, timestamps, ruído, idiomas, PII, resumos e análise de chamadas.

### Semana 27 — Classificação e sumarização de texto

Taxonomias, multi-label, tópicos, resumos extrativos/abstrativos, factualidade e avaliação humana.

### Semana 28 — AWS Textract e Comprehend

OCR gerenciado, formulários/tabelas, jobs assíncronos, entidades, frases-chave, sentimento e integração orientada a eventos.

### Semana 29 — APIs multimodais

Entradas de imagem, áudio e arquivo; outputs estruturados; validação; limites de tamanho; armazenamento; redaction.

### Semana 30 — Processamento assíncrono

Filas, workers, retry com backoff, dead-letter queue, idempotência, status de job, webhooks e compensação.

### Semana 31 — Resiliência e custo

Timeout, circuit breaker, rate limiting, cache, fallback, batching, quotas, budgets e medição por tenant.

### Semana 32 — Checkpoint da fase 4

**Desafio:** pipeline multimodal que recebe arquivo, processa em background, extrai sinais e publica resultado auditável.

## Fase 5 — Privacidade, segurança, Azure e detecção de anomalias

### Semana 33 — LGPD aplicada a sistemas de IA

Finalidade, necessidade, transparência, bases legais, dados pessoais/sensíveis, retenção, direitos do titular, operadores e registro de tratamento.

### Semana 34 — Segurança para LLMs

Prompt injection, indirect injection, data exfiltration, insecure output handling, excessive agency, poisoning, supply chain e denial of wallet.

### Semana 35 — Controles de arquitetura

Allowlist de tools, sandbox, autorização por recurso, isolamento de tenant, redaction, secrets, logs seguros, moderação e human approval.

### Semana 36 — Azure Document Intelligence e Vision

Extração de documentos, modelos pré-construídos/customizados, OCR, layout, confiança, integração e tratamento de falhas.

### Semana 37 — Azure AI Search e RAG empresarial

Índices, busca textual/vetorial/híbrida, filtros, segurança por documento, chunking, semantic ranking e atualização incremental.

### Semana 38 — Detecção de anomalias

Z-score robusto, IQR, Isolation Forest, One-Class SVM, Local Outlier Factor, séries temporais, thresholds e investigação.

### Semana 39 — Operação de IA

Model registry, feature/data drift, prompt drift, tracing, SLIs/SLOs, incidentes, feedback, rollback e governança.

### Semana 40 — Entrega final e hackathon

Demonstração do produto completo, ataque controlado, correção, avaliação final, arquitetura, custos, roadmap e retrospectiva.

## Carga por tipo de atividade

| Atividade | Horas |
|---|---:|
| Conteúdo e leitura | 80 |
| Laboratórios guiados | 110 |
| Exercícios independentes | 60 |
| Tech Challenge | 70 |
| Testes, documentação e revisão | 25 |
| Avaliações e apresentação | 15 |
| **Total** | **360** |

## Evidências de aprendizagem

Ao final de cada semana, registre:

- hipótese ou problema estudado;
- dataset e licença;
- experimento e parâmetros;
- resultado e métrica;
- erro encontrado;
- decisão arquitetural;
- próximo passo.

O objetivo do plano não é apenas “terminar vídeos”, mas produzir evidências reproduzíveis de competência.