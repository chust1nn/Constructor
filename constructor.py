import streamlit as st
from google import genai
import time

# --- CONFIGURACIÓN DE LA PÁGINA (WIDE MODE + LOGO PERSONALIZADO) ---
st.set_page_config(
    page_title="CYBR_ // Constructor Conceptual", 
    page_icon="logo.png",
    layout="wide"
)

# --- ESTILOS CSS MODO OSCURO / CYBR-BRUTALISM EXPANDIDO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Syne:wght@700;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Space Grotesk', sans-serif;
        background-color: #0d0d11;
        color: #f0f0f5;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .block-container {
        max-width: 100% !important;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 6rem;
        padding-right: 6rem;
    }

    .titulo-brutal {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: -0.03em;
        color: #f0f0f5;
    }

    /* Botones principales */
    .stButton>button {
        width: 100%;
        border-radius: 0px;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.15em;
        padding: 1rem;
        border: 2px solid #ffd166;
        background-color: #7209b7;
        color: #ffffff;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        background-color: #ffd166 !important;
        color: #0d0d11 !important;
        border-color: #ffd166 !important;
    }

    /* Contenedor HUD Estilo Panel Técnico */
    .hud-card {
        background-color: #16161e;
        border: 2px solid #7209b7;
        padding: 45px;
        box-shadow: 8px 8px 0px #ffd166;
        margin-top: 15px;
        position: relative;
    }

    /* Elementos decorativos laterales */
    .side-decor-left {
        position: fixed;
        left: 20px;
        top: 30%;
        writing-mode: vertical-rl;
        font-family: 'Syne', sans-serif;
        font-size: 0.75rem;
        color: #7209b7;
        letter-spacing: 0.2em;
        font-weight: 800;
        opacity: 0.6;
    }

    .side-decor-right {
        position: fixed;
        right: 20px;
        top: 30%;
        writing-mode: vertical-lr;
        font-family: 'Syne', sans-serif;
        font-size: 0.75rem;
        color: #ffd166;
        letter-spacing: 0.2em;
        font-weight: 800;
        opacity: 0.6;
    }

    .tag-cybr {
        display: inline-block;
        background-color: #22222f;
        color: #ffd166;
        padding: 8px 16px;
        margin: 5px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid #7209b7;
    }

    /* Inputs de texto grandes y visibles */
    .stTextInput input {
        border-radius: 0px !important;
        border: 2px solid #7209b7 !important;
        background-color: #16161e !important;
        padding: 16px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: 600;
    }
    .stTextInput input:focus {
        border-color: #ffd166 !important;
        box-shadow: 4px 4px 0px #ffd166 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SCRIPT GLOBAL DE ENFOQUE AUTOMÁTICO (MUTATION OBSERVER) ---
st.markdown("""
    <script>
        const observer = new MutationObserver((mutations, obs) => {
            const input = document.querySelector('input[type="text"]');
            if (input) {
                input.focus();
                obs.disconnect();
            }
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    </script>
""", unsafe_allow_html=True)

# --- CONFIGURACIÓN DE LA IA ---
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- CONTROL DE ESTADO ---
if "paso" not in st.session_state:
    st.session_state.paso = 1  
if "tema" not in st.session_state:
    st.session_state.tema = ""
if "palabras" not in st.session_state:
    st.session_state.palabras = []
if "definicion_generada" not in st.session_state:
    st.session_state.definicion_generada = ""
if "animacion_vista" not in st.session_state:
    st.session_state.animacion_vista = False

def avanzar_paso_1():
    tema_val = st.session_state.input_tema.strip()
    if not tema_val:
        st.warning("Ingrese un concepto central para continuar.")
    else:
        st.session_state.tema = tema_val
        st.session_state.paso = 2

def agregar_palabra():
    palabra = st.session_state.input_palabra.strip()
    if palabra and palabra not in st.session_state.palabras:
        st.session_state.palabras.append(palabra)
    st.session_state.input_palabra = ""

# --- DECORACIONES LATERALES ---
st.markdown("<div class='side-decor-left'>// SYS.STATUS: ACTIVE_NODE // 2026</div>", unsafe_allow_html=True)
st.markdown("<div class='side-decor-right'>[ SECURE_PROTOCOL_VERIFIED ]</div>", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<div style='display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2px solid #7209b7; padding-bottom: 12px; margin-bottom: 10px;'>", unsafe_allow_html=True)
st.markdown("<h1 class='titulo-brutal' style='font-size: 2.2rem; margin: 0;'>CYBR_DEF // KNOWLEDGE MATRIX</h1>", unsafe_allow_html=True)
st.markdown("<span style='font-size: 0.85rem; font-weight: 700; letter-spacing: 0.1em; color: #ffd166;'>SYS.CORE // 2026</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Contenedor HUD Principal
st.markdown("<div class='hud-card'>", unsafe_allow_html=True)

# ==========================================
# PASO 1: CONCEPTO CENTRAL
# ==========================================
if st.session_state.paso == 1:
    st.markdown("<span style='font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; color: #ffd166;'>/ 01</span>", unsafe_allow_html=True)
    st.markdown("<h3 class='titulo-brutal' style='font-size: 1.6rem; margin-top: 4px; margin-bottom: 12px;'>CORE CONCEPT</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a0b0; font-size: 1.1rem; margin-bottom: 25px;'>Define el núcleo conceptual que estructurará la sesión.</p>", unsafe_allow_html=True)
    
    st.text_input(
        "Concepto:", 
        value=st.session_state.tema,
        key="input_tema",
        placeholder="Ej. Sostenibilidad, Algoritmo...",
        label_visibility="collapsed",
        on_change=avanzar_paso_1
    )
    
    st.write("")
    if st.button("CONTINUAR"):
        avanzar_paso_1()
        st.rerun()

# ==========================================
# PASO 2: LLUVIA DE IDEAS
# ==========================================
elif st.session_state.paso == 2:
    st.markdown("<span style='font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; color: #ffd166;'>/ 02</span>", unsafe_allow_html=True)
    st.markdown(f"<h3 class='titulo-brutal' style='font-size: 1.6rem; margin-top: 4px; margin-bottom: 8px;'>LEXICON INPUTS</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #a0a0b0; font-size: 1.1rem; margin-bottom: 20px;'>Términos vinculados a: <b style='color:#ffd166;'>{st.session_state.tema}</b></p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.text_input("Añadir término:", key="input_palabra", on_change=agregar_palabra, label_visibility="collapsed", placeholder="Añadir término clave y presionar Enter...")
    with col2:
        st.button("AÑADIR", on_click=agregar_palabra)

    if st.session_state.palabras:
        st.write("")
        st.markdown("<p style='font-size: 0.8rem; font-weight: 700; color: #ffd166; text-transform: uppercase; letter-spacing: 0.15em;'>Buffer de datos:</p>", unsafe_allow_html=True)
        html_tags = "".join([f"<span class='tag-cybr'>{p}</span>" for p in st.session_state.palabras])
        st.markdown(html_tags, unsafe_allow_html=True)
        st.write("")
        
        if st.button("LIMPIAR BUFFER"):
            st.session_state.palabras = []
            st.rerun()
    
    st.divider()
    
    col_izq, col_der = st.columns(2)
    with col_izq:
        if st.button("ATRAS"):
            st.session_state.paso = 1
            st.rerun()
    with col_der:
        if st.button("GENERAR SINTESIS"):
            if len(st.session_state.palabras) < 2:
                st.warning("Se requieren al menos 2 términos para procesar.")
            else:
                st.session_state.paso = 3
                st.session_state.animacion_vista = False
                st.rerun()

# ==========================================
# PASO 3: RESULTADO Y ESCRITURA
# ==========================================
elif st.session_state.paso == 3:
    if not st.session_state.definicion_generada:
        lista_palabras_str = ", ".join(st.session_state.palabras)
        prompt_ia = f"""
        Actúa como un facilitador de aprendizaje. 
        Tu objetivo es construir una definición sobre el tema '{st.session_state.tema}' utilizando EXCLUSIVAMENTE el significado y la relación lógica de las siguientes palabras aportadas por los alumnos: {lista_palabras_str}.

        Instrucciones:
        1. NO busques la definición académica o técnica en tu base de datos.
        2. Analiza las palabras dadas y construye un concepto que tenga sentido lógico a partir de ellas. 
        3. Si las palabras parecen no tener relación directa, busca el punto común entre ellas para explicar el concepto de '{st.session_state.tema}'.
        4. Debes integrar OBLIGATORIAMENTE todas las palabras envolviéndolas exactamente con etiquetas HTML span en color amarillo, usando este formato exacto: <span style="color: #ffd166; font-weight: 700;">palabra</span>.
        5. Mantén un tono neutro, constructivo y simple. No añadas información técnica que los alumnos no hayan mencionado.
        6. Devuelve únicamente el texto de la definición resultante con esas etiquetas aplicadas a las palabras clave.
        """
        
        with st.spinner("PROCESANDO SÍNTESIS..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt_ia,
                )
                st.session_state.definicion_generada = response.text
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    st.session_state.definicion_generada = "Límite de cuota alcanzado temporalmente. Reintente en unos segundos."
                else:
                    st.session_state.definicion_generada = f"Error de conexión: {e}"
                st.rerun()
        st.rerun()

    st.markdown("<span style='font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; color: #ffd166;'>/ 03</span>", unsafe_allow_html=True)
    st.markdown("<h3 class='titulo-brutal' style='font-size: 1.6rem; margin-top: 4px; margin-bottom: 20px;'>SYNTHESIS RESULT</h3>", unsafe_allow_html=True)
    
    texto_placeholder = st.empty()
    texto_completo = st.session_state.definicion_generada
    
    if not st.session_state.animacion_vista:
        texto_actual = ""
        for palabra in texto_completo.split(" "):
            texto_actual += palabra + " "
            texto_placeholder.markdown(f"""
                <div style="border-left: 4px solid #ffd166; padding-left: 20px; margin: 15px 0; background-color: #111117; padding: 25px;">
                    <p style="font-size: 1.3rem; line-height: 1.7; margin: 0; font-weight: 600; color: #f0f0f5;">{texto_actual}█</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(0.05)
        st.session_state.animacion_vista = True

    texto_placeholder.markdown(f"""
        <div style="border-left: 4px solid #ffd166; padding-left: 20px; margin: 15px 0; background-color: #111117; padding: 25px;">
            <p style="font-size: 1.3rem; line-height: 1.7; margin: 0; font-weight: 600; color: #f0f0f5;">{texto_completo}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    col_reiniciar, _ = st.columns([1, 1])
    with col_reiniciar:
        if st.button("NUEVA DEFINICION"):
            st.session_state.paso = 1
            st.session_state.tema = ""
            st.session_state.palabras = []
            st.session_state.definicion_generada = ""
            st.session_state.animacion_vista = False
            st.rerun()