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

# MBTI + 혈액형 직업 추천
job_recommendations = {
    ("ISTJ", "A"): "세무사 📑",
    ("ISTJ", "B"): "프로젝트 매니저 📋",
    ("ISTJ", "O"): "군 장교 🎖️",
    ("ISTJ", "AB"): "기록 보존가 🗄️",

    ("ISFJ", "A"): "간호사 🏥",
    ("ISFJ", "B"): "사회복지사 🤲",
    ("ISFJ", "O"): "초등교사 🏫",
    ("ISFJ", "AB"): "아동 심리상담사 🧸",

    ("INFJ", "A"): "작가 ✍️",
    ("INFJ", "B"): "심리학자 🧠",
    ("INFJ", "O"): "컨설턴트 💼",
    ("INFJ", "AB"): "철학자 📚",

    ("INTJ", "A"): "데이터 과학자 📊",
    ("INTJ", "B"): "전략 컨설턴트 🗺️",
    ("INTJ", "O"): "정치 분석가 🏛️",
    ("INTJ", "AB"): "AI 연구원 🤖",

    ("ISTP", "A"): "자동차 정비사 🚗",
    ("ISTP", "B"): "드론 조종사 🚁",
    ("ISTP", "O"): "응급 구조원 🚑",
    ("ISTP", "AB"): "탐험가 🧭",

    ("ISFP", "A"): "플로리스트 💐",
    ("ISFP", "B"): "바리스타 ☕",
    ("ISFP", "O"): "사진작가 📸",
    ("ISFP", "AB"): "인테리어 디자이너 🏡",

    ("INFP", "A"): "시인 🖋️",
    ("INFP", "B"): "그림 작가 🎨",
    ("INFP", "O"): "소설가 📖",
    ("INFP", "AB"): "인권 운동가 ✊",

    ("INTP", "A"): "연구원 🔬",
    ("INTP", "B"): "발명가 🛠️",
    ("INTP", "O"): "게임 개발자 🎮",
    ("INTP", "AB"): "천문학자 🌌",

    ("ESTP", "A"): "영업 사원 📞",
    ("ESTP", "B"): "스포츠 선수 🏅",
    ("ESTP", "O"): "파일럿 ✈️",
    ("ESTP", "AB"): "모험가 🗺️",

    ("ESFP", "A"): "배우 🎭",
    ("ESFP", "B"): "이벤트 플래너 🎉",
    ("ESFP", "O"): "가수 🎤",
    ("ESFP", "AB"): "유튜버 📹",

    ("ENFP", "A"): "광고 기획자 📢",
    ("ENFP", "B"): "창업가 🚀",
    ("ENFP", "O"): "여행 작가 🌍",
    ("ENFP", "AB"): "다큐멘터리 감독 🎬",

    ("ENTP", "A"): "벤처 사업가 💼",
    ("ENTP", "B"): "방송 작가 📺",
    ("ENTP", "O"): "정치가 🏛️",
    ("ENTP", "AB"): "발명가 🧪",

    ("ESTJ", "A"): "경영 관리자 🏢",
    ("ESTJ", "B"): "군 장교 🎖️",
    ("ESTJ", "O"): "영업 이사 📊",
    ("ESTJ", "AB"): "품질 관리 전문가 🧾",

    ("ESFJ", "A"): "교사 🏫",
    ("ESFJ", "B"): "간호사 🩺",
    ("ESFJ", "O"): "인사 담당자 👥",
    ("ESFJ", "AB"): "이벤트 코디네이터 🎀",

    ("ENFJ", "A"): "강연가 🎤",
    ("ENFJ", "B"): "프로듀서 🎬",
    ("ENFJ", "O"): "외교관 🤝",
    ("ENFJ", "AB"): "비영리 단체 리더 🌍",

    ("ENTJ", "A"): "CEO 🏆",
    ("ENTJ", "B"): "투자 분석가 💹",
    ("ENTJ", "O"): "전략가 ♟️",
    ("ENTJ", "AB"): "국제 프로젝트 매니저 🌐",
}

# 제목
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

# 결과
st.markdown("---")
job = job_recommendations.get((mbti, blood), "직업 데이터 없음 🤷‍♂️")
st.subheader("✨ 추천 직업")
st.success(f"{mbti_emojis[mbti]} {mbti} + {blood_emojis[blood]} {blood}형 → **{job}**")

# 안내
st.info("🔎 재미로 보는 직업 추천입니다. 실제 성향과는 다를 수 있어요!")
