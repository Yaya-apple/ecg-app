import streamlit as st

st.set_page_config(page_title="ECG 설문형 알고리즘", page_icon="🫀")
st.title("🫀 단계별 ECG 리듬 알고리즘 (설문형)")

# 1. QRS 폭
if "qrs" not in st.session_state:
    qrs = st.radio("1️⃣ QRS 폭은?", ["정상", "넓음", "하나만 넓음", "얇은 흔들림", "염전형", "파형 없음"])
    st.session_state.qrs = qrs
    st.stop()

# 2. RR 간격
if "rr" not in st.session_state:
    if st.session_state.qrs == "얇은 흔들림" or st.session_state.qrs == "파형 없음":
        rr_options = ["파형 없음"]
    elif st.session_state.qrs == "넓음":
        rr_options = ["규칙", "이중나선"]
    else:
        rr_options = ["규칙", "불규칙", "규칙적이며 불규칙", "하나만 빠름"]
    rr = st.radio("2️⃣ RR 간격은?", rr_options)
    st.session_state.rr = rr
    st.stop()

# 3. 맥박
if "rate" not in st.session_state:
    if st.session_state.qrs in ["얇은 흔들림", "파형 없음"] or st.session_state.rr == "파형 없음":
        rate_options = ["파형 없음"]
    else:
        rate_options = ["서맥", "정상", "빈맥", "발작성빈맥(150 이상)"]
    rate = st.radio("3️⃣ 맥박은?", rate_options)
    st.session_state.rate = rate
    st.stop()

# 4. P파
if "p_wave" not in st.session_state:
    if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
        p_options = ["파형 없음"]
    else:
        p_options = ["있음", "없음", "T파에 가림", "모양 다름", "빨리 뛰는 곳만 없음"]
    p_wave = st.radio("4️⃣ P파는?", p_options)
    st.session_state.p_wave = p_wave
    st.stop()

# 5. PR 간격
if "pr" not in st.session_state:
    if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
        pr_options = ["파형 없음"]
    else:
        pr_options = ["정상", "5칸 이상", "점점 길어짐", "일정함", "불규칙"]
    pr = st.radio("5️⃣ PR 간격은?", pr_options)
    st.session_state.pr = pr
    st.stop()

# 6. P:QRS 비율
if "pqrs" not in st.session_state:
    if st.session_state.qrs in ["얇은 흔들림", "파형 없음"]:
        pqrs_options = ["파형 없음"]
    else:
        pqrs_options = ["1:1", "2:1~3:1", "무관", "하나 빠짐", "불규칙", "없음"]
    pqrs = st.radio("6️⃣ P:QRS 비율은?", pqrs_options)
    st.session_state.pqrs = pqrs
    st.stop()

# 결과 정리
st.subheader("🩺 입력 요약")
for label, key in [("QRS 폭", "qrs"), ("RR 간격", "rr"), ("맥박", "rate"), ("P파", "p_wave"), ("PR 간격", "pr"), ("P:QRS 비율", "pqrs")]:
    st.markdown(f"✅ **{label}**: {st.session_state[key]}")

if st.button("🔁 처음부터 다시"):
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.experimental_rerun()
