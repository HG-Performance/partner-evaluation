
import streamlit as st
import pandas as pd
import plotly.express as px

# 登录界面
def login():
    st.title("潜力伴侣评估系统 - 登录")
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")
    if st.button("登录"):
        if username == "admin" and password == "123456":
            st.session_state['logged_in'] = True
        else:
            st.error("用户名或密码错误")

# 验证码界面（简单模拟）
def verification():
    st.title("安全验证")
    code = st.text_input("请输入验证码（提示：6666）")
    if code == "6666":
        st.session_state['verified'] = True
    else:
        st.warning("验证码错误或未输入")

# 评估主页面
def evaluate():
    st.title("潜力伴侣评估系统")
    st.write("通过以下指标评估伴侣潜力：")

    # 输入评分项
    st.subheader("基本维度打分（0-10）")
    looks = st.slider("外貌吸引力", 0, 10, 5)
    stability = st.slider("情绪稳定性", 0, 10, 5)
    ambition = st.slider("生活野心", 0, 10, 5)
    loyalty = st.slider("忠诚度", 0, 10, 5)
    compatibility = st.slider("三观匹配", 0, 10, 5)
    family_bg = st.slider("家庭背景匹配", 0, 10, 5)
    contribution = st.slider("关系中付出", 0, 10, 5)

    data = {
        "维度": ["外貌", "情绪稳定", "野心", "忠诚", "三观", "家庭背景", "付出"],
        "评分": [looks, stability, ambition, loyalty, compatibility, family_bg, contribution]
    }

    df = pd.DataFrame(data)
    avg_score = df["评分"].mean()

    st.subheader("分析图表")
    fig = px.bar(df, x="维度", y="评分", title="各维度得分雷达图")
    st.plotly_chart(fig)

    st.success(f"综合评分为：{avg_score:.2f} / 10")
    if avg_score > 7:
        st.balloons()
        st.info("恭喜，这位伴侣具备较高潜力！")
    elif avg_score > 5:
        st.warning("有潜力，但需持续观察与经营。")
    else:
        st.error("建议慎重考虑，可能存在长期风险。")

# 程序入口
if 'logged_in' not in st.session_state:
    login()
elif 'verified' not in st.session_state:
    verification()
else:
    evaluate()
