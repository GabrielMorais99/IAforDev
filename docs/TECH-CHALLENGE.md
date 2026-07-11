# Tech Challenge — Enterprise AI Hub

O Tech Challenge é um projeto evolutivo, não cinco projetos descartáveis. Cada fase adiciona uma capacidade ao mesmo produto.

## Problema

Empresas recebem documentos, imagens, áudios, vídeos e eventos de sistemas. O produto deve extrair informações, classificar conteúdo, permitir perguntas com fontes, executar ferramentas controladas, detectar anomalias e manter auditoria.

## Incrementos

### Fase 1

- upload e validação;
- OCR;
- classificação;
- API Python;
- métricas e model card.

### Fase 2

- NLP em português;
- embeddings e busca semântica;
- chatbot limitado;
- gateway de provedores;
- arquitetura cloud portátil.

### Fase 3

- ingestão incremental;
- RAG híbrido;
- citações;
- tools;
- workflow com estado;
- avaliação de recuperação e geração.

### Fase 4

- áudio e vídeo;
- processamento assíncrono;
- filas, retries e DLQ;
- storage de objetos;
- timeline multimodal.

### Fase 5

- autenticação/autorização;
- LGPD e retenção;
- threat model;
- detecção de anomalias;
- observabilidade;
- CI/CD e implantação.

## Arquitetura mínima

- ASP.NET Core como API de negócio/orquestração;
- serviço Python para ML e processamento;
- banco relacional;
- vector store;
- fila e worker;
- object storage;
- provider de LLM substituível;
- OpenTelemetry ou telemetria equivalente.

## Entregáveis finais

1. código reproduzível;
2. diagrama C4 ou equivalente;
3. ADRs das decisões principais;
4. dataset e scripts de avaliação;
5. model cards e prompt cards;
6. threat model;
7. inventário de dados/LGPD;
8. testes unitários, integração, contrato e segurança;
9. dashboard de qualidade, custo e latência;
10. runbook de incidentes e rollback;
11. vídeo/demo de 10–15 minutos;
12. backlog de evolução.

## Restrições

- nenhum segredo no repositório;
- nenhuma ação externa irreversível sem confirmação;
- nenhuma resposta crítica sem evidência ou abstention;
- nenhuma métrica calculada sobre o conjunto de treino;
- nenhum documento recuperado antes da autorização;
- nenhuma dependência obrigatória de API paga para executar testes.

## Banca simulada

Prepare respostas para:

- Qual problema de negócio foi resolvido?
- Qual baseline foi superado?
- Como a qualidade foi medida?
- Onde o sistema pode falhar?
- Como você protege dados e tools?
- Quanto custa por 1.000 documentos/perguntas?
- Como trocar modelo ou provedor?
- Como detectar regressão?
- Como apagar os dados de um titular?
- Como reverter uma versão ruim?