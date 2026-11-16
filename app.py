import streamlit as st

st.set_page_config(page_title="Passaport Digital Sostenible", page_icon="🌱", layout="centered")

# Estat inicial ampliat
if 'punts' not in st.session_state:
    st.session_state.punts = 120
if 'segells' not in st.session_state:
    st.session_state.segells = ["Caiac Sostenible (Estiu)", "Mercat del Lleó (Tardor)"]

st.title("🌱 Passaport Digital Sostenible")
st.subheader("Girona i la Costa Brava de les 4 Estacions (ONU 2027)")

menu = st.sidebar.selectbox("Navegació", [
    "🗺️ Mapa i Gestió de Fluxos", 
    "🍃 Experiències per Estacions", 
    "🛂 El Meu Passaport", 
    "🛍️ Comerç KM0 i Artesania",
    "📊 El Teu Impacte i ODS"
])

# --- 1. MAPA EN TEMPS REAL ---
if menu == "🗺️ Mapa i Gestió de Fluxos":
    st.markdown("### Estat de les zones en temps real")
    st.warning("⚠️ **Alerta de Massificació:** El Call Jueu i les Escales de la Catedral estan al 90% de capacitat.")
    st.info("💡 **Ruta alternativa recomanada:** Canvia cap a la **Vall de Sant Daniel** o la **Muralla** (Zones Verdes) per evitar aglomeracions i guanyar ➕ 50 EcoPoints extres!")
    
    if st.button("➕ Fes Check-in a Ruta Sostenible Alternativa"):
        st.session_state.punts += 50
        st.success("¡Check-in realitzat! Has sumat 50 punts per redistribuir el turisme.")

# --- 2. LES 4 ESTACIONS ---
elif menu == "🍃 Experiències per Estacions":
    st.markdown("### Descobreix el territori tot l'any")
    estacio = st.selectbox("Selecciona una estació:", ["Estiu (Costa Brava Blava)", "Tardor (Sabors de l'Empordà)", "Hivern (Calma i Artesania Viva)", "Primavera (Natura i Descoberta)"])
    
    if "Estiu" in estacio:
        st.info("🌊 **Activitats:** Caiacs autoritzats a Palamós i camins de ronda a primera hora de matí.")
    elif "Tardor" in estacio:
        st.info("🍇 **Activitats:** Tast de productes de temporada al Mercat del Lleó de Girona.")
    elif "Hivern" in estacio:
        st.info("🏺 **Activitats:** Rutes de llegendes medievals en grups reduïts i tallers de picapedrers.")
    else:
        st.info("🚲 **Activitats:** Senderisme de baix impacte i rutes amb bicicleta per la Vall de Sant Daniel.")

# --- 3. EL MEU PASSAPORT ---
elif menu == "🛂 El Meu Passaport":
    st.markdown("### El teu Passaport Digital 4 Estacions")
    st.metric(label="EcoPoints acumulats", value=f"{st.session_state.punts} pts", delta="+50 pts")
    
    st.markdown("#### 🏆 Segells Desbloquejats (2/12)")
    for segell in st.session_state.segells:
        st.write(f"✅ **{segell}**")
    st.write("🔒 *Pendent:* Taller de Ceràmica, Ofici de Picapedrer, Enquadernació...")

# --- 4. COMERÇOS I ARTESANIA ---
elif menu == "🛍️ Comerç KM0 i Artesania":
    st.markdown("### Xarxa d'Artesans i Productors Locals")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Terrissa Artesana Girona**\nModelatge de fang tradicional.\n\n*Cost: 100 punts*")
    with col2:
        st.info("**Formatges de l'Empordà**\nProducte de proximitat KM0.\n\n*Cost: 150 punts*")

# --- 5. IMPACTE I ODS ---
elif menu == "📊 El Teu Impacte i ODS":
    st.markdown("### El teu impacte regeneratiu")
    st.write("Gràcies a la teva manera de viatjar, avui has aconseguit:")
    col1, col2, col3 = st.columns(3)
    col1.metric("CO₂ Estalviat", "4.2 kg", "-100% vehicle")
    col2.metric("Aigua Protegida", "120 L", "Protocols sequera")
    col3.metric("Comerços Suport", "3 negocis", "Economia local")
    
    st.markdown("---")
    st.markdown("#### 🌐 Alineació amb els ODS de l'ONU (2027)")
    st.write("- **ODS 8:** Treball estable i suport al petit comerç.")
    st.write("- **ODS 11:** Descentralització i protecció del patrimoni.")
    st.write("- **ODS 12:** Consum responsable i productes de l'Empordà.")
    st.write("- **ODS 15:** Preservació d'ecosistemes i límits de càrrega.")

st.markdown("---")
st.caption("Prototip de prova oficial - Any Internacional del Turisme Sostenible 2027.")