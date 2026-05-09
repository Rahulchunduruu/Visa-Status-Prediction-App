import streamlit as st
import requests
import threading
import uvicorn
import time

st.set_page_config(page_title="Visa Status Predictor", page_icon="🛂", layout="centered")

def start_server():
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

def wait_for_server(url, retries=10, delay=1):
    for _ in range(retries):
        try:
            requests.get(url)
            return True
        except:
            time.sleep(delay)
    return False

if "server_started" not in st.session_state:
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    with st.spinner("Starting server, please wait..."):
        ready = wait_for_server("http://127.0.0.1:8000")
    if ready:
        st.session_state["server_started"] = True
    else:
        st.error("❌ Server failed to start. Try restarting the app.")

API_URL = 'http://127.0.0.1:8000/predict'

st.title("🛂 Visa Status Prediction")
st.markdown("Fill in the details below to check your visa eligibility.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 Age", min_value=21, max_value=119, value=25)
    height = st.number_input("📏 Height (in meters)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    income_lpa = st.number_input("💰 Annual Income (LPA)", min_value=0, value=5)
    workexperience = st.number_input("💼 Work Experience (years)", min_value=0, value=2)

with col2:
    Degree = st.selectbox("🎓 Educational Degree", ['Graduate', 'Post Graduate', 'No Degree'])
    city = st.selectbox("🏙️ City", ["Visakhapatnam", "Itanagar", "Guwahati", "Patna", "Raipur", "Panaji",
                                     "Ahmedabad", "Gurugram", "Shimla", "Ranchi", "Bengaluru", "Kochi",
                                     "Indore", "Mumbai", "Imphal", "Shillong", "Aizawl", "Kohima",
                                     "Bhubaneswar", "Ludhiana", "Jaipur", "Gangtok", "Chennai",
                                     "Hyderabad", "Agartala", "Lucknow", "Dehradun", "Kolkata"])
    Nationality = st.selectbox("🌍 Nationality", ['INDIAN', 'NOT INDIAN'])
    crimerecord = st.selectbox("⚖️ Any Crime Record?", options=['no', 'yes'])

st.divider()

if st.button("🔍 Predict Visa Status", use_container_width=True):
    input_data = {
        "age": age,
        "height": height,
        "income_lpa": income_lpa,
        "workexperience": workexperience,
        "crimerecord": crimerecord,
        "city": city,
        "Nationality": Nationality,
        "Degree": Degree
    }

    with st.spinner("Analyzing your details..."):
        try:
            response = requests.post(API_URL, json=input_data)
            result = response.json()

            if response.status_code == 200 and "message" in result:
                prediction = result["message"]
                category = prediction['predicted_category']
                confidence = prediction["confidence"]
                print
                if category == "ACCEPTED":
                    st.success(f"Visa Status: **{category}**")
                else:
                    st.error(f"Visa Status: **{category}**")

                st.metric(label="Confidence Score", value=f"{round(confidence * 100, 2)}%")

                st.markdown("#### 📊 Class Probabilities")
                for label, prob in prediction["class_probabilities"].items():
                    st.progress(prob, text=f"{label}: {round(prob * 100, 2)}%")

            else:
                st.error("Unexpected response from the API:")
                st.error(f"API Error {response.status_code}")
                st.json(result)

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server. Please make sure it's running with: `uvicorn main:app --reload`")
