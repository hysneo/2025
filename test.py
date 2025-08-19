import streamlit as st
import pandas as pd

teams = ["LG", "KT", "SSG", "NC", "두산", "롯데", "KIA", "삼성", "한화", "키움"]
st.title("⚾ KBO 팀 정보 조회 (Statiz 기반)")

team = st.selectbox("팀을 선택하세요:", teams)

# ---------------------------
# 1) 순위표 가져오기
# ---------------------------
standings_url = "https://www.statiz.co.kr/standings.php"
standings = pd.read_html(standings_url)[0]

team_info = standings[standings["팀"] == team]

if not team_info.empty:
    st.subheader(f"{team} 순위 정보")
    st.write(f"📊 승률: {team_info['승률'].values[0]}")
    st.write(f"📈 순위: {team_info['순위'].values[0]}")
    st.write(f"⚔️ 경기수: {team_info['경기'].values[0]}, "
             f"승: {team_info['승'].values[0]}, "
             f"패: {team_info['패'].values[0]}, "
             f"무: {team_info['무'].values[0]}")
else:
    st.warning("순위 정보를 불러올 수 없습니다 😢")

# ---------------------------
# 2) 최근 경기 결과 가져오기
# ---------------------------
schedule_url = "https://www.statiz.co.kr/schedule.php?opt=1&sopt=0"
schedules = pd.read_html(schedule_url)[0]

# 선택한 팀 관련 경기만 추출
team_games = schedules[schedules["팀"].str.contains(team, na=False)]

# 날짜 컬럼이 있는지 확인
if "날짜" in team_games.columns:
    # datetime 변환, 변환 실패 시 그대로 두기
    try:
        team_games["날짜"] = pd.to_datetime(team_games["날짜"], errors="coerce")
        recent_games = team_games.sort_values("날짜", ascending=False).head(5)
    except:
        recent_games = team_games.head(5)
else:
    recent_games = team_games.head(5)

st.subheader(f"📝 {team} 최근 경기 결과")
if not recent_games.empty:
    for _, game in recent_games.iterrows():
        with st.container():
            opponent = game.get("상대", "")
            score = f"{game.get('점수','')} vs {game.get('실점','')}"
            result = game.get("결과", "")

            # 결과에 따라 아이콘 표시
            if result == "승":
                result_icon = "✅"
            elif result == "패":
                result_icon = "❌"
            else:
                result_icon = "➖"

            st.markdown(
                f"""
                <div style='padding:10px; border-radius:12px; 
                            background-color:#f9f9f9; margin-bottom:10px;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>
                    <b>{game.get('날짜','')}</b> | ⚾ <b>{team}</b> vs <b>{opponent}</b>  
                    점수: <b>{score}</b>  
                    결과: {result_icon} {result}
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.warning("최근 경기 결과를 불러올 수 없습니다 😢")
