🌊 *HydroGuard: Fontes Essenciais de Dados para Previsão de Enchentes* 

Para o nosso modelo de ML, precisamos focar em:

💧 *1. Níveis de Rios e Vazões:* 
*   *Brasil:* *ANA/SNIRH* (Agência Nacional de Águas)
    *   Dados em *tempo real* (Hidro-Telemetria) e históricos (HidroWeb).
    *   ✅ É a fonte *oficial* brasileira.
    *   ⚠️ `Atenção:` Alguns dados podem ser classificados como "duvidosos" ou ter lacunas.
	
    Notas:
    * Estações no mapa interativo: https://www.snirh.gov.br/hidroweb-mobile/mapa
	* Dados série histórica das estações (Sistema Hidroweb): https://www.snirh.gov.br/hidroweb/serieshistoricas
	* Dados abertos (Genérico): https://dadosabertos.ana.gov.br
	* Dataset Vulnerabilidade a inundações (de onde vamos escolher um rio): https://dadosabertos.ana.gov.br/datasets/62a3924c1da34f73bf5b7132677213ea_0/explore
  	* Escolha: Rio Capibaribe (PE)
       Rio Capibaribe (Trecho Alto) – Recife (PE)
      📌 Características: O trecho alto do Capibaribe, antes da Região Metropolitana, não possui grandes barragens.
      ⚠️ Problema: Enchentes frequentes nos bairros de Recife, como Santo Amaro, Boa Vista e Afogados.
      🔍 Observação: No entanto, há pequenas contenções em afluentes, então é importante verificar quais trechos são totalmente livres de controle.

*   *Internacional:* *WMO (WHOS)* (Organização Meteorológica Mundial)
    *   Agrega dados hidrológicos globais, incluindo a Bacia do Prata.
    *   Acesso via APIs (WaterML).
*   *Internacional:* *Copernicus (GloFAS)*
    *   🗺️ Fornece *previsões globais* de descarga de rios.

🌧️ *2. Precipitação (Chuva):* 
*   *Brasil:* *INMET* (Instituto Nacional de Meteorologia)
    *   Dados em *tempo real* e históricos (desde 2000).
    *   Fácil acesso via pacote Python `inmet-bdmep-data` para históricos.
    *   🔌 `Atenção:` Pode ter lacunas por interrupção de energia nas estações.
*   *Internacional:* *Copernicus (CAMS)*
    *   ✨ Dados globais de precipitação (ótimos para modelagem).

🌳 *3. Umidade do Solo:* 
*   *Brasil:* *CPTEC/INPE* (Centro de Previsão de Tempo e Estudos Climáticos)
    *   Dados diários em múltiplas camadas de profundidade.
    *   ⭐ `ALTAMENTE RECOMENDADO:` *Melhora MUITO* a precisão das previsões, especialmente com solo já saturado!

📜 *4. Dados Históricos de Enchentes (para Validação):* 
*   *Brasil:* *CEMADEN* (Centro Nacional de Monitoramento e Alertas de Desastres Naturais)
    *   Registros de alagamentos desde 2013. ✅ *Crucial* para validar o modelo.
    *   ❗ `Atenção:` A qualidade dos dados de *impacto* pode variar.
*   *Brasil:* *Atlas Digital de Desastres*
    *   Registros históricos de desastres desde 1991.

💡 *Acesso e Dicas para o HydroGuard:* 
*   🆓 Todas as fontes são *gratuitas e públicas* (portais web, APIs, downloads).
*   🤝 Busque integrar *dados nacionais em tempo real* com *previsões internacionais* de médio prazo.
*   💪 Aproveite ao máximo a *umidade do solo* do CPTEC/INPE!
*   🛠️ Sempre prepare seu código para lidar com lacunas ou inconsistências nos dados.