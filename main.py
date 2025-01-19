import streamlit as st


pg = st.navigation([
    st.Page("page1.py", title="First page", icon="🔥"),
    st.Page("page2.py", title="Second page", icon=":material/favorite:"),
])

pg.run()
