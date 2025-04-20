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
        if st.button("✅ 정상", key="qrs_normal"):
            st.session_state.qrs = "정상"
            st.stop()
        if st.button("⚡ 하나만 넓음", key="qrs_one_wide"):
            st.session_state.qrs = "하나만 넓음"
            st.stop()
        if st.button("🌀 염전형", key="qrs_torsade"):
            st.session_state.qrs = "염전형"
            st.stop()
    with col2:
        if st.button("🚨 넓음", key="qrs_wide"):
            st.session_state.qrs = "넓음"
            st.stop()
        if st.button("🌊 얇은 흔들림", key="qrs_fine"):
            st.session_state.qrs = "얇은 흔들림"
            st.stop()
        if st.button("⛔ 파형 없음", key="qrs_none"):
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

# 진단 결과 출력 및 리셋 버튼
def diagnose(qrs, rr, rate, p_wave, pr, pqrs):
    if qrs == "정상" and rr == "규칙" and rate == "서맥" and p_wave == "있음" and pr == "정상" and pqrs == "1:1":
        return "동서맥 (SB, Sinus Bradycardia)"
    elif qrs == "정상" and rr == "규칙" and rate == "정상" and p_wave == "있음" and pr == "정상" and pqrs == "1:1":
        return "정상동성리듬 (NSR, Normal Sinus Rhythm)"
    elif qrs == "정상" and rr == "규칙" and rate == "빈맥" and p_wave == "있음":
        return "동성빈맥 (ST, Sinus Tachycardia)"
    elif qrs == "정상" and rr == "규칙" and rate == "발작성빈맥(150 이상)" and p_wave == "T파에 가림":
        return "발작성심실상성빈맥 (PSVT, Paroxysmal SVT)"
    elif qrs == "정상" and rr == "불규칙" and rate == "정상" and p_wave == "있음" and pr == "정상" and pqrs == "1:1":
        return "동성부정맥 (SA, Sinus Arrhythmia)"
    elif qrs == "정상" and rr == "불규칙" and rate == "서맥" and p_wave == "모양 다름" and pr == "5칸 이상" and pqrs == "1:1":
        return "다소성심방서맥 (WAP, Wandering Atrial Pacemaker)"
    elif qrs == "정상" and rr == "불규칙" and rate == "빈맥" and p_wave == "모양 다름":
        return "다소성심방빈맥 (MAT, Multifocal Atrial Tachycardia)"
    elif qrs == "정상" and rr == "규칙적이며 불규칙" and p_wave == "있음" and pqrs == "2:1~3:1":
        return "심방조동 (AFL, Atrial Flutter)"
    elif qrs == "정상" and rr == "불규칙" and p_wave == "없음":
        return "심방세동 (AF, Atrial Fibrillation)"
    elif qrs == "정상" and pr == "5칸 이상" and pqrs == "1:1":
        return "1도 방실차단 (1°AVB, First-degree AV Block)"
    elif qrs == "정상" and pr == "점점 길어짐" and pqrs == "하나 빠짐":
        return "2도 1형 방실차단 (Mobitz I)"
    elif qrs == "정상" and pr == "정상" and pqrs == "2:1~3:1":
        return "2도 2형 방실차단 (Mobitz II)"
    elif qrs == "정상" and pr == "불규칙" and pqrs == "무관":
        return "3도 방실차단 (3°AVB, Complete AV Block)"
    elif qrs == "하나만 넓음" and rr == "하나만 빠름" and p_wave == "있음":
        return "심실조기수축 (PVC, Premature Ventricular Contraction)"
    elif qrs == "정상" and rr == "하나만 빠름" and p_wave == "빨리 뛰는 곳만 없음":
        return "결정성 조기수축 (PAC, Premature Atrial Contraction)"
    elif qrs == "넓음" and rr == "규칙" and (rate == "빈맥" or rate == "발작성빈맥(150 이상)") and p_wave == "없음":
        return "단형심실빈맥 (VT, Ventricular Tachycardia)"
    elif qrs == "넓음" and rr == "규칙" and rate == "정상":
        return "가속성심실고유리듬 (AIVR, Accelerated Idioventricular Rhythm)"
    elif qrs == "넓음" and rr == "규칙" and rate == "서맥":
        return "심실고유리듬 (IVR, Idioventricular Rhythm)"
    elif qrs == "염전형" or rr == "이중나선":
        return "염전성심실빈맥 (TdP, Torsades de Pointes)"
    elif qrs == "얇은 흔들림" and rr == "파형 없음":
        return "심실세동 (VF, Ventricular Fibrillation)"
    elif qrs == "파형 없음":
        return "무수축 (Asystole)"
    else:
        return "❓ 정확한 리듬을 판독할 수 없습니다."

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

if st.button("🔁 처음부터 다시", key="reset_button"):
    reset()
    st.rerun()

# 진단 결과 출력 및 리셋 버튼
def diagnose(qrs, rr, rate, p_wave, pr, pqrs):
    rules = {
        ("정상", "규칙", "서맥", "있음", "정상", "1:1"): "동서맥 (SB, Sinus Bradycardia)",
        ("정상", "규칙", "정상", "있음", "정상", "1:1"): "정상동성리듬 (NSR, Normal Sinus Rhythm)",
        ("정상", "규칙", "빈맥", "있음", None, None): "동성빈맥 (ST, Sinus Tachycardia)",
        ("정상", "규칙", "발작성빈맥(150 이상)", "T파에 가림", None, None): "발작성심실상성빈맥 (PSVT)",
        ("정상", "불규칙", "정상", "있음", "정상", "1:1"): "동성부정맥 (SA, Sinus Arrhythmia)",
        ("정상", "불규칙", "서맥", "모양 다름", "5칸 이상", "1:1"): "다소성심방서맥 (WAP)",
        ("정상", "불규칙", "빈맥", "모양 다름", None, None): "다소성심방빈맥 (MAT)",
        ("정상", "규칙적이며 불규칙", None, "있음", None, "2:1~3:1"): "심방조동 (AFL)",
        ("정상", "불규칙", None, "없음", None, None): "심방세동 (AF)",
        ("정상", None, None, None, "5칸 이상", "1:1"): "1도 방실차단 (1°AVB)",
        ("정상", None, None, None, "점점 길어짐", "하나 빠짐"): "2도 1형 방실차단 (Mobitz I)",
        ("정상", None, None, None, "정상", "2:1~3:1"): "2도 2형 방실차단 (Mobitz II)",
        ("정상", None, None, None, "불규칙", "무관"): "3도 방실차단 (3°AVB)",
        ("하나만 넓음", "하나만 빠름", None, "있음", None, None): "심실조기수축 (PVC)",
        ("정상", "하나만 빠름", None, "빨리 뛰는 곳만 없음", None, None): "결정성 조기수축 (PAC)",
        ("넓음", "규칙", "빈맥", "없음", None, None): "단형심실빈맥 (VT)",
        ("넓음", "규칙", "발작성빈맥(150 이상)", "없음", None, None): "단형심실빈맥 (VT)",
        ("넓음", "규칙", "정상", None, None, None): "가속성심실고유리듬 (AIVR)",
        ("넓음", "규칙", "서맥", None, None, None): "심실고유리듬 (IVR)",
        ("염전형", "이중나선", None, None, None, None): "염전성심실빈맥 (TdP)",
        ("얇은 흔들림", "파형 없음", None, None, None, None): "심실세동 (VF)",
        ("파형 없음", None, None, None, None, None): "무수축 (Asystole)"
    }

    # 규칙 탐색
    for key, diagnosis in rules.items():
        match = True
        for i, val in enumerate(key):
            if val is not None:
                if (i == 0 and qrs != val) or                    (i == 1 and rr != val) or                    (i == 2 and rate != val) or                    (i == 3 and p_wave != val) or                    (i == 4 and pr != val) or                    (i == 5 and pqrs != val):
                    match = False
                    break
        if match:
            return diagnosis

    return "🩺 새로운 형태의 리듬입니다. 추가 분석이 필요합니다."

# 결과 출력
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

if st.button("🔁 처음부터 다시", key="reset_button"):
    reset()
    st.rerun()