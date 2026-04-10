import streamlit as st


# Configuração da Página
st.set_page_config(
    page_title="Uno de Sete | Curadoria Automotiva",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Estilização Customizada (CSS) para manter o tom Premium
st.markdown("""
    <style>
    .subtitulo {
        color: #A0AEC0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# CABEÇALHO DA MARCA
# ==========================================
# Quando tiver a sua logo salva na pasta, troque o link abaixo por: st.image("sua_logo.png", width=250)
st.title("UNO DE SETE")
st.markdown("<p class='subtitulo'>A seleção definitiva para o seu projeto de som e tecnologia embarcada.</p>", unsafe_allow_html=True)
st.markdown("---")


# ==========================================
# SEÇÃO 1: MAIS VENDIDOS (Volume e Captura)
# ==========================================
st.header("🔥 Mais Vendidos da Semana")
st.caption("Faça o upgrade ideal no seu veículo com o melhor custo-benefício.")


# Criando 4 colunas para os produtos de giro rápido
col1, col2, col3, col4 = st.columns(4)


with col1:
    st.image("https://via.placeholder.com/300x200/1E1E1E/FFFFFF?text=Camera+de+Re", use_column_width=True)
    st.subheader("Câmera de Ré HD")
    st.text("Visão noturna e aproximação.")
    st.link_button("Ver Oferta", "https://link-do-seu-afiliado.com/camera")


with col2:
    st.image("https://via.placeholder.com/300x200/1E1E1E/FFFFFF?text=Kit+Super+LED", use_column_width=True)
    st.subheader("Kit Super LED 8000K")
    st.text("Iluminação branca premium.")
    st.link_button("Ver Oferta", "https://link-do-seu-afiliado.com/led")


with col3:
    st.image("https://via.placeholder.com/300x200/1E1E1E/FFFFFF?text=Moldura+Painel", use_column_width=True)
    st.subheader("Molduras 2 DIN")
    st.text("Acabamento original de fábrica.")
    st.link_button("Ver Oferta", "https://link-do-seu-afiliado.com/moldura")


with col4:
    st.image("https://via.placeholder.com/300x200/1E1E1E/FFFFFF?text=Alto-Falantes", use_column_width=True)
    st.subheader("Kit 2 Vias 6 Polegadas")
    st.text("Qualidade sonora interna.")
    st.link_button("Ver Oferta", "https://link-do-seu-afiliado.com/falantes")


st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")


# ==========================================
# SEÇÃO 2: PREMIUM (Ticket Alto e Lucro)
# ==========================================
st.header("💎 Projetos Premium Uno de Sete")
st.caption("Equipamentos selecionados pela nossa engenharia para quem exige o máximo de performance.")


# Criando 2 colunas grandes para destacar o valor agregado e as especificações
col_prem1, col_prem2 = st.columns(2)


with col_prem1:
    st.image("https://via.placeholder.com/600x400/1E1E1E/FFFFFF?text=Central+Pioneer+8+Pol", use_column_width=True)
    st.subheader("Central Multimídia Pioneer DMH-ZS8280TV (8\")")
    st.markdown("""
    - **Tela:** 8 Polegadas Capacitiva (24-bit truecolor)
    - **Conectividade:** Apple CarPlay e Android Auto
    - **Diferencial:** Integração nativa e áudio de alta fidelidade.
    """)
    # O 'type="primary"' deixa o botão com a cor de destaque do tema
    st.link_button("Garantir com Frete Grátis", "https://link-pioneer.com", type="primary")


with col_prem2:
    st.image("https://via.placeholder.com/600x400/1E1E1E/FFFFFF?text=Modulo+Taramps+MD3000", use_column_width=True)
    st.subheader("Módulo Amplificador Taramps MD 3000.1")
    st.markdown("""
    - **Potência Real:** 3000W RMS
    - **Impedância:** 2 Ohms
    - **Engenharia:** Sistema Smart Cooler contra superaquecimento.
    """)
    st.link_button("Ver Detalhes Técnicos", "https://link-taramps.com", type="primary")


st.markdown("<br><br>", unsafe_allow_html=True)


# ==========================================
# RODAPÉ
# ==========================================
st.markdown("---")
st.markdown("<div style='text-align: center; color: #A0AEC0;'>© 2026 Uno de Sete Curadoria Automotiva. Equipamentos certificados pelo nosso time técnico (Kael).</div>", unsafe_allow_html=True)