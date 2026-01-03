import streamlit as st
import pandas as pd
import json, os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Based NIDS",
    page_icon="🛡️",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #020617);
}
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #e0f2fe;
}
.sub-title {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 25px;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 25px rgba(56,189,248,0.25);
    margin-bottom: 25px;
}
.stat {
    text-align:center;
    padding:15px;
    background: linear-gradient(135deg,#1e3a8a,#312e81);
    border-radius:14px;
    color:#e0f2fe;
}
.stButton>button {
    width:100%;
    height:45px;
    background: linear-gradient(90deg,#38bdf8,#6366f1);
    color:black;
    font-weight:bold;
    border-radius:12px;
}
h1,h2,h3,label {color:#e0f2fe;}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.feature-box {
    background: rgba(255,255,255,0.06);
    padding: 15px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 0 15px rgba(99,102,241,0.3);
    transition: 0.3s;
}
.feature-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(56,189,248,0.6);
}
.feature-title {
    color:#38bdf8;
    font-weight:bold;
}
.login-note {
    color:#94a3b8;
    font-size:13px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)


# ================= MAIN HEADING =================
st.markdown("<div class='main-title'>🛡️ AI Based Network Intrusion Detection System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Secure • Detect • Prevent Cyber Attacks</div>", unsafe_allow_html=True)

# ================= USER AUTH =================
USER_FILE = "users.json"
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    return json.load(open(USER_FILE))

def save_users(u):
    json.dump(u, open(USER_FILE, "w"))

# ================= SESSION =================
defaults = {
    "page": "login",
    "user": None,
    "model": None,
    "features": None,
    "datasets_uploaded": 0,
    "test_files_checked": 0,
    "last_result": "None"
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ================= LOGIN =================
# ================= LOGIN =================
def login():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="text-align:center;">🔐 Secure Login</h2>
        <p style="text-align:center; color:#94a3b8;">
        Access your AI-powered intrusion detection dashboard
        </p>
        """,
        unsafe_allow_html=True
    )

    u = st.text_input("👤 Username")
    p = st.text_input("🔑 Password", type="password")

    remember = st.checkbox("💾 Remember Me")

    if st.button("🚀 Login"):
        users = load_users()
        if u in users and users[u] == p:
            st.session_state.user = u
            st.session_state.page = "home"
            if remember:
                st.session_state.remembered_user = u
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

    st.markdown("<p class='login-note'>Don't have an account? Create one below.</p>", unsafe_allow_html=True)

    st.markdown("<hr style='border:1px solid #334155;'>", unsafe_allow_html=True)

    st.markdown("### ✨ Platform Highlights")

    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='feature-box'><div class='feature-title'>🧠 AI Detection</div><p>ML-based attack analysis</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='feature-box'><div class='feature-title'>📊 Dashboard</div><p>Real-time insights</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='feature-box'><div class='feature-title'>🔐 Secure</div><p>User authentication</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("📝 Create New Account"):
        st.session_state.page = "signup"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ================= HOME PAGE =================
def home():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # Greeting
    st.markdown(
        f"""
        <h2 style="margin-bottom:5px;">
            👋 Hi, <span style="color:#38bdf8;">{st.session_state.user}</span>
        </h2>
        <p style="color:#cbd5f5; font-size:16px;">
            Welcome back! Here is a quick overview of your AI Based NIDS activity.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr style='border:1px solid #334155;'>", unsafe_allow_html=True)

    # Description
    st.markdown(
        """
        <p style="color:#e5e7eb; font-size:15px; line-height:1.6;">
        The <b>AI Based Network Intrusion Detection System</b> uses Machine Learning
        to analyze network traffic, detect malicious behavior, and help prevent
        cyber attacks in real time.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats cards
    c1, c2, c3 = st.columns(3)

    c1.markdown(
        f"<div class='stat'>📂<br><b>Datasets Uploaded</b><br>{st.session_state.datasets_uploaded}</div>",
        unsafe_allow_html=True
    )
    c2.markdown(
        f"<div class='stat'>📁<br><b>Files Checked</b><br>{st.session_state.test_files_checked}</div>",
        unsafe_allow_html=True
    )
    c3.markdown(
        f"<div class='stat'>🧠<br><b>Last Result</b><br>{st.session_state.last_result}</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Navigation
    if st.button("➡️ Go to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ================= DASHBOARD =================
def dashboard():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Dashboard")
    st.success(f"Welcome, {st.session_state.user}")

    dataset = st.file_uploader("📂 Upload Training Dataset (CSV)", type="csv")
    if dataset:
        df = pd.read_csv(dataset)
        if "label" not in df.columns:
            st.error("Dataset must contain a 'label' column")
            return

        st.dataframe(df.head())
        X = df.drop("label", axis=1)
        y = df["label"]

        if st.button("🧠 Train Model"):
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            model.fit(X_train, y_train)
            acc = model.score(X_test, y_test)

            st.session_state.model = model
            st.session_state.features = X.columns
            st.session_state.datasets_uploaded += 1

            st.success(f"Model trained successfully ✅ Accuracy: {acc*100:.2f}%")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.model:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📁 Upload File to Detect Attack")

        test_file = st.file_uploader("Upload Test CSV", type="csv")
        if test_file:
            test_df = pd.read_csv(test_file)
            test_df = test_df[st.session_state.features]
            pred = st.session_state.model.predict(test_df)

            attack = sum(pred)
            st.session_state.test_files_checked += 1

            if attack > 0:
                st.session_state.last_result = "ATTACK"
                st.error("🚨 HARMFUL / ATTACK DETECTED")
            else:
                st.session_state.last_result = "SAFE"
                st.success("✅ SAFE / NORMAL TRAFFIC")

        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.page = "login"
        st.rerun()

# ================= SIGNUP =================
def signup():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2 style="text-align:center;">📝 Create New Account</h2>
        <p style="text-align:center; color:#94a3b8;">
        Enter your details to get started
        </p>
        """,
        unsafe_allow_html=True
    )

    u = st.text_input("👤 Username")
    p = st.text_input("🔑 Password", type="password")
    cp = st.text_input("🔑 Confirm Password", type="password")

    if st.button("🚀 Sign Up"):
        if u.strip() == "" or p.strip() == "":
            st.error("❌ Username and password cannot be empty")
        elif p != cp:
            st.error("❌ Passwords do not match")
        else:
            users = load_users()
            if u in users:
                st.error("❌ Username already exists")
            else:
                users[u] = p
                save_users(users)
                st.success("✅ Account created successfully! Please login.")
                st.session_state.page = "login"
                st.rerun()

    if st.button("⬅️ Back to Login"):
        st.session_state.page = "login"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ================= ROUTER =================
if st.session_state.page == "login":
    login()
elif st.session_state.page == "signup":
    signup()
elif st.session_state.page == "home":
    home()
elif st.session_state.page == "dashboard":
    dashboard()

st.markdown("<div style='text-align:center;color:#94a3b8;'>© 2025 AI Based NIDS Project</div>", unsafe_allow_html=True)
