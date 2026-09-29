import streamlit as st
from datetime import datetime

# ---------------- Page config ----------------
st.set_page_config(
    page_title="My First Streamlit Cloud App",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------------- Light styling ----------------
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    padding: 24px;
    border-radius: 14px;
    color: white;
    text-align: center;
    margin-bottom: 24px;
}
.stButton>button {
    width: 100%;
    border-radius: 8px;
    height: 3em;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session state ----------------
if "submissions" not in st.session_state:
    st.session_state.submissions = []

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("⚙️ Settings")
    mood = st.selectbox("How are you feeling today?", ["😀 Great", "🙂 Good", "😐 Okay", "😴 Tired"])
    show_history = st.checkbox("Show submission history", value=True)
    st.markdown("---")
    st.caption(f"Session started: {datetime.now().strftime('%I:%M %p')}")

# ---------------- Header ----------------
st.markdown("""
<div class="main-header">
    <h1>👋 My First Streamlit Cloud App</h1>
    <p>A simple, friendly greeting app — built and deployed with Streamlit</p>
</div>
""", unsafe_allow_html=True)

st.write("Hello Students! 🎓 Fill in your details below and hit submit.")

# ---------------- Input form ----------------
with st.form("greeting_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter your name", placeholder="e.g. Ruchitha")
    with col2:
        role = st.selectbox("You are a...", ["Student", "Instructor", "Visitor"])

    message = st.text_area("Leave a short message (optional)", placeholder="Excited to learn Streamlit!", height=80)

    submitted = st.form_submit_button("🚀 Submit")

# ---------------- Handle submission ----------------
if submitted:
    if not name.strip():
        st.error("⚠️ Please enter your name before submitting.")
    else:
        st.success(f"Welcome, {name}! Great to have you here as a {role.lower()}. {mood}")
        st.balloons()
        st.session_state.submissions.append({
            "name": name.strip(),
            "role": role,
            "message": message.strip(),
            "mood": mood,
            "time": datetime.now().strftime("%I:%M:%S %p"),
        })

# ---------------- Submission history ----------------
if show_history and st.session_state.submissions:
    st.markdown("---")
    st.subheader("📋 Submission History")
    for entry in reversed(st.session_state.submissions):
        with st.expander(f"{entry['name']} ({entry['role']}) — {entry['time']}"):
            st.write(f"**Mood:** {entry['mood']}")
            if entry["message"]:
                st.write(f"**Message:** {entry['message']}")

    st.metric("Total Submissions", len(st.session_state.submissions))

    if st.button("🗑️ Clear History"):
        st.session_state.submissions = []
        st.rerun()