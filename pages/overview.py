import streamlit as st

if st.session_state.get("logged_in") == None:
    st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


st.set_page_config(page_title="Overview")

st.markdown("# Overview")

if st.session_state.logged_in:
    st.sidebar.success("Logged in")
    st.sidebar.button("Log out", on_click=logout)
else:
    st.sidebar.warning("Not logged in")
    st.sidebar.button("Log in", on_click=login)

st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)