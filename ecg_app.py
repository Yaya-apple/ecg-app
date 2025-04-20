import streamlit as st

st.set_page_config(page_title="ECG 리듬 판독기", page_icon="💓")
st.title("💓 ECG 리듬 판독기 (종식님 맞춤 알고리즘)")

# 사용자 입력
qrs = st.radio("QRS 폭", ["정상", "넓음", "하나만 넓음", "얇은 흔들림", "염전형", "파형 없음"])
rr = st.radio("RR 간격", ["규칙", "불규칙", "규칙적이며 불규칙", "하나만 빠름", "이중나선", "파형 없음"])
rate = st.radio("맥박", ["서맥", "정상", "빈맥", "발작성빈맥(150 이상)", "파형 없음"])
p_wave = st.radio("P파", ["있음", "없음", "T파에 가림", "모양 다름", "빨리 뛰는 곳만 없음", "파형 없음"])
pr = st.radio("PR 간격", ["정상", "5칸 이상", "점점 길어짐", "일정함", "불규칙", "파형 없음"])
p_qrs = st.radio("P:QRS 비율", ["1:1", "2:1~3:1", "무관", "하나 빠짐", "불규칙", "없음", "파형 없음"])

# 알고리즘
def diagnose(qrs, rr, rate, p_wave, pr, p_qrs):
    if qrs == "정상" and rr == "규칙" and rate == "서맥" and p_wave == "있음" and pr == "정상" and p_qrs == "1:1":
        return "동서맥 (SB, Sinus Bradycardia)"
    if qrs == "정상" and rr == "규칙" and rate == "정상" and p_wave == "있음" and pr == "정상" and p_qrs == "1:1":
        return "정상동성리듬 (NSR, Normal Sinus Rhythm)"
    if qrs == "정상" and rr == "규칙" and rate == "빈맥" and p_wave == "있음" and pr == "정상" and p_qrs == "1:1":
        return "동성빈맥 (ST, Sinus Tachycardia)"
    if qrs == "정상" and rr == "규칙" and rate == "발작성빈맥(150 이상)" and p_wave == "T파에 가림" and pr == "정상" and p_qrs == "1:1":
        return "발작성심실상성빈맥 (PSVT, Paroxysmal SVT)"
    if qrs == "정상" and rr == "불규칙" and rate == "정상" and p_wave == "있음" and pr == "정상" and p_qrs == "1:1":
        return "동성부정맥 (SA, Sinus Arrhythmia)"
    if qrs == "정상" and rr == "불규칙" and rate == "서맥" and p_wave == "모양 다름" and pr == "5칸 이상" and p_qrs == "1:1":
        return "다소성심방서맥 (WAP, Wandering Atrial Pacemaker)"
    if qrs == "정상" and rr == "불규칙" and rate == "빈맥" and p_wave == "모양 다름" and pr == "정상":
        return "다소성빈맥 (MAT, Multifocal Atrial Tachycardia)"
    if qrs == "정상" and rr == "규칙적이며 불규칙" and rate == "정상" and p_wave == "있음" and pr == "정상" and p_qrs == "2:1~3:1":
        return "심방조동 (AFL, Atrial Flutter)"
    if qrs == "정상" and rr == "불규칙" and rate == "정상" and p_wave == "없음" and pr == "정상":
        return "심방세동 (AF, Atrial Fibrillation)"
    if qrs == "정상" and rr == "규칙" and rate == "정상" and p_wave == "있음" and pr == "5칸 이상" and p_qrs == "1:1":
        return "1도 방실차단 (1°AVB, First-degree AV Block)"
    if qrs == "정상" and rr == "불규칙" and rate == "정상" and p_wave == "있음" and pr == "점점 길어짐" and p_qrs == "하나 빠짐":
        return "2도 1형 방실차단 (Mobitz I)"
    if qrs == "정상" and rr == "규칙" and rate == "서맥" and p_wave == "있음" and pr == "정상" and p_qrs == "불규칙":
        return "2도 2형 방실차단 (Mobitz II)"
    if qrs == "규칙적" and rr == "규칙" and rate == "서맥" and p_wave == "있음" and pr == "불규칙" and p_qrs == "무관":
        return "3도 방실차단 (3°AVB, Complete AV Block)"
    if qrs == "정상" and rr == "하나만 빠름" and rate == "정상" and p_wave == "빨리 뛰는 곳만 없음" and pr == "정상":
        return "결정성 조기수축 (PAC, Premature Atrial Contraction)"
    if qrs == "넓음" and rr == "규칙" and rate == "정상" and p_wave == "정상" and pr == "정상":
        return "가속성심실고유리듬 (AIVR, Accelerated Idioventricular Rhythm)"
    if qrs == "정상" and rr == "규칙" and rate == "서맥" and p_wave == "정상" and pr == "정상":
        return "심실고유리듬 (IVR, Idioventricular Rhythm)"
    if qrs == "하나만 넓음" and rr == "하나만 빠름" and rate == "정상" and p_wave == "있음":
        return "심실조기수축 (PVC, Premature Ventricular Contraction)"
    if qrs == "넓음" and rr == "규칙" and rate == "발작성빈맥(150 이상)" and p_wave == "없음" and pr == "정상":
        return "단형심실빈맥 (VT, Ventricular Tachycardia)"
    if qrs == "염전형" and rr == "이중나선" and rate == "파형 없음":
        return "염전성심실빈맥 (TdP, Torsades de Pointes)"
    if qrs == "얇은 흔들림" and rr == "파형 없음":
        return "심실세동 (VF, Ventricular Fibrillation)"
    if qrs == "파형 없음" and rr == "아주 얇은 파" and rate == "아주 얇은 파":
        return "무수축 (Asystole)"
    if qrs == "정상" and rr == "규칙" and rate == "정상" and p_wave == "정상" and pr == "정상" and p_qrs == "1:1":
        return "정상동성리듬 (NSR, Normal Sinus Rhythm)"
    return "❓ 해당 조건에 맞는 리듬이 없습니다. 다시 확인해보세요."

# 결과
if st.button("🩺 결과 보기"):
    result = diagnose(qrs, rr, rate, p_wave, pr, p_qrs)
    st.subheader("🔍 판독 결과")
    st.success(result)

