import pickle
import streamlit as st

# membaca model
water_model = pickle.load(open('water_model.sav', 'rb'))

#judul web
st.title('Prediksi Kualitas Air Yang Aman Dikonsumsi')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    aluminium = st.number_input ('Nilai Kadar Alumunium Dalam Air')
    ammonia = st.number_input ('Nilai Kadar Amonia Dalam Air')
    arsenic = st.number_input ('Nilai Kadar Arsenik Dalam Air')
    barium = st.number_input ('Nilai Kadar Barium Dalam Air')
    cadmium = st.number_input ('Nilai Kadar kadmium Dalam Air')
    

with col2 :
    chloramine = st.number_input ('Nilai Kadar kloramin Dalam Air')
    chromium = st.number_input ('Nilai Kadar kromium Dalam Air')
    copper = st.number_input ('Nilai Kadar Tembaga Dalam Air')
    flouride = st.number_input ('Nilai Kadar Flouride Dalam Air')
    bacteria = st.number_input ('Nilai Kadar Bakteria Dalam Air')

# code untuk prediksi
water_quality = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi water'):
    water_predict = water_model.predict([[aluminium, ammonia, arsenic, barium, cadmium, chloramine,
                                        chromium, copper, flouride, bacteria]])

    if water_predict == 0:
        water_quality = 'Air Tidak Aman Untuk Dikonsumsi'
    else:
        water_quality = 'Air Aman Untuk Dikonsumsi'
st.success(water_quality)
