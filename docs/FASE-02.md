# Fase 2 — NLP, cloud, algoritmos genéticos, GenAI e LLMs

**Carga:** 72 horas  
**Período sugerido:** meses 3 e 4  
**Resultado:** classificador de documentos em português com busca semântica, chatbot básico e implantação em container.

## Competências

Ao final da fase, você deve conseguir:

- preparar texto em português para modelos clássicos e neurais;
- comparar TF-IDF, embeddings e transformers;
- implementar classificação, NER, similaridade e sentimento;
- explicar o funcionamento conceitual de transformers e LLMs;
- desenhar uma arquitetura de ML portátil entre nuvens;
- resolver um problema de otimização com algoritmo genético;
- avaliar riscos éticos e operacionais de conteúdo generativo.

## Unidade 1 — Processamento de Linguagem Natural

### Pipeline clássico

1. identificar idioma e encoding;
2. normalizar com cuidado;
3. tokenizar;
4. remover ou preservar stop words conforme a tarefa;
5. aplicar stemming/lematização quando fizer sentido;
6. gerar representação numérica;
7. treinar e validar;
8. analisar erros por classe e tipo de texto.

### Cuidados com português

- contrações e acentos carregam informação;
- negação pode inverter sentimento;
- stemming agressivo pode destruir significado;
- nomes de empresas e códigos precisam de tokenização adequada;
- textos corporativos contêm siglas, tabelas e campos sem gramática tradicional.

### Laboratório 1 — Classificador TF-IDF

Construa um classificador de solicitações ou documentos com:

- `TfidfVectorizer`;
- n-gramas de palavras e/ou caracteres;
- modelo linear;
- validação estratificada;
- matriz de confusão;
- análise dos 20 erros mais relevantes;
- endpoint de inferência.

Compare com um baseline baseado em palavras-chave.

## Unidade 2 — N-gramas, embeddings e similaridade

### Representações

- Bag of Words;
- TF-IDF;
- n-gramas;
- Word2Vec e GloVe;
- sentence embeddings;
- distância cosseno;
- embeddings densos versus esparsos;
- impacto de domínio, idioma e tamanho do contexto.

### Laboratório 2 — Busca semântica

Implemente busca sobre um conjunto de documentos:

1. crie embeddings;
2. armazene vetor e metadados;
3. busque top-k por cosseno;
4. compare com busca por palavra-chave;
5. crie 30 perguntas de avaliação;
6. calcule Recall@k e MRR;
7. documente consultas em que a busca semântica piora.

## Unidade 3 — Parsing, entidades e classificação

### Conteúdo

- part-of-speech tagging;
- parsing e dependências;
- named entity recognition;
- extração por regras versus modelo;
- classificação multi-classe e multi-label;
- sentimento e ironia;
- tópicos e categorização;
- avaliação por entidade, classe e documento.

### Laboratório 3 — Extração híbrida

Extraia número, fornecedor, data e valor de documentos usando:

- regex/regras para formatos estáveis;
- NER ou LLM para variações;
- validador determinístico;
- score por campo;
- revisão humana quando houver conflito.

A solução deve registrar qual técnica produziu cada campo.

## Unidade 4 — Transformers e LLMs

### Conceitos

- tokenização subword;
- embeddings posicionais;
- atenção e self-attention;
- pretraining e previsão de tokens;
- instruction tuning e alinhamento;
- janela de contexto;
- temperatura, top-p e determinismo relativo;
- hallucination, grounding e abstention;
- modelos encoder, decoder e encoder-decoder;
- modelos proprietários e open source.

### Exercício conceitual

Explique, sem usar termos vagos:

- por que um LLM pode escrever texto convincente e incorreto;
- por que contexto maior não garante melhor resposta;
- por que baixar temperatura não transforma o modelo em fonte factual;
- por que embeddings não são “memória humana”;
- quando um modelo menor é tecnicamente superior.

## Unidade 5 — Desenvolvimento de ML na cloud

### Arquitetura de referência

```text
Data source -> ingestion -> validation -> feature/embedding job
     -> training -> registry -> approval -> deployment
     -> monitoring -> feedback -> retraining
```

### Conceitos

- storage de objetos;
- jobs batch;
- notebooks e ambientes gerenciados;
- CPU/GPU e dimensionamento;
- endpoint online;
- autoscaling;
- filas e workers;
- model registry;
- versionamento de dados e artefatos;
- custo por treino, inferência e armazenamento;
- IAM, identidade gerenciada e secrets;
- vendor lock-in.

### Atividade de arquitetura

Desenhe a mesma solução em AWS, Azure e GCP. Para cada serviço gerenciado, crie uma interface de domínio equivalente. O código de negócio não deve conhecer nomes do provedor.

Exemplo:

```text
IDocumentExtractor
IEmbeddingProvider
IObjectStorage
IModelEndpoint
ISecretProvider
```

## Unidade 6 — Algoritmos genéticos

### Conceitos

- indivíduo e cromossomo;
- representação binária, inteira ou real;
- função fitness;
- população inicial;
- seleção;
- crossover;
- mutação;
- elitismo;
- critérios de parada;
- convergência prematura;
- diversidade da população.

### Laboratório 4 — Otimização de alocação

Escolha um problema:

- distribuição de tarefas entre equipes;
- roteirização simplificada;
- seleção de features;
- composição de agenda;
- ajuste de hiperparâmetros discreto.

Requisitos:

- função fitness explicada;
- restrições penalizadas ou reparadas;
- seed configurável;
- gráfico de evolução;
- comparação com busca aleatória;
- análise de tempo e qualidade.

## Unidade 7 — IA generativa

### Modalidades

- texto;
- código;
- imagem;
- áudio;
- vídeo;
- dados sintéticos.

### Avaliação responsável

Antes de publicar conteúdo gerado, avalie:

- procedência;
- licença e direitos de uso;
- presença de pessoa real;
- risco de falsificação;
- informação pessoal;
- discriminação;
- transparência para o usuário;
- necessidade de revisão humana;
- capacidade de remoção/correção.

### Laboratório 5 — Dataset sintético controlado

Gere exemplos sintéticos para uma classe rara, mas:

- separe dados sintéticos do conjunto real;
- deduplique;
- faça revisão amostral;
- não permita que exemplos sintéticos contaminem o teste;
- compare modelo com e sem augmentação;
- documente ganhos e regressões.

## Unidade 8 — Chatbots com LLM

### Camadas

- interface;
- política de conversa;
- gerenciamento de estado;
- provider de modelo;
- ferramentas;
- fontes de conhecimento;
- safety filters;
- telemetria;
- fallback e transferência humana.

### Laboratório 6 — Chatbot básico

Construa um chatbot que:

- responda somente dentro de um domínio;
- use prompt versionado;
- limite tamanho de entrada;
- registre latência e tokens sem armazenar segredo;
- recuse pedidos fora do escopo;
- retorne JSON quando solicitado pelo backend;
- possua provider mock para testes;
- não execute ações externas nesta fase.

## Checkpoint — Semantic Document Assistant v1

### Cenário

Usuários precisam classificar documentos, encontrar itens semanticamente semelhantes e tirar dúvidas simples sobre as informações extraídas.

### Requisitos

- classificador de texto;
- busca por palavra-chave e vetor;
- chatbot com escopo limitado;
- endpoint Python e integração ASP.NET Core;
- container;
- testes offline sem dependência de API paga;
- logs estruturados;
- relatório de custo estimado;
- diagrama para uma nuvem e alternativa portátil.

### Critérios de aceite

- classificação supera baseline definido;
- Recall@5 da busca é medido;
- chatbot possui pelo menos 30 casos de teste;
- nenhuma chave está no repositório;
- respostas fora de domínio são tratadas;
- falha do provider produz erro controlado;
- documentação permite execução local.

## Perguntas para banca

1. Por que você escolheu TF-IDF ou embedding?
2. Como provar que a busca melhorou?
3. Onde existe risco de vazamento de dados?
4. Qual componente gera maior custo?
5. Como trocar de nuvem?
6. Que respostas o chatbot deve se recusar a dar?
7. Qual é o plano caso o modelo mude de comportamento?