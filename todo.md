## **GLOBAL SOLUTION 2025.1 - PROJETO HYDROGUARD**

### **Visão Geral do Projeto:**
Desenvolver um MVP de um sistema que monitora o nível de rios e precipitação via sensores (simulados por ESP32), utiliza Machine Learning em Python para prever o risco de enchentes e emite alertas precoces.

---

### **TODO List (MVP)**

### **Fase 1: Planejamento e Base**

*   [ ] **1.1. Alinhamento e Distribuição de Tarefas**
    *   [ ] Reunião de grupo para definir o escopo exato do MVP e atribuir responsáveis.
    *   [ ] **Documentação:** Criar rascunho da seção "Introdução" do PDF, incluindo a descrição da solução.
*   [ ] **1.2. Estudo de Referência e Ambiente**
    *   [x] Estudar a dissertação da Laleska (parte de dados e ML para enchentes).
    *   [ ] Configurar ambiente Python.
    *   [ ] Configurar ambiente Wokwi.
    *   [ ] **Documentação:** Incluir instruções de configuração do ambiente Python e Wokwi.
    *   [ ] **Documentação:** Incluir referências bibliográficas e links úteis na seção "Referências" do PDF.
*   [ ] **1.3. Projeto e Configuração do Banco de Dados PostgreSQL para HydroGuard**
    *   [x] 1.3.1. Modelar o MER (Modelo Entidade-Relacionamento) para o banco de dados.
    *   [ ] 1.3.2. Gerar o DER (Diagrama Entidade-Relacionamento) a partir do MER.
    *   [ ] 1.3.3. Criar o esquema do banco de dados conforme o MER definido.
    *   [ ] 1.3.4. Configurar ambiente PostgreSQL local ou em nuvem.
    *   [ ] **Documentação:** Incluir o MER, o DER e explicações das tabelas na seção "Arquitetura" do PDF.

---

### **Fase 2: Dados**

*   [ ] **2.1. Processamento e Ingestão de Dados Históricos**
    *   [ ] 2.1.1. Carregar, inspecionar e limpar os dados do Rio Meia Ponte (nível e chuva) dos CSVs da ANA.
    *   [ ] 2.1.2. Implementar script de ingestão de dados para popular as tabelas do banco de dados com os dados históricos.
    *   [ ] **Documentação:** Detalhar as fontes de dados usadas e o pré-processamento inicial (limpeza, tratamento de ausentes) na seção "Desenvolvimento" do PDF, incluindo a estratégia de ingestão no DB.
*   [ ] **2.2. Engenharia de Features para ML**
    *   [ ] 2.2.1. Adaptar script de engenharia de features para ler os dados necessários diretamente das tabelas do banco de dados.
    *   [ ] 2.2.2. Criar variáveis para o modelo (ex: níveis anteriores, chuva acumulada) e definir a variável alvo (nível futuro ou classe de risco).
    *   [ ] 2.2.3. Criar o dataset final para o modelo de ML, extraindo do DB, otimizado para séries temporais.
    *   [ ] 2.2.4. Separar dados para treino/validação/teste.
    *   [ ] **Documentação:** Descrever as features criadas e a preparação do dataset para o ML na seção "Desenvolvimento" do PDF.

---

### **Fase 3: Desenvolvimento do Sistema de Sensores (Wokwi + ESP32)**

*   [ ] **3.1. Simulação de Sensores ESP32 no Wokwi e Persistência de Dados**
    *   [ ] Projetar o circuito para ESP32, sensor de nível e pluviômetro (simulados).
    *   [ ] Escrever o código ESP32 para ler os sensores e enviar dados via Serial para o Python.
    *   [ ] **3.1.1. Script Python para receber dados serial do ESP32 e persistir na tabela `sensor_measurement` do banco de dados.**
    *   [ ] 3.1.2. Testar a comunicação ESP32-Python (leitura simples) e a persistência dos dados no DB.
    *   [ ] **Documentação:** Incluir o diagrama do circuito ESP32 (Wokwi) e explicar o funcionamento do código do ESP32 e a lógica de persistência de dados no DB na seção "Desenvolvimento" do PDF.

---

### **Fase 4: Desenvolvimento do Modelo de Machine Learning**

*   [ ] **4.1. Desenvolvimento e Treinamento do Modelo ML**
    *   [ ] 4.1.1. Implementar e treinar o modelo de ML (Regressão ou Rede Neural simples) em Python usando os dados históricos lidos do banco de dados.
    *   [ ] 4.1.2. Salvar o modelo treinado (arquivo) e **persistir seus metadados (nome, tipo, métricas, caminho) na tabela `ml_model` do DB.**
    *   [ ] **Documentação:** Descrever o tipo de modelo ML escolhido, o processo de treinamento e as métricas de avaliação na seção "Desenvolvimento" do PDF.

---

### **Fase 5: Integração e Sistema de Alerta**

*   [ ] **5.1. Integração do Sistema de Alerta com Banco de Dados**
    *   [ ] 5.1.1. Script Python para ler dados "em tempo real" do ESP32 (ou da tabela recém-populada).
    *   [ ] 5.1.2. Alimentar o modelo ML com os dados recebidos para fazer a previsão do nível do rio.
    *   [ ] **5.1.3. Persistir os resultados da previsão (nível previsto, risco, timestamp) na tabela `flood_prediction` do DB.**
    *   [ ] 5.1.4. Implementar a lógica de alerta: se o nível previsto ultrapassar um limiar crítico (lido da tabela `river_segment` ou configurado), o sistema emitirá um alerta visual (LED no ESP32 simulado) e uma mensagem no console.
    *   [ ] **5.1.5. Persistir os detalhes do alerta emitido (tipo, mensagem, severidade, status) na tabela `alert` do DB.**
    *   [ ] **5.1.6. Teste End-to-End da Solução (ESP32 simulado -> Python -> DB -> ML -> DB -> Alerta no ESP32 e Console -> DB).**
    *   [ ] **Documentação:** Explicar a arquitetura de integração Python-ESP32-DB e a lógica do sistema de alerta na seção "Desenvolvimento" do PDF. Incluir trechos de código relevantes.

---

### **Fase 6: Entrega e Refinamento**

*   [ ] **6.1. Finalização da Documentação Escrita**
    *   [ ] Completar as seções "Resultados Esperados" e "Conclusões" do PDF.
    *   [ ] Revisão final de todo o conteúdo do PDF (clareza, coesão, gramática).
    *   [ ] Inserir nomes dos integrantes e link do GitHub na primeira página.
*   [ ] **6.2. Gravação e Edição do Vídeo de Demonstração**
    *   [ ] Roteiro focado em mostrar o MVP funcional (ESP32 simulado interagindo com o Python e o alerta).
    *   [ ] Gravar e editar (até 5 minutos).
    *   [ ] Upload para YouTube (não listado) e adicionar o link ao PDF.
*   [ ] **6.3. Organização e Envio do Código**
    *   [ ] Garantir que o código está limpo, comentado e 100% operacional (scripts de modelagem, de DB, etc.).
    *   [ ] Fazer o último commit para o GitHub PÚBLICO.
    *   [ ] **Entrega Final (PDF + Vídeo + GitHub).**

---

**Lembretes Essenciais:**

*   **Foco no MVP:** Não se desvie para funcionalidades avançadas que não são cruciais para o MVP.
*   **Comunicação:** Mantenham-se em contato constante (via WhatsApp) e usem reuniões rápidas para sincronizar o progresso.
*   **Qualidade do Código:** Priorizem a clareza e funcionalidade, mesmo sob pressão.
*   **Documentação Contínua:** Integrar a documentação desde o início alivia muito a carga no final.

Vamos lá, equipe! O caminho está traçado.