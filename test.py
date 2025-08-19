import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# KBO 팀 리스트
teams = ["LG 트윈스", "KT 위즈", "SSG 랜더스", "NC 다이노스",
         "두산 베어스", "롯데 자이언츠", "KIA 타이거즈",
         "삼성 라이온즈", "한화 이글스", "키움 히어로즈"]

st.title("⚾ KBO 팀 정보 조회")

# 팀 선택
team = st.selectbox("팀을 선택하세요:", teams)

# 네이버 스포츠 KBO 순위 페이지
url = "https://sports.news.naver.com/kbaseball/record/index"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")   # ✅ lxml 파서 권장

# 순위표 가져오기
table = soup.select_one("table")  
df = pd.read_html(str(table))[0]

# 선택한 팀 정보
team_info = df[df["팀명"] == team]

if not team_info.empty:
    st.subheader(f"{team} 정보")
    승률 = team_info["승률"].values[0]
    st.write(f"📊 승률: {승률}")
else:
    st.write("팀 정보를 불러올 수 없습니다. 😢")
