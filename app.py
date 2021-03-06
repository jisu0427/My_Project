import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from PIL import Image
import random

from eda_app import run_eda_app
from information_app import run_information_app
from main import run_main_app
from ml_app import run_ml_app


#  파비콘 넣기
emojis = "🐧"
st.set_page_config(page_title='Palmer Penguins ML',page_icon=emojis, layout='wide',initial_sidebar_state='collapsed')





def main():
    menu = ['펭귄🐧','펭귄🐧 데이터 분석하기','펭귄🐧의 성별 예측하기', '자료 출처' ]
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == '펭귄🐧':
        run_main_app()
    elif choice == '펭귄🐧 데이터 분석하기':
        run_eda_app()

    elif choice == '펭귄🐧의 성별 예측하기':
        run_ml_app()
    elif choice == '자료 출처':
        run_information_app()


if __name__ == '__main__':
    main()