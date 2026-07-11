# Fase 5 — Segurança, LGPD, Azure, anomalias e produção

**Carga:** 72 horas  
**Período:** meses 9 e 10  
**Entrega:** produto final seguro, observável e operável.

## Competências

- aplicar privacy by design e requisitos da LGPD;
- fazer threat modeling de aplicações com IA;
- proteger RAG, prompts, tools e dados;
- detectar anomalias em séries e eventos;
- implantar e monitorar workloads de IA no Azure;
- planejar avaliação contínua, incidentes e rollback.

## Unidade 1 — LGPD e governança

Estude finalidade, adequação, necessidade, transparência, segurança, prevenção, não discriminação e responsabilização. Mapeie:

- dado pessoal e sensível;
- titular, controlador e operador;
- base legal;
- origem e destino;
- retenção;
- compartilhamento;
- direitos do titular;
- decisão automatizada;
- evidências de governança.

### Laboratório

Crie um inventário de dados do projeto e uma matriz `dado x finalidade x base x retenção x acesso`. Implemente exportação e exclusão de dados de um usuário fictício.

## Unidade 2 — Segurança para IA

Ameaças:

- prompt injection direta e indireta;
- data poisoning;
- exfiltração por contexto ou tool;
- output inseguro;
- dependência comprometida;
- segredo em log;
- acesso indevido ao índice vetorial;
- model denial of service;
- supply chain de modelos;
- abuso de custo.

### Controles

- autorização antes da recuperação;
- isolamento entre tenants;
- validação de entrada e saída;
- allowlist de tools;
- confirmação para ações sensíveis;
- sandbox;
- limites de tokens, tempo e gasto;
- red teaming;
- auditoria imutável;
- kill switch.

### Laboratório

Crie um threat model com ativos, fronteiras de confiança, atacantes, ameaças, controles e risco residual. Escreva testes para pelo menos dez ataques.

## Unidade 3 — Detecção de anomalias

- anomalia pontual, contextual e coletiva;
- z-score e IQR;
- Isolation Forest;
- Local Outlier Factor;
- One-Class SVM;
- autoencoders;
- sazonalidade;
- drift;
- avaliação sem rótulos perfeitos;
- custo do falso positivo.

### Laboratório

Detecte anomalias em telemetria de API: latência, erros, tokens, custo e volume. Compare regra estatística e Isolation Forest. Explique cada alerta com as features responsáveis.

## Unidade 4 — Azure AI e implantação

Projete uma alternativa Azure para o projeto usando serviços de identidade, secrets, storage, filas, containers, observabilidade, busca e modelos.

Requisitos:

- managed identity quando disponível;
- Key Vault;
- private endpoints quando necessário;
- RBAC mínimo;
- ambientes separados;
- infraestrutura como código;
- orçamento e alertas;
- dados e região documentados.

## Unidade 5 — LLMOps/MLOps

- versionamento de dados, modelos, prompts e índices;
- experiment tracking;
- registry;
- testes offline e online;
- shadow/canary;
- drift de dados e qualidade;
- rollback;
- SLO/SLI;
- incident response;
- feedback humano;
- reavaliação após troca de modelo.

### Quality gates

Uma versão só pode avançar quando:

- testes funcionais passam;
- métricas mínimas são atendidas;
- segurança não regrediu;
- custo está dentro do orçamento;
- migração/rollback foram testados;
- documentação foi atualizada.

## Unidade 6 — Observabilidade

Registre sem expor conteúdo sensível:

- request e trace IDs;
- modelo/provedor/versão;
- prompt/template version;
- tokens e custo;
- latência por etapa;
- documentos recuperados;
- tool calls;
- recusas e abstentions;
- feedback;
- erros categorizados.

## Tech Challenge final — Enterprise AI Hub

Finalize o produto integrador com:

- ingestão multimodal;
- OCR e classificação;
- busca híbrida e RAG com fontes;
- tools controladas;
- detecção de anomalias;
- autenticação e autorização;
- LGPD e retenção;
- threat model;
- observabilidade;
- CI/CD;
- containers;
- arquitetura local e cloud;
- relatório de avaliação;
- apresentação técnica.

## Critérios de aceite

- execução local reproduzível;
- nenhum segredo no Git;
- autorização aplicada antes da recuperação;
- respostas críticas citam evidências;
- ações sensíveis exigem confirmação;
- testes de segurança automatizados;
- custo e p95 visíveis;
- rollback documentado;
- exclusão de usuário testada;
- incident runbook disponível.