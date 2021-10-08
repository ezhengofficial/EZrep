# Goofy Goobers: Julia Nelson, Oscar Wang, Owen Yaggy
# SoftDev
# K10: Putting Little Pieces Together
# 2021-10-05

from flask import Flask, render_template
import random
import csv
app = Flask(__name__) #create instance of class Flask

import csv #imports built in csv library
import random #imports the random library
occupations = csv.DictReader(open("data/occupations.csv", "r")) #imports csv as a dict via rows
job_percentages = dict() #stores jobs mapping to their percentages of workforce
#formatting it to a more iterable format
for row in occupations:
	row_values = tuple(row.values()) #gets rid of the unecessary keys information
	job_percentages[row_values[0]] = float(row_values[1]) #maps jobs to their percentages of workforce in dict

# debug_print(job_percentages)

#generates a random job given a probability dict formatted {job: percentage with total at the bottom}
def random_job(probability_book = job_percentages): #default argument provided. Valid for an assignment use case.
	# removes total from dictionary
	try: #deletes total line if it exists
		del probability_book["Total"]
	except KeyError:
		pass
	jobs = list(probability_book.keys())
	percentages = list(probability_book.values())

	return random.choices(population=jobs, k=1, weights=percentages)[0]


@app.route("/")       #assign fxn to route
def display():      #code to display the HTML on the webpage
    output = f'''
    <head>
    <h1>Goofy Goobers:Edwin Zheng, Theodore Fahay, Oscar Wang</h1>
    <p>SoftDev</p>
    <p>K13: Template for Success</p>
    <p>2021-10-08</p>
    </head>
    <body>
    <b>Your randomized output: </b> {picker()} {getList()}
    </body>
    '''
    return output
@app.route("/occupyflaskst")
def test_tmplt():
        return render_template('tablified.html', randOcc=random_job(), collection = job_percentages.keys())
app.debug = True
app.run()
