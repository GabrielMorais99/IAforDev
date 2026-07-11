# Sistema de avaliação

A formação usa evidências práticas, não presença ou leitura.

## Nota por fase

| Critério | Peso |
|---|---:|
| funcionamento e requisitos | 25% |
| qualidade técnica e arquitetura | 20% |
| avaliação e métricas | 20% |
| testes e reprodutibilidade | 15% |
| segurança, privacidade e ética | 10% |
| documentação e comunicação | 10% |

Aprovação sugerida: **70/100**, sem zerar segurança nem avaliação.

## Rubrica

### 0 — ausente

Não há entrega ou evidência.

### 1 — inicial

Funciona apenas no cenário feliz, sem baseline, testes ou explicação.

### 2 — adequado

Atende requisitos principais, possui testes básicos, métricas e documentação reproduzível.

### 3 — profissional

Compara alternativas, trata falhas, mede custo/latência, possui observabilidade e decisões justificadas.

### 4 — excelente

Inclui análise de risco, experimentos reproduzíveis, quality gates, segurança testada e comunicação clara de limitações.

## Evidências obrigatórias

- commit history coerente;
- README de execução;
- testes automatizados;
- dataset de avaliação versionado ou script de obtenção;
- resultados em JSON/CSV;
- análise de erros;
- diagrama;
- registro de decisões;
- demonstração.

## Autoavaliação de laboratório

Antes de concluir, responda:

1. Qual baseline usei?
2. Qual dado ficou fora do treino?
3. Que métrica representa o custo real do erro?
4. Que entradas quebram a solução?
5. Que informação não deveria aparecer em logs?
6. Como executo sem serviço pago?
7. Como outra pessoa reproduz o resultado?
8. Qual limitação continua aberta?

## Avaliação de LLM/RAG

Não use somente avaliação subjetiva. Mantenha casos com:

- pergunta/entrada;
- resposta ou critérios esperados;
- fontes esperadas;
- tags de dificuldade;
- resultado por versão;
- custo e latência;
- motivo da falha.

Separe métricas de recuperação das métricas de resposta.

## Política de uso de IA no estudo

Ferramentas de IA podem explicar, revisar, gerar testes e ajudar a depurar. O aluno deve conseguir:

- explicar o código;
- reproduzir a solução sem conversa privada;
- justificar decisões;
- detectar sugestões incorretas;
- manter autoria e licenças;
- não enviar dados confidenciais a serviços não autorizados.