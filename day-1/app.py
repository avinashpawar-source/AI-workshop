from datetime import date
import streamlit as st

st.set_page_config(page_title="Brain Diary", page_icon="💡")

st.title("💡 Brain Diary")

# Use a different session state variable name
if "journal" not in st.session_state:
    st.session_state.journal = []

with st.form("quick_log", clear_on_submit=True):
    concept = st.text_input("What's on your mind today?")
    hours = st.slider("Hours", 0.5, 6.0, 1.0, step=0.5)
    mood = st.selectbox("How did it go?", ["Tricky", "Decent", "Aha! moment"])
    saved = st.form_submit_button("Save Entry")

if saved and concept.strip():
    st.session_state.journal.append(
        {
            "Date": date.today().isoformat(),
            "Concept": concept.strip(),
            "Hours": hours,
            "Vibe": mood,
        }
    )
    st.success("Saved!")

if st.session_state.journal:
    st.divider()
    st.dataframe(st.session_state.journal, use_container_width=True)
    total_time = sum(item["Hours"] for item in st.session_state.journal)
    st.caption(f"Total time logged: {total_time} hours")