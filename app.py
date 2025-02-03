import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Firebase (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "caravana-5fa6e",
        "private_key_id": "75110b78d39bb6078c8ba3b5396b56d3a2f9d4e1",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDf1caPvTJRWhVk\nN9ox0ll2DcgM0oY+UWigYdnUe9BGluC2OokNb8Y2QPjye6NQHbdKZcVEWpCJuhDU\na2rLvDtg/eMJGgMNHKYxRbpwMzoDqzY9tP5/1P8QCgSljjMRcaEBuTgF9we9AiOj\nYYDL2IWy71RQbGH4UOsuH+GznqmgMzdPDU9CHunmWGji3gljPh7pz6x4lcW403eT\nis9x0ncw+vkQNMuRgx1MFpkQvQl4xoZH0cMGQuq6M0I0sXRyvOBw36IIclhA9oen\nVRMXuJiIrKELes4RSfDvqejK2MZfh1narJnxm5FfL4GUXKCU8yPSBtyvOP/Ks59e\nqULb8xUdAgMBAAECggEADjV7mpXLyyrBB2DdRsLf33TeAWRe1bdkwSOdCJZIgSak\nQqUiHJp/FmQW+YucMSKFx2EA/gcSvE91sIpWF/NNwKk1P5dpYKx0J1YSEPvLf76f\nXZju++3pOBsustS9TKruKdYYZpaJJPgtC3rNyoLm79Yt/8H1kSYP29h1wyl8ApmH\nUcjl3B+BCwgiUNS6sX5F0uCFWexKsgYDwisJMinu0WGOgbpiFaa+pFdMCbKXD8s2\n4ehKJUx64ZxhoUJyQvypm4602lxY+QYnk/jvQsAz/E9HxkLHx1eL0MvnowkphGjY\n3OXn0Y8tqkABRZcTrvEHx/N8i7RWp3YidGuuHM9XAQKBgQDvwN01aZ3Vwp6Ok4ml\n9X/5nRx4marK9TPOgC8RdFuJxLqJBWGX5860WVKagqvhmTkzQBcNNypvGGwZMJWi\nbUrbteamnC0uKdERUulGDc2zpTvMo0QnS08NtXXSarnAMLr78F/BiWKtTJtuNzt+\nMMjrHQfukHlBIGZXZ3YY8VoxAQKBgQDvAMSDj6fKCLtqePxkZkikFTCYrv0n4Wix\nS23fXEQtgeOOzrpKsK8dhEyQFcI4sdxiur0fRixNKuhMGPrKUXILHc8RK9yYqTD2\ng6Xzy1LTwA6pRMgOQH27SRyxYpw+f4Juc/e6u/DCI/t31C2AWo1m3+Zc0yUxjC2g\nax+AV7OIHQKBgQCtaQgW2/+HXy8j3N7QpNMdjl/Lcwovpk8Ea36f11NmQF7TQIso\nPkgp9fljPGRp1lOjGBYUPvR4SmfViGiShQ6B//2GQKwFGcXYC+oh+1XvO/IWv3hK\nG5RgTAGeYgdcVWLJW0FHUMGIq0I448YqLcsFE4hrKyAo1PBxA6pNvDQKAQKBgQDu\nf+6adqVymComAtuieOtuSfL3uk/IF0j4+5OF/DXQz7g8TxFZ7VyicN5SPlRVbS/G\nmiCV79nPm8y5+4dwk7vhWfrDYOi+sr+4kADv+usJgbNfuNKGXlbZqQjn/sZ6G5YW\nEMWaY2fK5EtR9br+Rd6rVS01XkLUYdU6KwwBcAMpBQKBgQDA4QQy/syx9U4O2Htr\nrJPbDv1iuZjZKBpt/s+NZjld5GcOlFDCgEitqROGd+r5QKmGgn1KqHSb4OmZaerh\n/akWbSy09JPFecbsUxoE+8cyZEcuSikXgx4JcEiYX969wk/tqCHCcIMT3VpWyIpl\npRpnZz0ISFB5ZFvJb0dbKp9jUQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-18us6@caravana-5fa6e.iam.gserviceaccount.com",
        "client_id": "102150680425321404277",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-18us6%40caravana-5fa6e.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    })
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://caravana-5fa6e-default-rtdb.firebaseio.com/'
    })

# Configure the page
st.set_page_config(
    page_title="Cadastro para Caravana Templo de Campinas",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            background-color: #2563eb;
            color: white;
            height: 3rem;
            font-size: 1.1rem;
        }
        .stButton>button:hover {
            background-color: #1d4ed8;
        }
        h1 {
            text-align: center;
            color: #1e3a8a;
        }
        .stRadio>label {
            font-size: 1rem;
            color: #374151;
        }
        .stTextInput>div>div>input {
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🚌 Cadastro para Caravana")

# Main form
with st.form("cadastro_caravana", clear_on_submit=True):
    st.markdown("### Dados do Participante")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome = st.text_input("Nome Completo", max_chars=50)
        rg = st.text_input("RG", max_chars=20)
    
    with col2:
        idade = st.number_input("Idade", min_value=1, max_value=120, value=18)
        celular = st.text_input("Celular", max_chars=15)
    
    organizacao = st.radio(
        "Organização",
        options=["Quórum de Élderes", "Sociedade de Socorro", "Moças", "Rapazes", "Primária"],
        horizontal=True
    )
    
    submit = st.form_submit_button("Cadastrar")
    
    if submit:
        if nome and rg and celular:
            try:
                # Get reference to Firebase database
                ref = db.reference('/Caravana')
                
                # Prepare data
                data = {
                    'nome': nome,
                    'idade': idade,
                    'rg': rg,
                    'celular': celular,
                    'organizacao': organizacao,
                    'data_cadastro': datetime.now().isoformat()
                }
                
                # Push data to Firebase
                ref.push(data)
                
                # Show success message
                st.success("✅ Cadastro realizado com sucesso!")
                
            except Exception as e:
                st.error(f"❌ Erro ao realizar o cadastro: {str(e)}")
        else:
            st.warning("⚠️ Por favor, preencha todos os campos obrigatórios.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #6b7280;'>Desenvolvido com ❤️ para a Caravana ao Templo</p>",
    unsafe_allow_html=True
)