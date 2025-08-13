import streamlit as st

# MBTI와 이모지 매핑
mbti_emojis = {
    "ISTJ": "📋", "ISFJ": "🛡️", "INFJ": "🌌", "INTJ": "🧠",
    "ISTP": "🛠️", "ISFP": "🎨", "INFP": "📖", "INTP": "🔬",
    "ESTP": "⚡", "ESFP": "🎉", "ENFP": "🔥", "ENTP": "💡",
    "ESTJ": "📊", "ESFJ": "🤝", "ENFJ": "🌟", "ENTJ": "🏆"
}

# 혈액형과 이모지 매핑
blood_emojis = {
    "A": "🍎",
    "B": "🍌",
    "O": "🍊",
    "AB": "🥝"
}

# MBTI+혈액형 → 직업 추천 데이터
job_recommendations = {
    ("INFJ", "A"): "작가 ✍️",
    ("ENFP", "O"): "광고 기획자 📢",
    ("ISTJ", "B"): "회계사 📊",
    ("ENTP", "AB"): "스타트업 창업가 🚀",
}

# 웹 앱 제목
st.title("🔮 혈액형 + MBTI 직업 추천기")

# 선택 UI
col1, col2 = st.columns(2)

with col1:
    mbti = st.selectbox(
        "MBTI를 선택하세요:",
        options=list(mbti_emojis.keys()),
        format_func=lambda x: f"{mbti_emojis[x]} {x}"
    )

with col2:
    blood = st.selectbox(
        "혈액형을 선택하세요:",
        options=list(blood_emojis.keys()),
        format_func=lambda x: f"{blood_emojis[x]} {x}형"
    )

# 추천 결과
st.markdown("---")
if (mbti, blood) in job_recommendations:
    job = job_recommendations[(mbti, blood)]
else:
    job = "연구원 🔍"  # 기본 추천

st.subheader("✨ 추천 직업")
st.success(f"{mbti_emojis[mbti]} {mbti} + {blood_emojis[blood]} {blood}형 → **{job}**")

# 부가 정보
st.info("🔎 재미로 보는 직업 추천입니다. 실제 성향과는 다를 수 있어요!")
