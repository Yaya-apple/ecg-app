import streamlit as st

st.set_page_config(page_title="ECG 리듬 판독기", page_icon="🫀")
st.title("🫀 ECG 리듬 판독기")
st.write("아래 질문에 순서대로 답해주세요. 결과는 마지막에 나옵니다.")

# 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = {}

def reset():
    st.session_state.step = 0
    st.session_state.answers = {}

# 기본 질문
questions = [
    ("QRS 폭이 좁습니까? (≤ 0.12초)", "qrs_narrow"),
    ("RR 간격이 규칙적입니까?", "rr_regular"),
]

# 조건에 따라 추가 질문
def extra_questions():
    qrs = st.session_state.answers.get("qrs_narrow")
    rr = st.session_state.answers.get("rr_regular")

    if qrs == "예":
        if rr == "예":
            return [("톱니 모양이 보입니까?", "sawtooth"),
                    ("P파가 보입니까?", "p_wave")]
        else:
            return [("톱니 모양이 보입니까?", "sawtooth2"),
                    ("P파가 없고 기저선이 불규칙합니까?", "no_p_wave")]
    else:
        if rr == "예":
            return []
        else:
            return [("QRS가 커졌다 작아졌다 꼬여 있습니까? (Torsades 양상)", "torsades")]

# 질문 출력
def ask_question(text, key):
    st.subheader(text)
    col1, col2 = st.columns(2)
    if col1.button("✅ 예", key=f"{key}_yes"):
        st.session_state.answers[key] = "예"
        st.session_state.step += 1
        st.rerun()
    if col2.button("❌ 아니오", key=f"{key}_no"):
        st.session_state.answers[key] = "아니오"
        st.session_state.step += 1
        st.rerun()

# 결과 출력
def show_result():
    a = st.session_state.answers
    summary = []
    emoji = "❓"
    diagnosis = "결과 없음"

    if a.get("qrs_narrow") == "예":
        summary.append("QRS 폭이 좁고")
    else:
        summary.append("QRS 폭이 넓고")

    if a.get("rr_regular") == "예":
        summary.append("RR 간격이 규칙적이며")
    else:
        summary.append("RR 간격이 불규칙하며")

    if a.get("qrs_narrow") == "예":
        if a.get("rr_regular") == "예":
            if a.get("sawtooth") == "예":
                diagnosis = "심방조동 (Atrial Flutter)"
                emoji = "🪚"
            elif a.get("p_wave") == "예":
                diagnosis = "심방빈맥 (Atrial Tachycardia)"
                emoji = "💓"
            else:
                diagnosis = "PSVT 또는 AVNRT"
                emoji = "⚡"
        else:
            if a.get("sawtooth2") == "예":
                diagnosis = "심방조동 (전도율 가변)"
                emoji = "🪚"
            elif a.get("no_p_wave") == "예":
                diagnosis = "심방세동 (Atrial Fibrillation)"
                emoji = "🌀"
            else:
                diagnosis = "불규칙 상심실성 리듬"
                emoji = "🤔"
    else:
        if a.get("rr_regular") == "예":
            diagnosis = "심실빈맥 (Ventricular Tachycardia)"
            emoji = "🚨"
        else:
            if a.get("torsades") == "예":
                diagnosis = "Torsades de Pointes"
                emoji = "🌀⚡"
            else:
                diagnosis = "심실세동 또는 비정형 VT"
                emoji = "💀"

    st.success(f"🧾 조건 요약: {' '.join(summary)} → {diagnosis} {emoji}")
    if st.button("🔁 다시 시작하기"):
        reset()
        st.rerun()

# 실행 흐름 제어
if st.session_state.step < len(questions):
    qtext, key = questions[st.session_state.step]
    ask_question(qtext, key)
elif st.session_state.step < len(questions) + len(extra_questions()):
    qtext, key = extra_questions()[st.session_state.step - len(questions)]
    ask_question(qtext, key)
else:
    show_result()
