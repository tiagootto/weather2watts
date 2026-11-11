# Projeto Final: Pipeline Analítico Automatizado

**UC:** Analytics Coding & Automation | **Pós-Graduação FCEP** | **Trabalho de grupo**

---

## 1. Contexto

Uma empresa de distribuição de energia quer perceber em que medida as **condições meteorológicas influenciam o consumo diário de energia** em 5 cidades portuguesas. O vosso grupo deve construir um **pipeline reprodutível** que obtém dados meteorológicos através de uma API, combina-os com os dados internos da empresa, limpa-os, analisa-os e gera automaticamente um relatório.

## 2. Fontes de dados (iguais para todos os grupos)

| Fonte | Descrição |
|---|---|
| **API Open-Meteo (histórico)** | `https://archive-api.open-meteo.com/v1/archive`. Não requer chave nem registo. |
| **Ficheiro interno** | `data/dados_grupoXX.csv`: consumo diário de energia (kWh) por cidade. **Não pode ser editado manualmente**: toda a limpeza tem de ser feita em código. |
| **Parâmetros do grupo** | `parametros.py`: cidades, coordenadas e período. **Parâmetros diferentes dos atribuídos invalidam o trabalho.** |

**Parâmetros do pedido à API:** `latitude`, `longitude`, `start_date`, `end_date` (formato `AAAA-MM-DD`), `timezone=auto` e `daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max`. A resposta é JSON, com os dados em `daily` (uma lista por variável, mais a lista `time` com as datas).

> O serviço gratuito destina-se a uso não comercial e tem limites de pedidos diários. Façam **um pedido por cidade** e guardem a resposta em `data/raw/`, para não repetirem pedidos desnecessários durante o desenvolvimento.

## 3. Como trabalhar

O projeto constrói-se **a partir desta pasta-modelo**. O ambiente é livre. **Não é necessário usar Git.**

**Opção Google Colab (recomendada para quem não tem Python instalado):**
1. Descarreguem a pasta-modelo (botão *Code → Download ZIP* no GitHub), extraiam-na e **carreguem a pasta inteira para o vosso Google Drive** (por exemplo, `Meu Drive/analytics_projeto`). Se trabalharem vários, partilhem a pasta no Drive.
2. Abram os notebooks **a partir do Drive** (clique direito → *Abrir com → Google Colaboratory*), para que as alterações fiquem guardadas na mesma pasta.
3. A primeira célula de cada notebook liga o Drive e posiciona-se na pasta do projeto. Ajustem a variável `PASTA` se a pasta tiver outro nome.
4. Para correr o pipeline completo, numa célula: `!python main.py`.

> No Colab, **trabalhem sempre dentro da pasta do Drive**. Ficheiros criados fora dela perdem-se quando a sessão termina.

**Opção local:** extraiam a pasta, instalem as dependências com `pip install -r requirements.txt` e usem Jupyter e `python main.py`.

## 4. Requisitos

**Aquisição**
1. Função que obtém os dados de uma cidade (coordenadas e período) com *timeout*, tratamento de erros (`try/except`) e de resposta vazia.
2. Conversão do JSON para `DataFrame` e gravação dos dados brutos em `data/raw/`, com a data de obtenção na nomenclatura do ficheiro.

**Limpeza**
3. Tratamento de nulos, duplicados, tipos, formatos de data, nomes de cidades inconsistentes e valores anómalos.
4. Um relatório de qualidade de dados (tabela) com **o que foi encontrado e a decisão tomada**. Cada decisão é justificada numa célula de texto do notebook.
5. Junção das duas fontes por cidade e data, com verificação das linhas perdidas.

**Análise**
6. Estatísticas descritivas por cidade e **pelo menos 3 visualizações**.
7. **Pelo menos 3 variáveis derivadas**, com justificação do seu interesse para a decisão (ex.: dia de calor, média móvel de 7 dias, variação face à média da cidade, percentil).
8. Pelo menos uma análise da relação entre meteorologia e consumo (correlação ou comparação de grupos), com **leitura crítica das limitações**.

**Automatização**
9. `main.py` que executa o pipeline de ponta a ponta **com um único comando**.
10. Relatório gerado automaticamente (Excel ou HTML) com data na nomenclatura, contendo tabela-resumo, gráficos e data de geração.

**Qualidade e documentação**
11. Código organizado em funções com docstrings.
12. **Pelo menos 3 validações de qualidade com `assert`** no pipeline, com mensagens de erro claras (ex.: "não há duplicados por cidade e data", "não há consumos negativos", "as 5 cidades estão presentes").
13. Notebooks e `main.py` que **correm do início ao fim sem erros** a partir de uma sessão limpa, seguindo apenas as instruções deste README.
14. Este `README.md` completado: tabela de contribuições e instruções de execução (ver fim do ficheiro).
15. `AI_LOG.md` preenchido (ver secção 5).

## 5. Política de IA

O uso de assistentes de IA é **permitido e incentivado**, desde que declarado no `AI_LOG.md`. Todos os elementos do grupo são responsáveis por todo o código entregue e devem ser capazes de o explicar e alterar durante a defesa. **A incapacidade de explicar o próprio trabalho penaliza a nota individual, independentemente da qualidade do código.**

## 6. Entrega

Um ficheiro **`.zip`** carregado na plataforma da escola, com a pasta do projeto completa: notebooks, `main.py`, `parametros.py`, `data/` (incluindo `data/raw/`), relatório gerado em `reports/`, `README.md` e `AI_LOG.md`. No Drive: clique direito na pasta → *Descarregar*.

## 7. Calendário

| Marco | Data | Conteúdo |
|---|---|---|
| **Checkpoint** | 2026-11-23 | Entrega do notebook `A_aquisicao.ipynb` com as secções 1 a 4 (ver notebook): um pedido à API a funcionar para as 5 cidades. |
| **Entrega final** | 2026-12-10 | Ficheiro `.zip` na plataforma. |
| **Defesas** | 2026-12-11 e 2026-11-12 | Por grupo, em videochamada (câmara ligada, partilha de ecrã). |

## 8. Avaliação

| Componente | Peso | Tipo |
|---|---|---|
| Checkpoint | 5% | Grupo (avaliado por níveis: funciona / funciona parcialmente / não funciona) |
| Projeto | 55% | Grupo |
| Defesa | 40% | Individual, com **nota mínima na componente individual** (25% dessa componente) |



**Defesa:** realizada por grupo. O grupo executa o `main.py` e apresenta o relatório; depois, cada elemento responde a perguntas sobre partes do projeto escolhidas pelo docente no momento, e um elemento realiza uma pequena alteração ao vivo. A nota é individual: parte dela é comum ao grupo (demonstração, alteração ao vivo e reflexão sobre IA) e a maior parte depende do que cada elemento demonstra compreender, **de qualquer parte do projeto**.

---

## Estrutura da pasta

```
.
├── README.md            # este ficheiro (completar no fim)
├── AI_LOG.md            # registo do uso de IA
├── parametros.py        # parâmetros do grupo (substituir pelo fornecido)
├── main.py              # pipeline completo (resultado final)
├── requirements.txt     # só para quem trabalha localmente
├── data/
│   ├── dados_grupoXX.csv  # ficheiro interno (fornecido; não editar)
│   ├── raw/               # respostas brutas da API
│   └── processed/         # dados limpos
├── notebooks/           # A_aquisicao, B_limpeza, C_analise
└── reports/             # relatórios gerados
```

---

## A completar pelo grupo

### Tabela de contribuições
Indiquem quem trabalhou em quê. Pode haver várias pessoas na mesma área e a mesma pessoa em várias áreas.

| Nome | Nº de aluno | Áreas em que trabalhou (aquisição, limpeza, análise, relatório, documentação, ...) |
|---|---|---|
| | | |

### Como executar o projeto
*(Descrevam, em 3-5 passos, como correr o pipeline a partir de uma sessão limpa.)*
