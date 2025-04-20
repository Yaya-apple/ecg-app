import streamlit as st

st.set_page_config(page_title="ECG 설문형 알고리즘", page_icon="🫀")
st.title("🫀 단계별 ECG 리듬 알고리즘 (스마트 설문형)")

def reset():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# QRS
if "qrs" not in st.session_state:
    st.markdown("### 1️⃣ QRS 폭은? ❤️")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ 정상"):
            st.session_state.qrs = "정상"
            st.stop()
        if st.button("⚡ 하나만 넓음"):
            st.session_state.qrs = "하나만 넓음"
            st.stop()
        if st.button("🌀 염전형"):
            st.session_state.qrs = "염전형"
            st.stop()
    with col2:
        if st.button("🚨 넓음"):
            st.session_state.qrs = "넓음"
            st.stop()
        if st.button("🌊 얇은 흔들림"):
            st.session_state.qrs = "얇은 흔들림"
            st.stop()
        if st.button("⛔ 파형 없음"):
            st.session_state.qrs = "파형 없음"
            st.stop()

# RR
if "qrs" in st.session_state and "rr" not in st.session_state:
    st.markdown("### 2️⃣ RR 간격은? 🪢")
    if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
        rr_options = ["⛔ 파형 없음"]
    elif st.session_state.qrs == "넓음":
        rr_options = ["📏 규칙", "🌀 이중나선"]
    else:
        rr_options = ["📏 규칙", "📉 불규칙", "📈 규칙적이며 불규칙", "⏩ 하나만 빠름"]
    col1, col2 = st.columns(2)
    for i, option in enumerate(rr_options):
        label = option.split(" ")[1]
        if i % 2 == 0:
            with col1:
                if st.button(option):
                    st.session_state.rr = label
                    st.stop()
        else:
            with col2:
                if st.button(option):
                    st.session_state.rr = label
                    st.stop()

# Rate
if all(k in st.session_state for k in ["qrs", "rr"]) and "rate" not in st.session_state:
    st.markdown("### 3️⃣ 맥박은? 💓")
    if st.session_state.qrs in ["얇은 흔들림", "파형 없음"] or st.session_state.rr == "파형 없음":
        rate_options = ["⛔ 파형 없음"]
    else:
        rate_options = ["🐢 서맥", "🧘 정상", "🏃 빈맥", "🚀 발작성빈맥(150 이상)"]
    col1, col2 = st.columns(2)
    for i, option in enumerate(rate_options):
        label = option.split(" ")[1]
        if i % 2 == 0:
            with col1:
                if st.button(option):
                    st.session_state.rate = label
                    st.stop()
        else:
            with col2:
                if st.button(option):
                    st.session_state.rate = label
                    st.stop()

# P, PR, P:QRS
if all(k in st.session_state for k in ["qrs", "rr", "rate"]):

    if "p_wave" not in st.session_state:
        st.markdown("### 4️⃣ P파는? 🅿️")
        if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
            p_options = ["⛔ 파형 없음"]
        else:
            p_options = ["🟢 있음", "❌ 없음", "🪞 T파에 가림", "🎭 모양 다름", "⏩ 빨리 뛰는 곳만 없음"]
        col1, col2 = st.columns(2)
        for i, option in enumerate(p_options):
            label = option.split(" ")[1]
            if i % 2 == 0:
                with col1:
                    if st.button(option):
                        st.session_state.p_wave = label
                        st.stop()
            else:
                with col2:
                    if st.button(option):
                        st.session_state.p_wave = label
                        st.stop()

    if "p_wave" in st.session_state and "pr" not in st.session_state:
        st.markdown("### 5️⃣ PR 간격은? ⏱️")
        if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
            pr_options = ["⛔ 파형 없음"]
        else:
            pr_options = ["✅ 정상", "📏 5칸 이상", "📉 점점 길어짐", "📐 일정함", "📊 불규칙"]
        col1, col2 = st.columns(2)
        for i, option in enumerate(pr_options):
            label = option.split(" ")[1]
            if i % 2 == 0:
                with col1:
                    if st.button(option):
                        st.session_state.pr = label
                        st.stop()
            else:
                with col2:
                    if st.button(option):
                        st.session_state.pr = label
                        st.stop()

    if "pr" in st.session_state and "pqrs" not in st.session_state:
        st.markdown("### 6️⃣ P:QRS 비율은? 🔀")
        if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
            pqrs_options = ["⛔ 파형 없음"]
        else:
            pqrs_options = ["1️⃣ 1:1", "2️⃣ 2:1~3:1", "❓ 무관", "➖ 하나 빠짐", "🌀 불규칙", "0️⃣ 없음"]
        col1, col2 = st.columns(2)
        for i, option in enumerate(pqrs_options):
            label = option.split(" ")[1]
            if i % 2 == 0:
                with col1:
                    if st.button(option):
                        st.session_state.pqrs = label
                        st.stop()
            else:
                with col2:
                    if st.button(option):
                        st.session_state.pqrs = label
                        st.stop()