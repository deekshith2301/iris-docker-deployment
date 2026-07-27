import pickle
import pandas as pd
import gradio as gr


# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predict Iris species based on flower measurements.
    """

    # Create input dataframe
    input_data = pd.DataFrame({
        "sepal_length": [sepal_length],
        "sepal_width": [sepal_width],
        "petal_length": [petal_length],
        "petal_width": [petal_width]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    return prediction


# Create Gradio web interface
app = gr.Interface(
    fn=predict_species,
    inputs=[
        gr.Number(label="Sepal Length"),
        gr.Number(label="Sepal Width"),
        gr.Number(label="Petal Length"),
        gr.Number(label="Petal Width")
    ],
    outputs=gr.Textbox(label="Predicted Iris Species"),
    title="Iris Species Prediction App",
    description="Enter sepal length, sepal width, petal length, and petal width to predict the Iris species."
)


# Launch the app
app.launch(server_name="0.0.0.0", server_port=7860)