import streamlit as st
import numpy as np
from PIL import Image
import json
import os

st.set_page_config(
    page_title="CrabID — Klasifikasi Kepiting Laut",
    page_icon="🦀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.stApp {
    background: #fefce8;
}

.main .block-container {
    padding: 1rem;
    max-width: 1000px;
    margin: 0 auto;
}

@media (min-width: 768px) {
    .main .block-container {
        padding: 2rem;
    }
}

#MainMenu, footer, header {
    visibility: hidden;
}

.stDeployButton {
    display: none;
}

/* Header / Navbar */
.navbar {
    background: white;
    border-radius: 60px;
    padding: 0.8rem 1.5rem;
    margin-bottom: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    border: 1px solid #fde047;
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.3rem;
    font-weight: 700;
    color: #ca8a04;
}

.logo span {
    background: #eab308;
    color: white;
    padding: 0.2rem 0.6rem;
    border-radius: 40px;
    font-size: 0.8rem;
}

.nav-items {
    display: flex;
    gap: 1rem;
}

.nav-badge {
    background: #fef3c7;
    padding: 0.3rem 1rem;
    border-radius: 40px;
    font-size: 0.7rem;
    font-weight: 600;
    color: #b45309;
}

/* Hero Card */
.hero-card {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border-radius: 32px;
    padding: 2rem;
    margin-bottom: 2rem;
    text-align: center;
    border: 2px solid #fbbf24;
    box-shadow: 0 10px 30px rgba(234, 179, 8, 0.2);
}

.crab-icon {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.hero-title {
    font-size: 2rem;
    font-weight: 800;
    color: #78350f;
    margin-bottom: 0.5rem;
}

.hero-title span {
    background: #eab308;
    color: white;
    padding: 0.1rem 0.6rem;
    border-radius: 20px;
    display: inline-block;
}

.hero-sub {
    color: #92400e;
    font-size: 0.85rem;
    max-width: 500px;
    margin: 0 auto;
}

@media (min-width: 768px) {
    .hero-title {
        font-size: 2.5rem;
    }
}

/* Stat Cards */
.stats-wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}

.stat-item {
    background: white;
    border-radius: 20px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #fde047;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    transition: all 0.2s ease;
}

.stat-item:hover {
    transform: translateY(-3px);
}

.stat-num {
    font-size: 1.6rem;
    font-weight: 800;
    color: #eab308;
}

.stat-text {
    font-size: 0.65rem;
    font-weight: 600;
    color: #78350f;
    text-transform: uppercase;
    letter-spacing: 1px;
}

@media (min-width: 768px) {
    .stat-num { font-size: 2rem; }
    .stat-text { font-size: 0.7rem; }
}

/* Upload Box */
.upload-box {
    background: white;
    border-radius: 28px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border: 2px dashed #fbbf24;
    text-align: center;
    transition: all 0.3s ease;
}

.upload-box:hover {
    border-color: #eab308;
    background: #fefce8;
}

.upload-title {
    font-size: 1rem;
    font-weight: 700;
    color: #78350f;
    margin-bottom: 0.3rem;
}

.upload-sub {
    font-size: 0.7rem;
    color: #b45309;
    margin-bottom: 1rem;
}

div[data-testid="stFileUploadDropzone"] {
    background: #fefce8 !important;
    border: 2px dashed #fbbf24 !important;
    border-radius: 20px !important;
}

div[data-testid="stFileUploadDropzone"]:hover {
    background: #fef3c7 !important;
    border-color: #eab308 !important;
}

/* Image Container - CENTERED */
.image-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-bottom: 1.5rem;
}

.image-wrapper img {
    border-radius: 20px;
    border: 3px solid #fbbf24;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    max-width: 300px;
    width: 100%;
    height: auto;
}

.image-caption-text {
    text-align: center;
    font-size: 0.8rem;
    font-weight: 600;
    color: #78350f;
    background: #fef3c7;
    display: inline-block;
    padding: 0.4rem 1.2rem;
    border-radius: 40px;
    margin-top: 0.8rem;
}

/* Custom Spinner */
.custom-spinner {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #78350f;
    padding: 0.8rem 1.8rem;
    border-radius: 60px;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    border: 2px solid #fbbf24;
    z-index: 9999;
}

.spinner-icon {
    width: 20px;
    height: 20px;
    border: 3px solid #fef3c7;
    border-top-color: #fbbf24;
    border-radius: 50%;
    animation: spin 0.6s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.custom-spinner span {
    color: #fef3c7;
    font-weight: 600;
    font-size: 0.85rem;
}

/* Result Card */
.result-card {
    background: white;
    border-radius: 28px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border: 2px solid #fbbf24;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}

.result-edible {
    border-top: 8px solid #22c55e;
}

.result-poison {
    border-top: 8px solid #ef4444;
}

.result-reject {
    border-top: 8px solid #6b7280;
}

.species-badge {
    display: inline-block;
    background: #fef3c7;
    padding: 0.2rem 0.8rem;
    border-radius: 40px;
    font-size: 0.65rem;
    font-weight: 600;
    color: #b45309;
    margin-bottom: 1rem;
}

.species-name {
    font-size: 1.8rem;
    font-weight: 800;
    color: #78350f;
    margin-bottom: 0.2rem;
}

.species-latin {
    font-size: 0.8rem;
    font-style: italic;
    color: #b45309;
    margin-bottom: 1rem;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 1rem;
    border-radius: 40px;
    font-size: 0.75rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
}

.status-edible {
    background: #dcfce7;
    color: #15803d;
    border: 1px solid #86efac;
}

.status-poison {
    background: #fee2e2;
    color: #b91c1c;
    border: 1px solid #fca5a5;
}

.status-reject {
    background: #f3f4f6;
    color: #4b5563;
    border: 1px solid #d1d5db;
}

.conf-section {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid #fef3c7;
}

.conf-label {
    font-size: 0.65rem;
    font-weight: 600;
    color: #b45309;
    margin-bottom: 0.3rem;
}

.conf-bar {
    background: #fef3c7;
    border-radius: 20px;
    height: 8px;
    overflow: hidden;
}

.conf-fill {
    height: 100%;
    border-radius: 20px;
    transition: width 0.5s ease;
}

.conf-fill-edible {
    background: #22c55e;
}

.conf-fill-poison {
    background: #ef4444;
}

.conf-value {
    font-size: 1.2rem;
    font-weight: 800;
    color: #78350f;
    margin-top: 0.3rem;
}

.info-message {
    margin-top: 1rem;
    padding: 0.8rem 1rem;
    border-radius: 16px;
    font-size: 0.75rem;
    line-height: 1.5;
}

.info-edible {
    background: #dcfce7;
    color: #15803d;
    border: 1px solid #86efac;
}

.info-poison {
    background: #fee2e2;
    color: #b91c1c;
    border: 1px solid #fca5a5;
}

.info-reject {
    background: #f3f4f6;
    color: #4b5563;
    border: 1px solid #d1d5db;
}

/* Top 3 Card - LIST VIEW (kembali ke gaya awal) */
.top3-card {
    background: white;
    border-radius: 20px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    border: 1px solid #fde047;
}

.section-title {
    font-size: 0.7rem;
    font-weight: 700;
    color: #b45309;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 1rem;
}

/* PREDICTION ROWS - LIST VIEW seperti awal */
.pred-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.8rem 0;
    border-bottom: 1px solid #fef3c7;
}

.pred-row:last-child {
    border-bottom: none;
}

.pred-name {
    font-weight: 600;
    color: #78350f;
    font-size: 0.9rem;
}

.pred-name span {
    font-size: 1rem;
    margin-right: 0.5rem;
}

.pred-conf {
    font-weight: 700;
    color: #eab308;
    font-size: 0.9rem;
    font-family: monospace;
}

/* Detail Grid */
.detail-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
    margin-top: 1rem;
}

.detail-item {
    background: #fefce8;
    border-radius: 16px;
    padding: 0.8rem;
}

.detail-label {
    font-size: 0.6rem;
    font-weight: 600;
    color: #b45309;
    text-transform: uppercase;
    margin-bottom: 0.2rem;
}

.detail-value {
    font-size: 0.85rem;
    font-weight: 700;
    color: #78350f;
    word-wrap: break-word;
}

/* Species List - GRID 2 KOLOM */
.species-list {
    background: white;
    border-radius: 20px;
    padding: 1.2rem;
    border: 1px solid #fde047;
}

.species-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.5rem;
}

@media (min-width: 640px) {
    .species-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 0.8rem;
    }
}

.species-card {
    background: #fefce8;
    border-radius: 14px;
    padding: 0.8rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s ease;
    border: 1px solid #fef3c7;
}

.species-card:hover {
    border-color: #fbbf24;
    transform: translateX(3px);
}

.species-card-info {
    flex: 1;
}

.species-card-name {
    font-weight: 700;
    color: #78350f;
    font-size: 0.85rem;
}

.species-card-latin {
    font-size: 0.65rem;
    color: #b45309;
    font-style: italic;
}

.species-card-tag {
    font-size: 0.6rem;
    font-weight: 600;
    padding: 0.2rem 0.6rem;
    border-radius: 40px;
    white-space: nowrap;
}

.tag-edible-card {
    background: #dcfce7;
    color: #15803d;
}

.tag-poison-card {
    background: #fee2e2;
    color: #b91c1c;
}

/* Footer */
.footer {
    text-align: center;
    padding: 1.5rem 0;
    margin-top: 2rem;
    color: #b45309;
    font-size: 0.65rem;
    border-top: 1px solid #fde047;
}

/* Hide default streamlit elements */
.stSpinner > div {
    display: none !important;
}

/* Hide default streamlit caption */
.stImage figcaption {
    display: none !important;
}
</style>

<!-- Navbar -->
<div class="navbar">
    <div class="logo">
        🦀 Crab<span>ID</span>
    </div>
    <div class="nav-items">
        <div class="nav-badge">AI-Powered</div>
        <div class="nav-badge">ResNet50</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== DATA =====
SPECIES_INFO = {
    "asian_paddle_crab":  {"label": "Asian Paddle Crab",  "status": "EDIBLE",    "latin": "Charybdis japonica"},
    "blue_crab":          {"label": "Blue Crab",          "status": "EDIBLE",    "latin": "Callinectes sapidus"},
    "curry_puff_crab":    {"label": "Curry Puff Crab",    "status": "POISONOUS", "latin": "Lophozozymus pictor"},
    "devil_crab":         {"label": "Devil Crab",         "status": "POISONOUS", "latin": "Demania reynaudii"},
    "floral_egg_crab":    {"label": "Floral Egg Crab",    "status": "POISONOUS", "latin": "Atergatis floridus"},
    "mud_crab":           {"label": "Mud Crab",           "status": "EDIBLE",    "latin": "Scylla serrata"},
    "purple_shore_crab":  {"label": "Purple Shore Crab",  "status": "POISONOUS", "latin": "Hemigrapsus nudus"},
    "red_eye_crab":       {"label": "Red Eye Crab",       "status": "EDIBLE",    "latin": "Eriphia sebana"},
    "scorpion_crab":      {"label": "Scorpion Crab",      "status": "POISONOUS", "latin": "Myomenippe hardwickii"},
    "sentinel_crab":      {"label": "Sentinel Crab",      "status": "EDIBLE",    "latin": "Macrophthalmus japonicus"},
}

def download_model():
    import gdown
    weights_path = "model_kepiting.weights.h5"
    json_path = "model_kepiting.json"
    
    if not os.path.exists(weights_path):
        with st.spinner("⏬ Mengunduh model dari Google Drive..."):
            # File ID dari Google Drive
            file_id = "1CBh5iPcpo7SH5nKAml9Uk_zi_-7DugDU"
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, weights_path, quiet=False)

@st.cache_resource
def load_model():
    try:
        import tensorflow as tf
        import json
        download_model()
        with open("model_kepiting.json", "r") as f:
            config = json.load(f)
        model = tf.keras.models.model_from_json(json.dumps(config))
        model.load_weights("model_kepiting.weights.h5")
        return model
    except Exception as e:
        st.error(f"Error memuat model: {e}")
        return None

@st.cache_data
def load_class_names():
    return [
        "asian_paddle_crab", 
        "blue_crab", 
        "curry_puff_crab", 
        "devil_crab", 
        "floral_egg_crab", 
        "mud_crab", 
        "purple_shore_crab", 
        "red_eye_crab", 
        "scorpion_crab", 
        "sentinel_crab"
    ]

def predict(image_pil, model, class_names):
    import tensorflow as tf
    import numpy as np

    img = image_pil.resize((224, 224))
    img_array = np.array(img, dtype=np.float32)

    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]
        
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

    predictions = model.predict(img_array, verbose=0)
    probs = predictions[0]

    epsilon = 1e-10
    entropy = -np.sum(probs * np.log(probs + epsilon))
    max_entropy = np.log(len(class_names))
    entropy_ratio = entropy / max_entropy

    top3_idx = np.argsort(probs)[::-1][:3]
    
    results = []
    for idx in top3_idx:
        if idx < len(class_names):
            class_key = class_names[idx]
        else:
            class_key = class_names[0]
            
        info = SPECIES_INFO.get(class_key, {"label": class_key, "status": "UNKNOWN", "latin": "-"})
        results.append({
            "key": class_key,
            "label": info["label"],
            "status": info["status"],
            "latin": info["latin"],
            "confidence": float(probs[idx]) * 100
        })

    results[0]["entropy_ratio"] = float(entropy_ratio)
    return results

def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# ===== UI =====

# Hero Section
st.markdown("""
<div class="hero-card">
    <div class="crab-icon">🦀 🦞 🦀</div>
    <div class="hero-title">Crab<span>ID</span></div>
    <div class="hero-sub">Identifikasi spesies kepiting laut dan deteksi keamanan konsumsi</div>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown("""
<div class="stats-wrapper">
    <div class="stat-item">
        <div class="stat-num">10</div>
        <div class="stat-text">Spesies</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">1.921</div>
        <div class="stat-text">Dataset</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">ResNet50</div>
        <div class="stat-text">Model AI</div>
    </div>
</div>
""", unsafe_allow_html=True)

model = load_model()
class_names = load_class_names()

# Upload Section
st.markdown("""
<div class="upload-box">
    <div class="upload-title">📸 Upload Foto Kepiting</div>
    <div class="upload-sub">Format: JPG, JPEG, PNG</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload gambar kepiting", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

CONFIDENCE_THRESHOLD = 45.0
ENTROPY_THRESHOLD = 0.82

if uploaded_file:
    image = Image.open(uploaded_file)
    
    # Display image dengan posisi CENTER
    img_base64 = image_to_base64(image)
    st.markdown(f"""
    <div class="image-wrapper">
        <img src="data:image/png;base64,{img_base64}" alt="Uploaded crab">
        <div class="image-caption-text">📷 Gambar yang diupload</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom spinner
    spinner_placeholder = st.empty()
    spinner_placeholder.markdown("""
    <div class="custom-spinner">
        <div class="spinner-icon"></div>
        <span>🔍 Sedang menganalisis gambar...</span>
    </div>
    """, unsafe_allow_html=True)
    
    if model is not None:
        results = predict(image, model, class_names)
    else:
        st.error("Model gagal dimuat. Pastikan file model_kepiting.json dan model_kepiting.weights.h5 ada.")
        st.stop()
    
    spinner_placeholder.empty()

    top = results[0]
    entropy_ratio = top.get("entropy_ratio", 0.0)
    is_rejected = top["confidence"] < CONFIDENCE_THRESHOLD or entropy_ratio > ENTROPY_THRESHOLD

    if is_rejected:
        reject_reason = ""
        if top["confidence"] < CONFIDENCE_THRESHOLD and entropy_ratio > ENTROPY_THRESHOLD:
            reject_reason = "Confidence rendah dan model tidak yakin dengan prediksi ini."
        elif top["confidence"] < CONFIDENCE_THRESHOLD:
            reject_reason = f"Confidence terlalu rendah ({top['confidence']:.1f}% < {CONFIDENCE_THRESHOLD}%)."
        else:
            reject_reason = "Distribusi probabilitas terlalu merata — model tidak dapat membedakan spesies."

        st.markdown(f"""
        <div class="result-card result-reject">
            <div class="species-badge">⚠️ HASIL IDENTIFIKASI</div>
            <div class="species-name">Objek Tidak Dikenali</div>
            <div class="species-latin">Out of Distribution / Di Luar Dataset</div>
            <span class="status-badge status-reject">❌ Kategori Tidak Terdaftar</span>
            <div class="conf-section">
                <div class="conf-label">CONFIDENCE SCORE TERTINGGI</div>
                <div class="conf-bar">
                    <div class="conf-fill" style="width:{top['confidence']:.1f}%; background:#9ca3af;"></div>
                </div>
                <div class="conf-value">{top['confidence']:.1f}%</div>
            </div>
            <div class="info-message info-reject">
                ⚠️ <strong>SISTEM MENOLAK:</strong> {reject_reason}
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        is_edible = top["status"] == "EDIBLE"
        result_class = "result-edible" if is_edible else "result-poison"
        status_class = "status-edible" if is_edible else "status-poison"
        status_text = "✅ EDIBLE — Aman Dikonsumsi" if is_edible else "☠️ POISONOUS — Beracun"
        info_class = "info-edible" if is_edible else "info-poison"
        info_text = "✅ Spesies ini <strong>aman untuk dikonsumsi</strong>. Pastikan dimasak dengan benar." if is_edible else "⚠️ <strong>PERINGATAN:</strong> Spesies ini mengandung racun berbahaya. <strong>Jangan dikonsumsi!</strong>"
        fill_class = "conf-fill-edible" if is_edible else "conf-fill-poison"

        st.markdown(f"""
        <div class="result-card {result_class}">
            <div class="species-badge">🦀 HASIL IDENTIFIKASI</div>
            <div class="species-name">{top['label']}</div>
            <div class="species-latin">{top['latin']}</div>
            <span class="status-badge {status_class}">{status_text}</span>
            <div class="conf-section">
                <div class="conf-label">CONFIDENCE SCORE</div>
                <div class="conf-bar">
                    <div class="conf-fill {fill_class}" style="width:{top['confidence']:.1f}%;"></div>
                </div>
                <div class="conf-value">{top['confidence']:.1f}%</div>
            </div>
            <div class="info-message {info_class}">
                {info_text}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Top 3 Predictions - LIST VIEW (kembali ke gaya awal)
        st.markdown(f"""
        <div class="top3-card">
            <div class="section-title">🏆 TOP 3 PREDIKSI</div>
        """, unsafe_allow_html=True)
        
        medals = ["🥇", "🥈", "🥉"]
        for i, r in enumerate(results):
            dot_color = "#86efac" if r["status"] == "EDIBLE" else "#fecaca"
            st.markdown(f"""
            <div class="pred-row">
                <span class="pred-name">{medals[i]} {r['label']} <span style="color:{dot_color}; font-size:0.7rem;">●</span></span>
                <span class="pred-conf">{r['confidence']:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Detail Info
        st.markdown(f"""
        <div class="top3-card">
            <div class="section-title">📋 DETAIL INFORMASI</div>
            <div class="detail-grid">
                <div class="detail-item">
                    <div class="detail-label">Spesies</div>
                    <div class="detail-value">{top['label']}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Status</div>
                    <div class="detail-value" style="color:{'#15803d' if is_edible else '#b91c1c'}">{top['status']}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Nama Latin</div>
                    <div class="detail-value" style="font-style:italic;">{top['latin']}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Confidence</div>
                    <div class="detail-value">{top['confidence']:.1f}%</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    # Species List - GRID 2 KOLOM
    st.markdown("""
    <div class="species-list">
        <div class="section-title">🐚 10 SPESIES YANG DAPAT DIIDENTIFIKASI</div>
        <div class="species-grid">
    """, unsafe_allow_html=True)
    
    for key, info in SPECIES_INFO.items():
        is_ed = info["status"] == "EDIBLE"
        tag_class = "tag-edible-card" if is_ed else "tag-poison-card"
        tag_text = "✅ Edible" if is_ed else "☠️ Poisonous"
        st.markdown(f"""
            <div class="species-card">
                <div class="species-card-info">
                    <div class="species-card-name">{info['label']}</div>
                    <div class="species-card-latin">{info['latin']}</div>
                </div>
                <div class="species-card-tag {tag_class}">{tag_text}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>🦀 CrabID — Klasifikasi Spesies Kepiting Laut</p>
    <p>Mata Kuliah Pengolahan Citra Digital • Universitas Maritim Raja Ali Haji • 2025/2026</p>
</div>
""", unsafe_allow_html=True)
