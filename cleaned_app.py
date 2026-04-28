import streamlit as st
from datetime import datetime

# ── Session Setup ─────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True
    st.session_state.user_email = "guest@ecovault.app"
    st.session_state.user_data = {
        "name": "Guest User",
        "email": "guest@ecovault.app",
        "created_at": str(datetime.now())
    }

# ── Dummy Database Functions (Replace with real DB if needed) ──
def get_or_create_user(email, name, pic):
    return {
        "name": name,
        "email": email,
        "created_at": str(datetime.now())
    }

# ── Main App UI ───────────────────────────────────────────────
def show_app():
    st.set_page_config(page_title="EcoVault", layout="wide")

    st.title("🌱 EcoVault Dashboard")
    st.write(f"Welcome, {st.session_state.user_data['name']}!")

    st.divider()

    st.subheader("Your Activity")
    st.info("No activity yet. Start using the app 🚀")

    st.divider()

    if st.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ── Run App Directly (No Login Required) ──────────────────────
show_app()