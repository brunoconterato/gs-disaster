# 🌊 HydroGuard: Sistema Inteligente de Monitoramento e Alerta de Enchentes em Rios

---

## 🎯 **Objetivo do Projeto**

O **HydroGuard** é uma solução digital inovadora desenvolvida para enfrentar o crescente desafio das enchentes em rios, um dos eventos naturais extremos mais impactantes no Brasil e no mundo. Nosso principal objetivo é criar um sistema capaz de **prever, monitorar e mitigar os impactos de enchentes**, fornecendo alertas precoces para comunidades ribeirinhas e autoridades. Utilizando dados reais e as mais recentes tecnologias de Inteligência Artificial e IoT, buscamos transformar a resposta a desastres, tornando-a mais rápida, inteligente e eficaz.

---

## 💡 **Nossa Escolha: Por Que HydroGuard?**

A escolha do **HydroGuard** foi baseada em uma análise criteriosa das necessidades do desafio Global Solution 2025.1 e das capacidades da nossa equipe. Optamos por esta proposta pelas seguintes razões fundamentais:

*   **Impacto Direto e Tangível:** Enchentes fluviais afetam milhões, causam perdas de vidas e enormes prejuízos. Uma previsão e alerta eficazes salvam vidas e bens, o que confere ao projeto uma relevância social imediata e inegável.
*   **Alinhamento Perfeito com Requisitos Técnicos:**
    *   **Sensores ESP32 e IoT:** O monitoramento do nível do rio e da precipitação via sensores é a espinha dorsal do sistema, permitindo uma integração **natural e essencial** do ESP32, cumprindo um dos requisitos obrigatórios do projeto de forma orgânica.
    *   **Machine Learning/Redes Neurais em Python:** A previsão de enchentes é um problema clássico de séries temporais, ideal para aplicação de modelos de Machine Learning (como Regressão, Random Forest ou até Redes Neurais Recorrentes/Convolucionais), garantindo o cumprimento do outro requisito obrigatório do projeto.
*   **Disponibilidade e Facilidade de Dados:** Há uma vasta quantidade de dados hidrológicos e meteorológicos gratuitos e públicos no Brasil (ANA, SGB, CEMADEN), estruturados em séries temporais, o que facilita enormemente a coleta, limpeza e preparação para o treinamento do modelo de ML, otimizando nosso tempo de desenvolvimento.
*   **Escopo Viável para MVP:** Ao focar no monitoramento e alerta (e não no controle de fluxo, por exemplo), conseguimos delimitar um MVP robusto e funcional que pode ser entregue dentro do prazo apertado, mantendo a complexidade gerenciável.
*   **Foco em Dados Reais:** Mesmo com a flexibilização do `disasterscharter.org`, o HydroGuard se baseia em dados reais de rios e chuvas, mantendo a essência do desafio.

---

## 🚀 **Escopo do MVP (Produto Mínimo Viável)**

Para esta fase da Global Solution, o **HydroGuard** será apresentado como uma Prova de Conceito (PoC) funcional com as seguintes características:

1.  **Monitoramento Simulado de Sensores:**
    *   Utilização de um **ESP32 simulado no Wokwi** para representar sensores de nível de água (ultrassônico) e pluviômetro (chuva acumulada).
    *   O ESP32 enviará dados simulados (nível do rio e precipitação) para um script Python via comunicação serial.
2.  **Coleta e Pré-processamento de Dados Históricos:**
    *   Dados reais de nível do rio e precipitação para o **Rio Meia Ponte (Goiás)** serão coletados de fontes como o sistema HidroWeb da ANA.
    *   Esses dados serão limpos, integrados e utilizados para a engenharia de features, preparando-os para o treinamento do modelo de Machine Learning.
3.  **Modelo de Previsão de Enchentes (ML em Python):**
    *   Desenvolvimento de um modelo de Machine Learning (ex: Random Forest Regressor ou Rede Neural Densa simples) em Python.
    *   O modelo será treinado com os dados históricos para prever o nível do rio em um futuro próximo (ex: próximas 1-2 horas).
4.  **Sistema de Alerta Precoce:**
    *   O script Python receberá os dados "em tempo real" do ESP32 simulado.
    *   Utilizará o modelo treinado para prever o nível do rio.
    *   Se o nível previsto ultrapassar um limiar de "enchente iminente", o sistema emitirá um alerta visual (ex: LED no ESP32 simulado) e uma mensagem no console.
5.  **Documentação e Demonstração:**
    *   Entrega de um PDF detalhado com a arquitetura, justificativas e códigos.
    *   Vídeo de demonstração prática mostrando a interação do ESP32 simulado com o sistema Python e o acionamento do alerta.

---

## 🛠️ **Tecnologias Utilizadas**

| Categoria              | Ferramentas                   |
| :--------------------- | :---------------------------- |
| Linguagem              | Python 3.9+                   |
| Manipulação de Dados   | Pandas, NumPy                 |
| Visualização           | Matplotlib                    |
| Aprendizado Profundo   | PyTorch                       |
| Pré-processamento      | Scikit-learn (StandardScaler) |
| Ambiente               | Jupyter Notebook, CUDA (GPU)  |
| IoT/Hardware           | ESP32, Wokwi (simulação)      |
| Comunicação            | PySerial                      |

---

## 👥 **Equipe**

### Membros (Grupo 46)

-   Amandha Nery (RM560030)
-   Bruno Conterato (RM561048)
-   Gustavo Castro (RM560831)
-   Kild Fernandes (RM560615)
-   Luis Emidio (RM559976)

### Professores

-   Tutor: Leonardo Ruiz Orabona
-   Coordenador: André Godoi

---

## 🏃‍♀️ **Como Rodar o Projeto (MVP)**

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/luisfuturist/gs-disaster.git
    cd gs-disaster
    ```
2.  **Instale as Dependências Python:**
    ```bash
    pip install -r requirements.txt # (Será criado um arquivo requirements.txt com as libs necessárias)
    ```
3.  **Execute a Simulação do ESP32 no Wokwi:**
    *   Abra o link do projeto ESP32 no Wokwi (o link será fornecido na documentação do PDF).
    *   Inicie a simulação (play button).
    *   Manipule os sliders para simular o nível da água e a precipitação.
4.  **Execute os Script Python:**
    *  Abra o Jupyter Notebook ou execute os scripts Python diretamente.

---

## 📂 **Estrutura do Projeto**

```
.
├── asset                   # Imagens e diagramas do projeto (ex: circuitos, arquitetura)
│   ├── image_labels.png
│   └── image_raw.png
├── data                    # Dados brutos e pré-processados
│   ├── ANA HIDROWEB
│   │   └── RIO MEIA PONTE  # Dados CSV de estações ANA
│   │       ├── 60640000-MONTANTE DE GOIANIA.csv
│   │       ├── 60650000-JUSANTE DE GOIANIA.csv
│   │       └── 60655001-UHE SAO SIMAO FAZENDA BONITA DE BAIXO.
├── doc                     # Documentação do projeto (relatórios, etc.)
│   └── tmp
│       └── Fontes.md
├── README.md               # Este arquivo!
└── ref                     # Materiais de referência e pesquisa
    └── LaleskaAparecidaFerreiraMesquita # Dissertação de Mestrado
        ├── LaleskaAparecidaFerreiraMesquita_ME_revisada.md
        ├── LaleskaAparecidaFerreiraMesquita_ME_revisada.pdf
        └── ref.md
```

---

## ✨ **Próximos Passos e Melhorias Futuras**

O MVP do HydroGuard é um ponto de partida. Para futuras iterações e para concorrer ao pódio, pretendemos explorar:

*   **Modelos de ML Mais Avançados:** Implementação de Redes Neurais Recorrentes (RNNs/LSTMs) para aprimorar a previsão de séries temporais, inspiradas na tese de referência.
*   **Integração com Banco de Dados:** Armazenamento persistente de dados de sensores e previsões.
*   **Computação em Nuvem:** Deploy do sistema de monitoramento e ML em plataformas de nuvem para escalabilidade.
*   **Dashboards Interativos:** Desenvolvimento de uma interface gráfica para visualização em tempo real e configuração de alertas.
*   **Alerta Multi-canal:** Envio de alertas via SMS ou e-mail para autoridades e população.
*   **Validação com Dados Reais:** Testes em cenários reais com estações de monitoramento.

---
**Desenvolvido com paixão e inteligência para um futuro mais seguro.**
