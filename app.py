import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configure the page
st.set_page_config(
    page_title="Cadastro para Caravana",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to load or create Excel
def load_or_create_excel():
    excel_file = 'caravana.xlsx'
    if os.path.exists(excel_file):
        return pd.read_excel(excel_file)
    else:
        return pd.DataFrame(columns=[
            'nome', 'idade', 'rg', 'celular', 'organizacao', 'ordenancas', 'ala', 'data_cadastro'
        ])

# Function to save data to Excel
def save_to_excel(data):
    excel_file = 'caravana.xlsx'
    df = load_or_create_excel()
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_excel(excel_file, index=False)

# Function to clear Excel file
def clear_excel():
    excel_file = 'caravana.xlsx'
    df = pd.DataFrame(columns=['nome', 'idade', 'rg', 'celular', 'organizacao', 'ordenancas', 'ala', 'data_cadastro'])
    df.to_excel(excel_file, index=False)

# Header
st.title("Templo de Campinas 🕌")
st.subheader("Cadastro para Caravana 🚌")

# Main form
with st.form("cadastro_caravana", clear_on_submit=True):
    st.markdown("### Dados do Irmão/ã")

    ala = st.selectbox(
        "Caravana da ala", 
        options=["Selecione a ala", "Ala Geisel", "Ala Marechal Rondom", "Ala Independencia", "Ala Bauru", "Ala Bela Vista"],
        index=0
    )
    
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
    
    ordenancas = st.multiselect(
        "Ordenanças - Pode selecionar mais de um",
        options=["Batistério", "Confirmação", "Iniciatória", "Investidura", "Selamento"]
    )        
    
    submit = st.form_submit_button("Cadastrar 📝")
    
    if submit:
        if nome and rg and celular:
            try:
                # Prepare data
                data = {
                    'nome': nome,
                    'idade': idade,
                    'rg': rg,
                    'celular': celular,
                    'organizacao': organizacao,
                    'ordenancas': "/".join(ordenancas),
                    'ala': ala,
                    'data_cadastro': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
                # Save to Excel
                save_to_excel(data)
                
                # Show success message
                st.success("✅ Cadastro realizado com sucesso!")
                
            except Exception as e:
                st.error(f"❌ Erro ao realizar o cadastro: {str(e)}")
        else:
            st.warning("⚠️ Por favor, preencha todos os campos obrigatórios.")

# Display current registrations
st.markdown("---")
st.markdown("### Registros Cadastrados")

if 'show_table' not in st.session_state:
    st.session_state.show_table = False
    
if 'table_loaded' not in st.session_state:
    st.session_state.table_loaded = False

if st.button("Ver 📋"):
    st.session_state.show_table = not st.session_state.show_table
    if st.session_state.show_table:
        st.session_state.table_loaded = True
    st.rerun()

if st.session_state.show_table:
    password = st.text_input("Digite a senha para visualizar os dados:", type="password")
    if password == "alageisel2025":
        try:
            df = load_or_create_excel()
            if not df.empty:
                st.dataframe(df, hide_index=True, use_container_width=True)
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    if st.button("🔄 Atualizar"):
                        df = load_or_create_excel()
                        st.experimental_rerun()
                
                with col2:
                    if st.button("🧹 Limpar Tabela"):
                        clear_excel()
                        st.success("✅ A tabela foi limpa com sucesso!")
                        st.experimental_rerun()
                
            else:
                st.info("Nenhum registro cadastrado ainda.")
        except Exception as e:
            st.error(f"Erro ao carregar os registros: {str(e)}")
    else:
        st.error("❌ Senha incorreta!")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #6b7280;'>Desenvolvido com ❤️ para a Caravana ao Templo</p>",
    unsafe_allow_html=True
)
