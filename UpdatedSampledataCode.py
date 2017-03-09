import random
import uuid
from random import randint
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

def generate_random_automated_emails(nb, length):
    return [get_random_name(letters, length) + '@' + 'peterlist.org' for i in range(nb)]


def phn():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

def ID():
    return str(uuid.uuid4())[2:8]

def amount():
    return(randint(100,1000))

def age():
    return(randint(20,60))


item_type = ["Music","Books","Accessory","Bikes","Cars","Clothes","Phones"]
job_type = ["Accounting","Programming","Finance","Teaching","Research","Data Analyst","Consulting","Mechanical","Construction"]
event_type = ["Music Concert", "Community Service","Career Fair","Sports","TV and Cinema"]
housing_type = ["Rent","Lease", "Buy"]
status = ["Single","Married","Seperated"]
ethnicity = ["White","Asian","Indian","Hispanic"]
company_name = ["WellsFargo","Google","Chase","Yahoo","Facebook","Amazon","Verizon"]
true_false = ["true","false"]
gender = ["Male","Female"]

text_file = open("output.txt","w")
text_file2 = open("output2.txt","w")

for i in range(1,101):
    ownerID = ID();
    owneremailID = generate_random_emails(10,7)[1];
    randomemailID = generate_random_automated_emails(10,7);
    itemType = random.choice(item_type)
    jobType = random.choice(job_type)
    eventType = random.choice(event_type)
    housingType = random.choice(housing_type)
    value = random.choice(true_false)

    ownerstring = '{{"ownerID": "{0}","contactInfo":{{"phoneNumber": "{1}","emailID": "{2}"}}}}'
    text_file.write(ownerstring.format(ownerID,phn(),owneremailID))
    text_file.write("\n")

    job_string = '{{"postID": "{0}","postInfo":{{"location": point("07.44,80.65"),"dateTime": datetime("2014-10-16T01:09:35"),"description": "Work 20 hours a week",\
"amount": {1},"ownerID":"{2}","automatedEmailID": "{3}"}},"fullTime": {4}, "jobType": "{5}", "organizationName":"{6}"}}'

    text_file2.write(job_string.format(ID(),amount(),ownerID, random.choice(randomemailID), value,jobType,random.choice(company_name)))
    text_file2.write("\n")


    event_string = '{{"postID":"{0}",\
"startDetail":datetime("2014-05-26T11:09:35"),"endDetail":datetime("2014-10-16T01:09:35"),"eventType":"{1}","postInfo":{{"location": point("07.44,80.65"),"dateTime": datetime("2019-04-26T10:10:35"),\
"description": "a fun event","valueAmount": {2},"ownerID": "{3}","automatedEmailID":"{4}"}}}}'

    text_file2.write(event_string.format(ID(),random.choice(event_type),amount(),ownerID, random.choice(randomemailID)))
    text_file2.write("\n")

    item_string = '{{"postID":"{0}", "postInfo":{{"location": point("02.11,80.65"),"dateTime": datetime("2015-09-16T01:09:35"),"description": "Recently Bought",\
"amount": {1},"ownerID":"{2}","automatedEmailID": "{3}"}},"itemType": "{4}"}}'

    text_file2.write(item_string.format(ID(),amount(),ownerID, random.choice(randomemailID), itemType))
    text_file2.write("\n")

    personal_string = '{{"postID":"{0}", "postInfo":{{"location": point("02.11,80.65"),"dateTime": datetime("2015-09-16T01:09:35"),"description": "Looking for a friend",\
"amount": {1},"ownerID":"{2}","automatedEmailID": "{3}"}},"age": {4}, "status": "{5}","bodyType" : "Heavy","ethnicity": "{6}","advertiserGender": "{7}","seekingGender":"{8}"}}'
    
    text_file2.write(personal_string.format(ID(),amount(),ownerID, random.choice(randomemailID), age(), random.choice(status),random.choice(ethnicity),random.choice(gender),random.choice(gender)))                                           
    text_file2.write("\n")


    housing_string = '{{"postID":"{0}","postInfo":{{"location": point("02.11,80.65"),"dateTime": datetime("2015-09-16T01:09:35"),\
"description": "Looking for a friend","amount": {1},"ownerID":"{2}","automatedEmailID":"{3}"}}, "bedroomNumber":{4},"address":{{"streetname":"Berkeley","aptNumber": 277,"city":"Irvine","state": "CA"}},\
"petAllowed":{5},"housingType":"{6}","size": {7}}}'

    text_file2.write(housing_string.format(ID(),amount(),ownerID,random.choice(randomemailID), randint(1,7),value, housingType,float(randint(100000,1000000))))
    text_file2.write("\n")    
    







    
