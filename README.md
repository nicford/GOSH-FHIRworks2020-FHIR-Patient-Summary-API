# FHIR Patient Summary Generator

This package allows you to generate a patient summary in docx or pdf format from a single patient ID or a list of patient IDs.

## Prerequisites
python3.7 or later

[flask](https://pypi.org/project/Flask/)

[FHIR-patient-summary](https://pypi.org/project/FHIR-Patient-Summary/) library

[Dotnet](https://dotnet.microsoft.com)

[libreoffice](https://www.libreoffice.org) (if you want patient summaries in pdf format)

# Steps to run the API locally

## Step 1 - Clone this repository
Clone this repository and open it in a terminal.

## Step 2 - Installation of dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FHIR-Patient-Summary.

```bash
pip install FHIR-Patient-Summary
```

Install Flask

```bash
pip install Flask
```

Follow the steps [here](https://dotnet.microsoft.com) to install dotnet 

Follow the instructions [here](https://tipsonubuntu.com/2018/08/11/install-libreoffice-6-1-ubuntu-18-04-16-04/) to install libreoffice. Note: this installation is only required if you would like to create patient summaries in pdf format.


## Step 3 - start dotnet server
Change directory to the dotnet-azure-fhir-web-api folder. Then run the following command

```bash
dotnet run
```

## Step 4 - run flask server

Open a new terminal window and navigate the directory you cloned from this repository.

Change directory to Flask-API

To start the Flask server locally on port 3000 run:

```bash
flask run -h localhost -p 3000
```

## Step 5 - test the server

On your browser of choice, test the following:

### Single patient in docx format

localhost:3000/getPatientSummaryDocument?patientID=8f789d0b-3145-4cf2-8504-13159edaa747&format=docx

### Single patient in pdf format

localhost:3000/getPatientSummaryDocument?patientID=8f789d0b-3145-4cf2-8504-13159edaa747&format=pdf

### Multiple patients

Get summary documents for the patients indexed from 10 to 50:

localhost:3000/getMultiplePatientSummaryDocuments?start=10&end=50

# GOSH-FHIRworks2020-FHIR-Patient-Summary-API
