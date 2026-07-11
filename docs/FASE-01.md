# Fase 1 — Fundamentos, Machine Learning e visão computacional

**Carga:** 72 horas  
**Período sugerido:** meses 1 e 2  
**Resultado:** uma solução que recebe imagem/documento, extrai dados e classifica o conteúdo com métricas conhecidas.

## Competências

Ao final da fase, você deve conseguir:

- formular um problema de negócio como problema de ML;
- preparar dados sem provocar vazamento entre treino e teste;
- construir e comparar baselines;
- usar pipelines reproduzíveis do scikit-learn;
- escolher métricas coerentes com o custo do erro;
- expor inferência por API;
- aplicar OCR e modelos pré-treinados de visão;
- documentar limitações em um model card.

## Unidade 1 — Fundamentos de IA

### Conceitos essenciais

- IA baseada em regras, busca, otimização e aprendizado estatístico;
- tarefa, observação, atributo, alvo e hipótese;
- treino, validação, teste e produção;
- underfitting, overfitting, viés e variância;
- correlação, causalidade e variáveis proxy;
- classificação, regressão, clustering, ranking e detecção;
- aprendizado online, batch e por transferência;
- ciclo: problema → dados → baseline → experimento → avaliação → implantação → monitoramento.

### Exercício de decisão

Para cada cenário abaixo, diga se deve usar regras, ML clássico, LLM ou nenhuma IA:

1. validar CPF;
2. prever atraso de entrega;
3. resumir contrato;
4. aplicar desconto fiscal obrigatório;
5. identificar produto em fotografia;
6. bloquear pagamento de alto risco.

Justifique considerando custo, explicabilidade, volume, estabilidade e risco.

## Unidade 2 — Python para ML

### Conteúdo

- projeto com `src/`, testes e configuração;
- ambientes virtuais e dependências;
- tipos, dataclasses e funções puras;
- NumPy para vetores e matrizes;
- pandas para carga, limpeza, joins e agregações;
- gráficos para distribuição e relação entre variáveis;
- serialização segura de artefatos;
- notebooks para exploração e scripts para produção.

### Laboratório 1 — Qualidade de dados

Crie um pipeline que:

1. carregue um CSV;
2. valide colunas obrigatórias;
3. remova duplicatas conforme chave de negócio;
4. trate nulos com estratégia documentada;
5. detecte valores impossíveis;
6. gere relatório em JSON;
7. falhe com mensagem clara quando o contrato mudar.

### Critérios

- nenhuma transformação manual fora do código;
- resultado reproduzível;
- pelo menos cinco testes;
- log sem dados pessoais desnecessários.

## Unidade 3 — Regressão, classificação e pipelines

### Modelos

- DummyClassifier/DummyRegressor;
- regressão linear e logística;
- K-Nearest Neighbors;
- Support Vector Machine;
- Decision Tree;
- Random Forest e gradient boosting.

### Pré-processamento

- StandardScaler e normalização;
- OneHotEncoder;
- imputação;
- ColumnTransformer;
- Pipeline;
- transformação ajustada somente no conjunto de treino.

### Laboratório 2 — Classificação reproduzível

Implemente o script `src/python/ml_pipeline.py` e evolua-o para:

- aceitar caminho de dataset por argumento;
- separar features e target;
- usar validação cruzada estratificada;
- comparar dummy, logística e árvore;
- salvar métricas em JSON;
- exportar apenas o melhor pipeline;
- rejeitar inferência com schema incompatível.

### Perguntas de revisão

- Por que accuracy pode esconder um modelo inútil?
- Quando precision importa mais que recall?
- O que muda ao ajustar o threshold?
- Feature importance prova causalidade?
- Por que não se deve normalizar antes do split?

## Unidade 4 — Métricas e validação

### Classificação

- matriz de confusão;
- precision, recall, specificity e F1;
- macro, micro e weighted average;
- ROC-AUC e PR-AUC;
- calibração e threshold;
- custo esperado por tipo de erro.

### Regressão

- MAE, MSE e RMSE;
- MAPE e seus problemas próximos de zero;
- R²;
- análise de resíduos.

### Clustering

- inertia;
- silhouette score;
- estabilidade;
- avaliação qualitativa e utilidade de negócio.

### Atividade

Crie uma função de custo:

```text
custo = FN * custo_falso_negativo + FP * custo_falso_positivo
```

Escolha o threshold que minimiza o custo em validação. Não ajuste usando o conjunto final de teste.

## Unidade 5 — Agrupamento e redução de dimensionalidade

### Conteúdo

- distância euclidiana e cosseno;
- K-Means e inicialização;
- DBSCAN e ruído;
- PCA e variância explicada;
- t-SNE/UMAP apenas para exploração visual;
- risco de transformar clusters em “verdades” sobre pessoas.

### Laboratório 3 — Segmentação

- padronize features;
- compare K-Means e DBSCAN;
- avalie estabilidade com amostras diferentes;
- descreva cada grupo sem usar rótulos estigmatizantes;
- explique por que o agrupamento pode não ser acionável.

## Unidade 6 — Visão computacional

### Fundamentos

- pixels, canais, resolução e compressão;
- convolução, pooling e CNN;
- classificação, detecção, segmentação e tracking;
- transfer learning;
- data augmentation;
- confiança, IoU, precision/recall e mAP;
- YOLO e outros detectores pré-treinados;
- GANs: ideia, usos e riscos;
- OCR por etapas: detecção, reconhecimento, pós-processamento e validação.

### Laboratório 4 — OCR auditável

Construa uma API que:

- receba PNG, JPG ou PDF;
- valide tipo e tamanho;
- gere hash do arquivo;
- extraia texto;
- devolva score de confiança quando disponível;
- marque campos abaixo do limiar para revisão;
- nunca sobrescreva o arquivo original;
- registre tempo e versão do extrator.

### Laboratório 5 — Detecção de objetos

Use um modelo pré-treinado para detectar objetos em imagens próprias ou dataset autorizado. Compare:

- confiança mínima;
- resolução de entrada;
- tempo de execução CPU/GPU;
- falsos positivos;
- classes ausentes no modelo.

## Checkpoint — Document Intake API

### História

Uma empresa recebe notas, ordens, formulários e fotos. O sistema precisa identificar o tipo do documento, extrair texto e devolver um JSON padronizado para integração.

### Requisitos mínimos

- endpoint de upload;
- validação de arquivo;
- OCR;
- classificador com baseline;
- resposta estruturada;
- score e status de revisão;
- correlação por request ID;
- testes unitários e de integração;
- container;
- model card;
- relatório de métricas.

### Resposta esperada

```json
{
  "documentId": "uuid",
  "documentType": "invoice",
  "classificationConfidence": 0.91,
  "needsReview": false,
  "fields": {
    "number": "12345",
    "supplier": "Fornecedor Exemplo"
  },
  "warnings": [],
  "modelVersion": "document-type-v1"
}
```

## Model card obrigatório

Documente:

- objetivo e proprietário;
- população/dados cobertos;
- origem e licença do dataset;
- preprocessing;
- métricas globais e por subgrupo relevante;
- threshold;
- limitações;
- usos proibidos;
- plano de monitoramento;
- versão e data.

## Definição de pronto

A fase está concluída quando outra pessoa consegue clonar o projeto, preparar o ambiente, treinar, executar os testes e chamar a API usando apenas o README.