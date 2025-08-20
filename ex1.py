import streamlit as st
import random

st.set_page_config(page_title="혈액형별 직업 추천", page_icon="💼")
st.title("💼 혈액형별 직업 추천 앱")

# 혈액형별 추천 직업 리스트
jobs = {
    "A": ["회계사", "연구원", "공무원", "교사"],
    "B": ["디자이너", "프리랜서", "마케터", "작가"],
    "O": ["경영자", "영업사원", "운동선수", "파일럿"],
    "AB": ["의사", "엔지니어", "과학자", "예술가"]
}

# 혈액형 선택
blood_type = st.selectbox("혈액형을 선택하세요:", ["A", "B", "O", "AB"])

# 추천 버튼
if st.button("직업 추천받기"):
    recommended = random.choice(jobs[blood_type])
    st.subheader(f"💡 {blood_type}형에게 추천하는 직업:")
    st.write(recommended)
