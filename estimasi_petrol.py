import pickle
import streamlit as st

model = pickle.load(open('estimasi_petrol.sav', 'rb'))

st.title('Estimasi Harga Bensin')

DailyOilConsumption = st.number_input('Input Minyak Harian')
YearlyGallonsPerCapita = st.number_input('Input Galon Tahunan')
PricePerGallon = st.number_input('Input Harga Galon')
PricePerLiter = st.number_input('Input Harga Perliter')


predict = ''

if st.button('Estimasi Harga Bensin'):
    predict = model.predict(
        [[DailyOilConsumption, YearlyGallonsPerCapita, PricePerGallon, PricePerLiter]]
    )
    st.write ('Estimasi_petrol : ', predict)
    