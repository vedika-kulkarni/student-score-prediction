
import streamlit as st
import joblib
import numpy as np

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StudyScore",
    page_icon="🌷",
    layout="centered"
)

# ============================================================
# LOAD MODEL AND SCALER
# ============================================================

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #fff8fb,
        #f8f4ff,
        #f3f8ff
    );
}

/* Main container */
.block-container {
    max-width: 700px;
    padding-top: 35px;
    padding-bottom: 40px;
}

/* ============================================================
   HEADINGS
============================================================ */

h1 {
    color: #514276 !important;
    text-align: center;
    font-size: 44px !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #514276 !important;
    font-weight: 700 !important;
}

/* Normal text */
p {
    color: #5f566b !important;
    font-weight: 500;
}

/* Caption */
.stCaption,
small {
    color: #6f657a !important;
}

/* ============================================================
   TOP DECORATION
============================================================ */

.top-text {
    text-align: center;
    color: #806db0;
    font-size: 20px;
    font-weight: 600;
}

/* ============================================================
   SLIDER
============================================================ */

.stSlider label {
    color: #514276 !important;
    font-weight: 700 !important;
}

.stSlider [role="slider"] {
    background-color: #7563a8 !important;
}

/* ============================================================
   BUTTON
============================================================ */

.stButton button {
    width: 100%;
    height: 55px;

    border-radius: 18px;
    border: none;

    background: linear-gradient(
        90deg,
        #806db0,
        #b27fa9
    );

    color: white !important;

    font-family: 'Quicksand', sans-serif;
    font-size: 17px;
    font-weight: 700;

    box-shadow: 0 7px 18px rgba(100, 80, 130, 0.18);

    transition: 0.25s;
}

.stButton button:hover {
    transform: translateY(-2px);
    color: white !important;
}

/* ============================================================
   INFO BOX
============================================================ */

[data-testid="stAlert"] {
    color: #514276 !important;
    border-radius: 18px;
}

/* ============================================================
   METRIC
============================================================ */

[data-testid="stMetricLabel"] {
    color: #514276 !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #514276 !important;
    font-weight: 700 !important;
}

/* ============================================================
   PROGRESS BAR
============================================================ */

.stProgress > div > div > div > div {
    background-color: #7563a8;
}

/* ============================================================
   DIVIDER
============================================================ */

hr {
    border: none;
    height: 1px;
    background: #d9d0e5;
}

/* ============================================================
   FOOTER
============================================================ */

.footer-text {
    text-align: center;
    color: #6f657a;
    font-size: 13px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<p class="top-text">🌷　✦　♡　✦　🌷</p>',
    unsafe_allow_html=True
)

st.title("StudyScore ✨")

st.markdown(
    """
    <p style="
        text-align:center;
        color:#5f566b;
        font-size:16px;
        font-weight:500;
    ">
    A tiny study companion for your big dreams 🌙
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")


# ============================================================
# INTRODUCTION
# ============================================================

with st.container(border=True):

    st.subheader("📚 Let's see how you're doing!")

    st.write(
        "Tell me how many hours you study "
        "and I'll estimate your score ✨"
    )


st.write("")


# ============================================================
# STUDY HOURS
# ============================================================

st.subheader("🌸 Your study time")

st.write(
    "Move the slider to select your study hours."
)

hours = st.slider(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)


# ============================================================
# SELECTED HOURS
# ============================================================

st.info(
    f"📖 You selected **{hours:.1f} hours** of study time."
)


st.write("")


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("🌷  Predict My Score  ✨"):

    # --------------------------------------------------------
    # Prepare input
    # --------------------------------------------------------

    input_data = np.array([[hours]])

    # --------------------------------------------------------
    # Scale input
    # --------------------------------------------------------

    input_scaled = scaler.transform(input_data)

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    prediction = model.predict(input_scaled)

    # Convert NumPy result to normal number
    predicted_score = float(
        np.asarray(prediction).flatten()[0]
    )

    # Keep progress between 0 and 100
    display_score = max(
        0,
        min(100, predicted_score)
    )


    # ========================================================
    # PERFORMANCE MESSAGE
    # ========================================================

    if predicted_score >= 90:

        emoji = "🏆"
        message = "You're doing wonderfully! Keep shining ✨"

    elif predicted_score >= 75:

        emoji = "🌟"
        message = "Amazing work! You're on the right track 💜"

    elif predicted_score >= 60:

        emoji = "🌸"
        message = "Nice progress! Keep going, little by little 🌷"

    elif predicted_score >= 40:

        emoji = "🌱"
        message = "You're growing! A little more practice can help 💗"

    else:

        emoji = "☁️"
        message = "Every journey starts somewhere. Keep trying 🌱"


    # ========================================================
    # RESULT
    # ========================================================

    st.write("")

    st.divider()

    st.subheader("✨ Your Result")


    with st.container(border=True):

        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:48px;
                margin-bottom:5px;
            ">
                {emoji}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            label="Predicted Score",
            value=f"{predicted_score:.2f}"
        )

        st.success(message)

        st.write("📊 Score progress")

        st.progress(display_score / 100)

        st.caption(
            f"Prediction based on {hours:.1f} hours of study time."
        )


# ============================================================
# FOOTER
# ============================================================

st.write("")

st.divider()

st.markdown(
    """
    <p class="footer-text">
    🌷 Study a little. Dream a lot. 🌷
    <br><br>
    ♡ Student Score Prediction System ♡
    </p>
    """,
    unsafe_allow_html=True
)
