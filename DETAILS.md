pip install -r requirements.in

Microsoft Azure
App Registration

New Registration

ONly First Option and then Restration Click / 3rd ONe

then copy client id and tenat id

then go to Manage/ certificate & secrets for secret here..

New Client Secret can Copy Value

create and copy secrets value

API Permissions:

Add -> Microsoft Graph

Application Permissions

TYpe Mail:-

then select and grant permission of admin consent

Grant the consent here to okay

Client Id = 994d75b9-9f1a-431d-8e0b-002600937cb7
Tenant Id = 201b0b06-8e16-4c0c-903d-63951e7ad0b7
Secret  = E4X8Q~LuItX6X9gE2GGaATvayCljnd~P.BZYta1z

POST Man - 
Now hit the first request to get the access token and save it to the environment variables.

https://developer.microsoft.com/en-us/graph/graph-explorer

First Sign In

deepak12#volunteer

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'deepak@12#$volunteer';

sudo mysql -u root

FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'deepak12#volunteer';
FLUSH PRIVILEGES;
sudo systemctl restart mariadb

http://52.64.0.96/checknow/index.php

mysql -u root -p
CREATE DATABASE IF NOT EXISTS volunteer;
CREATE USER 'volunteer_user'@'localhost' IDENTIFIED BY '45879&$deepak';
GRANT ALL PRIVILEGES ON volunteer.* TO 'volunteer_user'@'localhost';
FLUSH PRIVILEGES;

admin@volunteer.nz
123456@volunteer

ssh -i "volunteerfinal.pem" ec2-user@ec2-52-64-0-96.ap-southeast-2.compute.amazonaws.com

gunicorn --reload --workers 1 --bind 0.0.0.0:8000 volunteer_project.wsgi:application

cp -r static/ /var/www/html/volunteer/

pip install pymysql

sudo yum install python3-pip -y

sudo lsof -i :8000

sudo kill -9 81939 465488

http://52.64.0.96/static/scripts/testimonials-slider.js

uid UNique
Title String
Organisation Name String
Regions List
Organisation Branch String
Physical Address String ?
Postal Address String ?
Contact Name String
Phone Number String
Email Email
Company AIM String
Website String
Date Added Date Time

Volunteer Details to be Passed to a representative their:-
Volunteer Name
Volunteer Phone
Volunteer Email
Time Role

Disability Bool Blank
Policies Bool Blank
Risk Bool Blank
Charity Number String Blank
Comment

Deactivated Date Date Time Blank
Fee Number Blank
Type String
Status Active/InActive
Attachments

Active And Deactivate

Comment Table
Comment
Owner Id
Date Added
Admin

Volunteer Form

Title
First Name
Last Name
Email
Street

City
Post Code
Phone
Year of Birth
Date Added with time here..
Hours
Qualification
Work Experience
Skills
Health
Other Info
Notes
Languages

Type of Work - checkbox
    Animal Wellfare
    Arts/Cultural/Heritage
    Churchs/Faith
    Converstion/Environment
    Disability Services
    Education
    Emergency Services
    Health Services [Other]
    Information/Advice
    Iwi/Maori Services
    Migrant/Refuge Services


region of placement - checkbox

refer from - checkbox
    Internet
    Social Media
    Volunteering Promotion
    Other Organisation
    Family/Friend

Days - checkbox
    Monday - Sunday

Time - checkbox
    AM
    PM
    Evenings
    No Preferences

Labour - checkbox
    Paid Employment
    Unpaid Employment
    Seeking Employment
    Retired
    Student
    Visitor
    Other

Status - Dropdown
    Deactivated
    Active
    Review

Color - Dropdown
    Green
    Orange
    Red

Transport - checkbox
    Own Car
    License
    Public Transport

Review Date - date time

Gender - dropdown
    Male
    Female
    Other
    Not to Answer

Ethnic Origin - Checkbox
    NZ Maori
    NZ Other
    Pasifika
    Asian
    Non-NZ Other
    Refuse to answer

Activities - Checkbox
    Research
    Handy person
    Sales
    Accounting/Finance
    Data Collection
    Data Entry
    Writing
    Street Collection
    Financial Counselling
    Sorting
    Shopping
    Science
    Technology
    Painting
    Repairing
    Music
    Iwi/Maori Services
    Housekeeping
    Hospitality support
    Homecrafts
    Gardening/ planting
    Fundraising
    Event Support
    Event Organisation
    Driving (eg courier)
    Driving (clients)
    Coordinating
    Cooking
    Conversation Work
    Arts
    Animal Care
    Working with children/youth
    Visiting
    Tutoring
    Reading/Writing
    Mentoring
    Interviewing
    Hospitality
    Health Support
    First Aid (trained)

Activities Driving - Checkbox
    Courier
    Clients

Activities Administration - Checkbox
    General
    Data Entry

Activities Mantinance - Checkbox
    Handy Person

Activities Home Cares - Checkbox
    Cooking

Activities Technology - Checkbox
    Technology

Activities Event - Checkbox
    Support

Activites Hospitality - Checkbox
    Hospitality

Activites Support - Checkbox
    Refuges

Activites Financial - Checkbox
    Counselling

Activites Other - Checkbox
    Conversation Work

Activites Sport - Checkbox
    Coaching
    Referring

Activites Group - Checkbox
    Guiding Member/Trustee

<!-- ----------------------ROLE---------------------- -->

Role

title - Str
organisation - foreign key
contact - Text area
branch - Str
status - Dropdown
    Active
    DeActivated
    On-Hold
vols_req - Str
reports- Str
email - Email
date_added - date and time
description - text area
results - text area
leagues_hours - Text area
skills - Text area
personality - Text area
criminal - Bool
transport - Bool
wheelchair - Bool
toilet - Bool
stairs - Bool
home - Bool
Oneoff - Bool
Leagues Days - Text area
start_date - date and time
end_date - data and time, blank can be true not required too
Training - text area
Reimbursement - Text area
Reimbursement Other - Text Area
supervision - str
Other - Text area
PaidJob - Bool
Notes - Text Area
Filter - Check Box
    red, green, organe, Nil
Youth - bool
English - bool
Disability - bool
Mental - bool
Region of Placement - Checkbox
Days - Checkbox
Time - CHeckbox
Activities Driving - Checkbox
Activities Administration - Checkbox
Activities Mantinance - Checkbox
Activities Home Cares - Checkbox
Activities Technology - Checkbox
Activities Event - Checkbox
Activites Hospitality - Checkbox
Activites Support - Checkbox
Activites Financial - Checkbox
Activites Other - Checkbox
Activites Sport - Checkbox
Activites Group - Checkbox
Attachments - Char