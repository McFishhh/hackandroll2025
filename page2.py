import streamlit as st
import re


# ----- Page Configuration -----
st.set_page_config(
    page_title="Name Compatibility Checker",
    page_icon=":heart:",
    layout="centered"
)

# ----- Page Title -----
st.title("Name Compatibility Checker :heart:")

st.markdown(
    """
    <style>
    /* Custom CSS to style the input boxes and text */
    .css-1cpxqw2 {
        font-size: 18px;
        font-family: "Helvetica", sans-serif;
        color: #333333;
    }
    
    .css-17c73fc {
        font-family: "Helvetica", sans-serif;
    }

    .stTextInput > label {
        font-weight: 600 !important;
    }

    .css-1c8bvwh p {
        text-align: center;
        font-size: 20px;
        font-weight: 500;
    }

    .stButton > button {
        background-color: #ff4b4b;
        color: #ffffff;
        font-size: 16px;
        border-radius: 10px;
        padding: 0.5em 1em;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #f22e2e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- User Input -----
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# Button to trigger compatibility check
if st.button("Check Compatibility"):
    # 1. Validate inputs:
    #    - Allow spaces
    #    - Disallow digits or other numeric characters
    if not name1.strip() or not name2.strip():
        st.error("Please enter both names!")
    elif re.search(r"\d", name1) or re.search(r"\d", name2):
        st.error("Names must not contain numbers!")
    else:
        # 2. Assign each name to a numerical score
        #    For instance, sum the alphabetical positions of each letter (ignoring case)
        def name_to_number_score(name):
            score = 0
            for char in name.lower():
                if 'a' <= char <= 'z':
                    score += (ord(char) - 96)  # 'a' -> 1, 'b' -> 2, etc.
            return score

        score1 = name_to_number_score(name1)
        score2 = name_to_number_score(name2)

        # 3. Compute similarity/compatibility between the two scores
        #    Example algorithm: 1 - (absolute difference / max score)
        if score1 == 0 and score2 == 0:
            # edge case if both are empty or invalid
            compatibility = 0
        else:
            compatibility = 1 - abs(score1 - score2) / max(score1, score2)
        
        # Convert to percentage
        compatibility_percent = round(compatibility * 100, 2)

        # 4. Display result
        st.markdown(
            f"<h3 style='text-align:center;'>{name1} and {name2} are {compatibility_percent}% compatible!</h3>",
            unsafe_allow_html=True
        )