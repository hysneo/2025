import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="KBO 팀 정보 조회", page_icon="⚾", layout="wide")
st.title("⚾ KBO 팀 실시간 정보 조회")

# -------------------------------------
# 1. 실시간 KBO 순위 데이터 가져오기
# -------------------------------------
@st.cache_data
def get_kbo_standings():
    url = "https://www.statiz.co.kr/standings.php"
    response = requests.get(url)
    response.raise_for_status()
    df_list = pd.read_html(response.text)
    standings = df_list[0]
    standings = standings[['팀', '경기', '승', '패', '무', '승률', '게임차']]
    return standings

# -------------------------------------
# 2. 실시간 KBO 경기 일정 및 결과 데이터
# -------------------------------------
@st.cache_data
def get_kbo_schedule():
    url = "https://www.statiz.co.kr/schedule.php?opt=1&sopt=0"
    response = requests.get(url)
    response.raise_for_status()
    df_list = pd.read_html(response.text)
    schedules = df_list[0]
    schedules = schedules[['날짜', '구장', '홈', '원정', '스코어', '비고']]
    return schedules

# 데이터 불러오기
try:
    standings = get_kbo_standings()
    schedules = get_kbo_schedule()
except Exception as e:
    st.error("⚠️ 데이터를 불러오는데 문제가 발생했습니다. 다시 시도해주세요.")
    st.stop()

# -------------------------------------
# 3. Streamlit 인터페이스 구성
# -------------------------------------
st.subheader("📌 팀 선택")
teams = standings["팀"].tolist()
team = st.selectbox("팀을 선택하세요:", teams)

# 팀 순위 정보 표시
st.subheader(f"🏆 {team} 순위 정보")
team_info = standings[standings["팀"] == team]
st.dataframe(team_info)

# 최근 5경기 표시
st.subheader(f"📅 {team} 최근 5경기 결과")
recent_games = schedules[(schedules["홈"] == team) | (schedules["원정"] == team)].head(5)
st.dataframe(recent_games)

st.caption("데이터 출처: Statiz (https://www.statiz.co.kr)")
