# '''
#                                             PROJECT DESCRIPTION
#
# Owner: Dan Herbatschek
# Start Date: 09/09/17
# Linked Website/Domain/Project title: My Brain Is Open; mybrainisopen.com; danherbatschek.com
# My Brain is Open
# by Dan Herbatschek
#
#
#                             website creation with python flask micro-framework
#
# - Front-end:
#  - add html content
#  - add css
#  - add javascript functionality and design
#  - make user of bootstrap and jquery
#  - launch site live and learn about deployment
#
# - Back-end:
#  - build REST API with Flask
#  - store resources in SQL database
#  - make use of NoSQL Database
#  - create data pipeline
#
# - website sections and goals:
#   - About section that introduces me and the website to the world noting that the site is meant to be:
#             - a public repository for my projects
#             - a platform to share my thoughts
#             - a learning method
#             - a display of my thought process
#             - user data collection
#   - personal section with writing samples
#   - snapshots that showcase the website's appearance in progress
#   - Articles of interest written by others
#   - Articles of interest written by me
#   - build and connect web-scraper of real estate data
#   - market research with real estate data to answer question about project
#   - present data story
#   - build blockchain real estate service
#   - financial data analysis - using Bokeh
#   - algorithmic trading platform
#   - banking / financial transaction website
#   - investment management platform
#   - Have a section that features a map of tech / software engineering / data science landscape
#
# - Sections
#   - ABOUT
#   - JOURNEY IN THE LIFE OF AN ASPIRING DATA SCIENTIST
#   - MAPPING THE SOFTWARE ENGINEERING LANDSCAPE
#   - WEBSITE HISTORY
#   - PROJECTS IN PROGRESS
#   - DH PORTFOLIO
#   - DATA SCIENCE
#   - MATHEMATICS
#   - BLOCKCHAIN TECHNOLOGIES
#   - HISTORY AND DATA SCIENCE
#   - INTELLECTUAL HISTORY
#   - HISTORY OF SCIENCE AND MATHEMATICS
#   - READING RECOMMENDATIONS
#   - TALKS
#
# - Ideas
#   - add quotes in each section or even a quotes sections
#
# '''


 # notes

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

