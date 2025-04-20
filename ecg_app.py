import streamlit as st

st.set_page_config(page_title="ECG 설문형 알고리즘", page_icon="🫀")
st.title("🫀 단계별 ECG 리듬 알고리즘 (스마트 설문형)")

# 리셋 함수
def reset():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# 진단 알고리즘
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

# 결과 표시
if all(k in st.session_state for k in ["qrs", "rr", "rate", "p_wave", "pr", "pqrs"]):
    st.markdown("## 🧾 입력 요약")
    for label, key in [
        ("QRS 폭", "qrs"), ("RR 간격", "rr"), ("맥박", "rate"),
        ("P파", "p_wave"), ("PR 간격", "pr"), ("P:QRS 비율", "pqrs")
    ]:
        st.markdown(f"✅ **{label}**: {st.session_state[key]}")

    # 진단 결과
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
    reset()
    st.rerun()
