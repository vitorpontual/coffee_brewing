from flask import Flask, render_template, request
from config.methods import METHODS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recipe = None
    if request.method == "POST":
        method_key = request.form.get("method")
        try:
            # Agora pegamos o peso do grão (coffee_beans)
            coffee_beans = float(request.form.get("coffee"))
            method_data = METHODS[method_key]
            
            # Cálculo: Água necessária = gramas de café * ratio
            water_needed = coffee_beans * method_data["ratio"]
            
            recipe = {
                "method_name": method_data["nome"],
                "coffee": coffee_beans,
                "water": round(water_needed, 0), # Água geralmente arredondamos para inteiro
                "grind": method_data["moagem"]
            }
        except (ValueError, TypeError, KeyError):
            recipe = "Error: Please enter a valid coffee weight."

    return render_template("index.html", methods=METHODS, recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)
