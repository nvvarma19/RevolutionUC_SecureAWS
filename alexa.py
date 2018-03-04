from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode


app = Flask(__name__)
ask = Ask(app,"/cis_reader")

def get_IAMData():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    false_count = 0
    true_count = 0
    manual_Count = 0
    for iamData in json_data['1']:
        cis1DataJsonResult = json_data['1'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    DataStatement = "Hi, You have " + str(true_count) + " passed tests , " + str(false_count) + " failed tests and " + str(manual_Count) + " would require manual inspection in Identity and Access Management"  
    return DataStatement
def get_overallData():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    false_count = 0
    true_count = 0
    manual_Count = 0
    for iamData in json_data['1']:
        cis1DataJsonResult = json_data['1'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    for iamData in json_data['2']:
        cis1DataJsonResult = json_data['2'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    for iamData in json_data['3']:
        cis1DataJsonResult = json_data['3'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1

    for iamData in json_data['4']:
        cis1DataJsonResult = json_data['4'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    DataStatement = "Hi, you have " + str(true_count) + " passed tests , " + str(false_count) + " failed tests and " + str(manual_Count) + " would require manual inspection in your AWS environment"  
    return DataStatement
def get_LoggingData():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    false_count = 0
    true_count = 0
    manual_Count = 0
    for iamData in json_data['2']:
        cis1DataJsonResult = json_data['2'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    DataStatement = "Hi, You have " + str(true_count) + " passed tests , " + str(false_count) + " failed tests and " + str(manual_Count) + " would require manual inspection in Logging"  
    return DataStatement
def get_MonitoringData():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    false_count = 0
    true_count = 0
    manual_Count = 0
    for iamData in json_data['3']:
        cis1DataJsonResult = json_data['3'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    DataStatement = "Hi, You have " + str(true_count) + " passed tests , " + str(false_count) + " failed tests and " + str(manual_Count) + " would require manual inspection in Monitoring"  
    return DataStatement
def get_SGData():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    false_count = 0
    true_count = 0
    manual_Count = 0
    for iamData in json_data['4']:
        cis1DataJsonResult = json_data['4'][iamData]['Result']
        if str(cis1DataJsonResult) == "true":
            true_count += 1
        if str(cis1DataJsonResult) == "false":
            false_count += 1
        if str(cis1DataJsonResult) == "Manual":
            manual_Count += 1
    DataStatement = "Hi, You have " + str(true_count) + " passed tests , " + str(false_count) + " failed tests and " + str(manual_Count) + " would require manual inspection in  networking"  
    return DataStatement
def get_reasons():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    list1 = []

    for iamData in json_data['1']:
        cis1DataJsonResult = json_data['1'][iamData]['failReason']
        list1.append(cis1DataJsonResult)
    for iamData in json_data['2']:
        cis1DataJsonResult = json_data['2'][iamData]['failReason']
        list1.append(cis1DataJsonResult)
    for iamData in json_data['3']:
        cis1DataJsonResult = json_data['3'][iamData]['failReason']
        list1.append(cis1DataJsonResult)
    for iamData in json_data['4']:
        cis1DataJsonResult = json_data['4'][iamData]['failReason']
        list1.append(cis1DataJsonResult)
    reasons = '....'.join([i for i in list1])
    return reasons

def get_FirstSectionDescriptions():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    list1 = []

    for iamData in json_data['1']:
        cis1DataJsonResult = json_data['1'][iamData]['Description']
        list1.append(cis1DataJsonResult)
    descriptions = '....'.join([i for i in list1])
    return descriptions
def get_SecondSectionDescriptions():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    list1 = []

    for iamData in json_data['2']:
        cis1DataJsonResult = json_data['2'][iamData]['Description']
        list1.append(cis1DataJsonResult)
    descriptions = '....'.join([i for i in list1])
    return descriptions
def get_ThirdSectionDescriptions():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    list1 = []

    for iamData in json_data['3']:
        cis1DataJsonResult = json_data['3'][iamData]['Description']
        list1.append(cis1DataJsonResult)
    descriptions = '....'.join([i for i in list1])
    return descriptions
def get_FourthSectionDescriptions():
    with open("test.json") as json_file:
        json_data = json.load(json_file)
    list1 = []

    for iamData in json_data['4']:
        cis1DataJsonResult = json_data['4'][iamData]['Description']
        list1.append(cis1DataJsonResult)
    descriptions = '....'.join([i for i in list1])
    return descriptions


@app.route('/')
def homepage():
    return "hi there how you doing?"

@ask.launch
def start_skill():
    welcome_message= 'Hello there, would you like to know more about your AWS CIS IAM benchmarks?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_IAMData()
 
    return statement(headlines)

@ask.intent("AskIntent")
def share_section2headlines():
    headlines = get_LoggingData()
 
    return statement(headlines)

@ask.intent("AskThreeIntent")
def share_section3headlines():
    headlines = get_MonitoringData()
 
    return statement(headlines)

@ask.intent("AskFourIntent")
def share_section4headlines():
    headlines = get_SGData()
    return statement(headlines)
@ask.intent("AskAWSIntent")
def getAWS():
    headlines = get_overallData()
    return statement(headlines)
@ask.intent("AskReasonsIntent")
def getAWSReasons():
    headlines = get_reasons()
    return statement(headlines)
@ask.intent("AskDescriptionFirst")
def getDescriptionsFirst():
    headlines = get_FirstSectionDescriptions()
    return statement(headlines)
@ask.intent("AskDescriptionSecond")
def getDescriptionsSecond():
    headlines = get_SecondSectionDescriptions()
    return statement(headlines)
@ask.intent("AskDescriptionThird")
def getDescriptionsThird():
    headlines = get_ThirdSectionDescriptions()
    return statement(headlines)
@ask.intent("AskDescriptionFourth")
def getDescriptionsFourth():
    headlines = get_FourthSectionDescriptions()
    return statement(headlines)




@ask.intent("NoIntent")
def no_intent():
 bye_text = 'I am not sure why you asked me to run then, but okay... bye'
 return statement(bye_text)

if __name__=='__main__':
 app.run(debug=True)