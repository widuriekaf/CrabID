# 🦀 CrabID — Klasifikasi Spesies Kepiting Laut

Aplikasi web berbasis **Streamlit** untuk mengidentifikasi spesies kepiting laut dan mendeteksi keamanan konsumsinya menggunakan model deep learning **ResNet50**.

> Proyek Mata Kuliah Pengolahan Citra Digital — Universitas Maritim Raja Ali Haji (UMRAH) 2025/2026

---

## ✨ Fitur

- 📸 **Upload gambar** kepiting (JPG, JPEG, PNG)
- 🤖 **Klasifikasi otomatis** menggunakan ResNet50
- ✅ / ☠️ **Deteksi keamanan** — membedakan spesies *edible* dan *poisonous*
- 🏆 **Top 3 prediksi** beserta confidence score
- ⚠️ **Out-of-distribution detection** — menolak gambar yang bukan kepiting atau di luar dataset
- 📋 Detail informasi spesies: nama umum, nama latin, dan status konsumsi

---

## 🐚 Spesies yang Dapat Diidentifikasi

| Spesies | Nama Latin | Status |
|---|---|---|
| Asian Paddle Crab | *Charybdis japonica* | ✅ Edible |
| Blue Crab | *Callinectes sapidus* | ✅ Edible |
| Mud Crab | *Scylla serrata* | ✅ Edible |
| Red Eye Crab | *Eriphia sebana* | ✅ Edible |
| Sentinel Crab | *Macrophthalmus japonicus* | ✅ Edible |
| Curry Puff Crab | *Lophozozymus pictor* | ☠️ Poisonous |
| Devil Crab | *Demania reynaudii* | ☠️ Poisonous |
| Floral Egg Crab | *Atergatis floridus* | ☠️ Poisonous |
| Purple Shore Crab | *Hemigrapsus nudus* | ☠️ Poisonous |
| Scorpion Crab | *Myomenippe hardwickii* | ☠️ Poisonous |

---

## 🛠️ Teknologi

- **Python** — bahasa pemrograman utama
- **Streamlit** — framework antarmuka web
- **TensorFlow / Keras** — loading dan inferensi model
- **ResNet50** — arsitektur deep learning untuk klasifikasi citra
- **Pillow (PIL)** — pemrosesan gambar
- **NumPy** — komputasi array
- **gdown** — pengunduhan model dari Google Drive

---

## ⚙️ Instalasi & Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/username/CrabID.git
cd CrabID
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run app.py
```

> **Catatan:** Model weights (`model_kepiting.weights.h5`) akan diunduh otomatis dari Google Drive saat pertama kali aplikasi dijalankan. Pastikan koneksi internet tersedia.

---

## 📁 Struktur File

```
CrabID/
├── app.py                      # Aplikasi utama Streamlit
├── model_kepiting.json         # Arsitektur model (Keras JSON)
├── model_kepiting.weights.h5   # Bobot model (diunduh otomatis)
├── requirements.txt            # Daftar dependensi
└── README.md
```

---

## 🔍 Cara Kerja

1. Pengguna mengupload foto kepiting
2. Gambar di-*resize* ke 224×224 piksel dan diproses menggunakan preprocessing ResNet50
3. Model memprediksi probabilitas untuk 10 kelas spesies
4. Sistem melakukan **validasi dua lapis**:
   - **Confidence threshold** — prediksi ditolak jika confidence < 45%
   - **Entropy threshold** — prediksi ditolak jika distribusi probabilitas terlalu merata (entropy ratio > 0.82)
5. Jika lolos validasi, aplikasi menampilkan spesies, status konsumsi, dan top 3 prediksi

---

## 📊 Dataset

- **Total gambar:** 1.921 gambar
- **Jumlah kelas:** 10 spesies kepiting laut
- **Split:** Train / Validation / Test

---

## 👩‍💻 TIM

2301020017 Widuri Eka Febriyanti 
2301020105 Adelia Kristianti Purba
2301020091 Yurida Normala Sari
