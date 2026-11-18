import streamlit as st

st.set_page_config(
    page_title="P P - AI Employee",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 P P - AI Employee")
st.caption("Your Personal AI Employee")

st.success("P P is ready!")

st.subheader("မင်္ဂလာပါ။ ကျွန်တော် P P ပါ။")
st.write(
    "မင်းရဲ့ ကိုယ်ပိုင် AI Employee အဖြစ် "
    "နေ့စဉ်အလုပ်တွေကို ကူညီပေးဖို့ အသင့်ရှိနေပါတယ်။"
)

st.subheader("Departments")

departments = [
    "Personal Assistant",
    "Excel Specialist",
    "Reporting Officer",
    "Data Analyst",
    "Office Admin",
    "Communication",
    "Research Assistant",
    "Project Coordinator",
]

for department in departments:
    st.write(f"📌 {department}")
