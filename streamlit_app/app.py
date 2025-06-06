import streamlit as st
from datetime import datetime
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importações do projeto
from db_utils import SessionLocal
from db.session_files.models import FloodPrediction, Alert
from sqlalchemy.orm import joinedload

st.set_page_config(page_title="HydroGuard Dashboard", layout="wide")

st.title("🌊 HydroGuard – Monitoramento de Enchentes em Rios")

# Função para buscar a previsão mais recente
def get_latest_prediction(session):
    return session.query(FloodPrediction)\
        .options(joinedload(FloodPrediction.monitoring_station))\
        .order_by(FloodPrediction.prediction_timestamp.desc())\
        .first()

# Função para buscar os alertas recentes
def get_recent_alerts(session, limit=10):
    return session.query(Alert)\
        .order_by(Alert.alert_timestamp.desc())\
        .limit(limit)\
        .all()

# Conexão com o banco
with SessionLocal() as session:
    latest = get_latest_prediction(session)
    alerts = get_recent_alerts(session)

    if latest:
        st.subheader("📈 Última Previsão")
        col1, col2 = st.columns(2)
        col1.metric("Nível Previsto", f"{latest.predicted_level:.2f} m")
        col2.metric("Risco Previsto", latest.predicted_risk_level)
        st.caption(f"Previsão feita para {latest.prediction_timestamp.strftime('%d/%m/%Y %H:%M')}")
    else:
        st.warning("Nenhuma previsão encontrada no banco de dados.")

    st.markdown("---")
    st.subheader("🚨 Últimos Alertas")

    if alerts:
        for alert in alerts:
            st.markdown(f"**{alert.alert_timestamp.strftime('%d/%m/%Y %H:%M')}** — {alert.message} *(Severidade: {alert.severity})*")
    else:
        st.info("Nenhum alerta registrado ainda.")
