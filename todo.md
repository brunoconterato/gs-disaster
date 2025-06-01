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

---

### **Fase 2: Dados**

*   [ ] **2.1. Processamento Inicial dos Dados Históricos**
    *   [ ] Carregar, inspecionar, limpar e integrar os dados do Rio Meia Ponte (nível e chuva) dos CSVs da ANA.
    *   [ ] **Documentação:** Detalhar as fontes de dados usadas e o pré-processamento inicial (limpeza, tratamento de ausentes) na seção "Desenvolvimento" do PDF.
*   [ ] **2.2. Engenharia de Features para ML**
    *   [ ] Criar variáveis para o modelo (ex: níveis anteriores, chuva acumulada) e definir a variável alvo (nível futuro ou classe de risco).
    *   [ ] Criar o dataset final para o modelo de ML.
    *   [ ] Separar dados para treino/validação/teste.
    *   [ ] **Documentação:** Descrever as features criadas e a preparação do dataset para o ML na seção "Desenvolvimento" do PDF.

---

### **Fase 3: Desenvolvimento do Sistema de Sensores (Wokwi + ESP32)**

*   [ ] **3.1. Simulação de Sensores ESP32 no Wokwi**
    *   [ ] Projetar o circuito para ESP32, sensor de nível e pluviômetro (simulados).
    *   [ ] Escrever o código ESP32 para ler os sensores e enviar dados via Serial para o Python.
    *   [ ] **Testar a comunicação ESP32-Python (leitura simples).**
    *   [ ] **Documentação:** Incluir o diagrama do circuito ESP32 (Wokwi) e explicar o funcionamento do código do ESP32 na seção "Desenvolvimento" do PDF.

---

### **Fase 4: Desenvolvimento do Modelo de Machine Learning**

*   [ ] **4.1. Desenvolvimento e Treinamento do Modelo ML**
    *   [ ] Implementar e treinar o modelo de ML (Regressão ou Rede Neural simples) em Python usando os dados históricos preparados.
    *   [ ] Salvar o modelo treinado.
    *   [ ] **Documentação:** Descrever o tipo de modelo ML escolhido, o processo de treinamento e as métricas de avaliação na seção "Desenvolvimento" do PDF.

---

### **Fase 5: Integração e Sistema de Alerta**

*   [ ] **5.1. Integração do Sistema de Alerta**
    *   [ ] Script Python para ler dados do ESP32 via Serial.
    *   [ ] Alimentar o modelo ML com os dados recebidos para fazer a previsão.
    *   [ ] Implementar a lógica de alerta: se a previsão exceder o limiar, imprimir alerta e enviar comando para o ESP32 acender o LED.
    *   [ ] **Teste End-to-End da Solução.**
    *   [ ] **Documentação:** Explicar a arquitetura de integração Python-ESP32 e a lógica do sistema de alerta na seção "Desenvolvimento" do PDF. Incluir trechos de código relevantes.

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
    *   [ ] Garantir que o código está limpo, comentado e 100% operacional (`all_code.py` e arquivos auxiliares).
    *   [ ] Fazer o último commit para o GitHub PÚBLICO.
    *   [ ] **Entrega Final (PDF + Vídeo + GitHub).**

---

**Lembretes Essenciais:**

*   **Foco no MVP:** Não se desvie para funcionalidades avançadas que não são cruciais para o MVP.
*   **Comunicação:** Mantenham-se em contato constante (via WhatsApp) e usem reuniões rápidas para sincronizar o progresso.
*   **Qualidade do Código:** Priorizem a clareza e funcionalidade, mesmo sob pressão.
*   **Documentação Contínua:** Integrar a documentação desde o início alivia muito a carga no final.

Vamos lá, equipe! O caminho está traçado.
