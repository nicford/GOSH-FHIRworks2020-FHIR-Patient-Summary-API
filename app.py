from flask import Flask, send_file, request
from fhir_patient_summary import createPatientSummaryDocument, createPatientSummaryDocumentFromPatientIDList
from fhir_parser import FHIR

app = Flask(__name__)

fhir = FHIR()

allowedFileTypes = ["docx", "pdf"]
destinationDir = "output"
allPatients = fhir.get_all_patients()
numberOfPatients = len(allPatients)
allPatientsIDList = [patient.uuid for patient in allPatients]


# dowload single patient summary document by patient ID
@app.route("/getPatientSummaryDocument", methods=["GET"])
def getPatientSummaryDocument():
    patientID = request.args.get("patientID")
    format = request.args.get("format") if request.args.get("format") is not None else "docx"     # set default file type to docx

    patientObservations = fhir.get_patient_observations(patientID)
    
    if format not in allowedFileTypes:
        return "Wrong file type specified. Valid formats are: " + ",".join(allowedFileTypes)

    documentDir = createPatientSummaryDocument(patientID, format, destinationDir)

    return send_file(documentDir)


# dowload multiple patient summary documents by list of patient IDs. The list of patient IDs is limited to 100 to avoid crashing the dotnet server.
@app.route("/getMultiplePatientSummaryDocuments")
def getAllPatientsSummaryDocument():
    format = request.args.get("format") if request.args.get("format") is not None else "docx"     # set default file type to docx
    startArg = request.args.get("start")
    endArg = request.args.get("end")

    if startArg is not None:
        if int(startArg) < 0 or int(startArg) > numberOfPatients:
            return "Start index error: Start index must be an integer between one and " + str(numberOfPatients)
        elif startArg.isnumeric():
            startIndex = int(startArg)
    else:
        startIndex = 1

    if endArg is not None:    
        if int(endArg) < 0 or int(endArg) > numberOfPatients:
            return "End index error: End index must be an integer between two and " + str(numberOfPatients)
        elif endArg.isnumeric() and int(endArg) > 0:
            endIndex = int(endArg)
    else:
        endIndex = startIndex + 100

    if startIndex > endIndex or abs(startIndex - endIndex) > 100:
        return "Index Error: Start index must be smaller than end index. Indexes must also be less than 100 apart as the request limit is 100 at a time"

    if format not in allowedFileTypes:
        return "Wrong file type specified. Valid formats are: " + ",".join(allowedFileTypes)

    patientsToUse = allPatientsIDList[startIndex-1:endIndex-1]
    documentsDir = createPatientSummaryDocumentFromPatientIDList(patientsToUse, format, destinationDir, zipFile=True)

    return send_file(documentsDir)