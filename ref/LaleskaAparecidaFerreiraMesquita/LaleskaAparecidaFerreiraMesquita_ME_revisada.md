### **Redes neurais artificiais aplicadas a séries temporais para predição de enchentes**

### **Laleska Aparecida Ferreira Mesquita**

Dissertação de Mestrado do Programa de Pós-Graduação em Ciências de Computação e Matemática Computacional (PPG-CCMC)

SERVIÇO DE PÓS-GRADUAÇÃO DO ICMC-USP

Data de Depósito:

Assinatura: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Laleska Aparecida Ferreira Mesquita**

### Redes neurais artificiais aplicadas a séries temporais para predição de enchentes

Dissertação apresentada ao Instituto de Ciências Matemáticas e de Computação – ICMC-USP, como parte dos requisitos para obtenção do título de Mestra em Ciências – Ciências de Computação e Matemática Computacional. *VERSÃO REVISADA*

Área de Concentração: Ciências de Computação e Matemática Computacional

Orientador: Prof. Dr. Jó Ueyama

**USP – São Carlos Julho de 2024**

#### Ficha catalográfica elaborada pela Biblioteca Prof. Achille Bassi e Seção Técnica de Informática, ICMC/USP, com os dados inseridos pelo(a) autor(a)

| M582r | Mesquita, Laleska Aparecida Ferreira<br>Redes neurais artificiais aplicadas a séries<br>temporais para predição de enchentes / Laleska<br>Aparecida Ferreira Mesquita; orientador Jo<br>Ueyama. -- São Carlos, 2024.<br>128 p. |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       | Dissertação (Mestrado - Programa de Pós-Graduação<br>em Ciências de Computação e Matemática<br>Computacional) -- Instituto de Ciências Matemáticas<br>e de Computação, Universidade de São Paulo, 2024.                        |
|       | 1. Inteligência Artificial. 2. Séries Temporais.<br>3. Deep Learning. 4. Enchentes. 5. Recurrence Plot.<br>I. Ueyama, Jo , orient. II. Título.                                                                                 |

 Bibliotecários responsáveis pela estrutura de catalogação da publicação de acordo com a AACR2: Gláucia Maria Saia Cristianini - CRB - 8/4938 Juliana de Souza Moraes - CRB - 8/6176

**Laleska Aparecida Ferreira Mesquita**

Applied time series neural networks for flood prediction

Master dissertation submitted to the Institute of Mathematics and Computer Sciences – ICMC-USP, in partial fulfillment of the requirements for the degree of the Master Program in Computer Science and Computational Mathematics. *REVISED VERSION*

Concentration Area: Computer Science and Computational Mathematics

Advisor: Prof. Dr. Jó Ueyama

**USP – São Carlos July 2024**

*Este trabalho é dedicado a minha família, e em especial a minha esposa Ana Gabriela os quais me deram amor e foram suporte nos dias em que eu não acreditava que havia uma saída.*

Os agradecimentos principais são direcionados à Jó Ueyama meu orientador presente e paciente em todo o trajeto até aqui e ao meu coorientador Caetano Mazzoni Ranieri que até aqui não mediu esforços para que eu cumprisse esta etapa.

Agradeço a Deus.

Sou profundamente grata aos meus queridos amigos Andreza, Sane, Leo, Lu, Lucas cuja presença transformou a jornada árdua em um caminho de leveza, sempre oferecendo palavras de conforto nos momentos mais sombrios e celebrando cada vitória ao meu lado com genuína alegria.

Agradecimentos especiais são direcionados ao Instituto de Ciências Matemáticas e de Computação - ICMC o qual faço parte com muito orgulho.

E agradeço a CAPES - Coordenação de Aperfeiçoamento de Pessoal de Nível Superior - Código de Financiamento 001, a qual contribuiu para o meu suporte financeiro no Programa.

*"O mundo quebra a todos, e depois, alguns são fortes nos lugares quebrados. (Ernest Hemingway)"*

# **RESUMO**

MESQUITA, LALESKA A. F. Redes neurais artificiais aplicadas a séries temporais para predição de enchentes. 2024. [128](#page-129-0) p. Dissertação (Mestrado em Ciências – Ciências de Computação e Matemática Computacional) – Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, São Carlos – SP, 2024.

Fenômenos hidrológicos extremos, aliados a uma falta de planejamento de escoamento, são responsáveis por diversos desastres climáticos e, dentre eles, destaca-se no Brasil a ocorrência de enchentes. Quando de encontro ao caminho de ocupação social, as enchentes trazem complicações, podendo ocasionar prejuízos econômicos e sociais. Diversos campos de estudo podem ajudar nos esforços para atenuar os efeitos desses desastres e a criar soluções para sua prevenção, como é o caso da inteligência artificial, que tem sido uma aliada nas soluções desta problemática. Buscam-se, cada vez mais, mecanismos que possibilitem um preparo antecipado às catástrofes iminentes para melhorar segurança da população em áreas de risco. Neste contexto, o presente trabalho tem como objetivo atuar na predição de enchentes utilizando redes neurais artificiais, que baseadas em dados de séries temporais, possibilitem um resultado preditivo quanto aos eventos de enchentes. Este trabalho está baseado em ferramentas que, a partir dos dados de nível de máxima do rio Xingu, possam gerar análises não só de dados em uma dimensão, mas também a partir da conversão desses dados em representações bidimensionais, possibilitando a aplicação em redes neurais recorrentes e convolucionais. Visando as possibilidades de ferramentas que supram essa demanda, o trabalho propõe uma resposta preditiva ou de classificação para os dados encontrados em séries históricas do rio Xingu, visando melhorar as técnicas existentes para predição de enchentes.

Palavras-chave: Enchentes, séries temporais, redes neurais artificiais, inteligência artificial, aprendizado de máquina, aprendizado profundo.

# **ABSTRACT**

MESQUITA, LALESKA A. F. Applied time series neural networks for flood prediction. 2024. [128](#page-129-0) p. Dissertação (Mestrado em Ciências – Ciências de Computação e Matemática Computacional) – Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, São Carlos – SP, 2024.

Extreme hydrological phenomena, combined with a lack of drainage planning, are responsible for several climatic disasters and, among them, the occurrence of floods stands out in Brazil. When encountering social occupation, floods bring complications and may lead to economic and social losses. Several fields of study can help mitigate the effects of these disasters, and create solutions for their prevention, as is the case of artificial intelligence, which has been an ally in solving this problem. Increasingly, there has been a search for mechanisms to prepare in advance for imminent catastrophes, and improve the population's safety in areas of risk. In this context, this work aims to act in flood prediction using artificial neural networks which, based on time series data, may enable a predictive result regarding flood events. This work uses the data of the maximum level of the Xingu River to analyze not only one-dimensional data but also on the conversion of this data into two-dimensional representations, allowing the application in recurrent and convolutional neural networks. Aiming at the possibilities of tools that fulfill this demand, this work proposes responses in the form of prediction or classification of historical data from the Xingu River, aiming to improve the existing techniques for flood prediction.

Keywords: Flooding, time series, neural networks, artificial intelligence, machine learning, deep learning.

| Figura 1<br>– | Exemplo de gráfico de recorrência de uma série temporal. Reproduzido de                                          |          |
|---------------|------------------------------------------------------------------------------------------------------------------|----------|
|               | Kirichenko, Zinchenko e Radivilova<br>(2021).                                                                    | 29       |
| Figura 2<br>– | Ciclo hidrológico. Reproduzido de<br>Telles<br>(2018)                                                            | 34       |
| Figura 3<br>– | Exemplificação dos Níveis do aumento pluviométrico e suas classificações.                                        |          |
|               | Adaptado de<br>Licco e Dowell<br>(2015).                                                                         | 35       |
| Figura 4<br>– | Registro jornalistico de Enchente em São Carlos.<br>CNN<br>(2020).                                               | 35       |
| Figura 5<br>– | Exemplos de séries temporais (a) Totais mensais de passageiros em linhas                                         |          |
|               | aéreas internacionais nos EUA entre 1949 e 1960, (b) número anual de linces                                      |          |
|               | capturados em armadilhas entre 1821 e 1934 no Canadá, (c) medições anuais                                        |          |
|               | de vazões do Rio Nilo em Ashwan entre 1871 e 1970, (d) consumo de gás no                                         |          |
|               | Reino Unido entre o primeiro trimestre de 1960 e o quarto trimestre de 1986.                                     |          |
| Figura 6<br>– | Adaptado de (EHLERS,<br>2005).<br>Modelo biológico de um neurônio. Reproduzido de<br>Russell e Norvig<br>(2013). | 37<br>42 |
| Figura 7<br>– | Esquema de uma unidade de Rede Neural Artificial.                                                                | 43       |
| Figura 8<br>– | Esquema exemplo de uma unidade de RNA. Reproduzido de<br>Osorio e Bitten                                         |          |
|               | court<br>(2000).                                                                                                 | 43       |
| Figura 9<br>– | Metodologia de exemplo para as etapas de um projeto de IA. Adaptado de                                           |          |
|               | Fagundes<br>(2021).                                                                                              | 44       |
| Figura 10 –   | Relação entre Inteligência Artificial (IA), Machine Learning (ML) e Deep                                         |          |
|               | Learning (DL) em forma de um diagrama de Venn. Adaptado de<br>Saraiva                                            |          |
|               | (2018).                                                                                                          | 44       |
| Figura 11 –   | Esquema de fluxo referente ao uso tanto de CNNs quanto de RNNs nos                                               |          |
|               | blocos de processamento. Implicando em uma arquitetura capaz de lidar com                                        |          |
|               | diferentes tipos de dados e tarefas, aproveitando a força das CNNs para dados                                    |          |
|               | espaciais (como imagens) e das RNNs para dados sequenciais (como texto                                           |          |
|               | ou séries temporais). .Adaptado<br>Kirichenko, Zinchenko e Radivilova<br>(2021).                                 | 45       |
| Figura 12 –   | Estrutura de um neurônio na imagem a) e estrutura de neurônios no decorrer                                       |          |
|               | do tempo na imagem b).Adaptado<br>Ranieri<br>(2018).                                                             | 46       |
|               | Figura 13 – Exemplo de arquitetura CNN. Adaptado de<br>Aurelien<br>(2019).                                       | 48       |
| Figura 14 –   | Estrutura de camadas de uma rede CNN do tipo de campos repetitivos retan                                         |          |
|               | gulares. Adaptado de<br>Aurelien<br>(2019).                                                                      | 48       |
| Figura 15 –   | Indicação de uma recorrência I em uma trajetória arbitrária em um espaço                                         |          |
|               | bi-dimensional.                                                                                                  | 49       |

| Figura 16 –<br>Exemplo de construção de um gráfico de recorrência 10x10 com dimensão 1<br>e raio 1.                                                                                                                                                                                                                                                                                      | 50       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Figura 17 –<br>Tipologias características dos gráficos de recorrência, sendo que (A) descreve<br>um comportamento homogêneo, (B) periódico, (C) drift (deriva, ruídos) e<br>(D) descontinuado.                                                                                                                                                                                           | 50       |
| Figura 18 –<br>Abordagem desenvolvida para avaliação da aplicação do uso combinado de<br>gráfico de recorrência + CNN para previsão de enchentes em comparação<br>com RNN, LSTM e GRU.                                                                                                                                                                                                   | 67       |
| Figura 19 –<br>(a) conjunto de dados geral e (b) resultado do processo de seleção das colunas<br>de cotas do conjunto de dados para seleção dos dados de interesse.                                                                                                                                                                                                                      | 70       |
| Figura 20 –<br>Representação esquemática da separação dos dados do conjunto em dados<br>mensais de mínima, máxima, e percentuais de 25% (primeiro quartil), 50%                                                                                                                                                                                                                          |          |
| (segundo quartil) e 75% (terceiro quartil).<br>Séries Temporais referentes ao conjunto de dados parametrizados contendo<br>Figura 21 –<br>os valores mensais de mínima, máxima e quartis p25, p50 e p75 da base de<br>dados do Rio Xingu. O eixo x vai de 0 a aproximadamente 400 porque o<br>DataFrame resultante tem cerca de 400 linhas, cada linha representando um<br>mês de dados. | 71<br>72 |
| Figura 22 – Esquema demonstrativo do processo de janelamento.                                                                                                                                                                                                                                                                                                                            | 73       |
| Figura 23 –<br>Conversão de cada uma das séries temporais (mínima, máxima, p25, p50 e<br>p75) em gráficos de recorrência gerados a partir de matrizes 20x20.                                                                                                                                                                                                                             | 74       |
| Figura 24 –<br>Gráficos de recorrência referentes à cada série temporal - mínima, máxima,<br>p25, p50 e p75                                                                                                                                                                                                                                                                              | 75       |
| Figura 25 –<br>Processo de conversão das séries temporais em gráficos de recorrência após a<br>etaá de empilhamento.                                                                                                                                                                                                                                                                     | 76       |
| Figura 26 –<br>Sequência metodológica executada no desenvolvimento do projeto, contem<br>data set<br>plando as etapas de conversão do<br>pré-processado em séries temporais,<br>seguida da geração dos gráficos de recorrência, utilizados como entradas nas                                                                                                                             |          |
| CNNs e, por fim, os resultados de previsão.<br>Figura 27 –<br>Esquemático. Estrutura de arquiteturas e implementações adotados, contem<br>plando os diferentes modelos utilizados (RP + CNN, LSTM, GRU e RNN) e                                                                                                                                                                          | 77       |
| também a adição da abordagem de transfer learning.<br>Figura 28 –<br>Esquemático. Divisão por faseamento das etapas executadas. Fase 1 - Gera<br>ção dos gráficos de recorrência a partir das séries temporais e alimentação<br>na CNN; Fase 2 - Adição da etapa de<br>transfer learning<br>ao processamento<br>desenvolvimento na Fase 1; Fase 3 - Aplicação de modelos convencionais   | 78       |
| para fins comparativos das previsões obtidas                                                                                                                                                                                                                                                                                                                                             | 79       |
| Figura 29 – Arquitetura da rede CNN                                                                                                                                                                                                                                                                                                                                                      | 81       |

| Figura 30 – | Processo esquemático do desenvolvimento de<br>Baseline<br>conforme abordagem<br>do valor médio                                                                              | 83  |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Figura 31 – | Processo esquemático do desenvolvimento de<br>Baseline<br>conforme abordagem                                                                                                |     |
|             | do último valor                                                                                                                                                             | 83  |
| Figura 32 – | transfer learning<br>Esquemático do processo de adição da etapa de<br>ao método<br>desenvolvido visando melhoria da capacidade de previsão                                  | 84  |
| Figura 33 – | Representação gráfica das séries temporais do rio Xingu, correspondentes<br>as colunas de valores do conjunto de dados de distribuição por percentis de<br>quartis.         | 91  |
| Figura 34 – | Representação gráfica das séries temporais correspondentes as colunas do<br>conjunto de dados de distribuição por percentis de quartis dos demais 11 rios.                  | 92  |
| Figura 35 – | Representação gráfica das séries temporais do rio Xingu, correspondentes<br>aos gráficos de recorrência.                                                                    | 93  |
| Figura 36 – | Gráficos de recorrência correspondentes a série temporal de valores de má<br>xima do rio Xingu                                                                              | 94  |
| Figura 37 – | Gráficos de recorrência correspondentes a série temporal de valores de mí<br>nimo do rio Xingu                                                                              | 94  |
| Figura 38 – | Gráficos de recorrência correspondentes a série temporal de valores de p25<br>do rio Xingu                                                                                  | 94  |
| Figura 39 – | Gráficos de recorrência correspondentes a série temporal de valores de p50<br>do rio Xingu                                                                                  | 95  |
| Figura 40 – | Gráficos de recorrência correspondentes a série temporal de valores de p75<br>do rio Xingu                                                                                  | 95  |
| Figura 41 – | Seleção de amostras de gráficos de recorrência em tempos distintos da sé<br>rie temporal. Essas amostras constituem o conjunto de dados de imagens<br>utilizado no projeto. | 96  |
| Figura 42 – | Seleção de amostras de gráficos de recorrência em tempos distintos da sé<br>rie temporal. Essas amostras constituem o conjunto de dados de imagens                          |     |
|             | utilizado no projeto.                                                                                                                                                       | 97  |
| Figura 43 – | Gráfico de Recorrência referente a série temporal de valores de máxima do<br>nível do rio                                                                                   | 98  |
| Figura 44 – | Gráfico de Recorrência referente a série temporal de valores de mínima do                                                                                                   |     |
|             | nível do rio                                                                                                                                                                | 98  |
|             | Figura 45 – Gráfico de Recorrência referente a série temporal de valores de percentil 25                                                                                    | 98  |
|             | Figura 46 – Gráfico de Recorrência referente a série temporal de valores de percentil 50                                                                                    | 98  |
|             | Figura 47 – Gráfico de Recorrência referente a série temporal de valores de percentil 75                                                                                    | 98  |
| Figura 48 – | Gráfico de R2 referente ao desempenho do modelo de RNN para o conjunto<br>de dados do rio Xingu.                                                                            | 102 |
|             |                                                                                                                                                                             |     |

| Gráfico de Dispersão dos dados de previsão para o conjunto de treino do<br>Figura 49 –<br>modelo de RNN                         | 103 |
|---------------------------------------------------------------------------------------------------------------------------------|-----|
| Figura 50 –<br>Gráfico de Dispersão dos dados de previsão para o conjunto de teste do<br>modelo de RNN                          | 103 |
| Figura 51 –<br>Gráfico de R2 referente ao desempenho do modelo de LSTM para o conjunto                                          |     |
| de dados do rio Xingu.<br>Figura 52 –<br>Gráfico de Dispersão dos dados de previsão para o conjunto de treino do                | 104 |
| modelo de LSTM                                                                                                                  | 104 |
| Gráfico de Dispersão dos dados de previsão para o conjunto de teste do<br>Figura 53 –<br>modelo de LSTM                         | 104 |
| Figura 54 –<br>Gráfico de R2 referente ao desempenho do modelo de GRU para o conjunto<br>de dados do rio Xingu.                 | 105 |
| Gráfico de Dispersão dos dados de previsão para o conjunto de treino do<br>Figura 55 –<br>modelo de GRU                         | 106 |
| Figura 56 –<br>Gráfico de Dispersão dos dados de previsão para o conjunto de teste do<br>modelo de GRU                          | 106 |
| Gráfico de Dispersão dos dados de previsão para o conjunto de treino do<br>Figura 57 –<br>modelo de CNN com RP                  | 107 |
| Figura 58 –<br>Gráfico de Dispersão dos dados de previsão para o conjunto de teste do<br>modelo de CNN com RP                   | 107 |
| Figura 59 –<br>Gráficos da curva de treino e teste do coeficiente de determinação R2 para o                                     |     |
| modelo de CNN com transfer learning.<br>Figura 60 –<br>Gráfico de Dispersão dos dados de previsão para o conjunto de treino do  | 108 |
| transfer learning<br>modelo de CNN com                                                                                          | 109 |
| Gráfico de Dispersão dos dados de previsão para o conjunto de teste do<br>Figura 61 –<br>modelo de CNN com<br>transfer learning | 109 |

| Tabela 1<br>– | Trabalhos Relacionados Referente aos Modelos de Previsão Hidrológicos                   | 64  |
|---------------|-----------------------------------------------------------------------------------------|-----|
| Tabela 2<br>– | Conjunto de dados gerais brutos contemplando todos os rios utilizados no                |     |
|               | treinamento e aplicação do modelo desenvolvido, exemplificando o período                |     |
|               | de captação, número de estações e número de dados totais referente à cada               |     |
|               | base de dados                                                                           | 68  |
| Tabela 3<br>– | Dados brutos do data set do rio Xingu, contemplando as informações coleta               |     |
|               | das mensalmente para todos os atributos adquiridos                                      | 68  |
| Tabela 4<br>– | Resultados obtidos com a parametrização de todos as cotas coletadas men                 |     |
|               | salmente em dados mensais de mínima, máxima, e percentis de 25% (p25),                  |     |
|               | 50% (p50) e 75% (p75).                                                                  | 72  |
| Tabela 5<br>– | Arquitetura da Rede Neural Convolucional                                                | 81  |
| Tabela 6<br>– | Arquitetura da Rede Neural com SimpleRNN                                                | 85  |
| Tabela 7<br>– | Arquitetura da Rede Neural LSTM                                                         | 86  |
| Tabela 8<br>– | Arquitetura da Rede Neural com GRU                                                      | 86  |
| Tabela 9<br>– | Tabela referente ao conjunto de dados pré-processados contendo dados cor                |     |
|               | respondentes as cotas do nível do rio Xingu, com a exclusão de valores nulos            |     |
|               | e ausentes.                                                                             | 88  |
| Tabela 10 –   | Tabela de Dados de cota resultante do pré processamento das demais 11                   |     |
|               | bases de rios: Kokraimoro, Joari, São João Felix do Xingu, base Neris1883,              |     |
|               | base Neris1886, porto, base Santo Antonio 1, base Santo Antonio 2, Belo                 |     |
|               | Horizonte, Santo José e Jusante; com a exclusão de valores nulos e ausentes.            | 89  |
|               | Tabela 11 – Conjunto de dados do rio Xingu em distribuição de percentis                 | 90  |
| Tabela 12 –   | Tabela de dados em distribuição de quartis das 11 bases de rios: Kokraimoro,            |     |
|               | Joari, São João Felix do Xingu, base Neris1883, base Neris1886, porto, base             |     |
|               | Santo Antonio 1, base Santo Antonio 2, Belo Horizonte, Santo José e Jusante             | 90  |
|               | baseline<br>Tabela 13 – Tabela de resultados métricos para o modelo<br>de média.        | 101 |
|               | baseline<br>Tabela 14 – Tabela de resultados métricos para o modelo<br>de ultimo valor. | 101 |
|               | Tabela 15 – Arquitetura do Modelo de Simple RNN                                         | 102 |
|               | Tabela 16 – Tabela de métricas para o modelo RNN.                                       | 102 |
|               | Tabela 17 – Arquitetura do Modelo LSTM de Rede Neural                                   | 103 |
|               | Tabela 18 – Tabela de resultado para as métricas do modelo de LSTM.                     | 103 |
|               | Tabela 19 – Arquitetura do Modelo GRU de Rede Neural                                    | 105 |
|               | Tabela 20 – Tabela de resultado para as métricas do modelo de GRU.                      | 105 |

| Tabela 22 – Tabela de métricas para o modelo CNN com RP.             | 106 |
|----------------------------------------------------------------------|-----|
| Tabela 21 – Configuração da Rede CNN profunda                        | 107 |
| Tabela 23 – Tabela de métricas para o modelo com transfer learning.  | 108 |
| Tabela 24 – Tabela dos Resultados dos Modelos                        | 110 |
| Tabela 25 – Cota de atenção, alerta e inundação do SAH – Xingu. 2023 | 110 |

# **LISTA DE ABREVIATURAS E SIGLAS**

| ANA      | Agência Nacional de Águas                                          |  |  |  |  |  |  |  |
|----------|--------------------------------------------------------------------|--|--|--|--|--|--|--|
| AR       | Auto Regressivos                                                   |  |  |  |  |  |  |  |
| ARIMA    | Auto-Regressive Integrated Moving Average model                    |  |  |  |  |  |  |  |
| ARMA     | Modelos Autoregressivos e de Médias Móveis                         |  |  |  |  |  |  |  |
| BHA      | Bacia Hidrográfica do Acre                                         |  |  |  |  |  |  |  |
| CEMADEN  | Centro Nacional de Monitoramento e Alerta de Desastres Naturais    |  |  |  |  |  |  |  |
| CNM      | Confederação Nacional de Municípios                                |  |  |  |  |  |  |  |
| CSA      | Algoritmo de Cooperação                                            |  |  |  |  |  |  |  |
| DEM      | Modelo Digital de Elevação                                         |  |  |  |  |  |  |  |
| EEG      | Classificação de Imagens de Eletroencefalograma                    |  |  |  |  |  |  |  |
| ELM      | Extreme Learning Machine                                           |  |  |  |  |  |  |  |
| GARCH    | Generalized Autoregressive Conditional Heteroscedasticity          |  |  |  |  |  |  |  |
| GRU      | Gated Recurrent Unit                                               |  |  |  |  |  |  |  |
| GRU LSTM | Conv long short-term memory encoder–decoder long short-term memory |  |  |  |  |  |  |  |
| HEC-RAS  | Hydrologic Engineering Center—River Analysis System                |  |  |  |  |  |  |  |
| IBGE     | Instituto Brasileiro de Geografia e Estatística                    |  |  |  |  |  |  |  |
| INEA     | Instituto Estadual do Ambiente                                     |  |  |  |  |  |  |  |
| LMI      | Índice de Legates-McCabe                                           |  |  |  |  |  |  |  |
| LSTM     | Long Short-Term Memory                                             |  |  |  |  |  |  |  |
| MA       | Médias Móveis                                                      |  |  |  |  |  |  |  |
| MAE      | Erro absoluto Médio                                                |  |  |  |  |  |  |  |
| MAPE     | Média Percentual Absoluta do Erro                                  |  |  |  |  |  |  |  |
| MARS     | Multivariate Adaptive Regression Splines                           |  |  |  |  |  |  |  |
| ME       | Erro Médio                                                         |  |  |  |  |  |  |  |
| MLP      | Multilayer Perceptron                                              |  |  |  |  |  |  |  |
| MSE      | Erro Quadrático Médio                                              |  |  |  |  |  |  |  |
| MSRE     | Erro Quadrático Relativo                                           |  |  |  |  |  |  |  |
| NASH     | Coeficiente de Nash – Sutcliffe                                    |  |  |  |  |  |  |  |
| NATL     | Atlântico Norte                                                    |  |  |  |  |  |  |  |
| NOAA     | National Oceanic and Atmosferic Administration                     |  |  |  |  |  |  |  |
| PD       | Pressão do Nível do Mar de Darwin                                  |  |  |  |  |  |  |  |

| PT<br>Pressão do Nível do Mar do Tahit<br>R2<br>Coeficiente de Determinação |                        |  |  |  |  |  |  |  |
|-----------------------------------------------------------------------------|------------------------|--|--|--|--|--|--|--|
|                                                                             |                        |  |  |  |  |  |  |  |
|                                                                             |                        |  |  |  |  |  |  |  |
| RAE                                                                         | Erro Relativo Absoluto |  |  |  |  |  |  |  |
| RF<br>Random Forest                                                         |                        |  |  |  |  |  |  |  |
| RMSE<br>Raiz Quadrada do Erro Médio                                         |                        |  |  |  |  |  |  |  |
| RNA<br>Rede Neural Artificial                                               |                        |  |  |  |  |  |  |  |
| RNN<br>Redes Neurais Recorrentes                                            |                        |  |  |  |  |  |  |  |
| RP<br>Recurrence Plots                                                      |                        |  |  |  |  |  |  |  |
| RQA<br>Análise de Quantificação de Recorrência                              |                        |  |  |  |  |  |  |  |
| Rtr<br>Coeficiente de Correlação para Dados de Treinamento                  |                        |  |  |  |  |  |  |  |
| Rtst<br>Coeficiente de Correlação para Dados de Teste                       |                        |  |  |  |  |  |  |  |
| SATL<br>Atlântico Sul                                                       |                        |  |  |  |  |  |  |  |
| SETAR<br>Self-Exciting Threshold Autoregressive                             |                        |  |  |  |  |  |  |  |
| SGB<br>Serviço Geológico do Brasil                                          |                        |  |  |  |  |  |  |  |
| SNIRH<br>Sistema Nacional de Informações sobre Recursos Hídricos            |                        |  |  |  |  |  |  |  |
| Stacked LSTM<br>stacked long short-term memory                              |                        |  |  |  |  |  |  |  |
| SVM<br>Support Vector Machine                                               |                        |  |  |  |  |  |  |  |
| SWMM<br>Storm Water Management Model                                        |                        |  |  |  |  |  |  |  |
| WI<br>Índice de Concordância de Willmott                                    |                        |  |  |  |  |  |  |  |

| 1       | INTRODUÇÃO                                                | 25 |
|---------|-----------------------------------------------------------|----|
| 1.1     | Motivação                                                 | 29 |
| 1.2     | Objetivos                                                 | 30 |
| 1.3     | Organização do Trabalho                                   | 30 |
| 2       | FUNDAMENTAÇÃO TEÓRICA                                     | 31 |
| 2.1     | Contextualização                                          | 31 |
| 2.2     | A climatologia e os fenômenos hidrológicos                | 32 |
| 2.3     | Séries Temporais                                          | 36 |
| 2.3.1   | Autoregressivos - AR                                      | 38 |
| 2.3.2   | Modelos de erro ou regressão                              | 38 |
| 2.3.3   | Modelos de média móvel (MA)                               | 39 |
| 2.3.4   | Modelos autorregressivos e de médias móveis (ARMA)        | 39 |
| 2.3.5   | Modelos autorregressivos Integrados médias móveis (ARIMA) | 39 |
| 2.4     | Inteligência Artificial                                   | 40 |
| 2.4.1   | Aprendizado de Máquina                                    | 41 |
| 2.4.2   | Redes Neurais Artificiais                                 | 42 |
| 2.4.2.1 | Características Gerais das Redes Neurais                  | 42 |
| 2.4.3   | Metodologia para o Desenvolvimento de Aplicações de IA    | 44 |
| 2.5     | Modelos Recorrentes e Convolucionais de Redes Neurais     | 45 |
| 2.5.1   | Rede Neural Recorrente - RNN                              | 46 |
| 2.5.2   | Rede Neural Convolucional - CNN                           | 47 |
| 2.6     | Recurrence Plot                                           | 48 |
| 2.7     | Considerações Finais                                      | 51 |
| 3       | TRABALHOS RELACIONADOS                                    | 53 |
| 3.1     | Modelos de Previsão com RNA                               | 53 |
| 3.2     | Modelos de Previsão Híbridos                              | 54 |
| 3.3     | Modelos de Previsão RNN                                   | 55 |
| 3.4     | Modelos de previsão CNN                                   | 58 |
| 3.5     | Modelos de previsão utilizando o Recurrence Plot          | 59 |
| 3.6     | Considerações Finais                                      | 62 |
| 4       | METODOLOGIA DE PREVISÃO COM RECURRENCE PLOT               | 65 |

| 4.1         | Abordagem<br>65                                                      |
|-------------|----------------------------------------------------------------------|
| 4.2         | Base de dados<br>67                                                  |
| 4.3         | Processamento de Dados<br>69                                         |
| 4.3.1       | Pré-Processamento de Dados<br>69                                     |
| 4.3.2       | Gráficos de Recorrência<br>72                                        |
| 4.3.3       | Implementação<br>78                                                  |
| 4.3.4       | Conjunto de dados do rio Xingu + Gráfico de Recorrência aplicado     |
|             | na CNN<br>80                                                         |
| 4.4         | Abordagens Convencionais<br>81                                       |
| 4.4.1       | Baseline: Ponto de Referência Inicial (Previsão Ingênua)<br>82       |
| 4.4.2       | Rede Neural Convolucional - (CNN) com<br>Transfer Learning<br>83     |
| 4.4.3       | Rede Neural Recorrente<br>85                                         |
| 4.4.4       | Modelo Long Short-Term Memory (LSTM)<br>85                           |
| 4.4.5       | Modelos Gated Recurrent Unit (GRU)<br>86                             |
| 4.5         | Considerações Finais<br>86                                           |
| 5           | RESULTADOS<br>87                                                     |
| 5.1         | Pré Processamento de Dados - Primeira Fase de Resultados<br>87       |
| 5.2         | Processamento de Dados - Segunda Fase de Resultados<br>90            |
| 5.3         | Recurrence Plot - Terceira Fase de Resultados<br>93                  |
| 5.4         | Implementação dos Modelos<br>100                                     |
| 5.5         | Modelo de<br>Baseline<br>- Resultado para ponto de Referência<br>101 |
| 5.6         | Modelos de Redes Neurais Recorrentes - Quarta Fase de Resultados102  |
| 5.6.1       | Rede Neural Recorrente (RNN) - Resultados<br>102                     |
| 5.6.2       | Rede Neural Long Short Term Memory (LSTM) - Resultados<br>103        |
| 5.6.3       | Rede Neural Gated Recurrent Unit (GRU) - Resultados<br>104           |
| 5.7         | Rede CNN com Recurrence Plot - Quarta Fase de Resultados<br>106      |
| 5.8         | Rede CNN com Transfer Learning - Quinta Fase de Resultados<br>107    |
| 5.9         | Discussão dos Resultados<br>110                                      |
| 6           | CONCLUSÃO<br>. 115                                                   |
| 6.1         | Trabalhos Futuros<br>117                                             |
| REFERÊNCIAS | . 119                                                                |

# CAPÍTULO 1

# **INTRODUÇÃO**

<span id="page-26-0"></span>Há tempos, esforços da área acadêmica são direcionados para soluções que contribuam, expliquem, inovem e agreguem valor à forma de vida humana. O que pode ser entendido dessa afirmação partindo da premissa de que a ciência procura explicar e conhecer sobre os fatos que se observam no mundo físico? [\(CHALMERS,](#page-122-2) [1993\)](#page-122-2). Como resultado desses esforços, temos contribuições de conhecimento nas mais diversas áreas sociais, econômicas, humanas e químicas. Outro bom exemplo da importância da ciência e da pesquisa são as informações de processos de transformações físicas, que colaboram com materiais importantes na área de estudo dos fenômenos naturais [\(GIRÃO; RABELO; ZANELLA,](#page-123-1) [2018\)](#page-123-1). As áreas de estudo que possuem como foco os fenômenos naturais são essenciais devido a relevância desses dados no controle e desenvolvimento da existência humana, levando em conta que, ao passo que o homem é agressor no ambiente em que vive, o mesmo também é vítima das manifestações naturais do espaço que está inserido [\(VEYRET,](#page-128-1) [2007\)](#page-128-1).

Essa inversão de papéis, em que o homem se torna vítima, dá-se na ocasião das manifestações dos fenômenos naturais em grande escala. Fenômenos naturais conhecidos pelo homem, como chuva, vento, neve, calor entre outros presentes na natureza, muitas vezes causam infortúnios à vida do homem urbano, de modo que, para essas manifestações naturais em grande escala, podemos elencar desastres naturais como enchentes, erosão, deslizamentos, vendavais, furações, entre tantos outros que são presentes no cotidiano do homem [\(TOMINAGA; SANTORO,](#page-128-2) [2009\)](#page-128-2). Dependendo da localização e o tipo de clima, esses desastres são presentes em diversas épocas do ano. Em países como o Brasil, são extremamente comuns episódios de desastres naturais ligados à água da chuva, devido a variabilidade do clima local e às mudanças climáticas severas no globo terrestre [\(GIRÃO; RABELO; ZANELLA,](#page-123-1) [2018\)](#page-123-1). Não obstante, além dos aspectos climáticos já mencionados, outro agravante para a exposição do homem urbano aos efeitos dos desastres naturais é sua ocupação indevida em locais que eram de natureza livre, reforçando sua exposição a situações impróprias.

O Brasil possui um grande número de registros relacionados a desastres naturais, ocupando o 79o. lugar na escala de países com mais catástrofes naturais. No período entre 2013 e 2023, aproximadamente 93% dos municípios brasileiros foram impactados por desastres naturais como tempestades, inundações, enxurradas e alagamentos. Neste período, foram registradas 59.311 declarações de situação de emergência e estado de calamidade pública em todo o Brasil, em decorrência dos diversos desastres ocorridos, sendo que os eventos ocasionados pelo excesso de chuva correspondente à 27%. Além do clima, a localização geográfica do Brasil é um agravante no que se refere à suscetibilidade a catástrofes. Se formos destacar as chuvas que têm como consequências desastres naturais como enchentes ou alagamentos, segundo o órgão da CNM - Confederação Nacional de Municípios , o Brasil é um dos países do mundo mais afetados por enchentes [\(BRASIL,](#page-121-0) [2023\)](#page-121-0).

Com dados tão significativos referentes às chuvas no Brasil, é esperado que as bacias consigam conter parte desse aumento de precipitação em períodos chuvosos. Porém, quando não é possível toda a drenagem desse aumento pluviométrico pela bacia, o excesso deve ser escoado para outro reservatório. No entanto, devido ao crescimento urbano irregular e à falta de planejamento, esse tipo de estrutura é inexistente, ocasionando diversos danos materiais às comunidades do entorno [\(CANHOLI,](#page-121-1) [2014\)](#page-121-1). Ademais, como vem sendo a movimentação para tratar esse tipo de problemática tão persistente? Além do objetivo da ciência de explicar, de modo cada vez mais preciso, o que acontece no mundo natural, contribuindo com conhecimentos que possibilitam explicação, compreensão e clareza dos elementos que constituem o todo [\(BERKELEY,](#page-121-2) [2007\)](#page-121-2), tem-se o crescente desenvolvimento de tecnologias inspiradas no "mundo natural". Estas tecnologias alavancam, por exemplo, as contribuições de pesquisas que buscam reproduzir artificialmente as habilidades humanas em sistemas de software e hardware, criando tecnologias capazes de alcançar resultados muito além do possibilitado por nós, humanos [\(PRADO,](#page-127-3) [2019\)](#page-127-3).

Em resposta à transformação digital, que possui como resultado este grande volume de dados decorrentes de sistemas e veículos tecnológicos, tem-se o que chamamos, hoje, da era *Big Data* [\(L'HEUREUX; GROLINGER; CAPRETZ,](#page-125-1) [2017\)](#page-125-1). Trata-se de uma grande quantidade de dados não apenas de cunho digital, do tipo "número de itens de compra, comportamento de mercado, ou número de aplicações de ações", mas também registros das ocorrências de catástrofes que caracterizam o ambiente do nosso país. Atualmente, temos dados de toda categoria possível.

Considerando as ferramentas que existem na atualidade, sistemas e mecanismos tecnológicos disponíveis hoje são capazes de lidar com grandes quantidades de dados, funcionar em ambientes insalubres e operar através de acessos remotos. Tais recursos promovem avanços com resultados mais rápidos e sem a necessidade de lidarmos com as limitações humanas, como se pode verificar pela diferença no número de registros que puderam ser catalogados entre 1960 a 2008, e desse período até os dias de hoje [\(PAZ,](#page-126-1) [2021\)](#page-126-1).

Para aproveitar a crescente disponibilidade de novos dados e o poder computacional atual,

vislumbra-se a possibilidade de tratar esses registros e desenvolver soluções para problemas como catástrofes naturais, incluindo enchentes. Para isso, precisamos de ferramentas que possam lidar com essa necessidade e resultar em soluções efetivas para a nossa sociedade [\(TAURION,](#page-128-3) [2013\)](#page-128-3). Com o advento da inteligência artificial, surgiu um vasto leque de oportunidades para resolver questões que anteriormente tinham um alcance limitado [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0). A evolução das técnicas de aprendizado de máquina (ML - Machine Learning) trouxe recursos poderosos. Atualmente, é possível mapear textos em busca de palavras de ódio, criar voz artificial, sintetizar imagens artificiais, entre muitas outras possibilidades.

O aprendizado de máquina é o estudo de algoritmos de computador que podem ser aprimorados automaticamente por meio da experiência e do uso de dados [\(WIKIPEDIA,](#page-129-1) [2021\)](#page-129-1). Este desafio encontra duas variáveis importantes: a qualidade dos dados no *dataset* e a eficiência do algoritmo escolhido. Esse tipo de manipulação de dados possibilita o trabalho em conjunto com as redes neurais, resultando em diversos tipo de manipulação de dados e respostas. No *ML*, ou em um algorítimo preditivo de *deep learning*, se a base de dados utilizada não for tratada adequadamente, é muito provável que o desempenho do modelo utilizado seja afetado, desse modo influenciando na eficiência de retorno dos resultados. Por exemplo, muitas vezes, ao trabalhar com determinado conjunto de dados, não haverá o mesmo número de itens por classe que se busca categorizar [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0).

Para o trabalho em questão, está sendo utilizado uma base de dados com registros dos níveis de máxima mensal do rio Xingu. Os dados hidrológicos disponíveis são fornecidos pela Agência Nacional de Águas - ANA, no sistema Hidroweb, selecionando-se a estação fluviométrica de Altamira - estado do Pará. O rio Xingu nasce no estado do Mato Grosso, na região do Parque Indígena do Xingu, resultado da junção de diversos cursos de água (os rios Culuene, Tamitatoala, Ronuro, Suia Missu, Arraias, Liberdade, Fresco, Iriri, Bacajá e Jarauçu), desaguando no rio Amazonas [\(ZUANON,](#page-129-2) [1999;](#page-129-2) [FERREIRA,](#page-123-2) [2019\)](#page-123-2). Trata-se de um dos mais importantes rios da região Norte do Brasil. Localizado na margem direita do rio Amazonas, ocupa uma área de 509.700 km<sup>2</sup> , sendo um elemento fundamental para as atividades socioeconômicas da região dos estados do Pará e do Mato Grosso [\(VILLAS-BOAS,](#page-128-4) [2012;](#page-128-4) [VIEIRA](#page-128-5) *et al.*, [2020\)](#page-128-5).

A versão utilizada neste trabalho foi acrescida com dados de medidas mensais referente a temperatura e pressão dos oceanos Atlântico e Pacífico juntamente com dados de precipitação captados através das estações da *National Oceanic and Atmosferic Administration* - NOAA. Essa versão aumentada do dataset é composta por dados do período de 1979 a 2016. O tipo de dado em questão, isto é, registros de máxima do rio, eventualmente indica eventos de enchentes na região em que foi obtido. Uma vez que o problema se caracteriza por dados que indicam um acontecimento ao longo do tempo de cunho estatístico, como é o caso do aumento pluviométrico que resulta em enchentes, tem-se uma série temporal. Redes neurais artificiais têm sido boas opções para trabalhar com esse tipo de dado [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0), especialmente redes recorrentes [\(HOCHREITER; SCHMIDHUBER,](#page-124-1) [1997;](#page-124-1) [VASWANI](#page-128-6) *et al.*, [2017\)](#page-128-6).

Neste trabalho de Mestrado, considerando a natureza dos dados que podem ser encontrados nos bancos de dados sobre enchentes, pretende-se explorar alternativas para utilizá-los em algoritmos baseados em técnicas de previsão. Dentro das diversas possibilidades, este trabalho foca em gerar representações bidimensionais para servir a técnicas baseadas em visão computacional, como a *Convolutional Neural Network* - CNN ou redes neurais convolucionais, em português, [\(KRIZHEVSKY; SUTSKEVER; HINTON,](#page-125-2) [2012\)](#page-125-2). Uma possível solução nesse sentido são os *Recurrence Plots* - RP ou gráficos de recorrência . Segundo [Marwan](#page-126-2) *et al.* [\(2007\)](#page-126-2):

> O gráfico de recorrência (*recurrence plot* - RP) é uma técnica avançada de análise de dados não lineares. É uma visualização (ou gráfico) de uma matriz quadrada, na qual os elementos da matriz correspondem aos tempos em que ocorre um estado de um sistema dinâmico (colunas e linhas correspondem então a um determinado par de tempos). Tecnicamente, o RP revela todos os tempos em que a trajetória do espaço de fase do sistema dinâmico visita aproximadamente a mesma área no espaço de fase [\(MARWAN](#page-126-2) *et al.*, [2007\)](#page-126-2).

Uma série temporal expressa a dinâmica dos dados, por exemplo uma sequência que representa um fenômeno real. Costuma apresentar um comportamento não-linear, por ter como tendência comportamentos cíclicos e sazonais, isto é, um comportamento não-estacionário. Uma série temporal de dados com uma dinâmica estacionária apresenta certas características imutáveis ao longo do tempo, como variância e média [\(MADDALA; LAHIRI,](#page-125-3) [2009\)](#page-125-3). Portanto, a utilização da técnica de RP permite analisar o comportamento da série temporal e verificar se ela exibe características estacionárias ou não-estacionárias.

Esse tipo de análise através de gráficos tem apresentado resultados promissores em abordagens que visam melhor acurácia de classificação em tarefas preditivas [\(BABICHEV](#page-120-2) *et al.*, [2020\)](#page-120-2). Por exemplo, o trabalho de [Kirichenko, Zinchenko e Radivilova](#page-124-0) [\(2021\)](#page-124-0) apresenta a técnica de RP aplicada a séries temporais de eletrocardiogramas, utilizando os gráficos para classificar se ele se refere a um comportamento de um paciente epiléptico ou não. A [Figura 1](#page-30-0) ilustra o exemplo prático de um gráfico de recorrência de uma série temporal de um eletrocardiograma.

Ao se representar uma série temporal como gráfico, deixa-se a escala unidimensional das séries temporais, passando a se ter as duas dimensões das imagens, viabilizando o emprego de arquiteturas de redes neurais convolucionais consolidadas para visão computacional [\(TAN;](#page-128-7) [LE,](#page-128-7) [2019\)](#page-128-7). Uma CNN consiste de múltiplas camadas compostas por filtros de convolução e operadores de subamostragem, de modo a discretizar pixel a pixel dos elementos que constem nas imagens de entrada e realizar tarefas como classificação de objetos [\(ROSA,](#page-127-4) [2018;](#page-127-4) [BUDA;](#page-121-3) [MAKI; MAZUROWSKI,](#page-121-3) [2018\)](#page-121-3). Realizada a conversão da série temporal em imagens gráficas, podem ser utilizadas redes neurais convolucionais bidimensionais para previsão e classificação de enchentes [\(ZHANG](#page-129-3) *et al.*, [2020\)](#page-129-3).

Portanto, em resumo, pretende-se explorar a conversão de uma série temporal de níveis

<span id="page-30-0"></span>Figura 1 – Exemplo de gráfico de recorrência de uma série temporal. Reproduzido de [Kirichenko, Zin](#page-124-0)[chenko e Radivilova](#page-124-0) [\(2021\)](#page-124-0).

do rio Xingu em matrizes bidimensionais, visando empregar redes neurais convolucionais às representações obtidas e prever as tendências futuras, incluindo a possível ocorrência de enchentes. Espera-se avaliar os resultados dessa abordagem frente a outras técnicas do estado-daarte.

### <span id="page-30-1"></span>**1.1 Motivação**

Tendo em vista o interesse de auxiliar a comunidade dos arredores do Xingu, que são por vezes afetadas por eventos de enchentes, visa-se propor um modelo preditivo e classificativo que permita avaliar a possibilidade futura desses eventos. Ou seja, utilizando uma abordagem de *deep learing*, particularmente redes neurais artificiais, espera-se prover um mecanismo que possibilite que as autoridades competentes se preparem para agir em prol da segurança local antes de catástrofes iminentes.

Um dos principais desafios em *deep learing* é mensurar a eficiência da técnica utilizada, seja na predição ou classificação de um conjunto de dados. Em vista disso, por vezes, a tarefa de classificar parece ter sido feita com êxito, porém, devido a lacunas nos dados, principalmente quando se trata de uma janela de tempo de série temporal, o resultado pode ser um desempenho fraco ou mediano [\(BROWNLEE,](#page-121-4) [2020\)](#page-121-4).

Desse modo, considerando os resultados promissores decorrentes do emprego de gráficos, como os RP, em trabalhos de classificação de séries temporais utilizando aprendizado de máquina, busca-se explorar o desempenho dos algoritmos de redes neurais convolucionais com o objetivo de aplicá-los no estudo de caso de detecção de enchentes por representações gráficas

bidimensionais [\(BABICHEV](#page-120-2) *et al.*, [2020\)](#page-120-2).

### <span id="page-31-0"></span>**1.2 Objetivos**

Esta dissertação tem como objetivo explorar os dados mensais dos níveis pluviométricos do rio Xingu na região de Altamira, utilizando-os como entrada em modelos de redes neurais artificiais. Após realizar as transformações necessárias nos dados de entrada, busca-se aprimorar a predição dos níveis do rio e a detecção de enchentes. Para alcançar esse objetivo geral, delineiamse os seguintes objetivos específicos, que detalham as ações necessárias para a concretização da ideia principal do trabalho:

favorecendo a predição de níveis do rio e a detecção de enchentes. Pretende-se alcançar esse objetivo geral através dos seguintes objetivos específicos, os quais detalham as medidas necessárias para realização da ideia principal do trabalho:

- ∙ Transformar a série temporal dos níveis de máxima do rio Xingu em representações matriciais bidimensionais, usando gráficos de recorrência;
- ∙ Estimar a ocorrência de enchentes baseado nessas representações com uso de redes neurais profundas;
- ∙ Realizar análise preditiva de enchentes com outros modelos de redes neurais, para fins de comparação;
- ∙ Comparar a acurácia dos modelos obtidos, utilizando diferentes métricas e parametrizações para modelagem e treinamento.

### <span id="page-31-1"></span>**1.3 Organização do Trabalho**

A dissertação será dividida em 6 capítulos. No Capítulo 2, serão apresentados os referenciais teóricos utilizados como base para o desenvolvimento do trabalho. O Capítulo 3 descreve os trabalhos relacionados com o tema principal do trabalho. O Capítulo 4 detalha os processos metodológicos e as técnicas de pesquisa aplicadas. No Capítulo 5 encontram-se os resultados obtidos com a metodologia proposta e a discussão de suas implicações. Por fim, o Capitulo 6 apresenta as conclusões obtidas, as principais contribuições e as previsões futuras relacionadas ao desenvolvimento do presente trabalho.

# CAPÍTULO 2

# <span id="page-32-0"></span>**FUNDAMENTAÇÃO TEÓRICA**

A seguir serão apresentados os conceitos fundamentais que foram utilizados como base para esta proposta de projeto de mestrado. Com o intuito de esclarecer as ferramentas e teorias aqui abordadas, serão apresentados os conceitos que envolvem a problemática desta pesquisa, os quais são os fenômenos hidrológicos, com ênfase na parte de enchentes, e as técnicas e os conceitos de previsão utilizados para o desenvolvimento da proposta, como IA, ML e DL.

### <span id="page-32-1"></span>**2.1 Contextualização**

Destaca-se, dentro as referências dos casos de enchentes e suas consequências, um estudo anterior realizado pelo Centro Nacional de Monitoramento e Alerta de Desastres Naturais - CEMADEN e o censo demográfico realizado no Brasil pelo Instituto Brasileiro de Geografia e Estatística - IBGE com dados de 2010, que teve por objetivo evitar tragédias e as perdas econômicas oriundas de episódios como enchentes e deslizamentos de terra e desabamentos de construções. O estudo apontou mais de 8 milhões de pessoas catalogadas em áreas de risco potencial de enchentes e deslizamentos, além dos 872 municípios por toda extensão do país. Outrossim, a pesquisa apresenta um *ranking* de cidades afetadas de maneira direta e constante sendo o primeiro lugar Salvador, o segundo lugar, a cidade de São Paulo, e o terceiro, o Rio de Janeiro [\(BRASIL,](#page-121-5) [2019\)](#page-121-5). Ainda com o olhar para as zonas de vulnerabilidade tem-se a realidade de enchentes na região de Altamira devido ao rio Xingum que têm ocorrido com certa frequência, especialmente durante a estação chuvosa, que geralmente vai de março a maio. Recentemente, estudos climatológicos e hidrológicos apontaram que a variabilidade das cheias está fortemente ligada à precipitação local e aos padrões de temperatura da superfície do mar, que influenciam as bandas de nuvens convectivas da Zona de Convergência do Atlântico Sul e da Zona de Convergência Intertropical. Além disso, a construção da Usina Hidrelétrica de Belo Monte alterou significativamente o regime hidrológico do rio Xingu, o que tem contribuído para mudanças nos padrões de enchentes na região. A barragem impacta tanto a quantidade

quanto a distribuição da água, afetando a dinâmica das cheias sazonais e a vida das comunidades ribeirinhas.

A realidade enfrentada por muitos cidadãos brasileiros diante de eventos naturais é evidente, bem como a lentidão na mudança dessa situação, mesmo após estudos realizados. Portanto, a necessidade de segurança e controle dessas ocorrências no perímetro urbano é fundamental. A gestão de riscos para o bem-estar dos cidadãos é uma necessidade real para a preservação da vida.

Visando a solução e a colaboração em sanar o problema de gestão de riscos e a previsão de eventos de enchentes, o presente trabalho propõe uma solução utilizando uma rede CNN associado a técnica de RP, aplicados a uma base de dados de séries temporais de cotas de máxima do rio Xingu.

A previsão de enchentes se apresenta como um assunto crítico em todo o mundo, uma vez que tais eventos podem resultar em perdas humanas, materiais e econômicas devastadoras. Agravado pelo cenário de mudanças climáticas e aumento da urbanização, a necessidade de previsões precisas e oportunas torna-se ainda mais indispensável no processo de prevenção do bem estar de cotidiano das pessoas. Sendo assim, o progresso da área de estudo da IA desempenha um papel transformador e de vital importância prever não só eventos de enchentes mas de desastres naturais em geral. Como apresentado no Capítulo [1,](#page-26-0) os problemas relacionados à macrodrenagem urbana (i.e., a drenagem das águas urbanas) resultante de fenômenos naturais, como as chuvas intensas e as cheias dos rios, implicam em adaptações de sobrevivência e segurança para aqueles que residem nas áreas afetadas. Inclusive, segundo dados do IBGE, além das adversidades relacionadas ao saneamento básico que os cidadãos precisam administrar, como água, esgoto e lixo, a macrodrenagem é o problema ambiental que mais afeta a população, em proporções de mais de 80% da população urbana [\(IBGE,](#page-124-2) [2013\)](#page-124-2). Os desastres naturais, como inundações bruscas e enchentes, ficam na escala dos milhares quando contabilizadas as ocorrências no território nacional. De norte a sul, ocorreram enchentes graduais em 1.543 municípios, com 8.942 casos relatados nos últimos 8 anos [\(BRASIL,](#page-121-0) [2023\)](#page-121-0). Além disso, esse tipo de acontecimento hidrológico gera efeitos colaterais como deslizamentos de encostas na casa das centenas. Segundo o último Censo Demográfico realizado no Brasil pelo IBGE, em 2018, apuram-se mais de 303.652 cidadãos desabrigados por algum tempo ou de forma definitiva como resultado desses acontecimentos e pela falta de segurança ambiental urbana [\(IBGE,](#page-124-2) [2013\)](#page-124-2).

### <span id="page-33-0"></span>**2.2 A climatologia e os fenômenos hidrológicos**

A climatologia, segundo [Mendonca e Oliveira](#page-126-3) [\(2007\)](#page-126-3), "é o estudo científico do clima. Ela trata dos padrões de comportamento da atmosfera em suas interações com as atividades humanas e com a superfície do planeta durante um longo período de tempo". Esse conceito mostra a relação direta do clima com o ambiente do espaço terrestre e como estão relacionados à

nossa sociedade à vida na natureza.

O clima de uma região geralmente costuma definir o estilo de vida dos cidadãos locais, seja no modo como constroem suas casas, na localização do comércio ou até mesmo nas escolhas de lazer. Em países tropicais como o Brasil, que apresentam um clima quente com chuvas de verão na maior parte do seu território [\(DUBREUIL](#page-122-3) *et al.*, [2018\)](#page-122-3), a influência das chuvas aparece no cotidiano formas positiva, como na irrigação de plantações, na limpeza do ar com o assentamento de poeiras e impurezas, na manutenção das florestas e nas cheias dos rios, e negativas, nos grandes períodos de estiagem causados pela ausência de chuvas. Períodos de seca interferem diretamente nas produções agrícolas que, inclusive, estão entre os pontos fortes do país economicamente. Porém, o contrário disso, ou seja, o excesso das chuvas, também traz problemas não só econômicos, mas também urbanos. A problemática das chuvas frente ao modo de vida urbano é resultante do crescimento populacional agregado à falta de planejamento no escoamento de grandes volumes de chuva nas ruas, o que pode resultar em enchentes ou alagamentos [\(TRINDADE](#page-128-8) *et al.*, [2016\)](#page-128-8).

Diante deste contexto, é fundamental compreender os conceitos sobre os fenômenos hidrológicos quando queremos tratar de assuntos como enchentes, vazão, enxurradas e alagamentos, que, apesar de serem eventos que possuem como elemento causal a água da chuva, são termos e processos fluviais que resultam em efeitos distintos no meio ambiente. Para abordamos esse assunto, vamos adentrar a esfera de conhecimento da climatologia, que é a ciência que descreve, classifica e explica os padrões de comportamento da atmosfera em um longo período de tempo [\(AYOADE,](#page-120-3) [1996\)](#page-120-3).

A chuva, por definição, "é uma precipitação líquida: água caindo do céu. As gotas de chuva caem na Terra quando as nuvens se tornam saturadas , ou cheias, de gotículas de água"[\(RUTLEDGE](#page-127-5) *et al.*, [2011\)](#page-127-5). Essa saturação se dá por meio do processo de condensação da água, formando as nuvens, de modo que quanto mais essas partículas de água colidem e se ligam umas às outras ficam mais pesadas e, por consequência, não sustentam o processo de flutuação na nuvem e resultando na queda ao chão [\(MENDONCA; OLIVEIRA,](#page-126-3) [2007\)](#page-126-3). Na [Figura 2](#page-35-0) é possível ver o esquemático do processo completo do ciclo hidrológico da chuva, evidenciando as fases terrestres e atmosféricascque pode ser descrito da seguinte maneira: Precipitação: A água na atmosfera condensa-se e precipita na forma de chuva, neve ou granizo, caindo sobre a superfície terrestre. Infiltração: Parte da água da precipitação infiltra-se no solo, movendo-se verticalmente para baixo e entrando na zona de aeração e posteriormente na zona de saturação, onde pode contribuir para os lençóis freáticos. Escoamento Superficial: A água que não se infiltra no solo pode escoar sobre a superfície, movendo-se em direção a rios, lagos e outros corpos d'água. Interceptação: Antes de atingir o solo, a precipitação pode ser interceptada pela vegetação e outras superfícies, onde pode evaporar diretamente de volta para a atmosfera. Evaporação e Transpiração: Na evaporação direta a água na superfície de corpos d'água (rios, lagos) e solo retorna à atmosfera na forma de vapor. E na transpiração as

plantas absorvem a água do solo e a liberam na atmosfera através de seus processos biológicos. Escoamento Subsuperficial e Subterrâneo: Parte da água que infiltra no solo pode mover-se horizontalmente como escoamento subsuperficial ou subsuperficial, alimentando rios e corpos d'água subterrâneos. Capilaridade e Percolação: A água pode se mover por capilaridade, subindo através de pequenos poros no solo, e por percolação, movendo-se mais profundamente para camadas subterrâneas. Rio: A água que se acumula nos rios pode seguir seu curso natural, retornando eventualmente ao oceano, onde o ciclo reinicia com a evaporação da água do mar. Condensação: No final do ciclo, o vapor de água na atmosfera condensa-se, formando nuvens e reiniciando o processo de precipitação.

<span id="page-35-0"></span>Figura 2 – Ciclo hidrológico. Reproduzido de [Telles](#page-128-0) [\(2018\)](#page-128-0)

É comum, quando citamos fenômenos hidrológicos, termos como enchentes, alagamentos, enxurradas e inundações se confundirem. Cada um desses eventos possui uma característica específica, com efeitos diversos no ambiente [\(LICCO; DOWELL,](#page-125-0) [2015\)](#page-125-0). Para ilustrar esses conceitos, tem-se a [Figura 3.](#page-36-0)

As enchentes ou cheias são caracterizadas pela temporária elevação do nível d'água devido o aumento da vazão, mas continuando dentro dos limites de leito menor sem haver o transbordamento. Já as inundações caracterizam-se pelo volume de transbordamento no canal de drenagem, ou seja, atingindo os perímetros da margem para além do leito maior. Nas inundações, é possível observar um aspecto dominante que são as águas concentradas em locais impermeabilizados como ruas e bairros de modo a acumular por não ter havido capacidade e velocidade na drenagem. Já nos alagamentos, o processo de acúmulo de água é de modo mais pontual, evento que é resultante do empoçamento de águas em locais que possuem deficiência de drenagem. Normalmente, podem ser vistos depois de uma forte chuva e alguns pontos da rua, que ficam com um quantidade significativa de água que não conseguiu seguir o fluxo de drenagem. Não menos importante, tem-se a ocorrência de enxurradas, resultado de um grande volume de água com força e velocidade, podendo produzir o arrastamento de objetos e detritos [\(COSTA;](#page-122-4) [MIYAZAKI,](#page-122-4) [2016\)](#page-122-4).

Considerando todos os fenômenos apresentados, um deles toma o protagonismo de

<span id="page-36-0"></span>Figura 3 – Exemplificação dos Níveis do aumento pluviométrico e suas classificações. Adaptado de [Licco](#page-125-0) [e Dowell](#page-125-0) [\(2015\)](#page-125-0).

ocorrência nas cidades brasileiras: as enchentes, provocando um índice de 70 desastres entre 2000 e 2019. O Brasil está no grupo dos países que mais sofrem com desastres climáticos, afetando um total de 70 milhões de pessoas [\(Estados Unidos da America,](#page-123-3) [2020\)](#page-123-3).

As enchentes, resultantes das chuvas, ocorrem tanto nas regiões ribeirinhas quanto no perímetro urbano, trazendo riscos significativos quando afetam áreas humanas [\(OLIVEIRA,](#page-126-4) [2016\)](#page-126-4). O crescimento urbano desordenado e horizontal impede a realização de planejamentos adequados para o escoamento pluvial, exacerbando os efeitos naturais das enchentes [\(DALAG-](#page-122-5)[NOL](#page-122-5) *et al.*, [2021\)](#page-122-5). Em determinados períodos do ano, é comum ver no noticiário imagens de enchentes acompanhadas de enxurradas, que causam mortes na escala das centenas e prejuízos financeiros na escala dos milhares, como o exemplo da [Figura 4.](#page-36-1) Esses eventos, embora naturais, têm seus efeitos agravados no meio urbano pela impermeabilização dos solos através de telhados, ruas, calçadas e o engessamento de córregos. Essa configuração dificulta o escoamento da água da chuva nas vias da cidade, obstruindo seu fluxo e resultando em danos como carros danificados e lojas alagadas, entre outros estragos [\(SHIMABUKU,](#page-127-6) [2017\)](#page-127-6).

<span id="page-36-1"></span>Figura 4 – Registro jornalistico de Enchente em São Carlos. [CNN](#page-122-0) [\(2020\)](#page-122-0).

Recursos e estratégias tem sido aplicados na expectativa de minimizar os efeitos colaterais das enchentes, como sistemas de alerta para os grandes volumes de chuva, drenos urbanos modernos, construções com calçadas mais altas e colaboração de campanha para redução de lixos nas ruas. Porém, ainda com essas iniciativas, os episódios de enchentes continuam frequente, causando danos à população [\(CARRIZOSA](#page-121-6) *et al.*, [2019\)](#page-121-6).

Em contrapartida aos índices ainda elevados, mesmo com as medidas já citadas, a tecnologia tem sido uma feliz aliada na solução dessas demandas [\(BRAGAGNOLO; SILVA;](#page-121-7) [GRZYBOWSKI,](#page-121-7) [2018\)](#page-121-7), como é o caso do aprendizado de máquina. Quando ocorrem eventos como enchentes, furacões ou terremotos, as estações de acompanhamento climático captam os dados gerados durante o acontecimento como a frequência de ocorrência, o volume de chuva, a data e a hora. Esses dados podem ser bem trabalhados através da analise por métodos estatísticos.

O ML, que é um caso particular da inteligência artificial [\(RUSSELL; NORVIG,](#page-127-0) [2013\)](#page-127-0), atua exatamente nessa manipulação de dados. É uma ferramenta que tem aberto portas quando o tema é ensinar as máquinas a partir de dados e criar soluções para problemáticas como essas, além de produzir informações que auxiliem a comunidade a se preparar para as condições de tempo extremas. Assim sendo, algoritmos de ML têm auxiliado na elaboração de modelos climáticos para tarefas como previsões de tempestades, além de sistemas de alarmes ao alcance dos *smartphones* [\(UEHARA](#page-128-9) *et al.*, [2020\)](#page-128-9).

### <span id="page-37-0"></span>**2.3 Séries Temporais**

O estudo de fenômenos e eventos levam a dados que refletem tendências e ocorrências de periodicidade e aperiodicidades (aleatoriedades), sejam por estações do ano, sazonalidade, movimentos mercadológicos ou comportamentos naturais como subida de marés, períodos de chuvas ou seca, que registrados ao longo de um período no tempo representam uma série de dados históricos. Os dados observados e coletados que constituem as séries históricas de uma determinada amostra pode ser chamada de "Série Temporal", vale ressaltar a importância de considerar cuidadosamente a resolução espaço-temporal ao definir as janelas temporais para a coleta e análise de dados em séries temporais. Isso garante que a análise capture adequadamente as variações e tendências do fenômeno estudado, podendo afirmar que:

> Uma série temporal é qualquer conjunto de observações ordenados no tempo como: (i) valores diários de poluição na cidade de são paulo; (ii) valores mensais de temperatura na cidade de Cananéia-SP; (iii) índices diários da bolsa de valores de São Paulo; (iv) precipitação atmosférica anual na cidade de Fortaleza; (v) número médio anual de manchas solares; (vi) registro de marés no porto de Santos.[\(MORETTIN; TOLOI,](#page-126-5) [2006\)](#page-126-5)

A [Figura 5](#page-38-0) a seguir apresenta alguns exemplos gráficos do comportamento de séries temporais mencionados anteriormente. De acordo com a literatura, basicamente uma série temporal é obtida através de uma amostragem de dados contínuos como a subida das marés ou discretos como valores mensais das chuvas [\(SUSTO; CENEDESE; TERZI,](#page-128-10) [2018\)](#page-128-10). Não necessariamente, mas, usualmente, uma série temporal discreta é resultado de uma série temporal contínua a qual foi decomposta em intervalos de tempo. Para a análise de séries temporais na qual tem-se o objetivo de construção de modelos para previsão, podem ser tomados dois caminhos: o de domínio temporal e o de domínio da frequência [\(WANG](#page-129-4) *et al.*, [2022\)](#page-129-4). Os modelos de previsão no domínio temporal são do tipo paramétricos, ou seja, possuem um número finito de parâmetros, e os modelos de previsão no domínio da frequência são do tipo não parametrizados (número infinito de parâmetros), isso quer dizer que a série é decomposta em uma faixa de espectro [\(COWPERTWAIT; METCALFE,](#page-122-6) [2009;](#page-122-6) [MORETTIN; TOLOI,](#page-126-5) [2006\)](#page-126-5).

<span id="page-38-0"></span>Figura 5 – Exemplos de séries temporais (a) Totais mensais de passageiros em linhas aéreas internacionais nos EUA entre 1949 e 1960, (b) número anual de linces capturados em armadilhas entre 1821 e 1934 no Canadá, (c) medições anuais de vazões do Rio Nilo em Ashwan entre 1871 e 1970, (d) consumo de gás no Reino Unido entre o primeiro trimestre de 1960 e o quarto trimestre de 1986. Adaptado de [\(EHLERS,](#page-122-1) [2005\)](#page-122-1).

Ao trabalhar com séries temporais é importante conhecer os modelos probabilísticos, que podem ser ditos estocásticos, o que por definição compreende "uma coleção de variáveis aleatórias ordenadas no tempo e definidas em um conjunto de pontos, que pode ser contínuo ou discreto"[\(EHLERS,](#page-122-1) [2005\)](#page-122-1). Isto posto, tais modelos podem ser do tipo estacionários e nãoestacionários, no qual segundo [\(KLEINSCHMIDT,](#page-124-3) [2019\)](#page-124-3) para ser estacionário "não deve apresentar tendência e tanto sua variação quanto o padrão dessa variação devem ser constantes no tempo". De maneira contrária, pode-se definir como não-estacionário séries que apresentam uma tendência nos dados ou uma sazonalidade de comportamento, ou seja, a sua variação e o padrão de variação devem ser constantes no tempo [\(KLEINSCHMIDT,](#page-124-3) [2019;](#page-124-3) [BROCKWELL;](#page-121-8) [DAVIS,](#page-121-8) [2002\)](#page-121-8).

Dentro dos conceitos mais tradicionais aplicados à predição de séries temporais, os modelos ARIMA *(Auto-Regressive Integrated Moving Average model)* [\(BOX; PIERCE,](#page-121-9) [1970\)](#page-121-9) são comumente empregados. Tal teoria é utilizada partindo-se da premissa de que a série é gerada por um processo estocástico e pode ser descrita por um modelo. Os termos p,d e q utilizados para descrição dos modelos referem-se, respectivamente, ao número de parâmetros

autoregressivos, número de diferenciações para que a série torne-se estacionária e ao número de parâmetros de médias móveis (MA) [\(MUMA,](#page-126-6) [2022\)](#page-126-6). Os modelos ARIMA podem representar três classes de modelos, sendo elas processos lineares estacionários, processos lineares nãoestacionários homogêneos e processos de memória longa. Para séries temporais representadas por modelos lineares estacionárias, ou seja, d = 0, tem-se os casos especiais, como modelos autoregressivos (AR, p) , modelo de médias móveis (q) e modelos autoregressivos e de médias móveis ARMA(p,q) [\(BOX; JENKINS,](#page-121-10) [1976\)](#page-121-10).

### <span id="page-39-0"></span>**2.3.1 Autoregressivos - AR**

Na literatura, como apresenta [Morettin e Toloi](#page-126-5) [\(2006\)](#page-126-5), o modelo de predição classificado como autoregressivo - AR possui essa denominação devido à sua característica de estimar os valores da série temporal com base em dois fatores: a média ponderada dos pontos de dados históricos e também através da média móvel. Ou seja, "utiliza a própria variável alvo para projetá-la a partir da variável no passado"[\(PINHEIRO,](#page-126-7) [2021\)](#page-126-7). Segundo [Xavier](#page-129-5) [\(2017\)](#page-129-5), o modelo AR(1) com *p = 1* assume que a série temporal *X<sup>t</sup>* é definida por:

$$X\_t = \Phi\_1 X\_{t-1} + a\_t \tag{2.1}$$

onde:

Φ<sup>1</sup> é o parâmetro autoregressivo de ordem 1, *Xt*−*<sup>1</sup>* é a série de tempo defasada de um período e *a<sup>t</sup>* é o termo do erro do modelo.

Generalizando e considerando *X<sup>t</sup>* ,*t* ∈ Z, pode-se afirmar que se trata de um modelo autoregressivo de ordem *p* se:

$$X\_t = \Phi\_0 + \Phi\_1 X\_{t-1} + \dots + \Phi\_p X\_{t-p} + a\_l \tag{2.2}$$

sendo Φ0,Φ1,...,Φ*<sup>p</sup>* os parâmetros reais.

### <span id="page-39-1"></span>**2.3.2 Modelos de erro ou regressão**

[Morettin e Toloi](#page-126-5) [\(2006\)](#page-126-5) define os modelos de erro ou regressão como:

O Sinal (f) é uma função do tempo completamente determinada (parte sistemática ou determinística) e *a<sup>t</sup>* é uma sequência aleatória, independente de f(t). Além disso, supõe-se que as variáveis *a<sup>t</sup>* sejam não correlacionadas, tenham média zero e variância constante [\(MORETTIN; TOLOI,](#page-126-5) [2006\)](#page-126-5).

No qual,

$$E(X\_t) = 0, \forall t, \quad E(X\_t) = \Phi\_0 + \Phi\_1 X\_{t-1} + \dots + \Phi\_p X\_{t-p} + a\_t \tag{2.3}$$

Isto posto, observa-se que para qualquer feito do tempo haverá influência apenas na parte determinística de f(t) e para os modelos nos quais Z(t) estiver em função de X(t), essa suposição não se aplica.

### <span id="page-40-0"></span>**2.3.3 Modelos de média móvel (MA)**

Para os modelos de MA, [Morettin e Toloi](#page-126-5) [\(2006\)](#page-126-5) define que ao se considerar um processo de ordem q, tem-se que:

$$X\_t = a\_t - \theta\_1 a\_{t-1} - \theta\_2 a\_{t-2} - \dots - \theta\_q a\_{t-q} + \varepsilon\_t \tag{2.4}$$

onde ε*<sup>t</sup>* descreve os erros que não podem ser explicados pelo modelo, enquanto *a<sup>t</sup>* são as ordens do modelo.

### <span id="page-40-1"></span>**2.3.4 Modelos autorregressivos e de médias móveis (ARMA)**

Segundo [Hassan](#page-124-4) [\(2014\)](#page-124-4), os modelos autoregressivos e de MA ou ARMA são a combinação de valores anteriores de X(t) e os erros passados, considerando as ordens p, q que geram a combinação conhecida como ARMA(p, q). A equação geral para ARMA(p, q) para uma série temporal pode ser descrita como:

$$X\_t = \mathfrak{sp}X\_{t-1} + \mathfrak{sp}X\_{t-2} + \dots + \mathfrak{sp}X\_{t-p} + a\_t - \theta\_1 a\_{t-1} - \theta\_2 a\_{t-2} - \dots - \theta\_q a\_{t-q} \tag{2.5}$$

no qual ϕ1,ϕ2,...,ϕ*<sup>p</sup>* e θ1,θ2,...,θ*<sup>q</sup>* são respectivamente coeficientes autoregressivos e de média móvel desconhecidos, e *a<sup>t</sup>* ,*at*−*1*,...,*at*−*<sup>q</sup>* são coeficientes aleatórios estatisticamente independentes que são assumidos para serem selecionados aleatoriamente a partir de uma distribuição normal com média zero e variância constante.

### <span id="page-40-2"></span>**2.3.5 Modelos autorregressivos Integrados médias móveis (ARIMA)**

De acordo com a literatura, os modelos ARIMA estão baseados nas autocorrelações dos dados, sendo uma combinação dos modelos anteriores já vistos, o modelo de média móvel (MA) e o modelo autoregressivo (AR). O que os diferencia dos modelos ARMA é a necessidade de

transformá-los em estacionários. Para processos lineares estacionários, podemos representar da seguinte maneira:

$$X\_t - \mu = a\_t + \Psi\_1 a\_{t-1} + \Psi\_2 a\_{t-2} + \dots = \sum\_{k=0}^{\infty} \Psi\_k a\_{t-k}, \quad \Psi\_0 = 1 \tag{2.6}$$

sendo *a<sup>t</sup>* ruído branco, µ = *E*(*Xt*) e ψ1,ψ*<sup>2</sup>* uma sequência de parâmetros tal que:

$$\sum\_{k=0}^{\infty} \Psi\_k^2 < \infty \tag{2.7}$$

### <span id="page-41-0"></span>**2.4 Inteligência Artificial**

A IA nasceu nos anos 50 sob a influência de matemáticos do século XVII e XIX, atrelado a conhecimentos da lógica que também estão entre nós há séculos [\(POZZEBON;](#page-127-7) [FRIGO; BITTENCOURT,](#page-127-7) [2004\)](#page-127-7). A IA teve inicio em meados de 1952, com avanços logo após a segunda guerra mundial, através de grandes nomes da ciência, como Alan turing, Nathaniel Rochester e Herbert Gelernter. Esses autores apresentaram os primeiros projetos de programa para demonstração de teoremas ou jogos que aprendiam a jogar e elevar o nível [\(RUSSELL;](#page-127-0) [NORVIG,](#page-127-0) [2013\)](#page-127-0).

[Rosa](#page-127-8) [\(2011\)](#page-127-8) apresenta os conceitos que integram os fundamentos da inteligência artificial do ponto de vista da ciência cognitiva, que contribui na estrutura do que se vê na área.

- ∙ Psicologia: busca tratar as representações do comportamento mental, no que diz respeito a interações, percepções, aprendizado modo de memorização e o efeito dessas relações, no comportamento e no controle.
- ∙ Linguística: considerando os elementos que comunicam e que construímos uma ideia ou um pensamento a partir disso, qual a ligação do humano com o universo e os objetos que ele nomeia ? que trajetória dessa informação faz e cria os conceitos do ambiente como o conhecemos?
- ∙ Filosofia: qual o envolvimento da nossa percepção de mundo com o raciocínio lógico?
- ∙ Ciência da Computação: como construir e quais as possibilidades de modelos computacionais a partir do que temos no meio ambiente?

São nesses princípios apresentados que a IA busca fundamentar a sua artificialidade. O potencial de repetibilidade e reprodutibilidade de elementos caracterizados como humanos é o que torna cada vez mais palpável a criação de sistemas inteligentes e das máquinas autônomas na atualidade [\(FRANCO,](#page-123-4) [2017\)](#page-123-4). Dentro do campo da IA, têm-se derivações da sua abordagem conforme a aplicação em questão. São elas simbólica, conexionista e evolutiva. É correto informar que um determinado sistema vai integrar duas ou mais destas abordagens para a resolução de um problema, resultando em sistemas híbridos que exploram de maneira pontual as vantagens de cada tipo de abordagem [\(MEDEIROS,](#page-126-8) [2004\)](#page-126-8).

Segundo [Medeiros](#page-126-8) [\(2004\)](#page-126-8), as diferentes abordagens refletem as técnicas disponíveis atualmente, como algoritmos genéticos, programação evolutiva, estratégias evolutivas, sistemas classificadores e programação genética. Considerando o intuito do trabalho apresentado nesta monografia, que é a classificação ou regressão de enchentes utilizando redes neurais convolucionais, utiliza-se um ramo fundamental para a concepção da IA: as redes neurais artificiais, em que modelos de ML foram desenvolvidos baseados na neurociência. Mais recentemente, os desenvolvimentos nessa área estruturaram o que conhecemos como DL [\(GOODFELLOW;](#page-123-5) [BENGIO; COURVILLE,](#page-123-5) [2016\)](#page-123-5).

### <span id="page-42-0"></span>**2.4.1 Aprendizado de Máquina**

Avanços significativos no campo da IA e nas soluções de problemas de classificação e regressão foram possíveis com as ferramentas de ML. Esta tecnologia capacita as máquinas e computadores, por meio de associação e de algoritmos autônomos, a aprender com entradas de informações em diversos tipos de formatos, sejam dados estruturados, imagens, textos, entre outros. As possibilidades advindas do desenvolvimento do ML revolucionaram os serviços e pesquisas desta área, além do potencial de valor tais algoritmos puderam agregar a outras tecnologias, como a visão computacional. Uma definição formal que podemos ter do ML é segundo [Micthell](#page-126-9) [\(1997\)](#page-126-9): "diz-se que um programa de computador aprende a partir da experiência em relação a uma classe de tarefas T e medida de desempenho P, se seu desempenho nas tarefas em T, conforme medido por P, resultar em uma melhora com a experiência E". Ainda tratando das definições de ML, segundo [Yao e Liu](#page-129-6) [\(2014\)](#page-129-6):

> O ML é um subcampo muito ativo da inteligência artificial voltado para o desenvolvimento de modelos computacionais de aprendizado. O ML é inspirado no trabalho em várias disciplinas: ciências cognitivas, ciência da computação, estatística, complexidade computacional, teoria da informação, teoria do controle, filosofia e biologia. Simplificando, o ML é o aprendizado por máquina. Do ponto de vista computacional, o ML se refere à capacidade de uma máquina de melhorar seu desempenho com base em resultados anteriores [\(YAO; LIU,](#page-129-6) [2014\)](#page-129-6).

Porém, não se trata de um aliado que esteve inerte. Durante todo o desenvolvimento das tecnologias, o ML vem atuando nos métodos estatísticos, no tratamento de dados e nos diversos processos que levam ao debate de como construir programas de computadores que melhoram automaticamente com a experiência.

### <span id="page-43-1"></span>**2.4.2 Redes Neurais Artificiais**

A inteligencia artificial como a conhecemos não seria possível sem a ótica da neurociência. Os estudos que tiveram como inspiração biológica as redes neurais iniciaram-se em 1943, com o trabalho de McCullock, um psiquiatra neuro-anatomista, e Pitts, um matemático. Ambos tinham como objetivo representar os eventos do sistema nervoso. Desse modo, poderiam criar redes lógicas de neurônios e novas máquinas de estados infinitos [\(RUSSELL; NORVIG,](#page-127-0) [2013\)](#page-127-0). A [Figura 6](#page-43-0) ilustra um neurônio anatômico que serviu como modelo para a estrutura algorítmica de uma rede neural como conhecemos hoje. As redes neurais são estruturas que possuem as funções de propriedade de aprendizagem, generalização, agrupamento e organização de dados.

<span id="page-43-0"></span>Figura 6 – Modelo biológico de um neurônio. Reproduzido de [Russell e Norvig](#page-127-0) [\(2013\)](#page-127-0).

O papel da Rede Neural Artificial - RNA em um projeto de IA é simular algumas estruturas do cérebro humano. Em uma RNA, as unidades de processamento estão para os neurônicos assim como as conexões estão para as sinapses.

### <span id="page-43-2"></span>2.4.2.1 Características Gerais das Redes Neurais

Os percussores das redes neurais McCullock e Pitts determinaram que, em uma rede neural artificial, o comportamento inteligente se dá através da troca de informação entre suas unidades de processamento. Uma unidade de processamento é composta por um numero prédeterminado de neurônios, que por um processo de correlação de pesos e conexões atrelados a uma função de ativação resulta no esquema da [Figura 7](#page-44-0) [\(ICMC USP,](#page-124-5) [2009\)](#page-124-5).

É possível observar a estrutura de algoritmo de modo detalhado na [Figura 8,](#page-44-1) que indica a função de cada elemento artificial correspondente ao modelo biológico do neurônio. Cada valor da entrada X1 a Xn na [Figura 7](#page-44-0) (dentritos) será em sua etapa seguinte multiplicado pelo peso Wx (sinapses). Os pesos possuem duas possibilidades de efeito na rede neural: excitação ou inibição. Esses efeitos resultarão, respectivamente, na estimulação da ação do neurônio ou na sua inibição. O produto dessa relação de valores de entrada e dos pesos da rede influencia diretamente no

<span id="page-44-0"></span>Figura 7 – Esquema de uma unidade de Rede Neural Artificial.

<span id="page-44-1"></span>resultado da rede neural. Por conseguinte, é feita então a soma ponderada dos pesos e o valor é processado por uma função de ativação.

Figura 8 – Esquema exemplo de uma unidade de RNA. Reproduzido de [Osorio e Bittencourt](#page-126-0) [\(2000\)](#page-126-0).

As estruturas das RNAs são organizadas em camadas. Uma arquitetura clássica de rede neural totalmente conectada é a (*Multilayer Perceptron* - MLP) , a qual é um tipo específico de rede *feed-forward* que é sempre totalmente conectada podendo contar com três camadas, sendo uma camada de entrada e duas intermediárias. Ainda há configurações que utilizam apenas duas camadas, uma de entrada e uma camada oculta, de neurônios. Porém, só o que irá determinar a necessidade de camadas e números de neurônios será em relação a qualidade de reposta esperada.

### <span id="page-45-2"></span>**2.4.3 Metodologia para o Desenvolvimento de Aplicações de IA**

<span id="page-45-0"></span>Dando ênfase à busca por uma solução que envolva soluções inteligentes, cunhadas nos aspectos fundamentas da IA, raciocínio, aprendizagem e os demais fundamentos, pode-se começar um projeto a partir do entendimento do esquema apresentado na [Figura 9.](#page-45-0)

Figura 9 – Metodologia de exemplo para as etapas de um projeto de IA. Adaptado de [Fagundes](#page-123-0) [\(2021\)](#page-123-0).

A inteligencia artificial é fundamentada na matemática e na lógica. Para implementar projetos que possuam como instrumento tecnológico e inteligente a IA, é preciso envolver bem mais do que foi visto até aqui. Como todo bom sistema, que opera de modo organizado e possui seus escalonamentos, a concepção de IA é possível através de duas grandes subáreas, o aprendizado de máquina e o *deep learning* (as redes neurais profundas). Essas duas áreas de estudos se responsabilizam pela matéria, o corpo que hospeda a alma da inteligência artificial nos dias atuais. A [Figura 10](#page-45-1) apresenta uma visão global de como esses temas se suportam e se conectam.

<span id="page-45-1"></span>Figura 10 – Relação entre Inteligência Artificial (IA), Machine Learning (ML) e Deep Learning (DL) em forma de um diagrama de Venn. Adaptado de [Saraiva](#page-127-1) [\(2018\)](#page-127-1).

Conhecer o que cada esfera dessa oferece de recurso é fundamental. Com o enriquecimento e aperfeiçoamento da pesquisa nessas áreas de atuação, a depender da linha de pesquisa e da problemática envolvida, essas ferramentas isoladas solucionam muito bem um problema. Assim, combinadas, podem resultar em criações inovadoras e sofisticadas.

Na [Figura 9,](#page-45-0) temos as fases e etapas de tomada de decisão que precisam ser consideradas na implementação de um projeto de inteligência artificial. A IA objetiva seu funcionamento na comunicação humano-máquina, e, para isso, tarefas como busca, associação e classificação já são muito bem representadas. Considere a seguinte situação hipotética: um produtor de tomates, costumeiramente, a depender do seu volume de colheita e das condições climáticas, pode obter uma safra de frutos de diferentes tamanhos e até mesmo de amadurecimento. Não apenas isso, mas também pode haver elementos intrusos dentro da colheita. Indo além da visão computacional, que possui boas soluções no campo da "inspeção", uma otimização no seu processo aplicando IA possibilitaria ao produtor conhecer diversos aspectos de sua produção, como "todos os elementos da colheita são tomates", classificar o ponto de amadurecimento do fruto, indicar a qualidade do fruto e até mesmo prever boas colheitas e o volume. O esquema na [Figura 11](#page-46-0) apresenta uma possível estrutura de diagrama de uma rede neural para esse exemplo.

<span id="page-46-0"></span>Figura 11 – Esquema de fluxo referente ao uso tanto de CNNs quanto de RNNs nos blocos de processamento. Implicando em uma arquitetura capaz de lidar com diferentes tipos de dados e tarefas, aproveitando a força das CNNs para dados espaciais (como imagens) e das RNNs para dados sequenciais (como texto ou séries temporais). .Adaptado [Kirichenko, Zinchenko e Radivilova](#page-124-0) [\(2021\)](#page-124-0).

## <span id="page-46-1"></span>**2.5 Modelos Recorrentes e Convolucionais de Redes Neurais**

A ciência tem como objetivo explicar, de modo cada vez mais preciso, o que acontece no mundo natural, contribuindo com conhecimentos que possibilitam explicação, compreensão e clareza dos elementos que constituem o todo [\(BERKELEY,](#page-121-2) [2007\)](#page-121-2). Desse modo, tem-se o crescente desenvolvimento de tecnologias inspiradas no "mundo natural"que alavancam, por exemplo, as contribuições de pesquisas que buscam reproduzir artificialmente as habilidades humanas em sistemas de software e hardware, criando tecnologias capazes de alcançar resultados muito além do possibilitado por nós humanos [\(PRADO,](#page-127-3) [2019\)](#page-127-3).

Ao citar métodos de previsão no campo da IA pode-se apresentar as redes neurais recorrentes e as redes neurais convolucionais como abordagem para esse fim de previsão.

### <span id="page-47-1"></span>**2.5.1 Rede Neural Recorrente - RNN**

As RNNs atuam com dados sequenciais, o que é uma característica particular quando comparamos com o modo de funcionamento de um rede neural tradicional, as quais, tem seu dado de entrada de modo não sequencial. Esse modo de atuação, no qual o resultado atual depende do processamento do resultado anterior, dão as RNN's preferência de aplicação quando o problema envolve dados sequenciais como series temporais [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0). Além dessa particularidade no tipo de dados de entrada a qual a RNN utiliza, outra característica de seu funcionamento é a capacidade de antecipação e previsão a partir da analise de dados, onde pode-se obter a previsão de um processo, por exemplo antecipando dados na compra e venda de ações, antecipar trajetórias de carros e outros elementos desse gênero [\(GOODFELLOW;](#page-123-6) [BENGIO; COURVILLE,](#page-123-6) [2017\)](#page-123-6).

Na estrutura da rede neural recorrente os itens presentes são os laços de repetição *(loops)*,os quais são responsáveis pela função de persistência da informação, no qual um nó S na rede tem uma entrada *Xt* e uma saída *ht*, isso corresponde a um *timestep t* [\(RANIERI,](#page-127-2) [2018\)](#page-127-2). O *loop*, se encarrega de transferir a informação para o próximo estagio da rede a Figura [12](#page-47-0) apresenta as estruturas da rede.

<span id="page-47-0"></span>Figura 12 – Estrutura de um neurônio na imagem a) e estrutura de neurônios no decorrer do tempo na imagem b).Adaptado [Ranieri](#page-127-2) [\(2018\)](#page-127-2).

A equação que representa a saída de uma rede neural recorrente pode ser vista a seguir.

$$h\_l = W^TX\_l + b = \sum\_{i=1}^{N} W\_i X\_{l,i} + b \tag{2.8}$$

A partir da estrutura principal de uma RNN, derivaram-se muitas outras variantes, como a *Long Short-Term Memory* (LSTM) . A LSTM aprimora certos aspectos, especialmente no que diz respeito às dependências temporais, permitindo analisar eventos em intervalos de tempo longos, como em séries temporais, enquanto considera os prazos prolongados de uma amostra. Outra variante importante é a *Gated Recurrent Unit* (GRU) , que é uma versão simplificada da LSTM. A GRU também visa resolver o problema dos gradientes em redes recorrentes tradicionais, permitindo que a rede capture dependências de longo prazo, mas sem a complexidade adicional das LSTMs.

### <span id="page-48-0"></span>**2.5.2 Rede Neural Convolucional - CNN**

A CNN apresenta uma abordagem do DL trabalhando com entradas do tipo imagem, e matematicamente falando entradas de matriz quadrada. As CNN's surgiram da observação do funcionamento do córtex visual do cérebro e foram largamente aplicadas no reconhecimento de imagens a partir dos anos 80. As aplicações das redes convolucionais são inúmeras no dia a dia social, como por exemplo a busca de imagens, carros autônomos devido o sistema de visão embarcado, além de sistemas de classificação de video e assim por diante. No que diz respeito a imagens e em camadas de DL tem-se uma aplicação convolucional, até mesmo em processamento de linguagem natural [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0).

Na CNN o bloco mais importante é a camada de convolução, no qual a convolução é uma operação matemática onde uma função passa sobre a outra e assim é medida a integral da multiplicação no ponto de passagem [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0). Como as imagens são de cunho bidimensional e compreendidas computacionalmente como matrizes, a convolução é dada pela [Equação 2.9,](#page-48-1) para um operador \* de convolução, uma entrada I, uma saída J e um filtro de convolução W [\(RANIERI,](#page-127-2) [2018\)](#page-127-2).

$$J(\mathbf{x}, \mathbf{y}) = W(\mathbf{x}, \mathbf{y}) \* I(\mathbf{x}, \mathbf{y}) = \sum\_{s=-a}^{a} \sum\_{t=-b}^{b} W(\mathbf{s}, t) I(\mathbf{x} - \mathbf{s}, \mathbf{y} - t) \tag{2.9}$$

<span id="page-48-1"></span>Para uma arquitetura própria convolucional, tem-se o empilhamento de algumas camadas convolucionais, normalmente após cada uma tem-se a função de ativação ReLU e depois uma camada *pooling*, e possivelmente algumas outras convolucionais seguidas de ReLU e depois uma de *pooling* e por conseguinte de modo intercalado. Esse processo onde a imagem avança pelas camadas da rede tem por objetivo gerar uma invariância da posição do filtro o que resulta numa saída da imagem com dimensão reduzida, a Figura [13](#page-49-0) mostra a arquitetura da rede.

<span id="page-49-0"></span><span id="page-49-1"></span>Figura 13 – Exemplo de arquitetura CNN. Adaptado de [Aurelien](#page-120-0) [\(2019\)](#page-120-0).

Figura 14 – Estrutura de camadas de uma rede CNN do tipo de campos repetitivos retangulares. Adaptado de [Aurelien](#page-120-0) [\(2019\)](#page-120-0).

O funcionamento da CNN está diretamente relacionado a capacidade de identificar características de baixo nível logo na primeira camada oculta da rede como da Figura [14,](#page-49-1) de modo que a cada nova camada transforme essas características em níveis superiores reunindo as informações e característica da imagem a cada próxima camada oculta [\(RANIERI,](#page-127-2) [2018\)](#page-127-2). Esse mecanismo é comum em estruturas ordenadas no mundo real, o que torna a CNN bem sucedida e indicada no trabalho com imagens [\(AURELIEN,](#page-120-0) [2019\)](#page-120-0).

### <span id="page-49-2"></span>**2.6 Recurrence Plot**

Nas últimas décadas, a busca pelo entendimento do funcionamento de recorrência de séries temporais vêm sendo utilizados em diferentes áreas como ferramenta para auxílio no entendimento de propriedades fundamentos de sistemas dinâmicos [\(MARWAN,](#page-126-10) [2008;](#page-126-10) HE *[et al.](#page-124-6)*, [2023;](#page-124-6) [SALES](#page-127-9) *et al.*, [2023;](#page-127-9) [AMOR](#page-120-4) *et al.*, [2024\)](#page-120-4). No entanto, estudos de recorrência remotam desde a antiguidade como uma tentativa de descrever a reincidência de fenômenos naturais e sociais, mas somente com o avanço do estudo computacional de sistemas dinâmicos que surgiu o termo atualmente conhecido como gráficos de recorrência (Recurrence Plot - RP), introduzido por [Eckmann, Kamphorst e Ruelle](#page-122-7) [\(1987\)](#page-122-7). Os autores apresentaram uma nova ferramenta gráfica para medir a constância temporal de sistemas dinâmicos por meio de uma análise de todas as condições possíveis representadas por uma trajetória no espaço e, quando a trajetória atingir uma área do espaço já visitada anteriormente, é identificado recorrência. Desta forma, uma recorrência indica que o estado atual de alguma maneira assemelha-se a um estado passado

[\(ECKMANN; KAMPHORST; RUELLE,](#page-122-7) [1987\)](#page-122-7). Os RP surgem então como uma ferramenta para explicar a correlação de um sinal num plano tempo-tempo.

Um gráfico de recorrência é descrito como uma matriz gráfica binária de tamanho *N* ×*N*, sendo *N* a quantidade de instantes que compõe a série temporal. Nesta matriz, um ponto de recorrência *Rij* será igual a 1 quando *x<sup>i</sup>* e *x<sup>j</sup>* estiverem na mesma vizinhança e, caso contrário, receberá o valor de 0 [\(MARWAN](#page-126-2) *et al.*, [2007;](#page-126-2) [YANG; REN; HU,](#page-129-7) [2021\)](#page-129-7). Nesta matriz gráfica, os valores 1 são representados por pontos pretos e os valores nulos por espaços em branco. O conceito de vizinhança é adotado uma vez que em sistemas dinâmicos, apesar de as trajetórias retornarem infinitas vezes próximas a quase todos os pontos iniciais de forma arbitrária, ela não recorre exatamente ao estado inicial [\(GOSWAMI,](#page-123-7) [2019\)](#page-123-7). A ideia de vizinhança em um espaço m-dimensional está expressa na Figura [15](#page-50-0) [\(GRANEMMAN,](#page-123-8) [2008\)](#page-123-8). A Figura [16](#page-51-0) representa um modelo de construção de um gráfico de recorrência a partir de uma série de *N* = 10, sendo {570, 571, 571, 568, 568, 569, 571, 571, 570 e 567}, estabelecendo uma vizinhança com dimensão 1 e raio 1 para uma matriz gráfica de 10×10 [\(BATISTA,](#page-120-5) [2011\)](#page-120-5).

<span id="page-50-0"></span>Figura 15 – Indicação de uma recorrência I em uma trajetória arbitrária em um espaço bi-dimensional. Fonte – [\(GRANEMMAN,](#page-123-8) [2008\)](#page-123-8)

A matriz permite visualizar a maneira com que os dados se comportam na série temporal com relação à recorrência. Diversos padrões podem ser gerados, representando comportamentos típicos de recorrência de sistemas em pequena e larga escala [\(GAO; CAI,](#page-123-9) [2000;](#page-123-9) [THIEL;](#page-128-11) [ROMANO; KURTHS,](#page-128-11) [2004\)](#page-128-11). Em pequena escala (baixo alcance, também chamado de textura) tem-se as representações que irão construir a matriz, podendo ser construída de padrões por pontos - que representam os estados de recorrência; linhas diagonais - que indicam que uma parte da trajetória apresenta uma evolução similar à outro segmento em tempos diferentes, cujo comprimento dita a duração da evolução; linhas verticais e horizontais - que representam um estado estacionário; formas geométricas repetidas - representam ciclicidade no processo. Uma linha diagonal principal é comumente presente nos gráficos de recorrência, uma vez que um

<span id="page-51-0"></span>Figura 16 – Exemplo de construção de um gráfico de recorrência 10x10 com dimensão 1 e raio 1.

Fonte – Próprio autor, adaptado de [Batista](#page-120-5) [\(2011\)](#page-120-5)

estado sempre recorre consigo mesmo [\(MARWAN,](#page-125-4) [2003;](#page-125-4) [BATISTA,](#page-120-5) [2011\)](#page-120-5). Quando esses elementos se combinam para descrever a trajetória surgem os padrões em larga escala, também chamados de tipologias, dos quais podem-se citar os padrões homogêneo, periódico, *drift* e descontinuado. A Figura [17](#page-51-1) ilustra os diferentes padrões em larga escala, conforme [Marwan](#page-125-4) [\(2003\)](#page-125-4).

<span id="page-51-1"></span>Figura 17 – Tipologias características dos gráficos de recorrência, sendo que (A) descreve um comportamento homogêneo, (B) periódico, (C) drift (deriva, ruídos) e (D) descontinuado.

#### Fonte – [\(MARWAN,](#page-125-4) [2003\)](#page-125-4)

Apesar de os gráficos de recorrência permitirem visualizar padrões de repetição não facilmente obtidos por outras técnicas, a sua interpretação visual depende de uma grande adaptação humana para observar pequenas variações de contraste. Para mitigar este risco, análises quantitativas são empregadas para extrair as informações estatísticas referentes aos dados avaliados. No caso do presente trabalho, o resultado obtido com os gráficos de recorrência não serão

meramente utilizados para tratamentos estatísticos de classificação e sim como alimentação a uma CNN para fins de melhoria da eficácia nos modelos de previsão.

### <span id="page-52-0"></span>**2.7 Considerações Finais**

Neste capítulo, foram apresentados os conceitos utilizados como base para o desenvolvimento do projeto. Situou-se sobre o aspecto geral dos extremos climáticos relacionados à precipitação, se tratando de suas relações entre o homem e o ambiente e como isso está relacionado à nossa sociedade. No âmbito dos fenômenos hidrológicos e seus efeitos diversos, destaca-se o protagonismo das enchentes no Brasil. Trata-se de uma consequência indesejada para o meio ambiente, podendo ocasionar prejuízos para o sistema público ou até mesmo fatalidades. Atuando como uma aliada ao combate à esse e também outros tipos de efeitos danosos ao meio ambiente e sistema social, a tecnologia tem ganhado cada vez mais visibilidade. Mais especificamente, o ML e o desenvolvimento de métodos de previsão têm representado importantes recursos na busca pela diminuição dos efeitos colaterais causados por tais fenômenos. Foi apresentado como as RNN e CNN se constituem e podem ser trabalhadas nessa conjunção e, a seguir, serão apresentados na prática como essas ferramentas têm sido aplicadas em trabalhos relacionados à modelos de previsão dos fenômenos da natureza.

# CAPÍTULO 3

## <span id="page-54-0"></span>**TRABALHOS RELACIONADOS**

É notável o quanto prever os fenômenos da natureza é importante nos dias de hoje. O crescimento urbano e a apropriação de terras em áreas de natureza livre torna necessário prever variáveis que indiquem fenômenos como inundações, tornados, maremotos, entre tantas outras manifestações comuns da natureza que, ao encontrar as construções do homem, têm o poder de devastar. Com o advento da IA, uma variedade de oportunidades surgiu para abordar questões que anteriormente tinham escopo limitado [\(AURELIEN,](#page-120-0) [2019;](#page-120-0) [L'HEUREUX; GROLINGER;](#page-125-1) [CAPRETZ,](#page-125-1) [2017\)](#page-125-1). Esforços significativos têm sido feitos para aprimorar os métodos de previsão de fenômenos naturais. Diferentes modelos de previsão são estudados para obter resultados cada vez mais precisos e eficazes. As RNNs são frequentemente empregadas devido à sua capacidade de reter memória e aprender padrões que evoluem ao longo do tempo. Alguns algoritmos de memória aprimorada, como LSTM e GRU, também são usados na tentativa de superar os obstáculos das dependências de longo prazo [\(GUHA; JANA; SANYAL,](#page-123-10) [2022;](#page-123-10) [HOCHREITER;](#page-124-1) [SCHMIDHUBER,](#page-124-1) [1997\)](#page-124-1). Mais recentemente, modelos CNN também foram aplicados devido à sua capacidade de extração de características complexas [\(CHEN](#page-122-8) *et al.*, [2021\)](#page-122-8). Outra abordagem usada como alternativa para otimizar o desempenho das RNAs é a combinação de algoritmos, os chamados modelos híbridos [\(FENG; NIU,](#page-123-11) [2021;](#page-123-11) [FATHIAN](#page-123-12) *et al.*, [2019\)](#page-123-12). Este capítulo irá descrever e detalhar os trabalhos mais relevantes da área e suas principais contribuições e limitações.

### <span id="page-54-1"></span>**3.1 Modelos de Previsão com RNA**

Desastres naturais podem afetar desde um pequeno vilarejo até cidades urbanas bem desenvolvidas, como é o caso de estudo do trabalho de [Lima](#page-125-5) *et al.* [\(2016\)](#page-125-5), o qual analisa os impactos de inundações em duas pequenas cidades: Nova Friburgo e Bom Jardim. Ambas cidades estão localizadas ao longo do rio Bengalas, sendo este o principal afluente associado ao rio Grande. Essas duas cidades são bons exemplos de crescimento populacional e de ocupação desordenados, pois são atravessadas por um dos afluentes do rio grande, o qual costumeiramente atinge a cidade com eventos de cheia e inundações.

No trabalho, buscou-se promover uma janela de tempo de previsão de inundação com 2 horas de antecedência ao acontecimento através de uma rede neural artificial. O banco de dados utilizado na implementação foi construído a partir de oito estações de monitoramento do Instituto Estadual do Ambiente (INEA) , de modo que a base de dados é composta por dados pluviométricos e de precipitação. Cada instância de entrada possui um vetor de tamanho 15, no qual 8 valores são de precipitação e 7 são valores de nível. Os dados foram coletados no período de 2013 à 2014, com uma janela temporal de 15 minutos.

O modelo utilizado para previsão do nível do rio foi uma rede MLP com a configuração de 15 nós de entrada e apenas uma camada oculta, com o vetor de característica contendo 8 valores referentes à dados de chuva e sete valores referentes ao nível do rio. Foram utilizadas as métricas padrão para esse tipo de implementação, como o erro médio (ME) , a raiz quadrada do erro médio (RMSE) , o coeficiente de Nash – Sutcliffe (NASH) e o erro absoluto médio (MAE) . Foram criados dois alvos de predição, um para 15 minutos de predição e outro para 120 minutos de antecedência. Os resultados das métricas apontaram que o alvo de 15 min apresentou resultados mais satisfatórios em relação ao de 120, devido ao maior erro associado ao maior o horizonte de predição.

### <span id="page-55-0"></span>**3.2 Modelos de Previsão Híbridos**

Algumas técnicas de combinações de algoritmos têm sido utilizadas como alternativa de otimização no desempenho das RNAs, pois geralmente identifica-se uma baixa eficiência de aprendizagem quando os hiperparâmetros escolhidos não são bem ajustados. O trabalho de [Feng e Niu](#page-123-11) [\(2021\)](#page-123-11) propôs um método de combinação de algoritmos composto por um algoritmo de cooperação (CSA) que, integrado ao processo de aprendizagem da RNA, resulta no método híbrido denominado rede neural artificial evolucionária (*artificial evolutionary neural network*) para a previsão de fluxo do rio com base em dados de vazão.

Nesse trabalho, o modelo híbrido foi aplicado aos dados de vazão do rio de duas estações hidrológicas do rio Yangtze, na China. As estações do estudo de caso utilizavam sensores de nível para a capitação dos dados. Os estudos da aplicação do modelo híbrido indicaram que o desempenho do modelo preditivo é diretamente influenciado pelas variáveis de entrada utilizadas, assim como o número de neurônios utilizados nas camadas ocultas. O método RNA-CSA se mostrou superior no resultado de 5 configurações testadas tendo uma eficiência maior de aproximadamente 11% em relação às RNA padrão. No entanto, ao comparar o modelo proposto com os modelos*extreme learning machine* (ELM) e *support vector machine (SVM)* , os resultados obtidos foram comparáveis, atingindo valores de erros de classificação em torno de 0,8. Tais resultados foram promissores quando comparados à RNA padrão, porém, o poder preditivo ainda

apresenta um grande espectro para melhorias.

Outro exemplo da aplicação e do estudo dos modelos híbridos é o que pode ser encontrado no trabalho de [Fathian](#page-123-12) *et al.* [\(2019\)](#page-123-12). O trabalho utiliza o dataset com dados de vazão referentes às estações Brantford e Galt, em Grand River, no Canadá. Foi considerado um período de 69 anos, de outubro de 1948 a setembro de 2017. Para o processo de previsão, foram realizadas várias combinações algorítmicas não só com os modelos propriamente híbridos, mas também a integração de modelos independentes como o algoritmo de RNA acoplado ao modelo de GARCH. A pesquisa se comprometeu com o a investigação do desempenho de duas técnicas empregadas em problemas de séries temporais de dados de nível de rio: *Self-exciting threshold autoregressive* (SETAR) e o *Generalized Autoregressive Conditional Heteroscedasticity* (GARCH) . Além destas, o trabalho expõe mais três arquiteturas de inteligência artificial que incluem a rede neural artificial, *multivariate adaptive regression splines* (MARS) e *random forest* (RF) .

Como resultado, essa pesquisa indicou que o modelo com melhor resultado preditivo do fluxo do rio, entre os modelos híbridos, foi o SETAR, com o coeficiente de Nash Sutcliffe (E) igual a 0.895 para as predições tanto da estação de Branstford quanto para a estação de Galt (em modelos hidrológicos, o coeficiente de Nash é dos mais utilizados para validar o desempenho do modelo, no qual, em uma faixa variação de menos infinito a 1, quanto mais próximo de 1 conclui-se que houve melhor adaptação entre os dados e o modelo [\(BRIGHENTI; BONIMá;](#page-121-11) [CHAFFE,](#page-121-11) [2015\)](#page-121-11)). Além disso, obteve maior acurácia frente aos resultados dos demais modelos autônomos e com acoplamento. Para os modelos autônomos, como o de RNA, o estudo indica interferências na performance de previsão devido ao número de neurônios nas camadas ocultas.

Apesar de a solução proposta ter apresentado bons resultados, é importante ressaltar algumas técnicas que foram deixadas de lado e que poderiam ter apresentado resultados tão bons quanto os obtidos no trabalho, como as LSTMs [\(HOCHREITER; SCHMIDHUBER,](#page-124-1) [1997\)](#page-124-1). As LSTM são muito bem sucedidas em problemas que possuem dados característicos de séries temporais, assim como as redes GRU, além de algumas outras ferramentas que, mesmo não possuindo caráter híbrido, quando utilizadas individualmente, oferecem eficiência de previsão similar.

### <span id="page-56-0"></span>**3.3 Modelos de Previsão RNN**

Parte do estudo sobre métodos preditivos tem por intuito criar sistemas de alarme que possam atuar nos perímetros urbanos e áreas de natureza preservada. Com isso, tem-se o trabalho de Lee *[et al.](#page-125-6)* [\(2020\)](#page-125-6), que propõe um estudo de caso na predição de rios para aplicar a um sistema de alarme de enchentes. Foi empregado um conjunto de dados resultante de 32 estações de nível de água no rio Han e 19 sistemas de monitoramento em riachos. Os dados de nível de água providos são da estação da ponte Dorin, estação Guro Digital Complex e estações da ponte Guro1.

No modelo proposto, utiliza-se a saída de resposta preditiva como entrada no sistema de alerta de inundação desenvolvido para o meio urbano. A pesquisa visou o poder preditivo de enchentes da rede neural tanto quanto a estatística de quantificação do risco de inundação de curto prazo (LEE *[et al.](#page-125-6)*, [2020\)](#page-125-6). O Sistema Integrado de Previsão e Alerta de Cheias, proposto pelos pesquisadores, trabalha com a faixa de previsão de curto prazo e curtíssimo prazo. A previsão de inundação é feita por uma rede neural LSTM, que utiliza no treinamento da rede intervalos de tempos de 30 a 90 minutos para a previsão. Para a previsão dos dados pluviométricos (LEE *[et al.](#page-125-6)*, [2020\)](#page-125-6), fez-se uso de um sistema combinado por *Storm Water Management Model* (SWMM) e do sistema *Hydrologic Engineering Center—River Analysis System* (HEC-RAS) . O SWMM é um sistema de modelo de gestão de águas pluviais "utilizado em todo o mundo para o planeamento, análise e concepção relacionados com o escoamento de águas pluviais, esgotos combinados e sanitários, e outros sistemas de drenagem"[\(EPA,](#page-123-13) [2021\)](#page-123-13). Conforme [USACE](#page-128-12) [\(2021\)](#page-128-12),

> O HEC-RAS é um software que permite ao utilizador efetuar cálculos unidimensionais de fluxo estável, cálculos unidimensionais e bidimensionais de fluxo instável, cálculos de transporte de sedimentos/cama móvel, e modelação da temperatura/qualidade da água.[\(USACE,](#page-128-12) [2021\)](#page-128-12)

Para o treinamento da LSTM, o conjunto de dados hidrológicos da série temporal é referente aos dados do nível de profundidade do riacho Dorin, obtidos em Seul, capital da Coreia do Sul. Na dinâmica do trabalho, os autores fizeram três casos de uso de dados, no intuito de analisar a acurácia da previsão conforme o número de dados utilizados na rede.

Para apenas um conjunto de dados, como é o caso da estação de Dorin, a previsão não foi satisfatória devido à utilização de apenas um dado de profundidade a montante, desse modo desconsiderando os demais fluxos do riacho. Já no caso em que utilizaram o conjunto de dados contendo os níveis das três estações, a previsão teve um de seus melhores resultados(LEE *[et al.](#page-125-6)*, [2020\)](#page-125-6). O tempo de resposta obtido de 40 minutos o que se mostrou satisfatório em comparação ao modulo de previsão de inundação que apresentou um tempo de resposta de 10 a 70 minutos. O que pode ser aprimorado nesse trabalho é a parte de previsão por radar com um conjunto de dados melhor. É sabido que, quanto melhor a base de dados agregada a um bom algoritmo, melhores os resultados de preditivos Lee *[et al.](#page-125-6)* [\(2020\)](#page-125-6).

O trabalho de [Li, Kiaghadi e Dawson](#page-125-7) [\(2021\)](#page-125-7) apresenta um estudo na construção de um modelo de previsão de chuvas excedentes que causam o processo de inundação severa na bacia hidrográfica de Houston, no estado do Texas, nos Estados Unidos da América. Para a construção do modelo, foi implementada uma rede LSTM, aplicada ao conjunto de dados com registros de 10 anos de precipitação das chuvas, com um total de 153 medidores. A metodologia contou com a comparação dos resultados da rede LSTM com o Gridded Surface Subsurface Hydrologic Analysis - GSSHA, um modelo orientado a processo de análises hidrológicas subsuperficial de superfície. O GSSHA é um modelo hidrológico de parâmetros distribuídos de código aberto, capaz de acoplar múltiplas interações físicas entre o fluxo do canal 1D, fluxo superficial 2D, infiltração e fluxo de água subterrânea, interceptação de precipitação, derretimento de neve e evapotranspiração. O GSSHA foi utilizado como referência por já ter sido aplicado a estudos que melhoraram a parametrização do modelo de gestão de águas pluviais. Com isso, foi desenvolvido um modelo de GSSAH próprio para a aplicação em questão ativando-se apenas os processos de roteamento de fluxo de superfície para gerar e simular o modelo hidrológico junto ao algoritmo de LSTM. A suposição do trabalho era o aprendizado da rede LSTM através da correlação física entre a precipitação e a vazão do rio, buscando assim resultados preditivos satisfatórios. Além disso, um modelo preditivo de bons resultados possibilitaria a redução do número de medidores existentes atualmente. Os resultados de [Li, Kiaghadi e Dawson](#page-125-7) [\(2021\)](#page-125-7) indicaram que a rede LSTM conseguiu aprender e identificar os pluviômetros que apresentaram os dados mais significativos no momento da previsão, se mostrando uma alternativa rápida e simples quanto à aplicabilidade. Além disso, o modelo se mostrou superior ao GSSHA nas predições em todos os testes realizados.

O trabalho de [Ha, Liu e Mu](#page-124-7) [\(2021\)](#page-124-7) aborda a previsão de enchentes do rio Yangtze, que faz parte de uma das bacias hidrográficas mais importantes da China, fortemente relacionada com o desenvolvimento econômico do local. O objetivo foi elaborar a previsão de enchentes em um intervalo de dois anos, tendo em vista previsões mensais. Os autores propuseram a aplicação de modelos de redes neurais profundas, especificamente utilizando as arquiteturas *stacked long short-term memory* (Stacked LSTM) e *Conv long short-term memory encoder–decoder long short-term memory* (GRU LSTM) . As arquiteturas de previsão selecionadas são modelos de regressão devido aos dados que integram o dataset serem uma série temporal de registros obtidos mensalmente no período de 1952 a 2018.

Após a implementação dos modelos de redes neurais profundas, a arquitetura que apresentou melhores respostas na previsão de enchentes foi a GRU ConvLSTM, para o ano de 2016 na estação de Hankou. Tal arquitetura indicou maior estabilidade de previsão em comparação com o período de cheias dos anos referidos, possuindo resultados satisfatórios nas métricas de RMSE, Índice de Legates-McCabe - LMI , Índice de Concordância de Willmott - WI e R2 - Coeficiente de Determinação . As demais estruturas apresentaram desempenhos de previsão bons, porém com diferenças de previsões em meses como julho e setembro. De um modo geral, a linha de regressão dos três modelos apresentou desempenhos semelhantes, apenas com diferenças na estabilidade de previsão nos meses .

Embora os modelos apresentados terem demonstrado resultados satisfatórios, deve-se pontuar que para que sejam atingidos valores de previsão superiores a 90% é necessário um grande volume de dados. Modelos RNN requerem um conjunto de dados abundantes para precisão, mas sua obtenção por meio de medições de campo é desafiador devido a restrições de recursos e custos, bem como ao número limitado de eventos de inundação registrados por ano em alguns locais. Adicionalmente, os modelos LSTM geralmente não são bem sucedidos para dados de curto prazo e sujeitos a rápidas mudanças e não periódicos, como os dados de ondas de inundação. Para superar tais obstáculos, o uso de modelos CNN vem sendo avaliado devido à sua capacidade de capturar padrões espaciais e características dentro dos dados, aproveitando camadas convolucionais para extrair padrões localizados e adquirir representações hierárquicas. Um desafio técnico, entretanto, consiste em realizar a conversão de dados de séries temporais para dados de imagem, a fim de serem inseridos na CNN.

### <span id="page-59-0"></span>**3.4 Modelos de previsão CNN**

A razão pela qual as CNNs também podem ter um bom desempenho na previsão de séries temporais é que ela pode extrair os padrões implícitos e repetitivos das séries temporais e extrair automaticamente características dos dados sem a necessidade de engenharias adicionais ou conhecimento prévio [\(AGONAFIR](#page-120-6) *et al.*, [2023\)](#page-120-6). Além disso, em relação a séries temporais ruidosas, CNN também pode eliminar o ruído nos dados e extrair características úteis através da construção de características hierárquicas [Chen](#page-122-8) *et al.* [\(2021\)](#page-122-8).

Em [Kimura](#page-124-8) *et al.* [\(2019\)](#page-124-8), foi proposto o uso de um modelo CNN juntamente com a técnica de *transfer learning* para pré-treinar o modelo e reaplicá-lo no conjunto de dados de destino. Os autores utilizaram o *dataset* da bacia hidrográfica do rio Oyodo para o prétreinamento do modelo para posterior aplicação de predição com o *dataset* do rio Abashiri. Para conversão dos dados, os autores organizaram uma matriz 16×16, de modo que as 16 variáveis (chuva e nível da água) em todas as estações de medição, desde a montante até a jusante, foram dispostas na vertical, e a variação temporal de cada variável na horizontal. Os valores digitais foram então convertidos em uma imagem usando a escala de cinza que varia de zero a um e é normalizada pelos valores máximos e mínimos de todos os conjuntos de dados observados de nível da água e chuva. Essa abordagem conseguiu reduzir o tempo de treinamento em 1/5 e diminuiu o erro médio em 15% em comparação com o CNN sem aprendizado por transferência. Os valores de RMSE diminuiram à medida que o número de re-treinamentos foi aumentado, permitindo obter resultados melhorados com um custo computacional substancialmente menor. No entanto, o modelo de previsão CNN não foi tão eficaz quanto os modelos tradicionalmente utilizados.

[Chen](#page-122-8) *et al.* [\(2021\)](#page-122-8) também propuseram um modelo de previsão de inundação com base em CNN com operação convolucional em duas dimensões (2D), considerando de forma abrangente as características espaço-temporais das chuvas, a característica geográfica e a característica de tendência. Primeiramente, as características espaço-temporais das chuvas foram importadas através de gradeamento na bacia de Xixian. Em seguida, os dados do Modelo Digital de Elevação - DEM foram processados como característica geográfica e utilizou-se o histórico do fluxo do rio na bacia de Xixian como característica de tendência. Os resultados numéricos mostram que o modelo proposto demonstrou maior precisão na previsão do pico da inundação e do momento de chegada, com uma antecedência de 24 horas e 36 horas, respectivamente. Aprimorar a precisão de previsão do modelo CNN ao ser aplicado a dados de séries temporais é uma tarefa crucial que pode ser realizada explorando várias técnicas para converter o conjunto de dados em dados de imagem. Em estudos recentes [Kirichenko, Zinchenko e Radivilova](#page-124-0) [\(2021\)](#page-124-0), o gráfico de recorrência - RP surgiu como uma ferramenta valiosa para melhorar a classificação de imagens de eletroencefalograma - EEG .

O trabalho de [Caseri, Santos e Stephany](#page-122-9) [\(2022\)](#page-122-9) aborda a previsão de chuvas intensas e convectivas de curto prazo (nowcasting). A proposta utiliza como base de dados captações do radar meteorológico em tempo real e se concentra na previsão de eventos de chuvas fortes através da abordagem de aprendizado profundo. O estudo propõe um método chamado M5Images, o qual é formado por uma rede neural recorrente convolucional com uma parte recorrente baseada em uma LSTM. O estudo mostra que o método M5Images demonstrou um desempenho significativamente melhor em comparação com o método de previsão de persistência - PFM , que é uma abordagem simples que considera a última observação como a previsão para a próxima observação. Isso indica que a abordagem baseada em redes neurais, proposta no artigo, tem o potencial de melhorar as previsões de chuvas convectivas intensas em curto prazo. Os resultados também sugerem que as redes neurais, incluindo a rede neural recorrente convolucional (CNN-LSTM) utilizada no método M5Images, podem ser eficazes na previsão de eventos climáticos extremos. Isso destaca o potencial das técnicas de aprendizado profundo em melhorar a precisão das previsões meteorológicas, especialmente para eventos de chuvas intensas. Apesar do desempenho melhorado, os resultados também destacam os desafios persistentes associados à previsão de eventos de chuva convectiva intensa em curto prazo. Adicionalmente, a alta variabilidade espaço-temporal desses eventos torna essa tarefa intrinsecamente desafiadora, e mesmo o método proposto ainda apresenta limitações em termos de precisão em momentos e locais específicos. Isto deve-se ao fato de que a aplicação do método M5Images depende da disponibilidade de dados de radar meteorológico, indo de encontro com a realidade de que nem todos os locais têm acesso a esses dados em tempo real, o que pode limitar a aplicabilidade do método em algumas regiões.

### <span id="page-60-0"></span>**3.5 Modelos de previsão utilizando o Recurrence Plot**

Adentrando o campo de classificação que utiliza como ferramenta o RP, pesquisadores que têm produzido bastante material nesta linha de pesquisa são [Kirichenko, Zinchenko e](#page-124-0) [Radivilova](#page-124-0) [\(2021\)](#page-124-0), com o intuito de obter melhores resultados em analises classificatórias em imagens de eletroencefalogramas com a finalidade de aumento de acurácia. Neste trabalho, os autores propõem a otimização de resultados em algoritmos de aprendizado de máquina em estudos de casos médicos utilizando um dataset com 178 registros de atividades cerebrais. Considerando que a atividade cerebral é mensurada ao longo de um determinado período de tempo, tem-se um comportamento de série temporal.

Para o caso em questão, propõe-se a conversão destas séries temporais em RP. Essa conversão de série temporal em gráfico possibilitou maior acurácia na classificação de exames onde havia ou não traços de comportamento epiléptico na imagem. A escolha dessa abordagem possibilitou resultados promissores. Utilizando o DL, em específico a CNN, a classificação desses gráficos se tornou viável, de modo que seus indicadores de acurácia e qualidade de aprendizagem do algoritmo atingiram 98% e 95%, respectivamente. Pesquisas como esta tornam possível propostas de pesquisas que visam a classificação ou até mesmo a predição em séries temporais que envolvam dados do tipo, que são apanhados ao longo do tempo e do estudo de um fenômeno.

A tarefa de prever eventos futuros nunca foi tão estimada, considerando as adversidades de tempo, mercadológicas e até mesmo biológicas prever o próximo "step"garante a vantagem da "preparação". Isto posto, voltando os olhares para o meio ambiente urbano um dos desafios dentro de centros populacionais é lidar com eventos hidrológicos como, inundações, enchentes, enxurradas que resultam em danos ao meio civil. Para isso tem-se utilizado de medidas associadas a algoritmos de RNA no intuito de potencializar recursos de previsão de eventos hidrológicos, como mostra a pesquisa de [Alberton](#page-120-7) *et al.* [\(2021\)](#page-120-7), aborda a aplicabilidade dos algoritmos de RNA na previsão de curto prazo dos níveis do rio Itajaí-Açu no município de Blumenau. O objeto de estudo escolhido se deu pelo extenso histórico de inundações. Para o treinamento das redes neurais foram utilizados dados de nível do rio referente a estação telemétricas do Sistema Nacional de Informações sobre Recursos Hídricos (SNIRH) da ANA da bacia hidrográfica do rio Itajaí-Açu. Para o estudo foram definidos 7 datas nos quais foram evidenciados alertas de inundação para realizar os testes, com a unidade de medida para nível sendo calculada em cm e para precipitação calculada em mm. Foram aplicadas as redes LSTM e MLP para o treinamento dos dados, os autores escolheram como parâmetros de desempenho o coeficiente de determinação (R2), o Coeficiente de Eficiência de Nash-Sutcliffe (NSE), a Raiz do Erro Quadrático Médio (RMSE), Erro Quadrático Médio (MSE) , o Erro Médio Absoluto (MAE) e a Média Percentual Absoluta do Erro (MAPE) . Para a analise de desempenho da rede foram testados diferentes valores de Dropout, o que resultou em impactos diferentes para cada modelo, notou-se que para a MLP o ganho foi proporcional ao aumento do parâmetro de drop-out para LSTM houve declínio no resultado de avaliação.No entanto os resultados obtidos são baseados em series de dados temporais de intervalos de dias entre três à dezessete dias, o que pode refletir na acurácia do desempenho em relação ao underfitting de dados, em comparação com o presente trabalho no qual as bases de teste e treinamento são de registros de janelas de tempo de anos, o que pode contribuir positivamente no aprendizado da rede devido o volume de dados.

Os eventos de enchente no Brasil são relatados desde o inicio da urbanização das cidades, não apenas resultado dos défices estruturais mas também pela localização das áreas urbanizadas muito próximas a rios. De tal modo o trabalho de [CRISTALDO](#page-122-10) *et al.* [\(2020\)](#page-122-10) aborda o histórico de enchentes na região do pantanal, na qual desde 1941 registra relatos de enchentes na cidade de Aquidauana e Anastácio. O cerne de sua pesquisa é direcionado a previsão de enchentes na

área urbana de Aquidauana utilizando técnicas de redes neurais artificiais, mais precisamente o modelo MLP aplicado a dados de cotas do rio Aquidauana e da precipitação entre os anos de 1995 e 2014. Foi utilizada a técnica de Análise de Componentes Principais com o objetivo de explicar a variância da matriz de observações e reduzir o número de dados meteorológicos. Para o trabalho em questão foi realizado um levantamento dentro do banco de dados da Agencia nacional das águas das medições de cota acima do valor de extravasamento do rio para a cidade, o qual é de oito metros, para então correlacionarem quantidade de dias com mês. O banco de dados desenvolvido para implementação da RNA utilizou informações dos postos fluviométricos e pluviométricos da ANA e do Serviço Geológico do Brasil - SGB , o treinamento da rede neural utilizou dados no intervalo de 1995 a 2013 e para teste dados do ano de 2014.Os autores utilizaram o software WEKA para uma configuração de rede MLP com oito entradas, uma camada oculta e um camada de saída com um neurônio para realizar o treinamento e os testes dos dados. As métricas de avaliação utilizadas foram: Rtr - coeficiente de correlação para dados de treinamento ; Rtst - coeficiente de correlação para dados de teste ; MAE - Erro Absoluto Médio; RAE - Erro Relativo Absoluto ; RMSE - Erro Quadrático Médio Relativo; MSRE - Erro Quadrático Relativo e o NSE - Coeficiente de Eficiência Nash-Sutcliffe. Os resultados de treinamento obtidos indicaram valores de previsão melhores para janelas de tempo de até três dias porem para previsões próximas de cinco dias o erro aumentou para um taxa de 30 cm a 69 cm de diferença e um RMSE de 0,95. Os resultados foram satisfatórios para a proposta da metodologia, no entanto a escolha de apenas um ano de dados para testes contribui para um resultado de acurácia frágil devido o volume de dados testados, partindo do principio que o numero de testes atesta a eficiência da rede, uma escolha diferente para essa faixa de tempo poderia ter refletido em resultados melhores até para um maior numero de dias.

Os períodos chuvosos variam de acordo com as estações do ano na maioria dos locais do globo, no entanto algumas regiões de local tropical com climas: tropical úmido, tropical úmido e seco ou tropical equatorial não apresentam as quatro estação tão bem definidas, principalmente o clima equatorial encontrado na região norte do Brasil nos estados do Amazonas, Acre, Rondônia, Roraima, Pára, Amapá e Tocantins que influenciam o local com períodos de forte chuva e de verões intensos. Isto posto, o trabalho de Neto *[et al.](#page-126-11)* [\(2020\)](#page-126-11), propõe a modelagem hidroclimatológica na bacia hidrográfica do Rio Acre na cidade de Rio Branco, a qual nos últimos anos sofreu com períodos de cheias recorrentes devido o volume de chuvas. Dentro do período de uma década foram registradas 3 enchentes históricas afetando significativamente a capital Rio Branco, causando danos materiais e de saúde aos moradores locais. Tendo em vista a situação atual objetivou-se a criação de um modelo de RNA MLP no intuito de prever cotas máximas mensais com até 4 meses de antecedência na bacia hidrográfica do Acre (BHA) , a área que será o objeto de estudo corresponde aos 35.967 km<sup>2</sup> de área de drenagem da bacia onde aproximadamente 23 km<sup>2</sup> que equivalem a 65,7% da área da bacia estão localizados no Rio Branco. O *dataset* utilizado para o estudo e treinamento da rede neural é composto por dados de cota de registros diários da cidade de Rio branco da estação pluviométrica 13600002 da ANA no período de

1971 a 2016. Para o modelo MLP as variáveis de entrada escolhidas são baseadas nas regiões oceânicas: Nino 4, Nino 3.4, Nino 3, Nino 1+2, ATN, ATS e ASW para dados médios mensais dos oceanos, temperatura e pressão atmosférica que possuem correlação com o nível mensal do Rio Acre em um período de variação de 12 meses.

A utilização de ferramentas como o gráfico de recorrência por vezes é atraente, devido alguns embates comuns encontrados quando busca-se prever ou classificar e os dados existentes por vezes deixam a desejar. É sabido que bons resultados são frutos da combinação de algoritmos eficientes juntamente a dados com informações consistentes. Em séries temporais, é comum haver lacunas de tempo. Quando não implementada alguma engenharia de seleção, essas lacunas podem comprometer a acurácia do classificador. Na tentativa de driblar essas questões, o gráfico de recorrência é implementado para uma visão mais global do comportamento da série.

O trabalho de [Majid, Omar e Noorani](#page-125-8) [\(2021\)](#page-125-8) apresenta um estudo realizado para analisar o fluxo do Rio Kelantan durante o período de 2000 a 2014, com o objetivo de detectar e prever enchentes. Para isso, foram utilizadas três técnicas: RP, análise de quantificação de recorrência (RQA) e ARIMA. O estudo discute vários métodos usados para prever enchentes, incluindo métodos estatísticos, aprendizado de máquina e teoria do caos. Assim como pontua a importância de um sistema de detecção de alerta antecipado para enchentes, que pode ser baseado em métodos de previsão. Os autores mencionam o uso de métodos como o modelo ARIMA e a análise de recorrência para prever as enchentes no Rio Kelantan, destacando que a análise de recorrência pode ser uma ferramenta útil para detectar recorrências em sistemas dinâmicos, como o comportamento do fluxo do rio. No geral, o estudo enfatiza a importância da previsão precisa de enchentes fluviais, especialmente em áreas propensas a enchentes recorrentes, como o Rio Kelantan, e sugere que a análise de recorrência pode ser uma abordagem promissora para melhorar a previsão de enchentes. Além disso, ressalta a necessidade de sistemas de alerta precoce eficazes para mitigar os riscos associados a enchentes. Os resultados foram baseados no critério RMSE, que é uma medida de erro de previsão.

Em resumo, o trabalho fornece uma visão geral das técnicas e métodos de previsão de enchentes fluviais usados em relação ao Rio Kelantan, mas não apresenta resultados específicos de previsões ou dados quantitativos relacionados às previsões de enchentes no rio. O texto apenas menciona que o modelo ARIMA teve um desempenho melhor em termos de previsão em comparação com a análise de recorrência para o ano de 2014.No entanto, até onde é sabido, nenhum estudo anterior aplicou a combinação de RP e CNNs para a previsão de enchentes.

### <span id="page-63-0"></span>**3.6 Considerações Finais**

Neste capítulo, apresentou-se como os modelos de previsão são aplicados na prática nos projetos de pesquisa, e como a utilização de redes neurais trouxe progressos nesse campo de algoritmos de previsão, não apenas com os modelos padrões de RNN e CNN mas também com modelos baseados em combinações de algoritmos específicos, como os modelos híbridos, modelos de LSTM, a Tabela [1](#page-65-0) apresenta os trabalhos discutidos nesta seção. Tais modelos são utilizados a fim de melhorar a performance das RNs quando utilizadas isoladamente. Foi apresentado também como a acurácia dos modelos de predição pode ser melhorada ao utilizar ferramentas alternativas como softwares de imagens e técnicas de recursos gráficos.

Considerando os resultados promissores do uso de RPs em tarefas de classificação baseadas em aprendizado de máquina, este presente trabalho objetiva explorar o desempenho das CNNs na previsão de enchentes usando representações gráficas bidimensionais. Essa abordagem alternativa, que utiliza imagens 2D, tem o potencial de melhorar a precisão das previsões. Com o objetivo de apoiar as comunidades nas áreas circundantes da bacia Amazônica, que frequentemente enfrentam inundações, pretende-se combinar o uso de RP com CNN para analisar os dados de chuvas mensais do rio Xingu, na região de Altamira. Um processo de *transfer learning* também foi aplicado para verificar o aprimoramento na precisão das previsões. Para comparar as técnicas, também aplicaremos como comparação os modelos GRU e LSTM no conjunto de dados do rio Xingu. Ao abordar os desafios da previsão de enchentes por meio dessa abordagem híbrida (RP+CNN), esperamos fornecer informações valiosas para a comunidade científica de previsão de enchentes e oferecer suporte às comunidades propensas a inundação.

| be<br>la<br>Ta<br>1 | – | ba<br>l<br>ho<br>Tr<br>a<br>s | lac<br>Re | io<br>do<br>na<br>s | fer<br>Re<br>te<br>en | ao<br>s | de<br>lo<br>M<br>o<br>s | de | is<br>Pr<br>ão<br>ev | i<br>dr<br>l<br>H<br>óg<br>o | ico<br>s |
|---------------------|---|-------------------------------|-----------|---------------------|-----------------------|---------|-------------------------|----|----------------------|------------------------------|----------|
|---------------------|---|-------------------------------|-----------|---------------------|-----------------------|---------|-------------------------|----|----------------------|------------------------------|----------|

<span id="page-65-0"></span>

| A<br>U<br>T<br>O<br>R<br>E<br>S                                                                                                                    | P<br>R<br>O<br>P<br>O<br>S<br>T<br>A                                                                                                                                                                                                                                                                                                                                                                                            | C<br>N<br>N | R<br>N<br>N                                                                 | R<br>P      | O<br>U<br>T<br>R<br>O<br>S        | Ã<br>P<br>R<br>E<br>V<br>I<br>S<br>O | Ã<br>D<br>E<br>T<br>E<br>C<br>Ç<br>O | Ã<br>C<br>L<br>A<br>S<br>S<br>I<br>F<br>I<br>C<br>A<br>Ç<br>O |
|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------------------------------------------------------------------------|-------------|-----------------------------------|--------------------------------------|--------------------------------------|---------------------------------------------------------------|
| (<br>G;<br>2<br>0<br>2<br>1<br>)<br>FE<br>N<br>N<br>IU<br>,                                                                                        | éto<br>do<br>h<br>í<br>br<br>i<br>do<br>den<br>ina<br>do<br>de<br>M<br>om<br>re<br>neu<br><br>l<br>i<br>f<br>ic<br>ia<br>l<br>luc<br>ion<br>ia<br>lg<br>itm<br>ár<br>art<br>ra<br>evo<br>a<br>or<br>o<br>-<br>de<br>(<br>C<br>S<br>A<br>)<br>RN<br>A<br>ão<br>co<br>op<br>era<br>ç<br>e                                                                                                                                         | Ã<br>O<br>N | S<br>(<br>S<br>)<br>IM<br>L<br>TM                                           | Ã<br>O<br>N | -                                 | S<br>IM                              | -                                    | -                                                             |
| (<br>F<br>AT<br>HI<br>AN<br>l.,<br>2<br>0<br>1<br>9<br>)<br>et<br>a                                                                                | Co<br>b<br>ina<br>do<br>de<br>los<br>(<br>S<br>ET<br>AR<br>)<br>õe<br>m<br>ç<br>s<br>s<br>mo<br>e<br>(<br>G<br>AR<br>C<br>)<br>H<br>o                                                                                                                                                                                                                                                                                           | Ã<br>N<br>O | S<br>IM<br>(<br>L<br>S<br>TM<br>)                                           | Ã<br>N<br>O | -                                 | S<br>IM                              | -                                    | -                                                             |
| (<br>LE<br>E<br>l.,<br>2<br>0<br>2<br>0<br>)<br>et<br>a                                                                                            | Ut<br>i<br>l<br>iza<br>ão<br>de<br>L<br>S<br>TM<br>ia<br>da<br>is<br>ç<br>ass<br>oc<br>ao<br>s<br>(<br>S<br>W<br>MM<br>)<br>do<br>ist<br>(<br>HE<br>C<br>tem<br>a<br>e<br>s<br>em<br>a<br>R<br>A<br>S<br>)                                                                                                                                                                                                                      | Ã<br>N<br>O | S<br>IM<br>(<br>L<br>S<br>TM<br>)                                           | Ã<br>N<br>O | -                                 | S<br>IM                              | -                                    | -                                                             |
| (<br>A<br>G<br>AD<br>LI<br>KI<br>H<br>I;<br>;<br>D<br>AW<br>S<br>O<br>N,<br>2<br>0<br>2<br>1<br>)                                                  | éto<br>do<br>h<br>í<br>br<br>i<br>do<br>den<br>ina<br>do<br>de<br>M<br>om<br>re<br>neu<br><br>l<br>i<br>f<br>ic<br>ia<br>l<br>luc<br>ion<br>ár<br>ia<br>lg<br>itm<br>art<br>ra<br>evo<br>a<br>or<br>o<br>-<br>de<br>(<br>C<br>S<br>A<br>)<br>RN<br>A<br>ão<br>co<br>op<br>era<br>ç<br>e                                                                                                                                         | Ã<br>O<br>N | -                                                                           | -           | S<br>(<br>AE<br>)<br>IM<br>N<br>N | S<br>IM                              | -                                    | -                                                             |
| (<br>A;<br>2<br>0<br>2<br>1<br>)<br>H<br>LI<br>U;<br>MU<br>,                                                                                       | Ap<br>l<br>ica<br>de<br>de<br>los<br>de<br>de<br>ão<br>ç<br>mo<br>re<br>s<br>neu<br><br>is<br>fun<br>da<br>(<br>Sta<br>ke<br>d<br>S<br>)<br>(<br>G<br>L<br>TM<br>RU<br>ra<br>p<br>ro<br>s<br>c<br>e<br>L<br>S<br>TM<br>)                                                                                                                                                                                                        | Ã<br>O<br>N | S<br>IM<br>(<br>S<br>)<br>(<br>G<br>)<br>L<br>TM<br>RU                      | Ã<br>O<br>N | -                                 | S<br>IM                              | -                                    | -                                                             |
| (<br>KI<br>MU<br>R<br>A<br>l.,<br>2<br>0<br>1<br>9<br>)<br>et<br>a                                                                                 | Mo<br>de<br>lo<br>C<br>N<br>N<br>écn<br>ica<br>de<br>fer<br>t<br>tra<br>com<br>ns<br>lea<br>rni<br>ng                                                                                                                                                                                                                                                                                                                           | S<br>IM     | Ã<br>N<br>O                                                                 | Ã<br>N<br>O | -                                 | S<br>IM                              | -                                    | -                                                             |
| l.,<br>(<br>C<br>HE<br>N<br>2<br>0<br>2<br>1<br>)<br>et<br>a                                                                                       | luc<br>ion<br>l<br>C<br>N<br>N<br>ão<br>com<br>op<br>era<br>ç<br>con<br>vo<br>a<br>em<br>du<br>d<br>im<br>(<br>2D<br>)<br>sõe<br>as<br>en<br>s                                                                                                                                                                                                                                                                                  | S<br>IM     | Ã<br>N<br>O                                                                 | Ã<br>N<br>O | -                                 | S<br>IM                              | -                                    | -                                                             |
| (<br>KI<br>RI<br>C<br>HE<br>N<br>K<br>O;<br>C<br>O;<br>AD<br>ZI<br>N<br>HE<br>N<br>K<br>R<br>I<br>V<br>IL<br>O<br>V<br>A,<br>2<br>0<br>2<br>1<br>) | Mo<br>de<br>lo<br>de<br>C<br>N<br>N<br>ia<br>do<br>á<br>f<br>ic<br>de<br>ass<br>oc<br>a<br>g<br>r<br>os<br>ên<br>ia<br>(<br>)<br>RP<br>rec<br>orr<br>c                                                                                                                                                                                                                                                                          | S<br>IM     | Ã<br>N<br>O                                                                 | S<br>IM     | -                                 | -                                    | -                                    | S<br>IM                                                       |
| (<br>AL<br>BE<br>RT<br>O<br>N<br>l.,<br>et<br>a<br>2<br>0<br>2<br>1<br>)                                                                           | A<br>bo<br>da<br>l<br>ica<br>b<br>i<br>l<br>i<br>da<br>de<br>do<br>lg<br>itm<br>r<br>a<br>ap<br>s<br>a<br>or<br>os<br>da<br>de<br>L<br>S<br>TM<br>Lo<br>S<br>ho<br>Te<br>Me<br>rt-<br>s<br>re<br>s<br>ng<br>rm<br>-<br><br>lt<br>i<br>ML<br>P<br>Mu<br>La<br>Pe<br>tro<br>mo<br>ry<br>e<br>y<br>er<br>rce<br>p<br>n<br>-                                                                                                        | Ã<br>N<br>O | S<br>IM<br>(<br>L<br>S<br>TM<br>)                                           | Ã<br>N<br>O | S<br>IM<br>(<br>ML<br>P<br>)      | S<br>IM                              | -                                    | -                                                             |
| (<br>C<br>RI<br>S<br>T<br>AL<br>D<br>O<br>l.,<br>et<br>a<br>2<br>0<br>2<br>0<br>)                                                                  | Mo<br>de<br>lo<br>Pe<br>Mu<br>lt<br>i<br>Ca<br>da<br>tro<br>rce<br>p<br>n<br>ma<br>s<br>(<br>ML<br>P<br>)                                                                                                                                                                                                                                                                                                                       | Ã<br>N<br>O | Ã<br>N<br>O                                                                 | Ã<br>N<br>O | S<br>IM<br>(<br>ML<br>P<br>)      | S<br>IM                              | S<br>IM                              | -                                                             |
| (<br>O<br>l.,<br>2<br>0<br>2<br>0<br>)<br>N<br>ET<br>et<br>a                                                                                       | de<br>lo<br>de<br>de<br>is<br>lt<br>i<br>Mo<br>Mu<br>La<br>re<br>s<br>neu<br>ra<br>er<br>y<br>Pe<br>(<br>ML<br>P<br>)<br>tro<br>rce<br>p<br>n                                                                                                                                                                                                                                                                                   | Ã<br>O<br>N | Ã<br>O<br>N                                                                 | Ã<br>O<br>N | S<br>(<br>)<br>IM<br>ML<br>P      | S<br>IM                              | -                                    | -                                                             |
| (<br>M<br>AJ<br>ID<br>O<br>M<br>AR<br>N<br>O<br>;<br>;<br>O<br>R<br>AN<br>I,<br>2<br>0<br>2<br>1<br>)                                              | Ut<br>i<br>l<br>iza<br>de<br>á<br>l<br>ise<br>de<br>ên<br>ia<br>ão<br>ç<br>an<br>rec<br>orr<br>c<br>(<br>RP<br>),<br>á<br>l<br>ise<br>de<br>i<br>f<br>ic<br>de<br>ão<br>nt<br>an<br>q<br>ua<br>aç<br>rec<br>or<br>ên<br>ia<br>(<br>Q<br>A<br>)<br>de<br>lo<br>ivo<br>R<br>aut<br>r<br>c<br>e<br>mo<br>o-r<br>eg<br>res<br>s<br>int<br>do<br>de<br>d<br>ia<br>l<br>é<br>óv<br>(<br>AR<br>IM<br>A<br>)<br>eg<br>ra<br>m<br>m<br>e | Ã<br>N<br>O | S<br>IM<br>(<br>AR<br>IM<br>A<br>)                                          | S<br>IM     | R<br>Q<br>A                       | S<br>IM                              | -                                    | -                                                             |
| (<br>C<br>A<br>S<br>ER<br>I;<br>S<br>AN<br>T<br>O<br>S;<br>S<br>TE<br>PH<br>AN<br>Y,<br>2<br>0<br>2<br>2<br>)                                      | M<br>éto<br>do<br>M<br>5<br>Im<br>l<br>ica<br>de<br>ão<br>ag<br>es<br>ap<br>ç<br>um<br>a<br>de<br>l<br>(<br>C<br>N<br>N-<br>L<br>S<br>TM<br>)<br>do<br>re<br>neu<br>ra<br>com<br>p<br>ara<br>éto<br>do<br>de<br>isã<br>de<br>ist<br>ên<br>ia<br>com<br>m<br>p<br>rev<br>o<br>p<br>ers<br>c<br>(<br>PF<br>M<br>)                                                                                                                 | S<br>IM     | S<br>IM<br>(<br>L<br>S<br>TM<br>)                                           | Ã<br>N<br>O | PF<br>M                           | S<br>IM                              | -                                    | -                                                             |
| j<br>i<br>Pr<br>De<br>lv<br>do<br>eto<br>o<br>sen<br>vo                                                                                            | Mo<br>de<br>lo<br>C<br>N<br>N<br>ia<br>do<br>á<br>f<br>ic<br>de<br>ass<br>oc<br>a<br>g<br>r<br>os<br>re<br>ên<br>ia<br>(<br>RP<br>)<br>cor<br>r<br>c                                                                                                                                                                                                                                                                            | S<br>IM     | S<br>IM<br>(<br>L<br>S<br>TM<br>)<br>(<br>G<br>RU<br>)<br>(<br>RN<br>N<br>) | S<br>IM     | -                                 | S<br>IM                              | -                                    | -                                                             |

64

# CAPÍTULO 4

# <span id="page-66-0"></span>**METODOLOGIA DE PREVISÃO COM RECURRENCE PLOT**

Este capítulo inicia com a apresentação da base de dados utilizada na tarefa de previsão de enchentes a partir de séries temporais. Na sequência será abordado e descrito a respeito do processamento dos dados, assim como a abordagem das técnicas de rede neural artificial de forma geral, seguida pelo detalhamento da técnica de *Recurrence plot* e dos tipos de arquiteturas de redes neurais escolhidas para o processo de *machine learning*.

### <span id="page-66-1"></span>**4.1 Abordagem**

A objetivo neste estudo consistiu em utilizar as CNNs no processo de previsão de enchentes por meio da avaliação de séries temporais. Os dados empregados, correspondentes as séries temporais do nível máximo do rio, foram convertidos em imagens de maneira a representar pontos de conversão para a tarefa de previsão. Definir essa metodologia visou explorar a viabilidade do uso de redes neurais convolucionais para aplicações no campo da previsão e regressão, ao invés do que é convencionalmente praticado em problemáticas que envolvem soluções por classificação. A fim de explorar os limites dos recursos da CNN para aplicação no campo da previsão, associou-se a rede CNN ao uso da técnica de gráficos de recorrência. A técnica de RP é dirigida à análise de dados não-lineares, o que a torna adequada aos dados que estão sendo manipulados neste trabalho [\(MARWAN](#page-126-2) *et al.*, [2007\)](#page-126-2).

A partir dos dados das series temporais realizou-se a abordagem de "janelamento deslizante", no qual a série temporal é dividida em janelas que correspondem a um intervalo de tempo e contém um conjunto de pontos de dados. No caso em questão, estes dados são referentes ao nível de máxima do rio. Dessa maneira, cada janela deslizante representa um valor no ponto e é tratada como uma "imagem". Nesta imagem, uma dimensão da matriz bidimensional representa o tempo, em que cada ponto corresponde a uma unidade de tempo (medição mensal), e a outra

dimensão representa o nível de máxima do rio. Por fim, ocorreu o processo de mapeamento da série temporal por completo, de modo que a medida que a janela corre no tempo novas imagens são geradas.

Por fim, cada imagem estará associada a uma etiqueta de previsão, que representa a previsão do valor de máxima do nível do rio. A transformação de séries temporais em um *recurrence plot* teve como alvo um maior potencial de analisar e visualizar a estrutura e os padrões intrínsecos nas séries temporais. Isto deve-se à consideração de que os gráficos de recorrência possibilitam a leitura de padrões complexos e estruturas nas séries temporais que podem não ser facilmente identificados em sua forma original [\(KIRICHENKO; ZINCHENKO;](#page-124-0) [RADIVILOVA,](#page-124-0) [2021\)](#page-124-0). Esta transformação possibilita uma melhor análise das tendências, ciclos, comportamentos periódicos e anomalias nos dados. Adicionalmente, os RPs permitem que modelos de aprendizado de máquina capturem padrões espaciais nos dados, o que pode ser valioso para tarefas de classificação ou previsão, possibilitando mais um fim para o uso das redes neurais convolucionais atuando no campo de problemas de previsão e regressão. Vale ressaltar que para isso ser possível a imagem que gera esse valor é oriunda de um gráfico de recorrência que corresponde à repetitividade da própria série, tendo como tamanho de janela temporal o valor de 20 unidades de tempo que corresponde ao horizonte de entrada da predição e o horizonte de saída da predição é de 1 unidade de tempo.

Foram realizados experimentos empregando o mesmo conjunto de dados em redes neurais recorrentes, que neste trabalho foram RNN, LSTM e GRU. Além destes, também foi abordado a técnica de *transfer learning*, que utilizou em seu treinamento um conjunto de dados constituído por dados de um conjunto de 12 bases de rios e então analisou-se o desempenho do modelo CNN previamente treinado. Tais implementações têm por interesse analisar o desempenho de previsão destes algoritmos em relação à abordagem principal aqui apresentada. Os resultados foram comparados usando métricas para avaliar a eficácia dos algoritmos utilizados.

O fluxo apresentado na Figura [18](#page-68-0) representa a abordagem desenvolvida para a avaliação da aplicação do uso combinado de RP com CNN para previsão de enchentes, em comparação com a RNN, LSTM e GRU. A resumo, os dados foram transformados em séries temporais, que alimentaram os diferentes modelos desenvolvidos para serem avaliados conforme as métricas escolhidas para previsão do estudo em questão.

<span id="page-68-0"></span>Figura 18 – Abordagem desenvolvida para avaliação da aplicação do uso combinado de gráfico de recorrência + CNN para previsão de enchentes em comparação com RNN, LSTM e GRU.

Fonte – Próprio autor.

### <span id="page-68-1"></span>**4.2 Base de dados**

Os dados hidrológicos utilizados neste estudo estão disponíveis gratuitamente no Banco de Dados Hidrometeorológicos da Agência Nacional de Águas (ANA), acessível por meio do portal HIDROWEB [\(Agência Nacional de Águas \(ANA\),](#page-120-9) [2023\)](#page-120-9). Esta plataforma é uma ferramenta complementar ao Sistema Nacional de Informações sobre Recursos Hídricos (SNIRH) , fornecendo acesso a um extenso conjunto de informações, incluindo níveis de rios, fluxos, precipitação e qualidade da água, entre outros pontos de observação. O conjunto de dados foco do desenvolvimento deste estudo diz respeito aos níveis máximos do Rio Xingu, extraídos da estação fluviométrica da Bacia Amazônica no estado do Pará na região de altamira.

A Tabela [2](#page-69-0) representa o conjunto de dados utilizado. Nela é possível verificar o período de captação de cotas e a base de dados correspondente utilizada neste trabalho. Para a implementação total deste projeto, foram utilizados conjuntos de dados referente a 12 rios apresentadas na tabela, cada qual com seus respectivos períodos de coleta. Para treinamento da rede neural (na etapa de *transferlearning* foram utilizadas as cotas dos seguintes rios: Kokraimoro, Joari, São João Felix do Xingu, Neris1883, Neris1886, porto, Santo Antonio 1, Santo Antonio 2, Belo Horizonte, Santo José e Jusante. O Rio Xingu foi utilizado como objeto final no processo de previsão de enchentes. Conforme visualizado, o conjunto de dados do Rio Xingu abrange um total de 444 meses de medições, cobrindo um período de coleta que se estende de 1974 a 2019. Cada entrada no conjunto de dados representa o valor de máxima do rio de um único mês.

<span id="page-69-0"></span>Tabela 2 – Conjunto de dados gerais brutos contemplando todos os rios utilizados no treinamento e aplicação do modelo desenvolvido, exemplificando o período de captação, número de estações e número de dados totais referente à cada base de dados

| Dataset                 | Início     | Fim        | o de Estações<br>N | o de Dados<br>N |
|-------------------------|------------|------------|--------------------|-----------------|
| Kokraimoro              | 01/02/1978 | 01/12/1985 | 31                 | 3705            |
| Joari                   | 01/10/1981 | 01/11/1998 | 31                 | 19914           |
| São João Feliz do Xingu | 01/06/1975 | 01/02/1998 | 31                 | 15582           |
| Neris1883               | 01/11/2000 | 01/12/2001 | 31                 | 1221            |
| Neris1886               | 01/12/2000 | 01/12/2001 | 31                 | 1183            |
| Porto                   | 01/10/1981 | 01/12/1986 | 31                 | 4854            |
| Santo Antonio1          | 01/11/2000 | 01/12/2001 | 31                 | 1221            |
| Santo Antonio2          | 01/12/2000 | 01/12/2001 | 31                 | 1183            |
| Belo Horizonte          | 01/05/1976 | 01/03/1998 | 31                 | 22353           |
| São José                | 01/05/1976 | 01/03/1998 | 31                 | 22353           |
| Jusante                 | 01/05/2001 | 01/12/2001 | 31                 | 670             |
| Xingu                   | 01/01/1974 | 01/12/2019 | 9                  | 444             |

A Tabela [3](#page-69-1) apresenta a divisão de dados brutos referente ao *dataset* do Xingu, conjunto de dados principal de pesquisa deste trabalho, a base de dados brutos é constituída por colunas com variáveis correspondentes as temperaturas de superfície do mar das áreas de Niño1+2, Niño3, Niño4, Nino3.4, Atlântico Norte (NATL) , Atlântico Sul (SATL) e Trópicos Global e as pressões ao nível do mar de Darwin (PD) e Tahit (PT) e variáveis de medidas de cota do nível do rio (Cota01, Cota02, ...., Cota09) das sub-bacias ao redor do Xingu captadas por 9 estações pluviométricas. Para o trabalho em questão foram utilizadas apenas os dados de cotas correspondente à altura do rio, objetivando-se a previsão de máxima do rio.

<span id="page-69-1"></span>Tabela 3 – Dados brutos do data set do rio Xingu, contemplando as informações coletadas mensalmente para todos os atributos adquiridos

| Data       | Max   | nino1_2 | nino3 | NATL  | SATL  | PD    | PT    |   | Cota07 | Cota08 | Cota09 |
|------------|-------|---------|-------|-------|-------|-------|-------|---|--------|--------|--------|
| 1979-01-01 | 560.0 | 24.97   | 25.39 | 28.38 | 26.48 | 25.95 | 25.31 |   | 1006.0 | 1009.6 | 471.6  |
| 1979-04-01 | 750.0 | 25.74   | 26.17 | 28.21 | 26.59 | 25.72 | 26.10 |   | 1006.9 | 1012.9 | 338.0  |
| 2014-11-01 | 776.0 | 26.07   | 27.27 | 28.27 | 27.41 | 25.67 | 26.48 |   | 1007.9 | 1011.3 | 216.9  |
|            | -     | -       | -     | -     | -     | -     | -     | - | -      | -      |        |
| 2015-10-01 | 324.0 | 25.41   | 29.11 | 26.90 | 27.54 | 23.05 | 27.45 |   | 0.1    | 0.7    | 222.7  |
| 2015-01-11 | 278.0 | 21.47   | 25.36 | 29.24 | 27.03 | NaN   | 22.99 |   | NaN    | 42.3   | 170.4  |
| 2015-01-12 | NaN   | 21.66   | 25.72 | 29.28 | 27.25 | 28.38 | 23.34 |   | 1013.2 | 28.2   | 139.3  |
| 2016-01-01 | 320.0 | 22.39   | 26.03 | NaN   | 27.52 | 27.73 | 23.52 |   | 1011.3 | 117.5  | 97.3   |
| 2016-01-02 | 447.0 | 23.36   | 26.07 | 29.33 | 27.40 | 26.84 | 24.35 |   | 1009.9 | 97.3   |        |
|            | -     | -       | -     | -     | -     | -     | -     | - | -      | -      |        |
| 2019-12-01 | 583.0 | 24.52   | 27.34 | 28.76 | 27.88 | 26.65 | 25.92 |   | 1011.2 | 1013.3 | 56.2   |

### <span id="page-70-0"></span>**4.3 Processamento de Dados**

O ponto focal deste trabalho de pesquisa foi o treinamento de uma rede neural convolucional profunda a partir de gráficos de recorrências de séries temporais do rio Xingu para prever o nível de máxima do rio visando a previsão de enchentes. Para tornar possível o treinamento da rede CNN a partir de gráficos de recorrências das séries temporais do rio Xingu primeiramente foi realizado o tratamento dos dados brutos do conjunto conforme etapas detalhadas a seguir.

### <span id="page-70-1"></span>**4.3.1 Pré-Processamento de Dados**

O pré-processamento do conjunto de dados do Rio Xingu e dos demais conjuntos de dados utilizados começou com o processo de remover linhas que continham valores ausentes (NaN). É possível observar nos dados apresentados na Tabela [3](#page-69-1) valores ausentes nas linhas e colunas. Para isso foi utilizada a biblioteca pandas, para remover todas as linhas que continham valores faltantes no conjunto de dados [\(TEAM,](#page-128-13) [2020\)](#page-128-13).

Após o processo de sanitização do conjunto foi feita a seleção das colunas de dados de interesse para este trabalho (ou seja, as colunas referentes às medidas dos valores máximos do nível do rio - cotas). Essa seleção de dados foi necessária, pois o conjunto de dados bruto disponibilizado pelo sistema da ANA possui várias variáveis, como fluxo, vazão, pressão e temperatura, as quais não são do interesse para a implementação proposta. Portanto, o processo de seleção considerou apenas as colunas de cotas que correspondiam aos dados máximos do nível do rio significativos para a execução da hipótese de previsão proposta neste projeto.

A partir do *dataset* de colunas de cota do rio original foi gerado um novo conjunto de dados referente às medições mensais do nível do rio, contendo apenas os valores de interesse para a previsão. O resultado de seleção do pré processamento pode ser visto na Figura [19,](#page-71-0) na qual nota-se que cada ponto de coleta referente ao rio Xingu (aqui denominado cota) foi selecionado para compor o conjunto de dados atribuído como base de interesse para o desenvolvimento do trabalho. Dessa forma, as demais informações não relevantes (nino, atlantico norte, etc) contidas no *dataset* original (Figura [19](#page-71-0) (a)) foram desconsideradas, obtendo como resultado um conjunto de dados contendo os valores de interesse conforme demonstrado na Figura [19](#page-71-0) (b).

<span id="page-71-0"></span>

|     |            |                       |                               |                                  |        |                |                |       |                | faxin nam 2 nam and 4 altantico pul stimitics replai presso danin presso partiti (cotol) Cotal) Cotall Cotall Cotall Cotall Cotall |        |                  |                  |              |              |              |              |               |               |               |               |              |
|-----|------------|-----------------------|-------------------------------|----------------------------------|--------|----------------|----------------|-------|----------------|------------------------------------------------------------------------------------------------------------------------------------|--------|------------------|------------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|--------------|
| (a) | 0          | 560.0                 | 24.97                         | 25.39 28.38                      |        | 26.48          |                | 25.95 | 25.31          | 27.51                                                                                                                              |        | 1006.0           | 1009.6           | 471.6        | 430.1        | 392.9        | 353.6        | 451.1         | 342.7         | 415.3         | 286.9         | 292.9        |
|     |            | 750.0                 |                               | 25.74 26.17 28.21                |        | 26.59          | 25.72          |       | 26.10          | 27.70                                                                                                                              |        | 1006.9           | 1012.9           | 338.0        | 322.9        | 301.3        | 379.2        | 404.4         | 395.2         | 205.8         | 379.5         | 325.2        |
|     | 2          | 776.0                 |                               | 26.07 27.27 28.27                |        | 27.41          |                | 25.67 | 26.48          | 28.15                                                                                                                              |        | 1007.9           | 1011.3           | 216.9        | 181.5        | 142.9        | 177.0        | 197.5         | 264.8         | 160.6         | 203.2         | 231.8        |
|     | 3          | 753.0                 | 25.63                         | 27.76                            | 28.51  | 27.93          |                | 26.16 | 26.66          | 28.47                                                                                                                              |        | 1009.7           | 1011.4           | 75.2         | 82.9         | 105.3        | 116.4        | 160.1         | 151.6         | 207.5         | 158.7         | 150.4        |
|     | 4          | 583.0                 |                               | 24.52 27.34 28.76                |        | 27.88          |                | 26 65 | 25.92          | 28.32                                                                                                                              |        | 1011 2           | 1013.3           | 56.2         | 54.5         | 24.0         | 33.1         | 46 5          | 85,5          | 70.2          | 118.4         | 152.4        |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     | 427        | 324.0                 |                               | 22.03 25.41 29.11                |        | 26.90          |                | 27.54 | 23.05          | 27.45                                                                                                                              |        | 1014.5           | 1014.4           | 0.1          | 0.7          | 0.1          | 1.5          | 3.0           | 16.6          | 2.9           | 27.7          | 69.0         |
|     | 428        | 278.0                 |                               | 21.47 25.36                      | 29.24  | 27.03<br>27.25 | 28.22<br>28.38 |       | 22.99<br>23.34 | 27.50<br>27.79                                                                                                                     |        | 1013.1<br>1011.6 | 1014.2<br>1013.2 | 42.3<br>28.2 | 26.6<br>24.2 | 39.3<br>40.2 | 29.5<br>51.4 | 59.5<br>133.6 | 46.0<br>101.2 | 72.8<br>207.0 | 80.5<br>215.5 | 55.2<br>81.7 |
|     | 429<br>430 | NaN<br>320.0          |                               | 21.66 25.72<br>22.39 26.03 29.37 | 29.28  | 27.52          |                | 27.73 | 23.52          | 27.97                                                                                                                              |        | 1000.9           | 1011.3           | 117.5        | 59.4         | 142.0        | 100.6        | 170.4         | 156.5         | 200.5         | 219.9         | 141.2        |
|     | 431        | 447.0                 |                               | 23.36 26.07 29.33                |        | 27.40          |                | 26.84 | 24.35          | 27.95                                                                                                                              |        | 1007 5           | 1009.9           | 2227         | 96.2         | 263.8        | 161.6        | 203.5         | 139.8         | 176.4         | 88.9          | 38.1         |
|     |            | 432 rows × 19 columns |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
| (b) |            |                       | Cota01                        | Cota02                           | Cota03 |                | Cota04  Cota05 |       | Cota06         | Cota07                                                                                                                             | Cota08 | Cota09           |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     | 0          |                       | 471.6                         | 430.1                            |        | 392.9          | 353.6          | 451.1 | 342.7          | 415.3                                                                                                                              | 286.9  | 292.9            |                  |              |              |              |              |               |               |               |               |              |
|     | 1          |                       | 338.0                         | 322.9                            | 301.3  |                | 379.2          | 404.4 | 395.2          | 205.8                                                                                                                              | 379.5  | 325.2            |                  |              |              |              |              |               |               |               |               |              |
|     | 2          |                       | 216.9                         | 181.5                            | 142.9  |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     | 3          |                       |                               |                                  |        |                | 177.0          | 197.5 | 264.8          | 160.6                                                                                                                              | 203.2  | 231.8            |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       | 75.2                          | 92.9                             | 105.3  |                | 116.4          | 160.1 | 151.6          | 207.5                                                                                                                              | 158.7  | 150.4            |                  |              |              |              |              |               |               |               |               |              |
|     | 4          |                       | 56.2                          | 54.5                             |        | 24.0           | 33.1           | 46.5  | 85.5           | 70.2                                                                                                                               | 118.4  | 152.4            |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     | 426        |                       | 4.3                           | 1.6                              |        | 3.2            | 2.0            | 1.0   | 6.3            | 0.2                                                                                                                                | 4.3    | 16.9             |                  |              |              |              |              |               |               |               |               |              |
|     | 427        |                       | 0 1                           | 0 7                              |        | 0 1            | 1.5            | 3.0   | 166            | 29                                                                                                                                 | 277    | 69.0             |                  |              |              |              |              |               |               |               |               |              |
|     | 428        |                       | 42.3                          | 26.6                             |        | 39.3           | 29.5           | 59.5  | 46.0           | 72.8                                                                                                                               | 80.5   | 55.2             |                  |              |              |              |              |               |               |               |               |              |
|     | 430        |                       | 117.5                         | 59.4                             | 142.0  |                | 100.6          | 170.4 | 156.5          | 200.5                                                                                                                              | 219.9  | 141.2            |                  |              |              |              |              |               |               |               |               |              |
|     |            |                       |                               |                                  |        |                |                |       |                |                                                                                                                                    |        |                  |                  |              |              |              |              |               |               |               |               |              |
|     | 431        |                       | 222.7<br>431 rows × 9 columns | 96.2                             | 263.8  |                | 161.6          | 203.5 | 139.8          | 176.4                                                                                                                              | 88.9   | 38.1             |                  |              |              |              |              |               |               |               |               |              |

Figura 19 – (a) conjunto de dados geral e (b) resultado do processo de seleção das colunas de cotas do conjunto de dados para seleção dos dados de interesse.

Fonte – Próprio autor.

Para maior refinamento deste conjunto de dados, foi realizado o processo de transformação de dados por meio da medida estatística de quantil dos dados e da seleção dos valores máximos e mínimos. A estatística de quantil constitui um aspecto essencial da estatística descritiva, concentrando-se na segmentação de um conjunto de dados em porções equitativas. Os quantis, nesse contexto, representam valores que efetuam essa divisão, conferindo a posição relativa de um dado em relação aos demais elementos da distribuição [\(HELSEL; HIRSCH,](#page-124-12) [2002\)](#page-124-12). A mediana é um exemplo proeminente de quantil, demarcando o ponto de divisão que equilibra os dados em duas partes iguais. Esses quantis são expressos mediante o uso de percentis, sendo estes indicativos da proporção de dados situados abaixo de um valor específico na distribuição [\(JUNIOR](#page-124-13) *et al.*, [2019\)](#page-124-13). Essa abordagem oferece uma perspectiva valiosa para compreender a distribuição de dados, destacando-se na identificação de valores extremos, na avaliação da simetria da distribuição e na detecção de padrões emergentes. Além disso, os quantis desempenham um papel fundamental na estatística não paramétrica e em métodos robustos de estimação estatística.

Considerando o descrito na literatura foi realizada a extração dos quantis em porcentagens de mínimo, máximo, 25%, 50% e 75% dos valores, conforme esquema de divisão apresentado na [20.](#page-72-0)

<span id="page-72-0"></span>Figura 20 – Representação esquemática da separação dos dados do conjunto em dados mensais de mínima, máxima, e percentuais de 25% (primeiro quartil), 50% (segundo quartil) e 75% (terceiro quartil).

Os quantis são úteis para entender a distribuição de dados, especialmente em conjuntos extensos [\(HELSEL; HIRSCH,](#page-124-12) [2002\)](#page-124-12). Eles fornecem informações sobre a dispersão e posição dos dados, permitindo a identificação de valores extremos, a compreensão da simetria da distribuição e a detecção de possíveis padrões [\(KOENKER,](#page-124-14) [2017\)](#page-124-14). Portanto, visando utilização da técnica do *recurrence plot*, este tratamento torna-se um caminho com potencial para a melhor utilização dos dados. A Tabela [4](#page-73-1) apresenta o conjunto de dados obtidos após a extração dos valores de quartis. A extração dos valores de quantil visou, sobretudo, padronizar a estrutura de dados entre as diferentes estações de medição. Uma vez que, se uma estação mediu cotas em 10 pontos e outra em 12, não seria possível utilizar todas as cotas diretamente no modelo, pois o esquema de dados seria diferente (uma estação teria 10 variáveis e a outra 12). Dessa forma, a Tabela [4](#page-73-1) resume os dados tratados resultantes da extração dos quartis, em que cada ao invés de apresentar todos os dados medidos, cada mês foi padronizado para conter os valores de mínima, máxima, e os percentuais em 25% (p25), 50% (p50) e 75% (p75). Assim, utilizando algumas medidas de resumo e gerando uma estrutura de dados padronizada, tornou-se possível treinar e fazer inferências no modelo usando dados de diferentes estações.

Após obter o conjunto de dados de quantis, estes se tornaram a base para gerar as séries temporais do Rio Xingu equivalente às 5 colunas do conjunto de dados da Tabela [3,](#page-69-1) no qual o eixo x representa o número de meses e o eixo y o valor referente a medida do nível do rio. A diferença nos valores máximos dos gráficos (400 e 600) ocorre porque as diferentes métricas agregadas (mínimo, máximo, percentis) têm diferentes faixas de valores. Os valores máximos do nível do rio podem atingir valores maiores que 600 para o gráfico do nível máximo do rio devido

| meses | min   | max   | p25   | p50   | p75   |
|-------|-------|-------|-------|-------|-------|
| 0     | 286.9 | 471.6 | 342.7 | 392.9 | 430.1 |
| 1     | 205.8 | 404.4 | 322.9 | 338.0 | 379.5 |
| 2     | 142.9 | 264.8 | 177.0 | 197.5 | 216.9 |
|       |       |       |       |       |       |
| 428   | 26.6  | 80.5  | 39.3  | 46.0  | 59.5  |
| 430   | 59.4  | 219.9 | 117.5 | 142.0 | 170.4 |
| 431   | 38.1  | 263.8 | 96.2  | 161.6 | 203.5 |

<span id="page-73-1"></span>Tabela 4 – Resultados obtidos com a parametrização de todos as cotas coletadas mensalmente em dados mensais de mínima, máxima, e percentis de 25% (p25), 50% (p50) e 75% (p75).

<span id="page-73-0"></span>aos eventos extremos de cheia, como mostra a Figura. [21.](#page-73-0)

Figura 21 – Séries Temporais referentes ao conjunto de dados parametrizados contendo os valores mensais de mínima, máxima e quartis p25, p50 e p75 da base de dados do Rio Xingu. O eixo x vai de 0 a aproximadamente 400 porque o DataFrame resultante tem cerca de 400 linhas, cada linha representando um mês de dados.

### <span id="page-73-2"></span>**4.3.2 Gráficos de Recorrência**

Uma vez que este trabalho considera o processo de previsão a partir de gráficos de recorrência, é esperado que os dados de entrada da rede não sejam os valores de nível do rio no formato numérico visto na Tabela 3, mas sim dados de entrada no formato de imagem (representação gráfica 2D), conforme proposto.

Inicialmente foi conduzida uma prova de conceito que visou extrair dos dados existentes na série temporal o seu equivalente no formato de imagens. Para tal feito foi aplicada a validação temporal com janela deslizante, objetivando não só a representação dos valores de previsão da série no modo gráfico mas também assegurar que durante o processo de treinamento de *machine learning* não ocorram erros de previsão devido o uso de dados do futuro.

Segundo a literatura, o método da janela deslizante exige a definição de três hiperparâmetros essenciais: o tamanho da janela de treinamento, o tamanho da janela de previsão (horizonte) e os passos deslizantes, no qual: o tamanho da janela de treinamento refere-se ao número de pontos de dados incluídos em uma única passagem de treinamento; o tamanho da janela de previsão indica o número de pontos de dados que serão considerados na etapa de previsão; passos deslizantes representa a quantidade de pontos de dados que são pulados de uma passagem para outra, determinando o espaçamento entre as janelas de treinamento consecutivas [\(CHU,](#page-122-14) [1995\)](#page-122-14).

Isto posto, segmentou-se a série em intervalos de tempo usando um tamanho de janela fixa de treinamento igual a 20 unidades de tempo (20 meses), com um passo deslizante igual a 1 mês e uma janela de previsão (horizonte) equivalente ao mês seguinte ao conjunto de pontos utilizados na janela fixa de treinamento. A Figura [22](#page-74-0) ilustra o esquema de janelamento realizado nos dados da série.

<span id="page-74-0"></span>Figura 22 – Esquema demonstrativo do processo de janelamento.

Cada janela gerou uma imagem no formato de gráfico de recorrência, de modo que cada imagem representa o valor de um ponto na série.

Fonte – Próprio autor.

A validação dos RPs foi feita a partir da correspondência do gráfico com o valor de previsão numérico feito inicialmente, sendo assim, foi conduzida a última etapa de pré-processamento. Essa fase consistiu em obter os gráficos de recorrência correspondentes à série temporal completa de cada quartil dos *dataset* da Tabela [3.](#page-69-1) O processo de extração da representação gráfica do sistema é exemplificado na Figura [23.](#page-75-0)

<span id="page-75-0"></span>Figura 23 – Conversão de cada uma das séries temporais (mínima, máxima, p25, p50 e p75) em gráficos de recorrência gerados a partir de matrizes 20x20.

Fonte – Próprio autor.

A técnica de gráficos de recorrência é comumente empregada na análise de sistemas dinâmicos, sendo especialmente relevante para séries temporais estacionárias, como é o caso das séries do rio Xingu. No contexto do processamento de sinais, essa abordagem visa aprofundar a análise de séries temporais por meio do reconhecimento de padrões presentes nos gráficos de recorrência correspondente aos quartis de 25%, 50%, 75%, os valores máximos e mínimos das séries temporais. Cada série temporal de quartil foi convertido em uma matriz 20x20. A Figura [24](#page-76-0) apresenta os resultados dos gráficos de recorrência referentes à cada série temporal em sua totalidade.

<span id="page-76-0"></span>Figura 24 – Gráficos de recorrência referentes à cada série temporal - mínima, máxima, p25, p50 e p75 Fonte – Próprio autor.

Considerando o conjunto de dados e as suas características, a implementação da combinação entre RP e redes neurais convolucionais se apresenta como um recurso inovador no que diz respeito à analise de comportamento desses dados para a proposta de previsões. O padrão formado pelo gráfico de recorrência fornece uma visão útil do sistema. A visualização em um espaço dimensional 2D permite a observação dos aspectos de comportamento da série temporal, das trajetórias de espaço e a evolução do dado na série temporal [\(KIRICHENKO; ZINCHENKO;](#page-124-0) [RADIVILOVA,](#page-124-0) [2021\)](#page-124-0). Desta forma, o RP apresenta-se como o tipo adequado de entrada para a aplicação na rede neural convolucional, para enfim atingir o objetivo de predição do nível do rio. Após o gráfico de recorrência ser produzido para cada segmento, a próxima fase foi realizar o processo de empilhamento dos Gráficos de Recorrência (RPs). Esta abordagem constitui uma estratégia que viabiliza a captura de diversas perspectivas ou características presentes nas séries temporais. Cada canal resultante representa uma visão única dos padrões de recorrência contidos nos dados. Essa técnica revela-se valiosa quando se busca preservar informações cruciais e aprimorar a representação da complexidade das séries temporais.

Ao empregar a técnica de empilhamento, os gráficos de recorrência são tratados como canais, possibilitando a exploração de diferentes aspectos do comportamento recorrente. Essa abordagem permite a análise de variações ao longo do tempo ou em diferentes partes dos dados, oferecendo uma compreensão mais abrangente e detalhada das propriedades temporais das séries temporais em questão.

<span id="page-77-1"></span><span id="page-77-0"></span>A Figura [25](#page-77-1) apresenta os gráficos individuais obtidos cada um com dimensões 20x20 e ilustra a etapa de empilhamento das matrizes, formando uma imagem 3D composta por cinco canais de gráficos de recorrência.

Figura 25 – Processo de conversão das séries temporais em gráficos de recorrência após a etaá de empilhamento.

Fonte – Próprio autor. O fluxo exibido na Figura [26](#page-78-1) delineia a abordagem metodológica empregada no desenvolvimento do estudo. No início observa-se o surgimento do *dataset* resultante, contendo os valores de quartis, após o pré-processamento dos dados originais. Em seguida, ocorre a conversão desses dados em séries temporais, que servem como base para a geração dos gráficos de recorrência. Posteriormente, esses gráficos bidimensionais são utilizados como entrada nas redes neurais convolucionais (CNN), findando na execução da tarefa de previsão dos dados de enchentes.

<span id="page-78-1"></span>Figura 26 – Sequência metodológica executada no desenvolvimento do projeto, contemplando as etapas de conversão do *data set* pré-processado em séries temporais, seguida da geração dos gráficos de recorrência, utilizados como entradas nas CNNs e, por fim, os resultados de previsão.

<span id="page-78-0"></span>Fonte – Próprio autor. ### <span id="page-79-1"></span>**4.3.3 Implementação**

Uma estratégia explorada neste estudo envolveu a aplicação do conjunto de dados do rio Xingu em modelos de redes neurais convencionais. O objetivo foi de proporcionar uma análise adicional de desempenho e eficiência preditiva em comparação com a abordagem de previsão baseada em gráficos de recorrência. Esses modelos foram aplicados à diferentes arquiteturas, gerando previsões para cada abordagem, que foram posteriormente avaliadas com base nas métricas definidas. O fluxograma das diversas etapas de implementação de arquiteturas adotadas neste estudo segue esquematizado na Figura [27.](#page-79-0)

<span id="page-79-0"></span>Figura 27 – Esquemático. Estrutura de arquiteturas e implementações adotados, contemplando os diferentes modelos utilizados (RP + CNN, LSTM, GRU e RNN) e também a adição da abordagem de transfer learning.

| Fonte – Próprio autor. |  |  |
|------------------------|--|--|
|------------------------|--|--|

Tal processo foi executado a partir da implementação dos algoritmos vistos na Figura [28,](#page-80-0) que demonstra as abordagem de implementação divididas em 3 fases. A primeira fase de implementação (Fase 1 - Figura [28\)](#page-80-0) considera a aplicação dos gráficos de recorrência resultantes das séries temporais do rio Xingu direto na rede CNN de configuração vista na Tabela [5.](#page-82-1) A segunda fase (Fase 2 - Figura [28\)](#page-80-0) adotou uma abordagem baseada na técnica de *transfer learning*, e esta foi implementada na arquitetura de rede CNN vista na Tabela [5.](#page-82-1) Por conseguinte, foram avaliados os resultados de previsão da rede com os dados de entrada do conjunto do Xingu. A terceira fase de implementação (Fase 3 - Figura [28\)](#page-80-0) considerou o enfoque no desenvolvimento de algoritmos de programação dos modelos convencionais de Rede Neural Recorrente *(Neural Recurrence Network - RNN)* utilizados em problemas de regressão. Para o trabalho em questão, foram desenvolvidos os modelos de memória de curto prazo longa *(Long Short Term Memory - LSTM)*, unidade recorrente fechada *(Gated Recurrent Unit - GRU)* e uma RNN simples de uma camada.

<span id="page-80-0"></span>Figura 28 – Esquemático. Divisão por faseamento das etapas executadas. Fase 1 - Geração dos gráficos de recorrência a partir das séries temporais e alimentação na CNN; Fase 2 - Adição da etapa de *transfer learning* ao processamento desenvolvimento na Fase 1; Fase 3 - Aplicação de modelos convencionais para fins comparativos das previsões obtidas

Fonte – Próprio autor.

### <span id="page-81-0"></span>**4.3.4 Conjunto de dados do rio Xingu + Gráfico de Recorrência aplicado na CNN**

O desenvolvimento da fase 1 representa a principal abordagem deste estudo, isto é, a previsão do nível do rio utilizando um modelo de rede neural convolucional com dados de entrada resultantes da associação com a técnica de Gráficos de Recorrência. Conforme mencionado no início da explicação metodológica deste capítulo, a CNN implementada possui como dado de entrada imagens no formato de gráficos de recorrência referente às séries temporais. A implementação realizou a formatação dos dados de entrada utilizando a biblioteca *TensorFlow* [\(ABADI](#page-120-1) *et al.*, [2015\)](#page-120-1), configurando a forma dos gráficos de recorrência em imagens com proporções de uma matriz (20x20). Após a obtenção de cada matriz foi realizado o processo de empilhamento, resultando em uma imagem de tamanho 20x20 com 5 canais conforme visto na Figura [25.](#page-77-0)

Na abordagem geral foi utilizado para treinar os modelos de redes neurais, uma proporção de divisão de 75% dos dados para treinamento e 25% para teste, nas fases 1 (um), 2 (dois) e 3 (três) vistas na Figur[a28.](#page-80-0) Os dados foram separados de modo que os meses mais recentes fossem usados na etapa de teste. A arquitetura do modelo de CNN utilizada por meio do método empírico inicia com três camadas convolucionais (Conv 1-3) com função de ativação ReLU *(Rectified Linear Unit)* pelas razões de sua simplicidade e a eficácia convencional. Assim sendo, a rede utiliza filtros de convolução para processar a entrada tridimensional de dimensões 20x20x5, mantendo as dimensões originais e aplicando *padding 'same'* para preservar a informação nas bordas. A camada de *max pooling* subsequente reduz pela metade as dimensões, utilizando um filtro 2x2 e mantendo *padding 'same'*. Em seguida, duas camadas convolucionais (Conv 4-5) processam a saída da camada anterior, resultando em representações mais complexas. Uma segunda camada de *max pooling* foi aplicada para reduzir as dimensões novamente.

As camadas Conv 6 e Conv 7 continuaram com o processo de extração de características, cada uma utilizando 40 filtros de convolução 3x3. As camadas de *max pooling* subsequentes continuaram com o processo de redução das dimensões. Após a terceira camada de *max pooling*, uma camada de *dropout* foi introduzida para prevenir *overfitting*. A camada *Flatten* transformou a saída em um vetor unidimensional, preparando-a para as camadas densas *(fully connected)*. Três camadas densas (Dense 1-3) seguidas por camadas de *dropout* conduziram à camada final com 1 neurônio, representando a saída da rede.

<span id="page-82-1"></span>A arquitetura da rede é resumida na Tabel[a5.](#page-82-1)

| Camadas    | Entrada   | Saída     | Filtro | Padding |  |
|------------|-----------|-----------|--------|---------|--|
| Conv1      | 20×20×5   | 20×20×5   | 3      | same    |  |
| Conv2      | 20×20×5   | 20×20×100 | 3      | same    |  |
| Conv3      | 20×20×100 | 20×20×100 | 3      | same    |  |
| Maxpooling | 20×20×5   | 20×20×100 | 2      | same    |  |
| Conv4      | 20×20×100 | 20×20×10  | 3      | same    |  |
| Conv5      | 20×20×10  | 20×20×10  | 3      | same    |  |
| Maxpooling | 20×20×10  | 20×20×10  | 2      | same    |  |
| Conv6      | 20×20×10  | 20×20×40  | 3      | same    |  |
| Conv7      | 20×20×40  | 20×20×40  | 3      | same    |  |
| Maxpooling | 20×20×40  | 20×20×40  | 2      | same    |  |
| Dropout1   | 20×20×40  | 20×20×40  | −      | −       |  |
| Flatten    | 20×20×40  | 16000     | −      | −       |  |
| Dropout2   | 16000     | 16000     | −      | −       |  |
| Dense1     | 16000     | 512       | −      | −       |  |
| Dropout3   | 512       | 512       | −      | −       |  |
| Dense2     | 512       | 32        | −      | −       |  |
| Dropout4   | 32        | 32        | −      | −       |  |
| Dense3     | 32        | 1         | −      | −       |  |

Tabela 5 – Arquitetura da Rede Neural Convolucional

A Figura [29](#page-82-0) ilustra as etapas e camadas da arquitetura da rede neural convolucional CNN implementada no desenvolvimento deste trabalho referente ao que foi descrito na Tabela [5.](#page-82-1)

<span id="page-82-0"></span>Figura 29 – Arquitetura da rede CNN

Fonte – Próprio autor.

### <span id="page-82-2"></span>**4.4 Abordagens Convencionais**

Para fins de análise e comparação da aplicabilidade da abordagem proposta neste estudo, foram adicionalmente conduzidas implementações focadas em modelos convencionais de Rede Neural. Essas implementações incluem:

∙ Baseline: Ponto de Referência Inicial

- ∙ Rede Neural Convolucional (CNN) com *Transfer Learning* (Aprendizado por Transferência).
- ∙ Rede Neural Recorrente Simples Simple (RNN)
- ∙ Rede LSTM *(Long Short-Term Memory)*
- ∙ Rede GRU *(Gated Recurrent Unit)*

A análise do desempenho preditivo desses modelos de rede proporciona a identificação da performance de previsão para o conjunto de dados do Rio Xingu. Esta avaliação oferece uma perspectiva valiosa sobre o valor agregado da proposta em questão. A seguir serão apresentadas em maior detalhamento a arquitetura de cada abordagem.

### <span id="page-83-0"></span>**4.4.1 Baseline: Ponto de Referência Inicial (Previsão Ingênua)**

Uma prática interessante no campo de estudo e avaliação de desempenho das redes neurais é estabelecer o ponto de referência inicial, o qual representa o desempenho mínimo alcançado por um modelo, diante do ganho obtido por modelos mais sofisticados [\(LAWRENCE;](#page-125-12) [EDMUNDSON; O'CONNOR,](#page-125-12) [2000\)](#page-125-12). Isto posto, tendo como alvo principal o desempenho de previsão resultante da abordagem principal deste trabalho - sendo a previsão de enchentes a partir dos gráficos de recorrência aplicado a rede neural convolucional, foi então estabelecido um *baseline* de referência.

O *baseline* ou o modelo de previsão ingênuo não ajustado, também conhecido como *naive forecasting* na literatura, é uma abordagem que, em geral, consiste em extrapolar o valor mais recentemente observado para o futuro. Nesse método, a previsão para o próximo período é determinada simplesmente tomando-se o último valor conhecido, sem considerar a sazonalidade da variável dependente [\(MAKRIDAKIS; WHEELWRIGHT; MCGEE,](#page-125-13) [1983\)](#page-125-13).

Assim, visando fornecer uma medida inicial do desempenho do modelo sem qualquer otimização e ajuste dos hiper parâmetros, sendo crucial para entender o quão bem o modelo principal se saiu diante do conjunto de dados do rio Xingu, foi desenvolvido um *Baseline* que seguiu a lógica para duas medidas de observação de referência. A primeira delas é com base no valor médio, ou seja, calcula-se a média da série temporal total e a partir de um vetor de valor unitário de 1 multiplica-se pelo valor médio de previsão de cada saída da série. Isso implica que todas as previsões serão baseadas na estimativa do valor médio, conforme ilustrado na Figura [30.](#page-84-0)

A segunda avaliação de *baseline* foi baseada no último valor, no qual ocorre a varredura de toda a série temporal e para cada uma das séries utilizasse o valor do último dia e estimasse que o valor seguinte será o mesmo que o valor do dia anterior. A Figura [31](#page-84-1) ilustra o fluxo do *baseline* implementado.

<span id="page-84-0"></span>Figura 30 – Processo esquemático do desenvolvimento de *Baseline* conforme abordagem do valor médio

Fonte – Próprio autor.

<span id="page-84-1"></span>Figura 31 – Processo esquemático do desenvolvimento de *Baseline* conforme abordagem do último valor Fonte – Próprio autor.

Para avaliação e acompanhamento dos resultados de previsão referente ao *baseline*, foram utilizadas as métricas de: função de perda do *Mean Absolute Error* (MAE) e o *coefficient of determination* (R2).

### <span id="page-84-2"></span>**4.4.2 Rede Neural Convolucional - (CNN) com Transfer Learning**

Ao abordar o conjunto principal de estudo deste trabalho, que consiste nas séries temporais do rio Xingu, identificou-se que um dos desafios potenciais a serem superados no processo de previsão estaria relacionado à escassez de dados devido à presença de valores ausentes. Portanto, o treinamento de uma Rede Neural Convolucional (CNN) a partir do zero torna-se uma tarefa árdua. Além disso, o treinamento de CNNs profundas demanda recursos consideráveis, tornando-se uma empreitada financeiramente custosa.

Logo, objetivou-se a estratégia de utilizar um modelo pré-treinado com o objetivo de gerar previsões e avaliar seu desempenho em comparação com a implementação principal deste trabalho, que envolveu o modelo de rede neural convolucional (CNN) em conjunto com os gráficos de recorrência sem estar pré treinado.

A técnica de aprendizado por transferência *(transfer learning)* é uma abordagem na qual um modelo treinado em uma tarefa é reutilizado ou adaptado para uma tarefa relacionada [\(WANG,](#page-129-8) [2022\)](#page-129-8). Em vez de treinar um modelo do zero, o conhecimento adquirido durante o treinamento em uma tarefa inicial é transferido para uma tarefa secundária. Isso é particularmente útil quando há uma falta de dados para a tarefa secundária, pois o modelo pré-treinado já aprendeu representações úteis em sua tarefa original (LU *[et al.](#page-125-14)*, [2023\)](#page-125-14).

Para o processo de *transfer learning* foram selecionados 12 conjuntos de rios os quais tiveram como critério de seleção possuírem dados de cotas referente a níveis de máxima dos rios, analogamente ao conjunto de dados principal do rio Xingu. O modelo de CNN foi treinado com gráficos de recorrência provenientes dos conjuntos dos 12 rios para assim possibilitar maior robustez ao modelo de CNN + RP, na tentativa de gerar resultados de previsão possivelmente mais precisos. Visou-se que ao aplicar o *dataset* do rio Xingu em um modelo pré – treinado a rede apresentaria uma melhor eficiência na capacidade de generalização de um novo conjunto de dados. A Figura [32](#page-85-0) ilustra o fluxo de operações realizado nessa implementação.

<span id="page-85-0"></span>Figura 32 – Esquemático do processo de adição da etapa de *transfer learning* ao método desenvolvido visando melhoria da capacidade de previsão

Foi aplicado o mesmo procedimento de tratamento de dados associado à técnica de *recurrence plot*. O processo de pré-treinamento envolveu os 12 conjuntos de dados do rio, totalizando 1200 dados. Após o pré-treinamento foi realizado o teste no modelo com o conjunto de dados do rio Xingu. Para isso, as nove primeiras camadas (as camadas mais profundas) foram congeladas e assim retreinou-se apenas as últimas camadas que de fato interpretariam o que foi aprendido e por fim gerou-se o valor de previsão do nível do rio Xingu. Para a avaliação e acompanhamento dos resultados de previsão referente a configuração do modelo de rede neural definido, foram utilizadas as métricas de: função de perda do *Mean Absolute Error* (MAE) e o *coefficient of determination* (R2). Em problemas de monitoramento ambiental, prever valores com erros grandes pode ter consequências ambientais negativas. Por exemplo, previsões

imprecisas no nível do rio podem resultar em enchentes catastróficas de grandes perdas. O MAE mede a média das diferenças absolutas entre as previsões do modelo e os valores reais. Portanto, sua utilização possui como vantagem o tratamento de todos os erros de maneira igual, mostrando-se útil em situações em que erros grandes podem ser problemáticos. Já o uso do R2 justifica-se a partir do ponto onde essa métrica é útil para entender o ajuste global do modelo aos dados. Tal métrica varia entre 0 e 1, sendo que um valor mais próximo de 1 indica que o modelo é capaz de explicar uma grande parte da variabilidade nos dados [\(SCHNEIDER; XHAFA,](#page-127-10) [2022;](#page-127-10) [SAPRA,](#page-127-11) [2014\)](#page-127-11).

### <span id="page-86-1"></span>**4.4.3 Rede Neural Recorrente**

A terceira fase desse desenvolvimento contou com a implementação da arquitetura de uma Rede Neural Recorrente (RNN). As RNNs são um tipo de arquitetura de rede neural projetada para lidar com dados sequenciais e dados temporais. Ao contrário das redes neurais recorrentes, as RNNs têm conexões que formam *loops*, permitindo que informações sejam persistidas entre passos de tempo. No entanto, as RNNs podem ter dificuldades em capturar dependências de longo prazo devido ao problema do gradiente que desaparece ou explode durante o treinamento [\(PRIYANKA; KUMARI; SOOD,](#page-127-12) [2021\)](#page-127-12).

A implementação realizada foi referente a um modelo do Keras [\(CHOLLET](#page-122-15) *et al.*, [2015\)](#page-122-15), que permite empilhar camadas em sequência. A definição dos parâmetros se deu de maneira empírica, com a primeira camada sendo do tipo SimpleRNN, a entrada da rede possui uma forma de (20, 5) indicando dados tridimensionais referente à imagem do gráfico de recorrência. Possui 300 neurônios e utiliza a função de ativação "RELU". A segunda camada, do tipo Dense, conta com 1 neurônio. O modelo apresenta um total de 92,101 parâmetros ajustáveis. O otimizador utilizado é o Adam com uma taxa de aprendizado de 0.001, a função de perda é baseada no erro médio quadrático *(mean squared error)*. Para avaliação do desempenho do modelo foi definida a métrica personalizada R2. A Tabela [6](#page-86-0) apresenta o resumo da arquitetura implementada.

Tabela 6 – Arquitetura da Rede Neural com SimpleRNN

<span id="page-86-0"></span>

| Camada    | Unidades | Ativação | Inicialização de Peso   |
|-----------|----------|----------|-------------------------|
| SimpleRNN | 300      | ReLU     | Glorot Normal (seed=42) |
| Dense     | 1        | Linear   | Glorot Normal (seed=42) |

### <span id="page-86-2"></span>**4.4.4 Modelo Long Short-Term Memory (LSTM)**

A principal diferença entre as arquiteturas LSTM e SimpleRNN está na natureza das camadas recorrentes que são utilizadas. No caso deste modelo LSTM foi definido seguir o mesmo padrão de camadas utilizado na rede RNN, sendo portanto composto por duas camadas: a primeira, do tipo LSTM, com 300 neurônios, e a segunda, do tipo Dense, com 1 neurônio. O número total de parâmetros ajustáveis foi de 367,501. O modelo foi configurado para minimizar

<span id="page-87-0"></span>o erro quadrático médio durante o treinamento, e a métrica R2 foi usada para avaliação do modelo. A tabela [17](#page-104-1) resume a arquitetura do modelo.

| Camada | Unidades | Ativação | Entrada | Inicialização           |
|--------|----------|----------|---------|-------------------------|
| LSTM   | 300      | ReLU     | (20, 5) | Glorot Normal (Seed=42) |
| Dense  | 1        | Linear   | -       | Glorot Normal (Seed=42) |

Tabela 7 – Arquitetura da Rede Neural LSTM

### <span id="page-87-2"></span>**4.4.5 Modelos Gated Recurrent Unit (GRU)**

O modelo *Gated Recurrent Unit* (GRU) é uma variação das células recorrentes tradicionais específica para lidar com dependências de longo prazo em sequências e apresentam menor suscetibilidade ao *overfitting* em comparação com os modelos LSTM (LIU *[et al.](#page-125-15)*, [2023\)](#page-125-15). A configuração do modelo GRU implementado seguiu a mesma configuração de camadas das redes recorrentes anteriores sendo uma camada GRU com 300 neurônios e uma camada Dense com 1 neurônio, totalizando 276,601 parâmetros ajustáveis. A Tabela [8](#page-87-1) apresenta a configuração do modelo GRU.

Tabela 8 – Arquitetura da Rede Neural com GRU

<span id="page-87-1"></span>

| Camada | Unidades | Ativação | Entrada | Inicialização           |
|--------|----------|----------|---------|-------------------------|
| GRU    | 300      | ReLU     | (20, 5) | Glorot Normal (seed=42) |
| Dense  | 1        | Linear   | -       | Glorot Normal (seed=42) |

Para além das métricas de MAE e R2 utilizadas, foi calculado o coeficiente de Eficiência de Nash-Sutcliffe (NSE) para avaliar o resultado de desempenho do modelo de previsão principal, CNN\_com\_RP aplicado ao conjunto de dados do rio Xingu.

### <span id="page-87-3"></span>**4.5 Considerações Finais**

Ao longo deste capítulo, foi detalhado minuciosamente a metodologia empregada para alcançar os objetivos desta pesquisa. Iniciou-se com a apresentação da metodologia de abordagem e contextualização, destacando-se a escolha das técnicas e ferramentas adequadas para a tarefa em questão. Em seguida, explorou-se os detalhes da aplicação das técnicas de rede neural artificial, incluindo CNN, RNN, LSTM e GRU, destacando suas características e benefícios. Além disso, foi discutida a técnica de *Recurrence Plot* e sua relevância para a análise de séries temporais, juntamente com a seleção dos algoritmos específicos.

# CAPÍTULO 5

# **RESULTADOS**

<span id="page-88-0"></span>O presente capítulo é dedicado à apresentação dos resultados da pesquisa. Aqui estão reunidos os dados, análises e resoluções obtidos neste trabalho ao longo do processo de investigação da pesquisa levantada. Os resultados possibilitarão uma visão concreta das respostas para as perguntas de pesquisa e fornecerão *insights* cruciais para a compreensão do tópico em estudo. Este capítulo pretende de maneira clara e objetiva possibilitar a compreensão do que foi desenvolvido e como isso contribuir para o conhecimento existente na área. Consequentemente, pretende-se contribuir com o estado da arte da aplicação de redes neurais convolucionais associadas a técnica de gráficos de recorrência no processo de previsão de enchentes.

## <span id="page-88-1"></span>**5.1 Pré Processamento de Dados - Primeira Fase de Resultados**

Considerando a natureza deste estudo, os resultados se apresentam desde o início das experimentações computacionais. Isto é, a partir do tratamento das bases de dados caracterizamse os resultados referentes ao pré-processamento dos dados. Isto posto tem-se na Tabela [9](#page-89-0) os resultados referente a transformação de pré-processamento dos dados brutos do conjunto principal, *Dataset* do Rio Xingu.

<span id="page-89-0"></span>Tabela 9 – Tabela referente ao conjunto de dados pré-processados contendo dados correspondentes as cotas do nível do rio Xingu, com a exclusão de valores nulos e ausentes.

| Meses | Cota01 | Cota02 | Cota03 | Cota04 | Cota05 | Cota06 | Cota07 | Cota08 | Cota09 |
|-------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0     | 471.6  | 430.1  | 392.9  | 353.6  | 451.1  | 342.7  | 415.3  | 286.9  | 292.9  |
| 1     | 338.0  | 322.9  | 301.3  | 379.2  | 404.4  | 395.2  | 205.8  | 379.5  | 325.2  |
| 2     | 216.9  | 181.5  | 142.9  | 177.0  | 197.5  | 264.8  | 160.6  | 203.2  | 231.8  |
| 3     | 75.2   | 92.9   | 105.3  | 116.4  | 160.1  | 151.6  | 207.5  | 158.7  | 150.4  |
| 4     | 56.2   | 54.5   | 24.0   | 33.1   | 46.5   | 85.5   | 70.2   | 118.4  | 152.4  |
|       |        |        |        |        |        |        |        |        |        |
| 426   | 4.3    | 1.6    | 3.2    | 2.0    | 1.0    | 6.3    | 0.2    | 4.3    | 16.9   |
| 427   | 0.1    | 0.7    | 0.1    | 1.5    | 3.0    | 16.6   | 2.9    | 27.7   | 69.0   |
| 428   | 42.3   | 26.6   | 39.3   | 29.5   | 59.5   | 46.0   | 72.8   | 80.5   | 55.2   |
| 430   | 117.5  | 59.4   | 142.0  | 100.6  | 170.4  | 156.5  | 200.5  | 219.9  | 141.2  |
| 431   | 222.7  | 96.2   | 263.8  | 161.6  | 203.5  | 139.8  | 176.4  | 88.9   | 38.1   |

<span id="page-90-1"></span>Conforme apresentado na abordagem deste trabalho, outras 11 bases de rio foram utilizadas nos experimentos computacionais, não obstante o mesmo pré-processamento foi aplicado nos conjuntos de dados corresponde. Isto posto, tem-se a Tabela [10](#page-90-1) após o processo de *feature selection* do pré processamento, para as bases de dados: Kokraimoro, Joari, São João Felix do Xingu, base Neris1883, base Neris1886, porto, base Santo Antonio 1, base Santo Antonio 2, Belo Horizonte, Santo José e Jusante, resultando em um conjunto de dados único com 31 colunas de cotas.

Tabela 10 – Tabela de Dados de cota resultante do pré processamento das demais 11 bases de rios: Kokraimoro, Joari, São João Felix do Xingu, base Neris1883, base Neris1886, porto, base Santo Antonio 1, base Santo Antonio 2, Belo Horizonte, Santo José e Jusante; com a exclusão de valores nulos e ausentes.

| M<br>es<br>es | Co<br>0<br>1<br>ta | Co<br>0<br>2<br>ta | Co<br>0<br>3<br>ta | Co<br>0<br>4<br>ta | 5<br>Co<br>0<br>ta | Co<br>0<br>6<br>ta | Co<br>0<br>7<br>ta | <br>Co<br>2<br>6<br>ta | Co<br>2<br>7<br>ta | Co<br>2<br>8<br>ta | Co<br>2<br>9<br>ta | Co<br>3<br>0<br>ta | Co<br>3<br>1<br>ta |
|---------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| 3             | 9<br>0<br>7<br>7.  | 8<br>0<br>1.<br>0  | 9<br>8.<br>0<br>7  | 9<br>0<br>7<br>7.  | 9<br>5.<br>0<br>7  | 9<br>2.<br>0<br>7  | 8<br>9.<br>0<br>7  | <br>6<br>3<br>0<br>7.  | 6<br>3<br>3.<br>0  | 6<br>2<br>2.<br>0  | 6<br>1<br>0<br>7.  | 6<br>1<br>2.<br>0  | 6<br>1<br>0.<br>0  |
| 8             | 3<br>6<br>3.<br>0  | 3<br>5<br>9.<br>0  | 3<br>5<br>3.<br>0  | 3<br>5<br>0.<br>0  | 3<br>4<br>4.<br>0  | 3<br>3<br>9.<br>0  | 3<br>3<br>4.<br>0  | <br>2<br>6<br>0.<br>0  | 2<br>5<br>9.<br>0  | 2<br>5<br>3.<br>0  | 2<br>4<br>9.<br>0  | 2<br>4<br>5.<br>0  | 2<br>4<br>1.<br>0  |
| 9             | 3<br>6<br>2.<br>0  | 3<br>5<br>6.<br>0  | 3<br>5<br>1.<br>0  | 3<br>4<br>7.<br>0  | 3<br>4<br>3.<br>0  | 3<br>3<br>7.<br>0  | 3<br>5<br>3.<br>0  | <br>2<br>6<br>0.<br>0  | 2<br>5<br>6.<br>0  | 2<br>5<br>1.<br>0  | 2<br>4<br>8.<br>0  | 2<br>4<br>4.<br>0  | 2<br>4<br>0.<br>0  |
| 1<br>0        | 3<br>6<br>2.<br>0  | 5<br>3<br>7.<br>0  | 5<br>3<br>2.<br>0  | 3<br>4<br>8.<br>0  | 3<br>4<br>3.<br>0  | 3<br>3<br>8.<br>0  | 3<br>3<br>3.<br>0  | <br>2<br>6<br>0.<br>0  | 5<br>2<br>7.<br>0  | 5<br>2<br>2.<br>0  | 2<br>4<br>8.<br>0  | 2<br>4<br>4.<br>0  | 2<br>4<br>0.<br>0  |
| 1<br>1        | 6<br>3<br>2.<br>0  | 5<br>3<br>7.<br>0  | 5<br>3<br>2.<br>0  | 3<br>4<br>8.<br>0  | 3<br>4<br>3.<br>0  | 3<br>3<br>8.<br>0  | 3<br>3<br>3.<br>0  | <br>6<br>2<br>0.<br>0  | 5<br>2<br>7.<br>0  | 5<br>2<br>2.<br>0  | 2<br>4<br>8.<br>0  | 2<br>4<br>4.<br>0  | 2<br>4<br>0.<br>0  |
|               |                    |                    |                    |                    |                    |                    |                    | <br>                   |                    |                    |                    |                    |                    |
| 2<br>4<br>1   | 4<br>9<br>0.<br>0  | 4<br>8<br>8.<br>0  | 4<br>8<br>6.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>0.<br>0  | 4<br>7<br>8.<br>0  | 4<br>7<br>8.<br>0  | <br>4<br>5<br>0.<br>0  | 4<br>5<br>0.<br>0  | 4<br>5<br>0.<br>0  | 4<br>4<br>8.<br>0  | 4<br>4<br>8.<br>0  | 4<br>4<br>5.<br>0  |
| 2<br>4<br>2   | 4<br>9<br>0.<br>0  | 4<br>8<br>8.<br>0  | 4<br>8<br>6.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>0.<br>0  | 4<br>7<br>8.<br>0  | 4<br>7<br>8.<br>0  | <br>4<br>5<br>0.<br>0  | 4<br>5<br>0.<br>0  | 4<br>5<br>0.<br>0  | 4<br>4<br>8.<br>0  | 4<br>4<br>8.<br>0  | 4<br>4<br>5.<br>0  |
| 2<br>4<br>6   | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>9.<br>0  | <br>4<br>6<br>9.<br>0  | 4<br>7<br>3.<br>0  | 4<br>8<br>0.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>3.<br>0  |
| 2<br>4<br>7   | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>9.<br>0  | <br>6<br>4<br>9.<br>0  | 4<br>7<br>3.<br>0  | 4<br>8<br>0.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>3.<br>0  |
| 2<br>4<br>8   | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>4.<br>0  | 4<br>3<br>9.<br>0  | <br>4<br>6<br>9.<br>0  | 4<br>3.<br>0<br>7  | 4<br>8<br>0.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>3.<br>0  | 4<br>8<br>3.<br>0  |
|               |                    |                    |                    |                    |                    |                    |                    |                        |                    |                    |                    |                    |                    |

<span id="page-90-0"></span>Diante disso, ao dispor do conjunto principal de dados, o *data set* Xingu, juntamente com as outras 11 bases de suporte já tratadas, tem-se o início da fase de processamento. Fase esta na qual foram extraídas informações de maior significado para os processos de modelagem que se seguiram no racional técnico deste trabalho.

## <span id="page-91-2"></span>**5.2 Processamento de Dados - Segunda Fase de Resultados**

Recapitulando, a partir dos conjuntos de dados tratados foi realizada a etapa de processamento baseada na estratégia de quartis conforme discutido no capítulo anterior. Logo, para o conjunto de dados principal, *dataset* do rio Xingu, foram extraídos os percentis de quartis para os valores de mínimo, máximo, assim como para as proporções de 25%, 50%, 75% dos dados disponíveis na Tabela [10.](#page-90-0) Por fim, tem-se como resultado a Tabela [11](#page-91-0) demonstrando a distribuição dos dados considerando as medidas de quartis.

<span id="page-91-0"></span>

| meses | mínimo | máxima | percentil 25 | percentil 50 | percentil 75 |
|-------|--------|--------|--------------|--------------|--------------|
| 0     | 286.9  | 471.6  | 342.7        | 392.9        | 430.1        |
| 1     | 205.8  | 404.4  | 322.9        | 338.0        | 379.5        |
| 2     | 142.9  | 264.8  | 177.0        | 197.5        | 216.9        |
|       |        |        |              |              |              |
| 428   | 26.6   | 80.5   | 39.3         | 46.0         | 59.5         |
| 430   | 59.4   | 219.9  | 117.5        | 142.0        | 170.4        |
| 431   | 38.1   | 263.8  | 96.2         | 161.6        | 203.5        |

Tabela 11 – Conjunto de dados do rio Xingu em distribuição de percentis

Analogamente o mesmo processo de distribuição por quartil foi realizado para os outros 11 conjuntos de dados de cotas representados pela Tabela [10.](#page-90-0) Como resultado do processo de extração dos percentis de quartis tem-se a Tabela [12](#page-91-1) a seguir.

<span id="page-91-1"></span>Tabela 12 – Tabela de dados em distribuição de quartis das 11 bases de rios: Kokraimoro, Joari, São João Felix do Xingu, base Neris1883, base Neris1886, porto, base Santo Antonio 1, base Santo Antonio 2, Belo Horizonte, Santo José e Jusante

| meses | mínimo | máxima | percentil 25 | percentil 50 | percentil 75 |
|-------|--------|--------|--------------|--------------|--------------|
| 3     | 610.0  | 801.0  | 645.0        | 704.0        | 785.5        |
| 8     | 241.0  | 363.0  | 271.5        | 295.0        | 329.5        |
| 9     | 240.0  | 362.0  | 269.5        | 295.0        | 328.5        |
|       |        |        |              |              |              |
| 246   | 429.0  | 483.0  | 434.0        | 450.0        | 458.0        |
| 247   | 429.0  | 483.0  | 434.0        | 450.0        | 458.0        |
| 248   | 429.0  | 483.0  | 434.0        | 450.0        | 458.0        |

É importante destacar que a metodologia empregada resulta em que cada coluna da tabela de distribuição por quartil corresponda a uma série temporal única do rio Xingu. Esta abordagem se aplica igualmente às outras 11 bases fluviais analisadas. A vantagem deste formato de conjunto de dados é que ele proporciona uma representação uniforme, independentemente da base fluviométrica escolhida, e não é afetado pelo número de medições de cota disponíveis.

O próximo estágio de processamento foi extrair a representação gráfica das séries temporais de cada conjunto de dados da distribuição de quartis, isto é, as séries temporais correspon<span id="page-92-0"></span>dentes a Tabela [11](#page-91-0) e Tabela [12.](#page-91-1) As séries temporais referente ao conjunto de dados do rio Xingu em distribuição de percentis é ilustrada na Figura [33,](#page-92-0) relembrando que cada coluna corresponde a uma série temporal individual.

Figura 33 – Representação gráfica das séries temporais do rio Xingu, correspondentes as colunas de valores do conjunto de dados de distribuição por percentis de quartis.

Fonte – Próprio autor.

Analogamente tem-se as representações gráficas para as séries temporais referente aos conjuntos de dados dos demais 11 rios a partir da distribuição de percentis conforme Figura [34.](#page-93-0)

<span id="page-93-0"></span>Figura 34 – Representação gráfica das séries temporais correspondentes as colunas do conjunto de dados de distribuição por percentis de quartis dos demais 11 rios.

Fonte – Próprio autor.

Ao analisar a representação gráfica das séries temporais obtidas, torna-se evidente que, para os resultados originados do conjunto de dados do Xingu os picos de distribuição da série

temporal apresentam maior padrão de espaçamento horizontal. Isto reflete a natureza dos dados, pois representa o acompanhamento de uma única variável de um mesmo conjunto de dados. Em contrapartida, os resultados gráficos da Figura [33](#page-92-0) demonstram uma distribuição dos pontos resultante da soma de medidas das cotas de vários rios ao longo de um mesmo período, isto é, os pontos de pico possuem uma formação de largura horizontal mais densa. Essa característica também pode ser explicada pela sazonalidade do comportamento do rio ao longo do ano. Isso resulta na concentração de pontos em um mesmo intervalo de tempo, contribuindo para a densidade observada na representação gráfica.

### <span id="page-94-1"></span>**5.3 Recurrence Plot - Terceira Fase de Resultados**

No contexto em que os gráficos de recorrência são o ponto chave do racional técnico deste trabalho, é fundamental destacar que esse resultado somente se tornou possível por meio da transformação das séries temporais dos conjuntos em imagens 2D. Para validar o processo de transformação das séries temporais em gráficos de recorrência foi realizada uma prova de conceito. Esta se baseou no procedimento de validação temporal com janela deslizante, para assim extrair a representação gráfica 2D correspondente para cada ponto de previsão da serie temporal, como mostra a Figura [35.](#page-94-0)

Para o caso em questão foi utilizado o conjunto de dados do Rio Xingu com a definição de uma janela de treinamento de 20 dias (Valor arbitrário) para a previsão do valor do dia seguinte. Esse rastreamento gerou um grupo de imagem correspondente 409 gráficos para cada série temporal.

<span id="page-94-0"></span>Figura 35 – Representação gráfica das séries temporais do rio Xingu, correspondentes aos gráficos de recorrência.

Fonte – Próprio autor.

Após os resultados parciais da extração em formato 2D no padrão ponto a ponto da série temporal, foram então obtidos os gráficos de recorrência correspondente a representação total de cada uma das séries temporais obtidas a partir do conjunto de dados do rio Xingu em distribuição de percentis conforme demonstrado no Capítulo [4.](#page-66-0) As Figuras a seguir apresentam a amostragem de gráficos de recorrência referente as séries temporais de valores de máxima, mínima e do percentil de 25% , 50% e 75% dos dados do rio Xingu respectivamente.

<span id="page-95-0"></span>Figura 36 – Gráficos de recorrência correspondentes a série temporal de valores de máxima do rio Xingu

<span id="page-95-1"></span>Figura 37 – Gráficos de recorrência correspondentes a série temporal de valores de mínimo do rio Xingu

<span id="page-95-2"></span>Figura 38 – Gráficos de recorrência correspondentes a série temporal de valores de p25 do rio Xingu

<span id="page-96-0"></span>Figura 39 – Gráficos de recorrência correspondentes a série temporal de valores de p50 do rio Xingu

<span id="page-96-1"></span>Figura 40 – Gráficos de recorrência correspondentes a série temporal de valores de p75 do rio Xingu

Fonte – Próprio autor.

<span id="page-97-1"></span>

A Figura [41](#page-97-1) exibe uma seleção de amostras de resultado de gráficos de recorrência que compõem o conjunto de dados utilizado no treinamento dos modelos de rede neural.

<span id="page-97-0"></span>Figura 41 – Seleção de amostras de gráficos de recorrência em tempos distintos da série temporal. Essas amostras constituem o conjunto de dados de imagens utilizado no projeto.

> Fonte – Próprio autor.

96

Visando extrair o máximo de informações dos diferentes valores de dados contidos no conjunto do *dataset* do Xingu, realizou-se empilhamento dos gráficos de recorrência, resultando em 409 entradas de dimensão 20 × 20 com 5 canais cada. Como resultado tem-se na Figura [42](#page-98-0) o exemplo de empilhamento dos gráficos de recorrência referente ao tempo (*t0)*. Na Figura [42,](#page-98-0) cada canal representa uma série temporal que corresponde a uma coluna do conjunto de dados da Tabela [12.](#page-91-1) Dessa maneira, ao combinar informações de diferentes canais em uma única imagem, cada canal pode representar uma característica específica referente aos dados de sua série temporal, em um momento específico no tempo, proporcionando ao modelo mais informações para aprender padrões.

<span id="page-98-0"></span>Figura 42 – Seleção de amostras de gráficos de recorrência em tempos distintos da série temporal. Essas amostras constituem o conjunto de dados de imagens utilizado no projeto.

Fonte – Próprio autor.

Além do resultado de gráficos de recorrência obtidos por janelamento, foram gerados os gráficos de recorrência referente ao comportamento de toda série temporal, para fins ilustrativos, considerando todos os pontos da sequência. Dessa forma, possibilita-se a observação do ponto de vista gráfico o comportamento recorrente do sistema de cada série utilizada. As Figuras [43,](#page-99-0) [44,](#page-99-0) [45,](#page-99-0) [46](#page-99-0) e [47](#page-99-0) a seguir apresentam o gráfico de RP para cada série temporal.

<span id="page-99-0"></span>Figura 43 – Gráfico de Recorrência referente a série temporal de valores de máxima do nível do rio

Figura 45 – Gráfico de Recorrência referente a série temporal de valores de percentil 25

Figura 47 – Gráfico de Recorrência referente a série temporal de valores de percentil 75

Figura 44 – Gráfico de Recorrência referente a série temporal de valores de mínima do nível do rio

Figura 46 – Gráfico de Recorrência referente a série temporal de valores de percentil 50Ao comparar os padrões de recorrência dos gráficos referentes à máxima e mínima do rio, percebe-se que o gráfico de máxima apresentam padrões de maior estabilidade, uma vez que demonstra maior densidade dos pontos, sugerindo períodos de comportamentos previsíveis. Em contrapartida o gráfico de mínima indica maior espaçamento entre os pontos e menor densidade, o que sugere que tais variações podem representar um comportamento característico de mudanças mais abruptas e menos previsíveis dos dados da série temporal. Analogamente, verifica-se que entre os percentis de 25, 50 e 75, este último apresenta comportamento similar ao gráfico de máxima, com pontos homogeneamente distribuídos, enquanto os demais assemelham-se ao gráfico de mínima, ainda que também possuam padrões regulares. Uma vez que os padrões foram gerados a partir de uma ampla série temporal, a diferenciação dos padrões por perspectivas visuais pode não acarretar em conclusões facilitadas, devido a limitação humana. Dessa forma, tratamentos de dados estatísticos/matemáticos são implementados para extrair informações quantitativas para interpretação. Uma vez que não buscou-se a construção dos gráficos de recorrência para análise qualitativa, os mesmos foram gerados para serem utilizados como parâmetro de entrada para modelos de previsão, que serão apresentados na sequência.

## <span id="page-101-0"></span>**5.4 Implementação dos Modelos**

Neste trabalho de pesquisa, a principal proposta se baseou na tarefa de previsão do nível de máxima do rio através das séries temporais, a partir da implementação de uma rede neural convolucional associada a técnica de recurrence plot. Os resultados gerados pelos modelos de redes neurais recorrentes, como RNN, LSTM e GRU, serão inicialmente apresentados para servir como parâmetros de comparação de desempenho. Esta comparação é crucial para avaliar a eficácia da rede CNN no mesmo contexto. Após a exposição dos resultados alcançados com os modelos convencionalmente utilizados na literatura, prosseguiremos com a apresentação dos resultados da rede CNN, em conjunto com o RP. Além disso, abordaremos o desempenho dessa rede com a implementação da técnica de *transfer learning*,visando maiores embasamentos de argumentação. Nas seções de resultados a seguir, dar-se-a início a apresentação dos valores numéricos referente ao desempenho dos modelos implementados, abordando tanto a acurácia quanto a precisão dos valores observados e previstos. As métricas aqui consideradas são para o contexto de algoritmos de regressão.

Para a avaliação dos resultados de desempenho dos modelos implementados neste trabalho utilizou-se como métrica o Erro Absoluto Médio, do inglês *Mean Absolute Error (MAE)*, visando avaliar os valores de previsão obtidos com os modelos implementados. Vale lembrar que a MAE representa a média das diferenças absolutas entre os valores previstos e os valores reais obtidos pelo modelo [\(SCHNEIDER; XHAFA,](#page-127-0) [2022;](#page-127-0) [ALURU](#page-120-0) *et al.*, [2011\)](#page-120-0). A segunda métrica utilizada no processo de avaliação dos resultados do processo de previsão foi a métrica do coeficiente de determinação R2, que leva em consideração o percentual de variação da variável dependente que pode ser explicada pelas variáveis independentes. Ou seja, o R2 irá apresentar uma ideia de como as variáveis se relacionam em um modelo de regressão, adotando-se como valores de parâmetros a faixa de 0 a 1. Valores próximos a 0 indicam que o modelo tem pouca capacidade de previsibilidade e valores mais próximos de 1 representam uma maior capacidade de previsibilidade nos dados de resposta do modelo [\(SAPRA,](#page-127-1) [2014;](#page-127-1) [CASELLA; BERGER,](#page-121-0) [2001\)](#page-121-0).

A utilização das métricas MAE (Erro Médio Absoluto) e R2 (Coeficiente de Determinação) representa uma abordagem estratégica para uma avaliação mais abrangente e holística do desempenho do modelo. Enquanto o MAE fornece uma conceito sobre o erro médio das previsões, o R2 indica quão bem essas previsões estão ajustadas aos dados reais em termos de variância explicada.

Além da análise a partir das métricas citadas anteriormente, houve a captura de valor referente a métrica do "Coeficiente de Eficiência de Nash-Sutcliffe"(NSE), sendo esta uma métrica estatística utilizada para avaliar o desempenho de modelos de previsão em comparação com dados observados, específica para avaliar a qualidade do desempenho de modelos hidrológicos. É comum obter um valor de NSE no intervalo de menos infinito a 1, no qual tem-se para quanto mais próximo de 1 o modelo melhor é o seu ajuste aos dados observados, ou seja, conclui-se que

<span id="page-102-2"></span>o modelo é capaz de prever os valores com alta precisão [\(NASH; SUTCLIFFE,](#page-126-0) [1970\)](#page-126-0).

# **5.5 Modelo de Baseline - Resultado para ponto de Referência**

Partindo de uma perspectiva técnica na qual os modelos de aprendizado de máquina (machine learning) representam um processo iterativo de avanço, é crucial estabelecer um modelo de referência como linha de base. Esse modelo serve como um parâmetro inicial para comparar e avaliar o aprendizado nos demais modelos desenvolvidos neste trabalho. Nesse contexto, um modelo de baseline foi desenvolvido para estabelecer um ponto de partida para os modelos subsequentes. O baseline, caracterizado por sua simplicidade representativa, serve como um critério de avaliação essencial. Ele permite não apenas entender os valores alcançados nas demais implementações, mas também identificar potenciais falhas. Além disso, é particularmente importante para validar os resultados alcançados neste projeto de pesquisa. Para este modelo de *baseline* foram estalecidos dois processos de aprendizagem na obtenção dos valores de previsão e das métricas. O primeiro considera como fator de aprendizado o valor médio da série temporal. Isto é, os valores de previsão para qualquer ponto são a média de todos os valores anteriores da série temporal. Os resultados de métricas obtidos para o modelo que considera a média dos valores possui os valores apresentados na Tabela [13](#page-102-0) abaixo.

<span id="page-102-0"></span>Tabela 13 – Tabela de resultados métricos para o modelo *baseline* de média.

| Métrica | Treino | Teste |
|---------|--------|-------|
| MAE     | 120    | 123   |
| R2      | 0.0    | -0.01 |
|         |        |       |

| 1 | 0.0 |  |  | -0.0 |  |
|---|-----|--|--|------|--|
|   |     |  |  |      |  |

Fonte – Próprio Autor

O segundo modelo de baseline implementado considera no processo previsão o ultimo valor do conjunto como referência para prever o próximo dia. Ou seja, a partir de uma lógica simples considera-se apenas que a melhor previsão para o próximo ponto na série temporal é simplesmente o último valor observado. Os resultados de métricas obtidos para o modelo de baseline estabelecido possui os valores apresentados na Tabela [14](#page-102-1) abaixo.

<span id="page-102-1"></span>Tabela 14 – Tabela de resultados métricos para o modelo *baseline* de ultimo valor.

| Métrica | Treino | Teste |
|---------|--------|-------|
| MAE     | 88.44  | 76.17 |
| R2      | 0.36   | 0.53  |
|         |        |       |

Fonte – Próprio Autor

# **5.6 Modelos de Redes Neurais Recorrentes - Quarta Fase de Resultados**

## **5.6.1 Rede Neural Recorrente (RNN) - Resultados**

<span id="page-103-0"></span>Como parte fundamental do processo de avaliação da hipótese proposta neste trabalho de pesquisa, foi realizada a implementação de uma rede neural recorrente simples para o conjunto de dados de entrada de séries temporais multivariadas correspondente às representações de 5 canais dos gráficos de recorrência de quartis dos valores de cota e máxima do rio. A configuração de arquitetura da RNN utilizada pode ser vista na Tabela [15](#page-103-0) a seguir. Tabela 15 – Arquitetura do Modelo de Simple RNN

| Camadas   | Entradas | Saídas |
|-----------|----------|--------|
| SimpleRNN | (20, 5)  | (300)  |
| Dense     | (300)    | (1)    |

Fonte – Próprio Autor

Os valores de métrica obtidos para a arquitetura apresentada podem ser vistas na Tabela Tabela 16 – Tabela de métricas para o modelo RNN.

| Métrica | Treino | Teste | Geral |
|---------|--------|-------|-------|
| MAE     | 56.79  | 58.07 |       |
| R2      | 0.72   | 0.74  |       |
| NSE     | -      | -     | 0.74  |
|         |        |       |       |

<span id="page-103-2"></span>Fonte – Próprio Autor Os resultados das métricas contidos na tabela anterior podem ser visualizados graficamente a seguir, permitindo a observação do comportamento dos dados do conjunto. A Figura [48,](#page-103-2) apresenta a curva de R2 referente ao valor de previsão e de teste dos dados do conjunto.

Figura 48 – Gráfico de R2 referente ao desempenho do modelo de RNN para o conjunto de dados do rio Xingu.

Fonte – Próprio autor.

<span id="page-103-1"></span>[16.](#page-103-1)

A Figura [49](#page-104-0) apresenta o gráfico referente ao comportamento dos dados para os valores de treino e a Figura [50](#page-104-0) para os valores de teste do modelo.

<span id="page-104-0"></span>Figura 49 – Gráfico de Dispersão dos dados de previsão para o conjunto de treino do modelo de RNN Figura 50 – Gráfico de Dispersão dos dados de previsão para o conjunto de teste do modelo de RNN

Fonte – Próprio Autor

## **5.6.2 Rede Neural Long Short Term Memory (LSTM) - Resultados**

<span id="page-104-1"></span>A configuração de arquitetura de LSTM utilizada para essa implementação consta na Tabela [17.](#page-104-1)

| Camadas               | Entradas | Saídas |
|-----------------------|----------|--------|
| LSTM                  | (20, 5)  | (300)  |
| Dense                 | (300)    | (1)    |
| Fonte – Próprio Autor |          |        |

Tabela 17 – Arquitetura do Modelo LSTM de Rede Neural

<span id="page-104-2"></span>Os valores de métrica obtidos para a arquitetura do modelo de LSTM apresentada estão indicadas na Tabela [18.](#page-104-2)

Tabela 18 – Tabela de resultado para as métricas do modelo de LSTM.

| Métrica               | Treino | Teste | Geral |
|-----------------------|--------|-------|-------|
| MAE                   | 61.05  | 55.66 |       |
| R2                    | 0.71   | 0.71  |       |
| NSE                   | -      | -     | 0.71  |
| Fonte – Próprio Autor |        |       |       |

A Figura [51,](#page-105-0) apresenta as curvas de R2 referente ao valor de previsão e de teste dos dados do conjunto.

<span id="page-105-0"></span>Figura 51 – Gráfico de R2 referente ao desempenho do modelo de LSTM para o conjunto de dados do rio Xingu.

A Figura [52](#page-105-1) apresenta o gráfico referente ao comportamento dos dados para os valores de treino e a Figura [53](#page-105-1) para os valores de teste do modelo.

<span id="page-105-1"></span>Figura 52 – Gráfico de Dispersão dos dados de previsão para o conjunto de treino do modelo de LSTM

Figura 53 – Gráfico de Dispersão dos dados de previsão para o conjunto de teste do modelo de LSTM

## **5.6.3 Rede Neural Gated Recurrent Unit (GRU) - Resultados**

A configuração do modelo GRU implementada pode ser vista na Figura [19.](#page-106-0)

| Camadas | Entradas | Saídas |
|---------|----------|--------|
| GRU     | (20, 5)  | (300)  |
| Dense   | (300)    | (1)    |
|         |          |        |

<span id="page-106-0"></span>Tabela 19 – Arquitetura do Modelo GRU de Rede Neural

Fonte – Próprio Autor

<span id="page-106-1"></span>Os valores de métrica obtidos para a arquitetura do modelo de GRU apresentada estão indicadas na Tabela [20.](#page-106-1)

| Métrica               | Treino | Teste | Geral |
|-----------------------|--------|-------|-------|
| MAE                   | 51.44  | 52.72 |       |
| R2                    | 0.76   | 0.76  |       |
| NSE                   | -      | -     | 0.76  |
| Fonte – Próprio Autor |        |       |       |

Tabela 20 – Tabela de resultado para as métricas do modelo de GRU.

<span id="page-106-2"></span>A Figura [54,](#page-106-2) apresenta as curvas de R2 referente ao valor de previsão e de teste dos dados do conjunto.

Figura 54 – Gráfico de R2 referente ao desempenho do modelo de GRU para o conjunto de dados do rio Xingu.

Fonte – Próprio autor.

A Figura [55](#page-107-0) apresenta o gráfico referente ao comportamento dos dados para os valores de treino e a Figura [56](#page-107-0) para os valores de teste do modelo.

<span id="page-107-0"></span>Figura 55 – Gráfico de Dispersão dos dados de previsão para o conjunto de treino do modelo de GRU

Figura 56 – Gráfico de Dispersão dos dados de previsão para o conjunto de teste do modelo de GRU

Fonte – Próprio Autor

# **5.7 Rede CNN com Recurrence Plot - Quarta Fase de Resultados**

Tendo em vista que a abordagem principal deste trabalho considera a hipótese de previsão a partir de uma rede neural convolucional treinada com imagens de gráficos de recorrência, temse a implementação principal da CNN profunda com a arquitetura vista na Tabela [21.](#page-108-0) O conjunto de dados de entrada para esse experimento contém 409 imagens de plotagem de recorrência de tamanho 20x20 configurados por uma matriz de 5 canais para cada imagem.

<span id="page-107-1"></span>Os valores de métrica obtidos para a modelagem de CNN associado a técnica de recurrence plot estão indicados na Tabela [22.](#page-107-1)

| Métrica                | Treino | Teste | Geral |
|------------------------|--------|-------|-------|
| MAE                    | 36.60  | 50.85 | -     |
| R2                     | 0.88   | 0.74  | -     |
| NSE                    | -      | -     | 0.71  |
| Fonte – Próprio autor. |        |       |       |

Tabela 22 – Tabela de métricas para o modelo CNN com RP.

Os gráficos da Figura [57](#page-108-1) e Figura [58](#page-108-1) ilustram o comportamento de variança dos dados em relação a reta que representa a previsão ideal.

<span id="page-108-0"></span>

| Camadas     | Entradas  | Saídas    | Kernel size |
|-------------|-----------|-----------|-------------|
| Conv 1      | 20×20×5   | 20×20×5   | 3           |
| Conv 2      | 20×20×5   | 20×20×100 | 3           |
| Conv 3      | 20×20×100 | 20×20×100 | 3           |
| Max Pooling | 20×20×100 | 20×20×100 | 2           |
| Conv 4      | 20×20×100 | 20×20×10  | 3           |
| Conv 5      | 20×20×10  | 20×20×10  | 3           |
| Max Pooling | 20×20×10  | 20×20×10  | 2           |
| Conv 6      | 20×20×10  | 20×20×40  | 3           |
| Conv 7      | 20×20×40  | 20×20×40  | 3           |
| Max Pooling | 20×20×40  | 20×20×40  | 2           |
| Dropout 1   | 20×20×40  | 20×20×40  | -           |
| Flatten     | 20×20×40  | 16000     | -           |
| Dropout 2   | 16000     | 16000     | -           |
| Dense 1     | 16000     | 512       | -           |
| Dropout 3   | 512       | 512       | -           |
| Dense 2     | 512       | 32        | -           |
| Dropout 4   | 32        | 32        | -           |
| Dense 3     | 32        | 1         | -           |

Tabela 21 – Configuração da Rede CNN profunda

Fonte – Próprio autor.

<span id="page-108-1"></span>Figura 57 – Gráfico de Dispersão dos dados de previsão para o conjunto de treino do modelo de CNN com RP Figura 58 – Gráfico de Dispersão dos dados de previsão para o conjunto de teste do modelo de CNN com RP

# **5.8 Rede CNN com Transfer Learning - Quinta Fase de Resultados**

Considerou-se avaliar o desempenho da CNN principal a partir de uma abordagem que considerasse o pré treinamento da rede na tarefa de previsão. Isto posto, a rede CNN proposta foi submetida ao processo de *transfer learning*, para o qual foram utilizados no processo de treinamento 12 conjuntos de dados de diferentes rios, que totalizaram em 1200 dados, detalhados no Capítulo [4.](#page-66-0) O conjunto de dados de rios foi aplicado a mesma arquitetura do modelo de CNN com a configuração vista na Tabela [21.](#page-108-0)

Após concluir o treinamento com a base de dados composta pelos 12 rios, procedeu-se a fase de teste utilizando o conjunto de dados específicos do rio Xingu. Nessa etapa, optou-se por congelar as 9 camadas iniciais (as mais profundas) do modelo. Essa abordagem permitiu realizar um novo treinamento focado exclusivamente nas camadas finais, as quais desempenham a função de interpretação e geração das previsões para os níveis do rio Xingu com base no que foi aprendido no processo de *transfer learning*.

<span id="page-109-0"></span>Os valores de MAE de treino e teste e R2 de treino e testes obtidos, são apresentando na Tabela [23.](#page-109-0)

| Métrica               | Treino | Teste | Geral |
|-----------------------|--------|-------|-------|
| MAE                   | 47.20  | 83.16 |       |
| R2                    | 0.79   | 0.46  |       |
| NSE                   | -      | -     | 0.55  |
| Fonte – Próprio Autor |        |       |       |

Tabela 23 – Tabela de métricas para o modelo com transfer learning.

<span id="page-109-1"></span>Para o modelo de CNN com *tranfer learning* tem-se o gráfico de R2 na Figura [59](#page-109-1) que demonstram as curvas de treino e teste obtidos para esta abordagem.

Figura 59 – Gráficos da curva de treino e teste do coeficiente de determinação R2 para o modelo de CNN com transfer learning.

A seguir tem-se os gráficos resultantes para os valores de treino na Figura [60](#page-110-0) e valores de teste na Figura [61.](#page-110-0)

<span id="page-110-0"></span>Figura 60 – Gráfico de Dispersão dos dados de previsão para o conjunto de treino do modelo de CNN com *transfer learning*

Figura 61 – Gráfico de Dispersão dos dados de previsão para o conjunto de teste do modelo de CNN com *transfer learning*

## <span id="page-111-2"></span>**5.9 Discussão dos Resultados**

Nesta seção, será realizada à análise detalhada dos resultados obtidos, explorando as implicações e o significado dos valores obtidos em relação aos objetivos estabelecidos no início do estudo. A Tabela [24](#page-111-0) apresenta o resumo de todos os valores métricos obtidos em cada uma das implementações de DL desenvolvidas.

<span id="page-111-0"></span>

|       | Abordagem                                   | Métricas      |              |              |             |      |
|-------|---------------------------------------------|---------------|--------------|--------------|-------------|------|
|       |                                             | MAE<br>TREINO | MAE<br>TESTE | R2<br>TREINO | R2<br>TESTE | NSE  |
| Xingu | CNN com RP +<br>Transfer Learning (11 Rios) | 47,20         | 83,16        | 0,79         | 0,46        | 0,55 |
| Xingu | CNN com RP                                  | 36,60         | 50,85        | 0,87         | 0,74        | 0,70 |
| Xingu | RNN sem RP                                  | 56,79         | 58,07        | 0,72         | 0,74        | 0,74 |
| Xingu | LSTM sem RP                                 | 61,05         | 55,66        | 0,71         | 0,71        | 0,71 |
| Xingu | GRU sem RP                                  | 51,44         | 52,72        | 0,76         | 0,76        | 0,76 |

Tabela 24 – Tabela dos Resultados dos Modelos

Fonte – Próprio Autor

O processo de avaliação dos resultados das métricas estão diretamente ligados a relevância do valor obtido para a escala dos dados que são tratados neste projeto. Portanto, considerando que o nível do rio Xingu é medido em centímetros e que seu período de cheias é influenciado principalmente pelas precipitações na região (valores de cotas do *dataset*), assim como possui seu pico de cheias tipicamente entre os meses de março e maio. Para estabelecer o valor de referência tomou-se como base os dados do relatório de operação do sistema de alerta hidrológico da bacia do rio Xingu de 2023, publicado em outubro de 2023. Este determina os valores de cota para as classes de: nível de atenção, alerta e inundação, como mostra a tabela [25.](#page-111-1) Portanto, definiu-se o valor de 800 cm para referência, correspondente ao valor de pico para atenção. Esse valor serve como parâmetro para comparar a relevância das métricas obtidas. Em outras palavras, esse valor de referência será utilizado para quantificar o risco associado às previsões no contexto da gestão do rio e da proteção contra enchentes.

<span id="page-111-1"></span>Tabela 25 – Cota de atenção, alerta e inundação do SAH – Xingu. 2023

| Nome da Estação | RIO   | Cotas (cm) |        |           |  |  |
|-----------------|-------|------------|--------|-----------|--|--|
|                 |       | Atenção    | Alerta | Inundação |  |  |
| Altamira        | Xingu | 800        | 850    | 950       |  |  |

### Considerações para MAE e R2

Isto posto,tomando como parâmetro de referência 800 cm para o nível do rio, a análise das métricas leva em conta o impacto do erro no valor observado. Ao discutir os resultados de desempenho, a abordagem CNN\_com\_RP supera os modelos RNN, LSTM e GRU. No treinamento, a CNN\_com\_RP apresenta um Erro Médio Absoluto (MAE\_TRAIN) de 36,60, demonstrando sua eficácia em captar as características dos dados de treino, superando as técnicas de recorrência. Essa eficiência pode ser creditada ao uso da técnica de gráfico de recorrência, que contribui na extração de características complexas dos dados. No teste, a CNN\_com\_RP também se destaca com um MAE\_TEST de 50,85, indicando uma melhor generalização para dados novos em comparação com os outros modelos. Interessante notar que o modelo GRU, com uma pequena diferença entre o MAE de treino (51,44) e teste (52,72), mostra uma boa capacidade de generalização, obtendo o segundo melhor desempenho.Contudo, os valores de desempenhos não surpreendem para os modelos de regressão tendo em vista serem especializados nesse tipo de problemática.

O aumento do valor no MAE\_TEST da CNN\_com\_RP, contudo, sugere um possível sobreajuste *(overfitting)* aos dados de treino. Considerando o valor de referência de 800 cm e o MAE\_TEST alcançado, isso implica em um erro médio de previsão de cerca de 50 unidades. Por exemplo, uma previsão que deveria ser 800 cm poderia resultar em 850 cm, o que poderia levar a um alerta equivocado de subida do nível do rio na bacia do rio Xingu. Esse sobreajuste *(overfitting)* pode estar relacionado ao tamanho limitado do conjunto de dados de treinamento; um conjunto maior poderia melhorar a capacidade do modelo de generalizar a partir da amostra.

No processo de avaliação deve-se observar a métrica de R2 em conjunto com os valores de MAE para uma conclusão completa. Portanto, retomando os valores vistos na Tabela [24](#page-111-0) nota-se que a CNN\_com\_RP apresentou o maior R2 para o conjunto de treino (0,87), o que indica que o modelo foi capaz de aprender e capturar a maior parte da variância nos dados de treinamento em comparação com os outros modelos. Para o conjunto de teste o resultado de R2 com melhor desempenho, por uma diferença menor que 3%, atribui-se ao modelo de GRU com um (R2\_TEST = 0,76), quando comparado com o valor do conjunto de teste (R2\_TEST = 0,74) obtido no modelo da CNN\_com\_RP. Os modelos LSTM e RNN tiveram um R2 de treino e teste muito próximos (LSTM com 0,71 e RNN com 0,72 para treino e 0,71 e 0,74 para teste, respectivamente. Ambos resultados satisfatórios no entanto se igualaram ao valor obtido pelo modelo de CNN\_com\_RP. Considerando que a abordagem principal não possui em sua estrutura uma construção dedicada para problemáticas de regressão, o valor de R2 obtido no teste para a CNN\_com\_RP mostra-se mais do que satisfatório na tarefa de previsão de nível de máxima do rio, com marguem para otimizações no seu desempenho.

No entanto, é cabível uma avaliação do ponto de vista de escolha do modelo para outras situações como por exemplo, se o objetivo for a busca por ter um modelo mais explicativo para os dados de treinamento, a CNN\_com\_RP seria a melhor escolha. No entanto, se a capacidade de generalização for mais importante, o GRU seria a melhor opção, seguido pelo modelo RNN, contudo tais resultados de performance como este já eram esperados para tais modelos.

Na busca por obter melhores valores para as métricas de MAE e R2 do modelo de CNN\_com\_RP, utilizou-se como estratégia o uso do pré treinamento da rede com conjuntos de dados maiores para que assim ao realizar os testes com o conjunto do Xingu o modelo tivesse maior capacidade de generalização dos dados. Contudo, os resultados se mostraram inferires em relação ao modelo puro sem pré treinamento, com valores de MAE de treino e teste igual a 47,20, 83,16 e um R2 de treino e teste igual a 0,79 e 0,46, respectivamente. Possivelmente esses resultados reflitam que a distribuição dos dados utilizados no treinamento sejam significativamente diferentes da distribuição do conjunto de teste resultando em um modelo que com baixa capacidade de generalização do modelo, ou ainda que os dados de treinamento continham muitos ruído ou erros, e o modelo aprendeu característica distorcidas se tornando ineficiente para a tarefa de previsão do modelo do Xingu.

### Considerações para o Coeficiente de NSE

A CNN\_com\_RP demonstrou um bom desempenho em comparação com os modelos de rede recorrente, com um NSE de 0,7 indicando que a CNN tem boa correspondência entre os valores previstos e os observados para o modelo, assim como está capturando uma porção substancial da variabilidade dos dados. O valor obtido na abordagem principal foi o mesmo para a arquitetura do modelo LSTM, o qual vale relembrar, possui em sua estrutura de arquitetura características que o tornam adequado para tarefas e conjuntos de dados de séries temporais. De fato o melhor resultado de NSE deve ser atribuído ao modelo GRU, sendo este uma variação da RNN que também é capaz de capturar dependências temporais, mas com uma estrutura mais simples que a LSTM, obteve um valor de 0,76. Revelando que a GRU foi a mais competente em prever os valores corretos e em capturar a variabilidade dos dados.

De maneira geral um NSE próximo de 1 nos dados de teste é especialmente importante, pois indica uma boa generalização do modelo para dados não vistos durante o treinamento. Analisando do ponto de vista da hipótese proposta nesse trabalho, a implementação de uma rede CNN associada aos gráficos de recorrência na tarefa de previsão com series temporais se mostrou satisfatória considerando o NSE.

### Considerações de Análise Gráfica

A partir da representação gráfica é possível extrair análises de desempenho com base na dispersão dos pontos em relação a linha vermelha que representa a linha de previsão perfeita, onde as previsões do modelo são exatamente iguais aos valores reais. Além disso, os gráficos auxiliam a corroborar os valores numéricos obtidos nas métricas.

Observando a variança dos pontos em relação a reta de linha de ajuste, conclui-se o modelo com melhor desempenho pode ser atribuído a abordagem da CNN\_com\_RP para o qual os dados de teste são semelhante ao desempenho nos dados de treino, sendo portanto um <span id="page-114-0"></span>sinal positivo de que não há sobreajuste (*overfitting*) significativo no processo de previsão dos resultados. Contudo o modelo pode se beneficiar de técnicas de regularização para diminuir a variância das previsões ou também implementar a engenharia de seleção de dados o que poderia otimizar a capacidade do modelo de capturar as dinâmicas subjacentes, particularmente para previsões de valores mais elevados.

O modelo GRU sendo um dos modelos com melhores resultados de implementação pareceu generalizar de maneira satisfatória já que o padrão de dispersão nos dados de teste reflete a dos dados de treino, apesar de visualmente apresentar uma precisão ligeiramente menor. Uma segunda característica ao observar os gráficos do modelo de GRU, é a variância que se mostra crescente com valores de teste mais altos, podendo ser um sinal de que o modelo pode não ter capturado completamente a complexidade subjacente dos dados ou que pode estar faltando dados representativos para valores mais altos no conjunto de treinamento. A análise gráfica para os demais modelos LSTM e RNN apresentam comportamento de dispersão semelhantes ao de GRU. Exibindo um desempenho razoável em ambos os conjuntos de dados, porém a precisão das previsões diminui para valores de teste mais altos, a consistência na tendência de dispersão entre treino e teste sugere que os modelos não sofreram *overfitting* significativo, mantendo um padrão de previsão para ambos os conjuntos.

### Discussão Geral

Analisando os resultados sob duas perspectivas distintas – quantitativa, pelas métricas, e qualitativa, pela interpretação gráfica dos dados –, observa-se que o modelo CNN\_com\_RP obteve o melhor desempenho no treinamento. Este modelo registrou o menor MAE e o mais alto R2, evidenciando um ajuste superior aos dados de treino. Entretanto, notou-se um possível sobreajuste, refletido pelo aumento do MAE e pela redução do R2 na transição do treino para o teste. A despeito disso, a análise gráfica possibilita um olhar complementar em que o modelo CNN\_com\_RP ajusta-se bem aos dados, um resultado que pode ser atribuído a vantagem do uso de gráficos de recorrência. Visto que a análise de recorrência agrega valor ao modelo devido a capacidade de captar dependências temporais, portanto o uso dos RPs oferece a robustez contra ruídos e variações, discernindo padrões consistentes durante o treinamento [\(KIRICHENKO;](#page-124-0) [RADIVILOVA; STEPANENKO,](#page-124-0) [2021\)](#page-124-0).

Por outro lado, a abordagem de Transfer Learning apresentou limitações, indicadas pelo aumento do MAE de teste e pela queda nos índices R2 e NSE, sugerindo que o modelo pré-treinado pode não ser o mais adequado para a tarefa em questão. Já os modelos LSTM e RNN, mostraram a consistência esperada em arquiteturas projetadas para séries temporais, como demonstrado pela similaridade nos valores de R2 entre os conjuntos de treino e teste, evidenciando um equilíbrio entre ajuste e generalização.

Destaca-se ainda o modelo GRU, que demonstrou equilíbrio geral. Apresentou um bom desempenho de treino e resultados de teste levemente superiores aos da CNN\_com\_RP, tanto em R2 quanto em NSE, consolidando-se como uma abordagem eficaz.

Adicionalmente, a análise dos resultados das implementações revela um aprendizado substancial dos modelos em relação aos valores de *baseline* estabelecidos. O *baseline* , seja a referencia média ou o último valor observado, não alcançaram um R2 superior a 0,5 assim como um MAE próximo de 0,5 enquanto que todos os modelos implementados superaram esses referenciais, reafirmando a eficácia dos métodos de aprendizado de máquina para a tarefa em análise.

# CAPÍTULO 6

# **CONCLUSÃO**

Com o intuito de proporcionar uma compreensão mais abrangente, é relevante salientar que os resultados apresentados na seção anterior estão intrinsecamente ligados ao objetivo geral da pesquisa, o qual explora a possibilidade de que, a partir dos dados mensais de níveis pluviométricos do rio quando utilizados como dados de entrada no formato de gráficos de recorrência em um modelo de rede neural convolucional, tem-se a oportunidade de prever os níveis do rio e a realizar a previsão de enchentes. Para isso, retomando os objetivos específicos estipulados no início do projeto, conforme exposto:

- ∙ *Transformar a série temporal dos níveis de máxima do rio Xingu em representações matriciais bidimensionais, particularmente os gráficos de recorrência;*
- ∙ *Estimar a ocorrência de enchentes baseado nessas representações, com uso de redes neurais profundas;*
- ∙ *Realizar análise preditiva de enchentes com outras arquiteturas de redes neurais, como redes neurais recorrentes para fins de comparação;*
- ∙ *Comparar diferentes métricas dos modelos obtidos, usando diferentes parametrizações para modelagem e treinamento.*

podemos concluir que, de maneira geral, a implementação da metodologia proposta neste projeto permitiu atingir os objetivos pretendidos com êxito.

A transformação da série temporal dos níveis máximos do rio Xingu em representações matriciais bidimensionais foi realizada com sucesso. A partir do janelamento do dataset referente às medidas de quartis, máximas e mínimos, foi possível transformar os valores numéricos em gráficos de recorrência, obtendo como produto 409 imagens com 5 canais cada.

A principal inovação deste trabalho residiu em alcançar o objetivo de usar as séries temporais transformadas em gráficos de recorrência, e assim, utilizar como entradas para uma Rede Neural Convolucional (CNN). Esta abordagem metodológica foi projetada para avaliar a eficácia das CNNs em tarefas de previsão e regressão, uma aplicação menos convencional para estas redes, que são tradicionalmente usadas em problemas de classificação. A combinação da CNN com a técnica de "recurrence plot"(gráficos de recorrência) permitiu explorar novas fronteiras no uso de CNNs para previsão. Dessa forma, a abordagem utilizada permitiu também alcançar o objetivo de estimar a ocorrência de enchentes, utilizando redes neurais profundas baseadas nessas representações matriciais.

Os resultados obtidos a partir desta abordagem inovadora foram comparados com resultados provenientes de redes neurais recorrentes. Dessa forma, foi possível utilizar as implementações de arquiteturas das redes RNN, LSTM e GRU como uma base comparativa valiosa para avaliar o desempenho da abordagem principal. Parte do aspecto comparativo crucial abrangeu o objetivo específico de realizar comparações usando diferentes métricas, como MAE, R2 e Coeficiente Nash-Sutcliffe, para obter uma perspectiva mais detalhada e embasada sobre a eficácia de cada modelo.

A partir dos resultados obtidos com a Rede Neural Convolucional (CNN) implementada, o presente trabalho demonstrou o grande potencial de aplicação desta abordagem, cujo desempenho equiparou-se à eficácia da melhor rede de arquitetura especializada, em particular a Gated Recurrent Unit (GRU). Além disso, a CNN superou significativamente outras redes especializadas, como a Long Short-Term Memory (LSTM) e a Recurrent Neural Network (RNN), em termos de desempenho. Esta constatação ressalta a competência e a adequação da CNN para as tarefas específicas abordadas no estudo. A eficácia dos resultados obtidos com a CNN no processo de previsão pode ser atribuída à integração da CNN com a técnica de gráficos de recorrência, que aprimorou significativamente a análise de padrões nos dados usados para previsão. Os gráficos de recorrência demonstraram ser fundamental para capturar a complexidade e as nuances dos padrões nos dados temporais, permitindo visualizar padrões de repetição não facilmente capturados por outras técnicas, o que resulta no potencial notável de sua utilização em sistemas de previsões.

As conclusões aqui apresentadas não se basearam apenas na aplicação prática da metodologia, mas também em uma análise comparativa rigorosa, reforçando a solidez e a relevância dos resultados alcançados neste estudo. Alcançar os objetivos propostos de carácter inovador não só demonstrou a viabilidade das CNNs em previsões complexas, mas também forneceu *insights* valiosos para o campo da inteligência artificial. Os resultados deste estudo abrem caminho para futuras pesquisas na aplicação de redes neurais convolucionais em desafios de previsão, expandindo seu escopo além das tradicionais tarefas de classificação.

## **6.1 Trabalhos Futuros**

A conclusão deste trabalho representa o início de uma jornada fascinante no campo de predição de enchentes. Apesar de explorar os resultados referentes ao *dataset* do rio Xingu, a abordagem apresenta uma estrutura que permite expandir sua aplicabilidade para qualquer base de dado, respeitando-se a metodologia aqui desenvolvida e validada. Os resultados obtidos trazem novas perspectivas das redes neurais convolucionais para aplicações além dos aspectos da classificação e detecção, mas também abrem um leque de novas perguntas para que lacunas que surgiram durante o desenvolvimento possam ser preenchidas e que representam oportunidades valiosas para pesquisas futuras. Este capítulo esboça algumas direções para futuras pesquisas, destacando a importância de continuar explorando os seguintes aspectos:

- ∙ Considerar no processo de seleção dos dados as variáveis climáticas ( temperaturas médias, eventos de onda de calor, chuvas intensas) que possam também influenciar na periodicidade dos eventos relatados;
- ∙ Agregar ao conjunto de dados variáveis metrológicas que possam influenciar modelos de previsão hidrológicas como : umidade, temperatura do ar, pressão atmosférica;
- ∙ Desenvolver uma estrutura que possibilite uma janela de previsão de maior espaçamento;

ABADI, M.; AGARWAL, A.; BARHAM, P.; BREVDO, E.; CHEN, Z.; CITRO, C.; CORRADO, G. S.; DAVIS, A.; DEAN, J.; DEVIN, M.; GHEMAWAT, S.; GOODFELLOW, I.; HARP, A.; IRVING, G.; ISARD, M.; JIA, Y.; JOZEFOWICZ, R.; KAISER, L.; KUDLUR, M.; LEVEN-BERG, J.; MANé, D.; MONGA, R.; MOORE, S.; MURRAY, D.; OLAH, C.; SCHUSTER, M.; SHLENS, J.; STEINER, B.; SUTSKEVER, I.; TALWAR, K.; TUCKER, P.; VANHOUCKE, V.; VASUDEVAN, V.; VIéGAS, F.; VINYALS, O.; WARDEN, P.; WATTENBERG, M.; WICKE, M.; YU, Y.; ZHENG, X. TensorFlow: Large-Scale Machine Learning on Heterogeneous Systems. 2015. [<https://www.tensorflow.org/>.](https://www.tensorflow.org/) Citado na página [80.](#page-81-0)

AGONAFIR, C.; LAKHANKAR, T.; KHANBILVARDI, R.; KRAKAUER, N.; RADELL, D.; DEVINENI, N. A review of recent advances in urban flood research. Water Security, v. 19, p. 100141, 2023. ISSN 2468-3124. Disponível em: [<https://www.sciencedirect.com/science/article/](https://www.sciencedirect.com/science/article/pii/S2468312423000093) [pii/S2468312423000093>.](https://www.sciencedirect.com/science/article/pii/S2468312423000093) Citado na página [58.](#page-59-0)

Agência Nacional de Águas (ANA). HidroWeb - Sistema Nacional de Informações sobre Recursos Hídricos. 2023. Disponível em: [<https://www.snirh.gov.br/hidroweb/apresentacao>.](https://www.snirh.gov.br/hidroweb/apresentacao) Citado na página [67.](#page-68-0)

ALBERTON, G. B.; SEVERO, D. L.; MELO, M. N. V. d.; POTELICKI, H.; SARTORI, A. Aplicação de redes neurais artificiais para previsão de enchentes no rio itajaí-açu em blumenau, sc, brasil. Revista Ibero-Americana de Ciências Ambientais - RICA, v. 12, n. 4, p. 686–696, 2021. ISSN 2179-6858. Citado nas páginas [60](#page-61-0) e [64.](#page-65-0)

<span id="page-120-0"></span>ALURU, S.; BANDYOPADHYAY, S.; CATALYUREK, U. V.; DUBHASHI, D. P.; JONES, P. H.; PARASHAR, M.; SCHMIDT, B. Contemporary Computing. 1. ed. [S.l.]: Springer, 2011. ISBN 978-3-642-22606-9. Citado na página [100.](#page-101-0)

AMOR, F. N. del; PRATS-BOLUDA, G.; LI, W.; JUAN, J. L. M. de; YANG, L.; YANG, Y.; HAO, D.; YE-LIN, Y. Recurrence quantification analysis of uterine vectormyometriogram to identify pregnant women with threatened preterm labor. Biomedical Signal Processing and Control, v. 89, p. 105795, 2024. ISSN 1746-8094. Disponível em: [<https://www.sciencedirect.](https://www.sciencedirect.com/science/article/pii/S1746809423012284) [com/science/article/pii/S1746809423012284>.](https://www.sciencedirect.com/science/article/pii/S1746809423012284) Citado na página [48.](#page-49-0)

AURELIEN, G. Mãos à Obra: Aprendizado de Máquina com Scikit-Lear & TensorFlow. Rio de Janeiro: "O'Reilly Media, Inc", 2019. v. 1. Citado nas páginas [15,](#page-16-0) [27,](#page-28-0) [46,](#page-47-0) [47,](#page-48-0) [48](#page-49-0) e [53.](#page-54-0)

AYOADE, J. O. Introdução a Climatologia para os Trópicos. Rio de Janeiro, v. 4, 1996. Citado na página [33.](#page-34-0)

BABICHEV, S.; LYTVYNENKO, V.; WóJCIK, W.; VYSHEMYRSKAYA, S. Lecture Notes in Computational Intelligence and Decision Making. Poland, v. 1246, 2020. Citado nas páginas [28](#page-29-0) e [30.](#page-31-0)

BATISTA, M. A. Aplicação de gráficos de recorrência na análise de casos notificados de dengue, atendimento antirrábico humano e leishmaniose. 104 p. Dissertação (Mestrado) — Faculdade de Medicina de São José do Rio Preto, Sao José do Rio Preto, 2011. Citado nas páginas [49](#page-50-0) e [50.](#page-51-0)

BERKELEY, U. of C. Undertanding Science, How science really works. 2007. Disponível em: [<https://undsci.berkeley.edu/index.php>.](https://undsci.berkeley.edu/index.php) Acesso em: 05/04/2021. Citado nas páginas [26](#page-27-0) e [46.](#page-47-0)

BOX, G. E. P.; JENKINS, G. Time Series Analysis: Forecasting and Control. [S.l.]: Holden-Day, 1976. Citado na página [38.](#page-39-0)

BOX, G. E. P.; PIERCE, D. A. Distribution of residual autocorrelations in autoregressiveintegrated moving average time series models. Journal of the American Statistical Association, Taylor Francis, v. 65, n. 332, p. 1509–1526, 1970. Citado na página [37.](#page-38-0)

BRAGAGNOLO, L.; SILVA, R. V.; GRZYBOWSKI, J. M. V. Comitê de redes neurais artificiais aplicado ao mapeamento de Áreas suscetíveis a deslizamentos. In: I END - Encontro Nacional de Desastres. Porto Alegre-RS, Brasil: [s.n.], 2018. p. 1 – 8. Citado na página [36.](#page-37-0)

BRASIL. Estudo inédito mostra moradores sujeitos a enchentes e deslizamentos. Geociências, 2019. Disponível em: [<https://](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/21566-estudo-inedito-mostra-moradores-sujeitos-a-enchentes-e-deslizamentos) [agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/21566-estudo-inedito-mostra-moradores-sujeitos-a-enchentes-e-deslizamentos) [21566-estudo-inedito-mostra-moradores-sujeitos-a-enchentes-e-deslizamentos>.](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/21566-estudo-inedito-mostra-moradores-sujeitos-a-enchentes-e-deslizamentos) Citado na página [31.](#page-32-0)

. Confederação Nacional de Municípios. Brasília: [s.n.], 2023. Citado nas páginas [26](#page-27-0) e [32.](#page-33-0)

BRIGHENTI, T. M.; BONIMá, N. B.; CHAFFE, P. L. Calibração hierárquica do modelo swat em uma bacia hidrográfica catarinense. Revista Brasileira de Recursos Hídricos, v. 21, n. 1, 2015. Citado na página [55.](#page-56-0)

BROCKWELL, J. P.; DAVIS, R. A. Introduction to Time Series and Forecasting. 2. ed. [S.l.]: Springer, 2002. ISBN 0387953515. Citado na página [37.](#page-38-0)

BROWNLEE, J. Tour of Data Sampling Methods for Imbalanced Classification:2020. 2020. Disponível em: [<https://machinelearningmastery.com/](https://machinelearningmastery.com/data-sampling-methods-for-imbalanced-classification/) [data-sampling-methods-for-imbalanced-classification/>.](https://machinelearningmastery.com/data-sampling-methods-for-imbalanced-classification/) Acesso em: 06/04/2021. Citado na página [29.](#page-30-0)

BUDA, M.; MAKI, A.; MAZUROWSKI, M. A. Asystematic study of the class imbalance problem in convolutional neural networks. Elsevier, v. 106, n. 2, p. 249 – 259, 2018. Citado na página [28.](#page-29-0)

CANHOLI, A. P. Drenagem Urbana e Controle de enchentes. São Paulo, v. 2, 2014. Citado na página [26.](#page-27-0)

CARRIZOSA, M.; COHEN, M.; GUTMAN, M.; LEITE, F.; LóPEZ, D.; NESPRIAS, J. Enfrentar el riesgo. Nuevas prácticas de resiliencia urbana en América Latina. Caracas, v. 1, 2019. Citado na página [36.](#page-37-0)

<span id="page-121-0"></span>CASELLA, G.; BERGER, R. Statistical Inference. [S.l.]: Duxbury Resource Center, 2001. Textbook Binding. ISBN 0534243126. Citado na página [100.](#page-101-0)

CASERI, A. N.; SANTOS, L. B. L.; STEPHANY, S. A convolutional recurrent neural network for strong convective rainfall nowcasting using weather radar data in southeastern brazil. Artificial Intelligence in Geosciences, v. 3, p. 8–13, 2022. ISSN 2666-5441. Disponível em: [<https:](https://www.sciencedirect.com/science/article/pii/S2666544122000211) [//www.sciencedirect.com/science/article/pii/S2666544122000211>.](https://www.sciencedirect.com/science/article/pii/S2666544122000211) Citado nas páginas [59](#page-60-0) e [64.](#page-65-0)

CHALMERS, A. F. O que é ciência afinal. Rio de Janeiro, v. 1, 1993. Citado na página [25.](#page-26-0)

CHEN, C.; HUI, Q.; XIE, W.; WAN, S.; ZHOU, Y.; PEI, Q. Convolutional neural networks for forecasting flood process in internet-of-things enabled smart city. Computer Networks, v. 186, p. 107744, 2021. ISSN 1389-1286. Disponível em: [<https://www.sciencedirect.com/science/](https://www.sciencedirect.com/science/article/pii/S1389128620313281) [article/pii/S1389128620313281>.](https://www.sciencedirect.com/science/article/pii/S1389128620313281) Citado nas páginas [53,](#page-54-0) [58](#page-59-0) e [64.](#page-65-0)

CHOLLET, F. *et al.* Keras. 2015. Version 2.0.8. Disponível em: [<https://keras.io>.](https://keras.io) Citado na página [85.](#page-86-0)

CHU, C.-S. J. Time series segmentation: A sliding window approach. Information Sciences, v. 85, n. 1, p. 147–173, 1995. ISSN 0020-0255. Disponível em: [<https://www.sciencedirect.com/](https://www.sciencedirect.com/science/article/pii/002002559500021G) [science/article/pii/002002559500021G>.](https://www.sciencedirect.com/science/article/pii/002002559500021G) Citado na página [73.](#page-74-0)

CNN, S. P. Chuva arrasta carros durante alagamento em são carlos (sp); veja imagens. CNN Brasil, 2020. Disponível em: [<https://www.cnnbrasil.com.br/nacional/](https://www.cnnbrasil.com.br/nacional/chuva-arrasta-carros-durante-alagamento-em-sao-carlos-sp-veja-imagens/) [chuva-arrasta-carros-durante-alagamento-em-sao-carlos-sp-veja-imagens/>.](https://www.cnnbrasil.com.br/nacional/chuva-arrasta-carros-durante-alagamento-em-sao-carlos-sp-veja-imagens/) Citado nas páginas [15](#page-16-0) e [35.](#page-36-0)

COSTA, H. R. d. O.; MIYAZAKI, L. C. P. Análise preliminar dos dados pluviométricos e caracterização das áreas de risco à enchente, inundação e alagamento na cidade de capinópolis/mg. Boletim de Geografia, v. 33, n. 3, p. 46–67, mar. 2016. Disponível em: [<https://periodicos.uem.](https://periodicos.uem.br/ojs/index.php/BolGeogr/article/view/23760) [br/ojs/index.php/BolGeogr/article/view/23760>.](https://periodicos.uem.br/ojs/index.php/BolGeogr/article/view/23760) Citado na página [34.](#page-35-0)

COWPERTWAIT, P.; METCALFE, A. Introductory Time Series With R. [S.l.]: Springer, 2009. ISBN 0387886974, 9780387886978. Citado na página [37.](#page-38-0)

CRISTALDO, M. F.; JESUS, L. d.; OLIVEIRA, P. T. d.; SOUZA, C. C. d.; VIGANÓ, H. H. G.; PADOVANI, C. R. Redes neurais artificiais aplicadas à previsão de enchentes para região do pantanal no mato grosso do sul. Geociências (São Paulo, Brazil), v. 39, n. 1, p. 191–201, 2020. ISSN 1980-900X. Citado nas páginas [60](#page-61-0) e [64.](#page-65-0)

DALAGNOL, R.; GRAMCIANINOV, C. B.; CRESPO, N. M.; CHIQUETTO, R. L. B.; MAR-QUES, M. T. A.; NETO, G. D.; ABREU, R. C. de; LI, S.; LOTT, F. C.; ANDERSON, L. O.; SPARROW, S. Extreme rainfall and its impacts in the brazilian minasgerais state in january: Can we blame climate change? Climate Resil Sustain, v. 1, p. 1–15, 2021. Citado na página [35.](#page-36-0)

DUBREUIL, V.; FANTE, K. P.; PLANCHON, O.; NETO, J. L. S. Os tipos de climas anuais no brasil : uma aplicação da classificação de köppen de 1961 a 2015. Confins, v. 37, 2018. Disponível em: [<http://journals.openedition.org/confins/15738>.](http://journals.openedition.org/confins/15738) Citado na página [33.](#page-34-0)

ECKMANN, J.-P.; KAMPHORST, S. O.; RUELLE, D. Recurrence plots of dynamical systems. Europhysics Letters, v. 4, n. 9, p. 973, nov 1987. Disponível em: [<https://dx.doi.org/10.1209/](https://dx.doi.org/10.1209/0295-5075/4/9/004) [0295-5075/4/9/004>.](https://dx.doi.org/10.1209/0295-5075/4/9/004) Citado nas páginas [48](#page-49-0) e [49.](#page-50-0)

EHLERS, R. S. Análise de Séries Temporais. Paraná: LEG, Departamento de Estatística e Geoinformação, UFPR, 2005. v. 3. Disponível em: [<http://www.est.ufpr.br/ehlers/notas>.](http://www.est.ufpr.br/ehlers/notas) Acesso em: 16 nov 2022. Citado nas páginas [15](#page-16-0) e [37.](#page-38-0)

EPA. Storm Water Management Model. 2021. Disponível em: [<https://www.epa.gov/](https://www.epa.gov/water-research/storm-water-management-model-swmm) [water-research/storm-water-management-model-swmm>.](https://www.epa.gov/water-research/storm-water-management-model-swmm) Acesso em: 06 Agosto 2021. Citado na página [56.](#page-57-0)

Estados Unidos da America. Ocha: Brasil entre países com maior número de pessoas expostas a inundações. 2020. Disponível em[:<https://news.un.org/pt/story/2020/01/1699571>.](https://news.un.org/pt/story/2020/01/1699571) Acesso em: 06 agosto 2021. Citado na página [35.](#page-36-0)

FAGUNDES, E. Projetos de inteligência artificial. Green and Digital Business, 2021. Disponível em: [<https://efagundes.com/projetos-de-inteligencia-artificial/>.](https://efagundes.com/projetos-de-inteligencia-artificial/) Citado nas páginas [15](#page-16-0) e [44.](#page-45-0)

FATHIAN, F.; MEHDIZADEH, S.; SALES, A. K.; SAFARI, M. J. S. Hybrid models to improve the monthly river flow prediction: Integrating artificial intelligence and non-linear time series models. Journal of Hydrology, v. 575, p. 1200–1213, 2019. ISSN 0022-1694. Disponível em: [<https://www.sciencedirect.com/science/article/pii/S0022169419305748>.](https://www.sciencedirect.com/science/article/pii/S0022169419305748) Citado nas páginas [53,](#page-54-0) [55](#page-56-0) e [64.](#page-65-0)

FENG, Z. K.; NIU, W. J. Hybrid artificial neural network and cooperation search algorithm for nonlinear river flow time series forecasting in humid and semi-humid regions. Knowledge Based Systems, v. 211, p. 49–53, 2021. Citado nas páginas [53,](#page-54-0) [54](#page-55-0) e [64.](#page-65-0)

FERREIRA, D. C. Caminhos do rio xingu: Povos, paisagens e belezas naturais no médio xingu. Resvista de Antropologias, v. 11, p. 859–871, 2019. Citado na página [27.](#page-28-0)

FRANCO, C. R. Inteligência Artificial. Iadaial: Uniasselvi, 2017. v. 1. Citado na página [40.](#page-41-0)

GAO, J.; CAI, H. On the structures and quantification of recurrence plots. Physics Letters A, v. 270, n. 1, p. 75–87, 2000. ISSN 0375-9601. Disponível em: [<https://www.sciencedirect.com/](https://www.sciencedirect.com/science/article/pii/S0375960100003042) [science/article/pii/S0375960100003042>.](https://www.sciencedirect.com/science/article/pii/S0375960100003042) Citado na página [49.](#page-50-0)

GIRÃO, I. R. F.; RABELO, D. R.; ZANELLA, M. E. Análise teórica dos conceitos: Riscos socioambientais, vulnerabilidade esuscetibilidade. Regne, v. 4, n. Edição EspeciAL, p. 71–83, 2018. Citado na página [25.](#page-26-0)

GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. Deep learning. [S.l.]: MIT press, 2016. Citado na página [41.](#page-42-0)

. Deep Learning. London, England, v. 1, 2017. Citado na página [46.](#page-47-0)

GOSWAMI, B. A brief introduction to nonlinear time series analysis and recurrence plots. Vibration, v. 2, n. 4, p. 332–368, 2019. ISSN 2571-631X. Disponível em: [<https://www.mdpi.](https://www.mdpi.com/2571-631X/2/4/21) [com/2571-631X/2/4/21>.](https://www.mdpi.com/2571-631X/2/4/21) Citado na página [49.](#page-50-0)

GRANEMMAN, E. Caracterizacão de Sistemas Dinâmicos atraves de Gráficos de Recorrência. 104 p. Dissertação (Mestrado) — Universidade Federal do Paraná, Curitiba, 2008. Citado na página [49.](#page-50-0)

GUHA, S.; JANA, R. K.; SANYAL, M. K. Artificial neural network approaches for disaster management: A literature review. International Journal of Disaster Risk Reduction, v. 81, p. 103276, 2022. ISSN 2212-4209. Disponível em: [<https://www.sciencedirect.com/science/article/](https://www.sciencedirect.com/science/article/pii/S2212420922004952) [pii/S2212420922004952>.](https://www.sciencedirect.com/science/article/pii/S2212420922004952) Citado na página [53.](#page-54-0)

HA, S.; LIU, D.; MU, L. Prediction of yangtze river streamflow based on deep learning neural network with el niño–southern oscillation. Scientific Reports, v. 1, n. 11738, p. 49–58, 2021. Citado nas páginas [57](#page-58-0) e [64.](#page-65-0)

HASSAN, J. Arima and regression models for prediction of daily and monthly clearness index. Renewable Energy, v. 68, p. 421–427, 2014. ISSN 0960-1481. Disponível em: [<https://www.](https://www.sciencedirect.com/science/article/pii/S0960148114000962) [sciencedirect.com/science/article/pii/S0960148114000962>.](https://www.sciencedirect.com/science/article/pii/S0960148114000962) Citado na página [39.](#page-40-0)

HE, Q.; YU, F.; CHANG, J.; OUYANG, C. Fuzzy granular recurrence plot and quantification analysis: A novel method for classification. Pattern Recognition, v. 139, p. 109456, 2023. ISSN 0031-3203. Disponível em: [<https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/S0031320323001565) [S0031320323001565>.](https://www.sciencedirect.com/science/article/pii/S0031320323001565) Citado na página [48.](#page-49-0)

HELSEL, D. R.; HIRSCH, R. M. Statistical methods in water resources. USGS Publications Warehouse, 2002. Citado nas páginas [70](#page-71-0) e [71.](#page-72-0)

HOCHREITER, S.; SCHMIDHUBER, J. Long short-term memory. Neural computation, MIT Press, v. 9, n. 8, p. 1735–1780, 1997. Citado nas páginas [27,](#page-28-0) [53](#page-54-0) e [55.](#page-56-0)

IBGE. GRID, Gestão de Riscos e Desastres. 2013. Disponível em: [<http://www.ufrgs.br/grid/](http://www.ufrgs.br/grid/noticias/ibge-desastres-naturais-atingiram-40-9-dos-municipios-do-pais-nos-ultimos-anos) [noticias/ibge-desastres-naturais-atingiram-40-9-dos-municipios-do-pais-nos-ultimos-anos>.](http://www.ufrgs.br/grid/noticias/ibge-desastres-naturais-atingiram-40-9-dos-municipios-do-pais-nos-ultimos-anos) Citado na página [32.](#page-33-0)

ICMC USP. Redes Neurais Artificiais. 2009. Disponível em:sites.icmc.usp.br. Citado na página [42.](#page-43-0)

JUNIOR, C. A. A.; SOUZA, P. D. d.; ASSIS, A. L. d.; CABACINHA, C. D.; LEITE, H. G.; SOARES, C. P. B.; SILVA, A. A. L. d.; CASTRO, R. V. O. Artificial neural networks, quantile regression, and linear regression for site index prediction in the presence of outliers. Pesquisa Agropecuária Brasileira, Embrapa Secretaria de Pesquisa e Desenvolvimento; Pesquisa Agropecuária Brasileira, v. 54, p. e00078, 2019. ISSN 0100-204X. Disponível em: [<https://doi.org/10.1590/S1678-3921.pab2019.v54.00078>.](https://doi.org/10.1590/S1678-3921.pab2019.v54.00078) Citado na página [70.](#page-71-0)

KIMURA, N.; YOSHINAGA, I.; SEKIJIMA, K.; AZECHI, I.; BABA, D. Convolutional neural network coupled with a transfer-learning approach for time-series flood predictions. Water, MDPI AG, v. 12, n. 1, p. 96, Dec 2019. ISSN 2073-4441. Disponível em: [<http://dx.doi.org/10.](http://dx.doi.org/10.3390/w12010096) [3390/w12010096>.](http://dx.doi.org/10.3390/w12010096) Citado nas páginas [58](#page-59-0) e [64.](#page-65-0)

<span id="page-124-0"></span>KIRICHENKO, L.; RADIVILOVA, T.; STEPANENKO, J. Applying recurrence plots to classify time series. In: Proceedings of the 5th International Conference on Computational Linguistics and Intelligent Systems (COLINS 2021). Volume I: Main Conference. Lviv, Ukraine: CEUR-WS, 2021. p. Data não especificada. Published online 26-May-2021. Disponível em: [<http://ceur-ws.org/Vol-2870/>.](http://ceur-ws.org/Vol-2870/) Citado na página [113.](#page-114-0)

KIRICHENKO, L.; ZINCHENKO, P.; RADIVILOVA, T. Classification of Time Realizations Using Machine Learning Recognition of Recurrence Plots. [S.l.: s.n.], 2021. 687-696 p. ISBN 978-3-030-54214-6. Citado nas páginas [15,](#page-16-0) [28,](#page-29-0) [29,](#page-30-0) [45,](#page-46-0) [59,](#page-60-0) [64,](#page-65-0) [66](#page-67-0) e [75.](#page-76-0)

KLEINSCHMIDT, V. Econometria II. 1. ed. Indaial, SC: UNIASSELVI, 2019. 213 p. ISBN 9788551503089. Citado na página [37.](#page-38-0)

KOENKER, R. Quantile regression: 40 years on. Annual Review of Economics, v. 9, n. 1, p. 155–176, 2017. Citado na página [71.](#page-72-0)

KRIZHEVSKY, A.; SUTSKEVER, I.; HINTON, G. E. Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems, v. 25, 2012. Citado na página [28.](#page-29-0)

LAWRENCE, M.; EDMUNDSON, B.; O'CONNOR, M. A field study of sales forecasting accuracy and processes. European Journal of Operational Research, Elsevier, v. 122, n. 1, p. 151–160, April 2000. Citado na página [82.](#page-83-0)

LEE, J. H.; YUK, G. M.; MOON, H. T.; MOON, Y.-I. Integrated flood forecasting and warning system against flash rainfall in the small-scaled urban stream. Atmosphere, v. 11, n. 9, 2020. ISSN 2073-4433. Disponível em: [<https://www.mdpi.com/2073-4433/11/9/971>.](https://www.mdpi.com/2073-4433/11/9/971) Citado nas páginas [55,](#page-56-0) [56](#page-57-0) e [64.](#page-65-0)

L'HEUREUX, A.; GROLINGER, K.; CAPRETZ, M. A. M. Machine learning with big data: Challenges and approaches. IEEE Access, v. 5, n. 2, p. 7776 – 7797, 2017. Citado nas páginas [26](#page-27-0) e [53.](#page-54-0)

LI, W.; KIAGHADI, A.; DAWSON, C. High temporal resolution rainfall–runoff modeling using long-short-term-memory (lstm) networks. Neural Computing and Applications, v. 33, n. 1261-1278, p. 49–53, 2021. Citado nas páginas [56,](#page-57-0) [57](#page-58-0) e [64.](#page-65-0)

LICCO, E. A.; DOWELL, S. F. M. Alagamentos, enchentes enxurradas e inundações: Digressões sobre seus impactos sócio econômicos e governança. Revista de Iniciação Científica, Tecnológica e Artística Edição Temática em Sustentabilidade, v. 5, 2015. ISSN 2179-474X. Citado nas páginas [15,](#page-16-0) [34](#page-35-0) e [35.](#page-36-0)

LIMA, G. R. T. de; SANTOS, L. B. L.; CARVALHO, T. J. de; CARVALHO, A. R.; CORTIVO, F. D.; SCOFIELD, G. B.; NEGRI, R. G. An operational dynamical neuro-forecasting model for hydrological disasters. Modeling Earth Systems and Environment, v. 2, n. 94, 2016. Citado na página [53.](#page-54-0)

LIU, W.-B.; THANH, P. N.; CHO, M.-Y.; DA, T. N. Categorizing 15 kv high-voltage hdpe insulator's leakage current surges based on convolution neural network gated recurrent unit. Energies (Basel), MDPI AG, Basel, v. 16, n. 5, p. 2500, 2023. ISSN 1996-1073. Citado na página [86.](#page-87-0)

LU, Y.; WANG, L.; ZHU, C.; ZOU, L.; ZHANG, M.; FENG, L.; CAO, Q. Predicting surface solar radiation using a hybrid radiative transfer–machine learning model. Renewable & sustainable energy reviews, Elsevier Ltd, v. 173, p. 113105, 2023. ISSN 1364-0321. Citado na página [84.](#page-85-0)

MADDALA, G. S.; LAHIRI, K. Introduction to Econometrics. UK: John Wiley & Sons Ltd, 2009. v. 4. Citado na página [28.](#page-29-0)

MAJID, M. A.; OMAR, M. H.; NOORANI, M. S. M. Analysis and predictive validity of kelantan river flow using rqa and time series analysis. Kuwait journal of science, v. 48, n. 1, 2021. ISSN 2307-4108. Citado nas páginas [62](#page-63-0) e [64.](#page-65-0)

MAKRIDAKIS, S.; WHEELWRIGHT, S. C.; MCGEE, V. E. Forecasting: Methods and Applications. 2nd. ed. New York: John Wiley & Sons, 1983. Citado na página [82.](#page-83-0)

MARWAN, N. Encounters with neighbours : current developments of concepts based on recurrence plots and their applications. 159 p. Dissertação (Mestrado) — Universität Potsdam, Postdam, 2003. Citado na página [50.](#page-51-0)

MARWAN, N. A historical review of recurrence plots. The european physical journal, n. 164, p. 3–12, 2008. Citado na página [48.](#page-49-0)

MARWAN, N.; ROMANO, M. C.; THIEL, M.; KURTHS, J. Recurrence plots for the analysis of complex systems. Physics Reports, n. 438(5-6), p. 237–329, 2007. Citado nas páginas [28,](#page-29-0) [49](#page-50-0) e [65.](#page-66-1)

MEDEIROS, M. R. Uma Metologia de Desenvolvimento de Programas em Inteligência Artificial: MEDSIA. 125 p. Dissertação (Mestrado em Ciencia da Computação) — Universidade Federal de Santa Catarina, Florianopolis, SC, 2004. Citado na página [41.](#page-42-0)

MENDONCA, F.; OLIVEIRA, I. M. D. Climatologia noções básicas e climas do Brasil. São Paulo, v. 4, 2007. Citado nas páginas [32](#page-33-0) e [33.](#page-34-0)

MICTHELL, T. M. Machine Learning. [S.l.]: "McGraw-Hill Science/Engineering/Math", 1997. v. 1. Citado na página [41.](#page-42-0)

MORETTIN, P. A.; TOLOI, C. M. C. Análise de Séries Temporais. 2. ed. São Paulo: Edgar Blucher, 2006. 533 p. ISBN 9788521203896. Citado nas páginas [36,](#page-37-0) [37,](#page-38-0) [38](#page-39-0) e [39.](#page-40-0)

MUMA, A. K. B. Modeling gdp using autoregressive integrated moving average (arima) model: A systematic review. Scientific research, v. 9, n. 4, p. 1–8, 2022. Citado na página [38.](#page-39-0)

<span id="page-126-0"></span>NASH, J.; SUTCLIFFE, J. River flow forecasting through conceptual models part i — a discussion of principles. Journal of Hydrology, v. 10, n. 3, p. 282–290, 1970. ISSN 0022-1694. Disponível em: [<https://www.sciencedirect.com/science/article/pii/0022169470902556>.](https://www.sciencedirect.com/science/article/pii/0022169470902556) Citado na página [101.](#page-102-2)

NETO, L. A. d. S.; MANIESI, V.; QUERINO, C. A. S.; SILVA, M. J. G. d.; BROWN, V. R. Modelagem hidroclimatologica utilizando redes neurais multi layer perceptron em bacia hidrogrÁfica no sudoeste da amazÔnia. Revista Brasileira de Climatologia (Impresso), v. 26, 2020. ISSN 1980-055X. Citado nas páginas [61](#page-62-0) e [64.](#page-65-0)

<span id="page-126-1"></span>OLIVEIRA, D.; MATOS, A. J. S. d. Relatório de operação do sistema de alerta hidrológico da bacia do rio Xingu 2023. Recife: Serviço Geológico do Brasil – CPRM, 2023. Recurso eletrônico: PDF; il. Programa de Gestão de Riscos e Desastres Ação Levantamentos, Estudos, Previsão e Alerta de Eventos Hidrológicos Críticos. ISBN 978-65-5664-418-9. Citado na página [110.](#page-111-2)

OLIVEIRA, P. ENCHENTE, INUNDAÇÃO E ALAGAMENTO. 2016. Disponível em: [<http:](http://www.jovemexplorador.iag.usp.br/?p=blog_enchente) [//www.jovemexplorador.iag.usp.br/?p=blog\\_enchente>.](http://www.jovemexplorador.iag.usp.br/?p=blog_enchente) Acesso em: 10/04/2021. Citado na página [35.](#page-36-0)

OSORIO, F.; BITTENCOURT, J. R. Sistemas inteligentes baseados em redes neurais artificiais aplicados ao processamento de imagens. In: I Workshop de Inteligência Artificial - UNISC. Santa Cruz do Sul, RGS: [s.n.], 2000. Citado nas páginas [15](#page-16-0) e [43.](#page-44-0)

PAZ, C. A. Legal challenges for artificial intelligence in chile. In: [Desafíos legales de la inteligencia artificial en Chile] Revista Chilena De Derecho y Tecnologia, Universidad de Chile 2021. [S.l.: s.n.], 2021. v. 9, n. 2, p. 257–290. ISBN 07192576. Citado na página [26.](#page-27-0)

PINHEIRO, N. M. Introdução a Séries Temporais. 2021. Disponível em: [<https://medium.](https://medium.com/data-hackers/series-temporais-parte-1-a0e75a512e72) [com/data-hackers/series-temporais-parte-1-a0e75a512e72>.](https://medium.com/data-hackers/series-temporais-parte-1-a0e75a512e72) Acesso em: 01/02/2021. Citado na página [38.](#page-39-0)

POZZEBON, E.; FRIGO, L.; BITTENCOURT, G. Inteligencia artificial na educação universitaria: Quais as contribuições. CCEI, 01 2004. Citado na página [40.](#page-41-0)

PRADO, C. A era da Inteligência Artificial. 2019. Disponível em: [<https://cienciahoje.org.br/](https://cienciahoje.org.br/artigo/a-era-da-inteligencia-artificial/) [artigo/a-era-da-inteligencia-artificial/>.](https://cienciahoje.org.br/artigo/a-era-da-inteligencia-artificial/) Acesso em: 05/04/2021. Citado nas páginas [26](#page-27-0) e [46.](#page-47-0)

PRIYANKA; KUMARI, A.; SOOD, M. Implementation of simplernn and lstms based prediction model for coronavirus disease (covid-19). IOP conference series. Materials Science and Engineering, IOP Publishing, Bristol, v. 1022, n. 1, p. 12015, 2021. ISSN 1757-8981. Citado na página [85.](#page-86-0)

RANIERI, C. M. Aprendizado de máquina e aplicações para robótica em ambientes inteligentes. 106 p. Tese (Doutorado) — Universidade de São Paulo, São Paulo, São Carlos, 2018. Citado nas páginas [15,](#page-16-0) [46,](#page-47-0) [47](#page-48-0) e [48.](#page-49-0)

ROSA, J. L. G. Fundamentos da Inteligência Artificial. Rio de Janeiro: LTC, 2011. v. 1. ISBN 978-85-216-0593-5. Citado na página [40.](#page-41-0)

ROSA, R. de P. Método de Classificação de Pragas por meio de Rede Neural Convolucional Profunda. 101 p. Dissertação (Mestrado em Computação Aplicada) — Universidade de Ponta Grossa, Ponta Grossa, 2018. Citado na página [28.](#page-29-0)

RUSSELL, S.; NORVIG, P. Inteligência Artificial. Rio de Janeiro: Elsevier, 2013. v. 3. Citado nas páginas [15,](#page-16-0) [36,](#page-37-0) [40](#page-41-0) e [42.](#page-43-0)

RUTLEDGE, K.; RAMROOP, T.; BOUDREAU, D.; MCDANIEL, M.; TENG, S.; SPROUT, E.; COSTA, H.; HALL, H.; HUNT, J. Rain. 2011. Disponível em: [<https://www.nationalgeographic.](https://www.nationalgeographic.org/encyclopedia/rain/) [org/encyclopedia/rain/>.](https://www.nationalgeographic.org/encyclopedia/rain/) Citado na página [33.](#page-34-0)

SALES, M. R.; MUGNAINE, M.; SZEZECH JOSé D., J.; VIANA, R. L.; CALDAS, I. L.; MARWAN, N.; KURTHS, J. Stickiness and recurrence plots: An entropy-based approach. Chaos: An Interdisciplinary Journal of Nonlinear Science, v. 33, n. 3, p. 033140, 03 2023. ISSN 1054-1500. Disponível em: [<https://doi.org/10.1063/5.0140613>.](https://doi.org/10.1063/5.0140613) Citado na página [48.](#page-49-0)

<span id="page-127-1"></span>SAPRA, R. Using r2 with caution. Current Medicine Research and Practice, v. 4, n. 3, p. 130– 134, 2014. ISSN 2352-0817. Disponível em: [<https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/S2352081714000646) [S2352081714000646>.](https://www.sciencedirect.com/science/article/pii/S2352081714000646) Citado nas páginas [85](#page-86-0) e [100.](#page-101-0)

SARAIVA, S. Deep learning passo a passo. PROGRAMAR, 2018. Disponível em: [<https:](https://www.revista-programar.info/artigos/deep-learning-passo-passo/) [//www.revista-programar.info/artigos/deep-learning-passo-passo/>.](https://www.revista-programar.info/artigos/deep-learning-passo-passo/) Citado nas páginas [15](#page-16-0) e [44.](#page-45-0)

<span id="page-127-0"></span>SCHNEIDER, P.; XHAFA, F. Chapter 3 - anomaly detection: Concepts and methods. In: SCH-NEIDER, P.; XHAFA, F. (Ed.). Anomaly Detection and Complex Event Processing over IoT Data Streams. Academic Press, 2022. p. 49–66. ISBN 978-0-12-823818-9. Disponível em: [<https://www.sciencedirect.com/science/article/pii/B9780128238189000134>.](https://www.sciencedirect.com/science/article/pii/B9780128238189000134) Citado nas páginas [85](#page-86-0) e [100.](#page-101-0)

SHIMABUKU, P. Existe solução para as enchentes urbanas e inundações? 2017. Disponível em: [<http://https://noticias.botucatu.com.br/2017/03/28/](http://https://noticias.botucatu.com.br/2017/03/28/existe-solucao-para-as-enchentes-urbanas-e-inundacoes/) [existe-solucao-para-as-enchentes-urbanas-e-inundacoes/>.](http://https://noticias.botucatu.com.br/2017/03/28/existe-solucao-para-as-enchentes-urbanas-e-inundacoes/) Acesso em: 10/04/2021. Citado na página [35.](#page-36-0)

SUSTO, G. A.; CENEDESE, A.; TERZI, M. Chapter 9 - time-series classification methods: Review and applications to power systems data. In: ARGHANDEH, R.; ZHOU, Y. (Ed.). Big Data Application in Power Systems. Elsevier, 2018. p. 179–220. ISBN 978-0-12-811968-6. Disponível em: [<https://www.sciencedirect.com/science/article/pii/B9780128119686000097>.](https://www.sciencedirect.com/science/article/pii/B9780128119686000097) Citado na página [36.](#page-37-0)

TAN, M.; LE, Q. Efficientnet: Rethinking model scaling for convolutional neural networks. In: PMLR. International conference on machine learning. [S.l.], 2019. p. 6105–6114. Citado na página [28.](#page-29-0)

TAURION, C. BIG DATA. Rio de Janeiro: Brasport, 2013. v. 1. Citado na página [27.](#page-28-0)

TEAM, T. pandas development. pandas-dev/pandas: Pandas. 2020. Version 1.0.5. Disponível em: [<https://pandas.pydata.org/>.](https://pandas.pydata.org/) Citado na página [69.](#page-70-0)

TELLES, D. D. Ciclo Ambiental da Água da Chuva a Géstão. [S.l.]: Blucher LTDA, 2018. Citado nas páginas [15](#page-16-0) e [34.](#page-35-0)

THIEL, M.; ROMANO, M. C.; KURTHS, J. How much information is contained in a recurrence plot? Physics Letters A, v. 330, n. 5, p. 343–349, 2004. ISSN 0375-9601. Disponível em: [<https://www.sciencedirect.com/science/article/pii/S0375960104009922>.](https://www.sciencedirect.com/science/article/pii/S0375960104009922) Citado na página [49.](#page-50-0)

TOMINAGA, L. K.; SANTORO, R. d. A. J. DESASTRES NATURAIS:Conhecer para prevenir. São Paulo, v. 1, 2009. Citado na página [25.](#page-26-0)

TRINDADE, A. L. F.; OLIVEIRA, P.; ANACHE, T. Sanches de; JAMIL, A. A.; WENDLAND, E. Variabilidade espacial da erosividade das chuvas no brasil. Pesquisa agropecuaria brasileira, v. 51, 2016. Citado na página [33.](#page-34-0)

UEHARA, T. D. T.; CORRêA, S. P. L. P.; QUEVEDO, R. P.; KöRTING, T. S.; DUTRA, L. V.; RENNó, C. D. Detecção de cicatrizes de movimentos de massa utilizando sensoriamento remoto e técnicas de reconhecimento de padrões: Comparação entre os classificadores redes neurais artificiais, máxima verossimilhança gaussiana, random forest e support vector machine. Revista Brasileira de Cartografia, v. 72, n. 4, p. 665–680, 2020. Disponível em: [<http://www.seer.ufu.](http://www.seer.ufu.br/index.php/revistabrasileiracartografia/article/view/54037) [br/index.php/revistabrasileiracartografia/article/view/54037>.](http://www.seer.ufu.br/index.php/revistabrasileiracartografia/article/view/54037) Citado na página [36.](#page-37-0)

USACE. Hydrologic Engineering Center River Analysis System (HEC-RAS). 2021. Disponível em: [<https://www.hec.usace.army.mil/software/hec-ras/collaborators.aspx>.](https://www.hec.usace.army.mil/software/hec-ras/collaborators.aspx) Acesso em: 06 Agosto 2021. Citado na página [56.](#page-57-0)

VASWANI, A.; SHAZEER, N.; PARMAR, N.; USZKOREIT, J.; JONES, L.; GOMEZ, A. N.; KAISER, Ł.; POLOSUKHIN, I. Attention is all you need. Advances in neural information processing systems, v. 30, 2017. Citado na página [27.](#page-28-0)

VEYRET, Y. OS RISCOS:O HOMEM COMO AGRESSOR E VÍTIMA DO MEIO AM-BIENTE. São Paulo, v. 1, 2007. Citado na página [25.](#page-26-0)

VIEIRA, A. C.; GARCIA, G.; PABÓN, R. E. C.; COTA, L. P.; SOUZA, P.; UEYAMA, J.; PESSIN, G. Improving flood forecasting through feature selection by a genetic algorithm – experiments based on real data from an amazon rainforest river. Earth Science Informatics, 2020. Doi:10.1007/s12145-020-00528-8. Citado na página [27.](#page-28-0)

VILLAS-BOAS. De olho na bacia do xingu. Instituto Socioambiental (ISA), 2012. Citado na página [27.](#page-28-0)

WANG, J. xin. Transfer learning assisted transmission quality evaluation based on machine learning. Guangtongxin Yanjiu, Optical Communication Research - Editorial Department, n. 6, p. 45–49, 2022. ISSN 1005-8788. Citado na página [83.](#page-84-0)

WANG, W. K.; CHEN, I.; HERSHKOVICH, L.; YANG, J.; SHETTY, A.; SINGH, G.; JIANG, Y.; KOTLA, A.; SHANG, J. Z.; YERRABELLI, R.; ROGHANIZAD, A. R.; SHANDHI, M. M. H.; DUNN, J. A systematic review of time series classification techniques used in biomedical applications. Sensors, v. 22, n. 20, 2022. ISSN 1424-8220. Disponível em: [<https://www.mdpi.](https://www.mdpi.com/1424-8220/22/20/8016) [com/1424-8220/22/20/8016>.](https://www.mdpi.com/1424-8220/22/20/8016) Citado na página [37.](#page-38-0)

WIKIPEDIA. Aprendizado de máquina. 2021. Online; acessado em 13 de outubro de 2021. Disponível em: [<wikipedia.org>.](wikipedia.org) Citado na página [27.](#page-28-0)

XAVIER, J. M. N. ANÁLISE E PREVISÃO DE SÉRIES TEMPORAIS COM MODELOS ARIMA E ANÁLISE ESPECTRAL SINGULAR. 102 p. Dissertação (Mestrado) — Universidade Aberta do Brasil, 2017. Citado na página [38.](#page-39-0)

YANG, D.; REN, W.-X.; HU, Y.-D. Non-stationary assessment of structural operational measurements using recurrence quantification analysis. Measurement, v. 171, p. 108791, 2021. ISSN 0263-2241. Disponível em: [<https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/S0263224120312860) [S0263224120312860>.](https://www.sciencedirect.com/science/article/pii/S0263224120312860) Citado na página [49.](#page-50-0)

YAO, X.; LIU, Y. Machine Learning. Boston, MA: Springer US, 2014. 477–517 p. ISBN 978-1-4614-6940-7. Disponível em: [<https://doi.org/10.1007/978-1-4614-6940-7\\_17>.](https://doi.org/10.1007/978-1-4614-6940-7_17) Citado na página [41.](#page-42-0)

ZHANG, Y.; HOU, Y.; ZHOU, S.; OUYANG, K. Encoding time series as multi-scale signed recurrence plots for classification using fully convolutional networks. Sensors, v. 20, n. 14, 2020. ISSN 1424-8220. Disponível em: [<https://www.mdpi.com/1424-8220/20/14/3818>.](https://www.mdpi.com/1424-8220/20/14/3818) Citado na página [28.](#page-29-0)

ZUANON, J. A. S. Método de Classificação de Pragas por meio de Rede Neural Convolucional Profunda. 214 p. Dissertação (Doutorado em Biologia) — Universidade Estadual de Campinas, Campinas, SP, 1999. Citado na página [27.](#page-28-0)

**UNIVERSIDADE DE SÃO PAULO**

Instituto de Ciências Matemáticas e de Computação