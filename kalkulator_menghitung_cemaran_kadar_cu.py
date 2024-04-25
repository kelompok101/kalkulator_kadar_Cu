import streamlit as st

st.header('Perhitungan kadar c terukur', divider='rainbow')

y = st.number_input("Masukkan nilai y:", step=0.0001)
st.write ("Nilai absorbansi adalah", y)
a = st.number_input("Masukkan nilai a:", step=0.0001)
st.write ("Nilai intersept adalah", a)
b = st.number_input("Masukkan nilai b:", step=0.0001)
st.write ("Nilai slope adalah", b)

y2 = st.number_input("Masukkan nilai y2:", step=0.0001)
st.write ("Nilai absorbansi adalah", y2)
a2 = st.number_input("Masukkan nilai a2:", step=0.0001)
st.write ("Nilai intersept adalah", a2)
b2 = st.number_input("Masukkan nilai b2:", step=0.0001)
st.write ("Nilai slope adalah", b2)

hitung_x = st.button("Hitung kadar c terukur")

if hitung_x:
    x = (y - a) / b
    x2 = (y2 - a2) / b2
    rata_rata_x = (x + x2) / 2
    st.write(f"Hasil perhitungan x = {rata_rata_x} (mg/L)")

st.header("CEMARAN KADAR Cu DALAM SAMPEL", divider='rainbow')

c_terukur = st.number_input("Masukkan kadar C terukur (mg/L)", step=0.0001)
st.write("Nilai kadar C terukur adalah", c_terukur)
v = st.number_input("Masukkan nilai V (L):", step=0.0001)
st.write("Nilai volume adalah", v)
FP = st.number_input("Masukkan nilai FP:", step=0.0001)
st.write("Nilai FP adalah", FP)
bobot_sampel = st.number_input("Masukkan nilai bobot sampel (gram):", step=0.0001)
st.write("Nilai bobot sampel adalah", bobot_sampel)

hitung_cu = st.button("Hitung kadar cemaran Cu")

if hitung_cu:
    kadar_cemaran_cu = (c_terukur * v * FP) / (bobot_sampel * 0.001)
    st.write(f"Hasil perhitungan kadar cemaran Cu = {kadar_cemaran_cu} ppm ")