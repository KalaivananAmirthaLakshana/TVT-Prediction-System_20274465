from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("extra_trees_deployment.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        MD = float(request.form["MD"])
        X = float(request.form["X"])
        Y = float(request.form["Y"])
        Z = float(request.form["Z"])
        GR = float(request.form["GR"])

        input_data = pd.DataFrame(
            [[MD, X, Y, Z, GR]],
            columns=["MD", "X", "Y", "Z", "GR"]
        )

        prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)