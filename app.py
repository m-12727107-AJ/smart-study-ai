import streamlit as st

# ==============================
# SMARTSTUDY AI
# ==============================

st.set_page_config(
    page_title="SmartStudy AI",
    page_icon="💜",
    layout="wide"
)

# ==============================
# PURPLE SURFACE
# ==============================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5efff, #ffffff);
}

.main-title {
    text-align: center;
    color: #6A1B9A;
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(106,27,154,0.12);
    margin-bottom: 18px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="main-title">💜 SMARTSTUDY AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Aplikasi pembelajaran pintar untuk belajar, merancang dan melihat perkembangan</div>',
    unsafe_allow_html=True
)

# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("⚙️ Tetapan")

nama = st.sidebar.text_input(
    "👤 Nama Pelajar",
    placeholder="Masukkan nama"
)

bahasa = st.sidebar.selectbox(
    "🌐 Bahasa",
    ["BM", "English"]
)

# ==============================
# MENU
# ==============================

menu = st.sidebar.radio(
    "📚 Menu Utama",
    [
        "🏠 Dashboard",
        "🤖 AI Tutor",
        "📅 Study Planner",
        "📝 Quiz AI",
        "📊 Progress",
        "🏆 Misi & Lencana"
    ]
)

# ==============================
# DASHBOARD
# ==============================

if menu == "🏠 Dashboard":

    st.subheader("🏠 Dashboard")

    if nama:
        st.success(f"Selamat datang, {nama}! 👋")
    else:
        st.info("Masukkan nama anda di bahagian Tetapan.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("⭐ XP", "0")

    with col2:
        st.metric("🪙 Coin", "0")

    with col3:
        st.metric("📚 Aktiviti", "0")

    with col4:
        st.metric("🏆 Level", "1")

    st.markdown(
        '<div class="card"><h3>💡 SmartStudy AI</h3>'
        '<p>Satu aplikasi untuk membantu pelajar merancang pembelajaran, '
        'mendapat bantuan belajar, menjawab kuiz dan melihat perkembangan.</p>'
        '</div>',
        unsafe_allow_html=True
    )

# ==============================
# AI TUTOR
# ==============================

elif menu == "🤖 AI Tutor":

    st.subheader("🤖 AI Tutor")

    soalan = st.text_area(
        "💬 Masukkan soalan anda",
        placeholder="Contoh: Apakah sistem suria?"
    )

    if st.button("✨ Tanya AI Tutor"):

        if not soalan.strip():
            st.warning("Sila masukkan soalan dahulu.")

        else:

            q = soalan.lower()

            if bahasa == "BM":

                if "sistem suria" in q:
                    jawapan = (
                        "🌍 **Sistem suria** ialah sistem yang terdiri "
                        "daripada Matahari dan objek-objek yang mengelilinginya "
                        "seperti planet, bulan, asteroid dan komet."
                    )

                elif "fotosintesis" in q:
                    jawapan = (
                        "🌱 **Fotosintesis** ialah proses tumbuhan menghasilkan "
                        "makanan menggunakan cahaya matahari, karbon dioksida dan air."
                    )

                elif "sel" in q:
                    jawapan = (
                        "🔬 **Sel** ialah unit asas bagi struktur dan fungsi "
                        "hidupan."
                    )

                elif "graviti" in q:
                    jawapan = (
                        "🌎 **Graviti** ialah daya tarikan antara objek. "
                        "Contohnya, graviti menyebabkan objek jatuh ke arah Bumi."
                    )

                else:
                    jawapan = (
                        "💡 Cuba masukkan topik seperti **Sistem Suria, "
                        "Fotosintesis, Sel atau Graviti**."
                    )

            else:

                if "solar system" in q:
                    jawapan = (
                        "🌍 **The Solar System** consists of the Sun and "
                        "objects that orbit it, such as planets, moons, "
                        "asteroids and comets."
                    )

                elif "photosynthesis" in q:
                    jawapan = (
                        "🌱 **Photosynthesis** is the process by which "
                        "plants make food using sunlight, carbon dioxide and water."
                    )

                elif "cell" in q:
                    jawapan = (
                        "🔬 **A cell** is the basic structural and functional "
                        "unit of living organisms."
                    )

                elif "gravity" in q:
                    jawapan = (
                        "🌎 **Gravity** is a force of attraction between objects. "
                        "For example, it causes objects to fall toward Earth."
                    )

                else:
                    jawapan = (
                        "💡 Try asking about **Solar System, Photosynthesis, "
                        "Cell or Gravity**."
                    )

            st.markdown(
                f'<div class="card"><h3>💡 Jawapan</h3>{jawapan}</div>',
                unsafe_allow_html=True
            )

# ==============================
# STUDY PLANNER
# ==============================

elif menu == "📅 Study Planner":

    st.subheader("📅 Study Planner")

    subjek = st.text_input("📚 Subjek")
    topik = st.text_input("📖 Topik")
    masa = st.number_input(
        "⏱️ Masa belajar (minit)",
        min_value=15,
        max_value=180,
        value=30
    )

    if st.button("📅 Jana Study Plan"):

        if not subjek or not topik:
            st.warning("Sila isi subjek dan topik.")

        else:

            st.success("Study Plan berjaya dijana!")

            st.markdown(f"""
### 🎯 Pelan Pembelajaran

**Subjek:** {subjek}

**Topik:** {topik}

**Masa:** {masa} minit

#### 📝 Pelan

1. 📖 Baca dan fahami konsep utama
2. 🧠 Catat perkara penting
3. ✏️ Buat latihan
4. 🔍 Semak kesalahan
5. ⭐ Buat ulang kaji ringkas
""")

# ==============================
# QUIZ AI
# ==============================

elif menu == "📝 Quiz AI":

    st.subheader("📝 Quiz AI")

    st.write("### 🌍 Topik: Sistem Suria")

    q1 = st.radio(
        "1. Planet yang paling hampir dengan Matahari ialah:",
        ["A. Bumi", "B. Utarid", "C. Marikh"]
    )

    q2 = st.radio(
        "2. Planet yang dikenali sebagai Planet Merah ialah:",
        ["A. Zuhrah", "B. Musytari", "C. Marikh"]
    )

    q3 = st.radio(
        "3. Pusat Sistem Suria ialah:",
        ["A. Bumi", "B. Matahari", "C. Bulan"]
    )

    if st.button("✅ Semak Quiz"):

        markah = 0

        if q1.startswith("B"):
            markah += 1

        if q2.startswith("C"):
            markah += 1

        if q3.startswith("B"):
            markah += 1

        peratus = int((markah / 3) * 100)

        st.success(f"🎉 Markah anda: {peratus}%")

        st.write(f"⭐ XP diperoleh: {markah * 20}")
        st.write(f"🪙 Coin diperoleh: {markah * 5}")

# ==============================
# PROGRESS
# ==============================

elif menu == "📊 Progress":

    st.subheader("📊 Progress Pelajar")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📚 Jumlah Aktiviti", "0")
        st.metric("📝 Purata Markah", "0%")

    with col2:
        st.metric("⭐ Jumlah XP", "0")
        st.metric("🪙 Jumlah Coin", "0")

    st.info("Lengkapkan aktiviti pembelajaran untuk melihat progress anda.")

# ==============================
# MISSIONS & BADGES
# ==============================

elif menu == "🏆 Misi & Lencana":

    st.subheader("🏆 Misi & Lencana")

    st.markdown("""
### 🎯 Misi Pembelajaran

🔹 Lengkapkan aktiviti pertama  
🔹 Jawab kuiz  
🔹 Kumpul XP  
🔹 Teruskan pembelajaran

### 🏅 Lencana

🌱 **Langkah Pertama**

📚 **Pelajar Aktif**

🔥 **Pembelajar Hebat**

🏆 **Master Pembelajaran**

👑 **Master SmartStudy**
""")

st.markdown("---")

st.caption("💜 SmartStudy AI | AI Learning Innovation")
