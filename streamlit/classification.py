
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load dataset
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()

# Train model
model = RandomForestClassifier(random_state=42)

X = df.iloc[:, :-1]
y = df['species']

model.fit(X, y)

# Streamlit application
st.title("Iris Flower Classification")
st.write("Adjust the input features to predict the flower species.")

# Sidebar inputs
st.sidebar.title("Input Features")

sepal_length = st.sidebar.slider(
    "Sepal Length (cm)", 4.0, 8.0, 5.1
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)", 2.0, 4.5, 3.5
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)", 1.0, 7.0, 1.4
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)", 0.1, 2.5, 0.2
)

# Prepare input data
input_data = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=X.columns
)

# Prediction
if st.button("Predict Flower"):
    prediction = model.predict(input_data)

    predicted_species = target_name[prediction[0]]

    st.success(f"Predicted Flower: {predicted_species}")

    # Prediction probabilities
    probabilities = model.predict_proba(input_data)[0]

    st.subheader("Prediction Probabilities")

    probability_df = pd.DataFrame({
        "Species": target_name,
        "Probability": probabilities
    })

    st.bar_chart(
        probability_df.set_index("Species")
    )
