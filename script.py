
# Dan Herbatschek
# website creation with python flask micro-framework


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/journey_in_the_life_of_an_aspiring_data_scientist")
def journey_in_the_life_of_an_aspiring_data_scientist():
    return render_template("/journey_in_the_life_of_a_data_scientist.html")

@app.route("/mapping_the_software_engineering_landscape")
def mapping_the_software_engineering_landscape():
    return render_template("/mapping_the_software_engineering_landscape.html")

@app.route("/website_history")
def website_history():
    return render_template("/website_history.html")

@app.route("/projects")
def projects():
    return render_template("/projects.html")

@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")

@app.route("/data_science")
def data_science():
    return render_template("/data_science.html")

@app.route("/mathematics")
def mathematics():
    return render_template("/mathematics.html")

@app.route("/blockchain_technologies")
def blockchain_technologies():
    return render_template("/blockchain_technologies.html")

@app.route("/history_and_data_science")
def history_and_data_science():
    return render_template("/history_and_data_science.html")

@app.route("/intellectual_history")
def intellectual_history():
    return render_template("/intellectual_history.html")

@app.route("/history_of_science_and_mathematics")
def history_of_science_and_mathematics():
    return render_template("/history_of_science_and_mathematics.html")

@app.route("/recommendations")
def recommendations():
    return render_template("/recommendations.html")

@app.route("/training_page")
def training_page():
    return render_template("/training_page.html")

@app.route("/training_page2")
def training_page2():
    return render_template("trainingpage2.html")

@app.route("/awsbackeddata")
def awsbackeddata():
    return render_template("awsbackeddata.html")

if __name__=="__main__":
    app.run(debug=True)

