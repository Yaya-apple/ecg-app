import streamlit as st

st.set_page_config(page_title="ECG 설문형 알고리즘", page_icon="🫀")
st.title("🫀 단계별 ECG 리듬 알고리즘 (스마트 설문형)")

# 리셋 함수
def reset():
    for key in st.session_state.keys():
        del st.session_state[key]

# 1. QRS 폭
if "qrs" not in st.session_state:
    st.markdown("### 1️⃣ QRS 폭은? ❤️")
    if st.button("✅ 정상"):
        st.session_state.qrs = "정상"
    elif st.button("🚨 넓음"):
        st.session_state.qrs = "넓음"
    elif st.button("⚡ 하나만 넓음"):
        st.session_state.qrs = "하나만 넓음"
    elif st.button("🌊 얇은 흔들림"):
        st.session_state.qrs = "얇은 흔들림"
    elif st.button("🌀 염전형"):
        st.session_state.qrs = "염전형"
    elif st.button("⛔ 파형 없음"):
        st.session_state.qrs = "파형 없음"
    st.stop()

# 2. RR 간격
if "rr" not in st.session_state:
    qrs = st.session_state.qrs
    st.markdown("### 2️⃣ RR 간격은? 🪢")
    rr_options = []

    if qrs in ["얇은 흔들림", "파형 없음"]:
        rr_options = ["⛔ 파형 없음"]
    elif qrs == "넓음":
        rr_options = ["📏 규칙", "🌀 이중나선"]
    else:
        rr_options = ["📏 규칙", "📉 불규칙", "📈 규칙적이며 불규칙", "⏩ 하나만 빠름"]

    for option in rr_options:
        if st.button(option):
            st.session_state.rr = option.split(" ")[1]
            st.stop()

# 3. 맥박
if "rate" not in st.session_state:
    qrs, rr = st.session_state.qrs, st.session_state.rr
    st.markdown("### 3️⃣ 맥박은? 💓")
    if qrs in ["얇은 흔들림", "파형 없음"] or rr == "파형 없음":
        rate_options = ["⛔ 파형 없음"]
    else:
        rate_options = ["🐢 서맥", "🧘 정상", "🏃 빈맥", "🚀 발작성빈맥(150 이상)"]
    for option in rate_options:
        if st.button(option):
            st.session_state.rate = option.split(" ")[1]
            st.stop()

# 4. P파
if "p_wave" not in st.session_state:
    qrs = st.session_state.qrs
    st.markdown("### 4️⃣ P파는? 🅿️")
    if qrs in ["얇은 흔들림", "파형 없음"]:
        p_options = ["⛔ 파형 없음"]
    else:
        p_options = ["🟢 있음", "❌ 없음", "🪞 T파에 가림", "🎭 모양 다름", "⏩ 빨리 뛰는 곳만 없음"]
    for option in p_options:
        if st.button(option):
            st.session_state.p_wave = option.split(" ")[1]
            st.stop()

# 5. PR 간격
if "pr" not in st.session_state:
    qrs = st.session_state.qrs
    st.markdown("### 5️⃣ PR 간격은? ⏱️")
    if qrs in ["얇은 흔들림", "파형 없음"]:
        pr_options = ["⛔ 파형 없음"]
    else:
        pr_options = ["✅ 정상", "📏 5칸 이상", "📉 점점 길어짐", "📐 일정함", "📊 불규칙"]
    for option in pr_options:
        if st.button(option):
            st.session_state.pr = option.split(" ")[1]
            st.stop()

# 6. P:QRS 비율
if "pqrs" not in st.session_state:
    qrs = st.session_state.qrs
    st.markdown("### 6️⃣ P:QRS 비율은? 🔀")
    if qrs in ["얇은 흔들림", "파형 없음"]:
        pqrs_options = ["⛔ 파형 없음"]
    else:
        pqrs_options = ["1️⃣ 1:1", "2️⃣ 2:1~3:1", "❓ 무관", "➖ 하나 빠짐", "🌀 불규칙", "0️⃣ 없음"]
    for option in pqrs_options:
        if st.button(option):
            st.session_state.pqrs = option.split(" ")[1]
            st.stop()

# 결과
st.markdown("## 🧾 입력 요약")
for label, key in [
    ("QRS 폭", "qrs"), ("RR 간격", "rr"), ("맥박", "rate"),
    ("P파", "p_wave"), ("PR 간격", "pr"), ("P:QRS 비율", "pqrs")
]:
    if key in st.session_state:
        st.markdown(f"✅ **{label}**: {st.session_state[key]}")

# 리셋 버튼
if st.button("🔁 처음부터 다시"):
    reset()
    st.rerun()
