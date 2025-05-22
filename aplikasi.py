import streamlit as st
import matplotlib.pyplot as plt

st.title("🏍️ Aplikasi Penghitung Waktu Baku Produksi Motor")

st.markdown("""
Aplikasi ini menghitung **waktu baku** berdasarkan:
- Waktu siklus (Cycle Time)
- Faktor kelonggaran (Allowance Factor)

Dan menampilkan **grafik komponen waktu kerja**.
""")

# Input dari pengguna
ct = st.number_input("⏱️ Masukkan Waktu Siklus (dalam detik):", min_value=0.0, value=60.0)
af_percent = st.number_input("📉 Masukkan Faktor Kelonggaran (dalam persen):", min_value=0.0, value=15.0)

# Konversi persen ke desimal
af = af_percent / 100

# Hitung waktu tambahan dan waktu baku
waktu_tambahan = ct * af
waktu_baku = ct + waktu_tambahan

# Tampilkan hasil
st.subheader("📊 Hasil Perhitungan:")
st.write(f"**Waktu Baku = {ct:.2f} × (1 + {af:.2f}) = {waktu_baku:.2f} detik**")
st.write(f"- Waktu Siklus: {ct:.2f} detik")
st.write(f"- Waktu Tambahan (Kelonggaran): {waktu_tambahan:.2f} detik")

# Grafik batang
st.subheader("📈 Grafik Komponen Waktu Baku")

labels = ['Waktu Siklus', 'Kelonggaran', 'Total Waktu Baku']
values = [ct, waktu_tambahan, waktu_baku]
colors = ['blue', 'orange', 'green']

fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=colors)
ax.set_ylabel("Waktu (detik)")
ax.set_title("Komponen Waktu Baku Produksi Motor")

# Tambahkan nilai di atas batang
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.1f}', ha='center', va='bottom')

st.pyplot(fig)
