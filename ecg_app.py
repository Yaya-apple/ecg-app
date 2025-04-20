# 🧩 1단계: QRS 선택 블록 (ecg_survey_app.py 상단에 넣기)
import streamlit as st

st.set_page_config(page_title="ECG 설문형 알고리즘", page_icon="🫀")
st.title("🫀 단계별 ECG 리듬 알고리즘 (스마트 설문형)")

# 리셋 함수
def reset():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# QRS 폭 선택 - 첫 질문
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
# ✅ [1단계 코드]
if "qrs" not in st.session_state:
    ...  # QRS 버튼 선택

# ✅ [2단계 코드]
if "rr" not in st.session_state:
    ...  # RR 버튼 선택

# ✅ 3단계
if "rate" not in st.session_state:
    ...  # 맥박 선택 블록
# 🧩 4단계: P파, PR 간격, P:QRS 비율 선택 블록 (맥박 선택 후 붙이기)

# P파 선택
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

# PR 간격 선택
if "pr" not in st.session_state and "p_wave" in st.session_state:
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

# P:QRS 비율 선택
if "pqrs" not in st.session_state and "pr" in st.session_state:
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
# 🧩 5단계: 진단 결과 출력 + 다시 시작 버튼

# 진단 알고리즘 함수는 이미 위에 붙여주셨으면 다시 넣지 않아도 돼요
# 없으면 아래 전체 포함해서 붙이세요

def diagnose(qrs, rr, rate, p_wave, pr, pqrs):
    # [진단 로직은 그대로 위에서 줬던 것과 동일]
    # ...
    return "❓ 정확한 리듬을 판독할 수 없습니다."

# 모든 값이 입력되었을 때 결과 출력
if all(k in st.session_state for k in ["qrs", "rr", "rate", "p_wave", "pr", "pqrs"]):
    st.markdown("## 🧾 입력 요약")
    for label, key in [
        ("QRS 폭", "qrs"), ("RR 간격", "rr"), ("맥박", "rate"),
        ("P파", "p_wave"), ("PR 간격", "pr"), ("P:QRS 비율", "pqrs")
    ]:
        st.markdown(f"✅ **{label}**: {st.session_state[key]}")

    result = diagnose(
        st.session_state.qrs,
        st.session_state.rr,
        st.session_state.rate,
        st.session_state.p_wave,
        st.session_state.pr,
        st.session_state.pqrs
    )
    st.markdown("## 🩺 판독 결과")
    st.success(result)

# 리셋 버튼
if st.button("🔁 처음부터 다시"):
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.rerun()

