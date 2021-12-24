import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import joblib

def run_ml_app():
    classifier = joblib.load('data/best_model.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    df = pd.read_csv('data/penguins.csv', encoding='ISO-8859-1', index_col=0)
    st.title('펭귄 성별 예측하기')

    # species	island	culmen_length_mm	culmen_depth_mm	
    # flipper_length_mm	body_mass_g	sex


    # species = st.text_input('펭귄 종 입력하기 (Chinstrap, Adelie, 또는 Gentoo)')
    # island = st.text_input('남극 섬 입력하기 (Dream, Torgersen, 또는 Biscoe)')
    culmen_length = st.number_input('부리 길이 입력하기( 단위 mm )',min_value=32, max_value=60)
    culmen_depth = st.number_input('부리 깊이 입력하기( 단위 mm )',min_value=13, max_value=22)
    flipper_length = st.number_input('지느러미 길이( 단위 mm )',min_value=170, max_value=240)
    body_mass = st.number_input('체질량 입력하기 ( 단위 g )', min_value=2700, max_value=6300)

    if st.button('성별 예측하기'):
        new_data = np.array([culmen_length, culmen_depth, flipper_length, body_mass])
        new_data = new_data.reshape(1, 4)

        new_data = scaler_X.transform(new_data)
        y_pred = classifier.predict(new_data)

        print(y_pred[0])
        if y_pred[0] == 'MALE' :
            st.write('예측 결과는, 수컷 입니다.')
        else :
            st.write('예측 결과는, 암컷입니다.')