# Fase 4 — Multimodalidade, áudio, vídeo, AWS e APIs

**Carga:** 72 horas  
**Período:** meses 7 e 8  
**Entrega:** pipeline assíncrono que processa documentos, imagens, áudio e vídeo.

## Competências

- projetar ingestão multimodal;
- transcrever, segmentar e resumir áudio/vídeo;
- usar OCR e análise de documentos;
- criar APIs resilientes e jobs assíncronos;
- integrar serviços de IA da AWS;
- avaliar qualidade por modalidade;
- controlar custo, armazenamento e retenção.

## Unidade 1 — Arquitetura multimodal

Modele uma entrada comum com arquivo, tipo, hash, origem, proprietário, classificação, política de retenção e status de processamento.

```text
upload -> validação -> storage -> fila -> workers especializados
       -> resultados normalizados -> indexação -> auditoria
```

Inclua antivírus, allowlist de MIME, limite de tamanho, hash, deduplicação, isolamento e descarte seguro.

## Unidade 2 — Áudio

- sample rate, canais, codecs e ruído;
- voice activity detection;
- speech-to-text;
- diarização;
- timestamps;
- avaliação por Word Error Rate;
- PII em transcrições;
- síntese de voz e consentimento.

### Laboratório

Transcreva uma reunião autorizada, identifique falantes quando possível, gere resumo e ações. Preserve timestamps e permita voltar ao trecho original.

## Unidade 3 — Vídeo

- extração de frames;
- keyframes;
- detecção e tracking;
- legendas;
- sincronização temporal;
- custo de processamento;
- direitos de imagem.

### Laboratório

Crie um indexador que extrai áudio, transcreve, seleciona frames e gera uma linha do tempo pesquisável. Não use reconhecimento facial de pessoas sem base legal e consentimento apropriado.

## Unidade 4 — Document AI e AWS

Explore equivalentes locais e serviços como armazenamento de objetos, filas, funções, OCR/document extraction, NLP e endpoints de ML.

### Laboratório AWS

Implemente uma arquitetura de referência com:

- upload em object storage;
- evento/fila;
- worker;
- extração de documento;
- persistência de resultado;
- dead-letter queue;
- métricas e alarmes;
- IAM de mínimo privilégio.

A execução real na nuvem é opcional; infraestrutura e mocks devem permitir estudo sem custo.

## Unidade 5 — APIs de IA

Pratique:

- OpenAPI;
- versionamento;
- autenticação e autorização;
- upload seguro;
- polling, webhook e Server-Sent Events;
- idempotency key;
- correlation ID;
- rate limiting;
- retry e circuit breaker;
- health checks;
- contratos de erro.

### Contrato de job

```json
{
  "jobId": "uuid",
  "status": "queued",
  "createdAt": "2026-01-01T00:00:00Z",
  "links": { "status": "/jobs/uuid" }
}
```

## Unidade 6 — Avaliação multimodal

Defina métricas por tarefa:

- OCR: character/word error e acerto de campos;
- áudio: WER e erro por contexto;
- vídeo: precision/recall, IoU ou qualidade da timeline;
- resumo: cobertura factual e citações temporais;
- sistema: throughput, p95, falhas e custo por arquivo.

## Checkpoint — Multimodal Processing Hub

### Requisitos

- upload seguro;
- processamento assíncrono;
- pelo menos três modalidades;
- storage desacoplado;
- fila e DLQ;
- status de job;
- resultado normalizado;
- rastreabilidade até arquivo/tempo/página;
- testes com mocks;
- política de retenção;
- dashboard básico de métricas.

## Critérios de aceite

- arquivo inválido não chega ao worker;
- mensagens podem ser reprocessadas sem duplicar efeitos;
- falha transitória não perde o job;
- conteúdo original não é alterado;
- custo e tempo são registrados;
- exclusão remove derivados conforme a política.