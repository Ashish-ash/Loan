from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('loan.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
	if request.method == 'POST':

		ApplicantIncome = float(request.form['Income'])
		CoApplicantIncome = float(request.form['Income1'])
		LoanAmount = float(request.form['LoanAmount'])
		LoanAmountTerm = int(request.form['LoanAmountTerm'])
		CreditHistory = int(request.form['Credit'])
		Gender=request.form['Gender']
		if Gender == 'Male':
			Gender =1
		else:
			Gender =0
		MaritalStatus=request.form['Status']
		if MaritalStatus == 'Married':
			MaritalStatus =1
		else:
			MaritalStatus =0
		Education=request.form['Education']
		if Education == 'Graduate':
			Education =1
		else:
			Education =0
		Employement=request.form['Employement']
		if Employement == 'Employed':
			Employement =1
		else:
			Employement =0
		Dependents = request.form['Dependents']
		if Dependents == 0:
			Dependents=0
		elif Dependents==1:
			Dependents=1
		elif Dependents==2:
			Dependents=2
		elif Dependents == 3:
			Dependents=3

		Property = request.form['Property']
		if Property == 'Urban':
			Property=2
		elif Property=='Semi Urban':
			Property=1
		elif Property=='Rural':
			Property=0
		prediction = int(model.predict([[ApplicantIncome,CoApplicantIncome,LoanAmount,LoanAmountTerm,CreditHistory,Gender,MaritalStatus,Education,Employement,Dependents,Property]]))
		return render_template('index.html',prediction_text='Loan : {}'.format(prediction))

if __name__=="__main__":
    app.run(debug=True)