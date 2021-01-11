from flask import Flask, request #flask implemented
import requests
from twilio.twiml.messaging_response import MessagingResponse 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World...app is working fine."

@app.route('/bot', methods=['POST'])

#greeting function 
def greeting():

    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()

   #--------------------------------------------------------------------------------------------------------------------------------------------------------
    if 'hey' or 'hi' or 'hy' or 'hello' or 'halo' or 'Hey' or 'Hi' or 'Hy' or 'Hello' or 'Halo' in incoming_msg:
        # it will return the greeting message prompted  
        msg.body("Hello :) Welcome to Re-invent Students \n ")
        msg.body("Please select one of the following: \n 1) Educational \n 2) Events \n 3) Skills & Platforms \n 4) Opportunuties")
      
   #--------------------------------------------------------Options for the first selection------------------------------------------------------------------------------------------------
    if '1' in incoming_msg:
            resp.message("Educational \n a) Evaluation \n b) Pychological \n c) Certification")
   #--------------------------------------------------------------------------------------------------------------------------------------------------------            
    if 'a' in incoming_msg:
        resp.message("Career evaluation \n 1)"+'https://www.careerexplorer.com/'+"\n 2)"
                    +'https://www.123test.com/career-test/'+"\n 3)" 
                    +'https://www.careeronestop.org/toolkit/careers/interest-assessment.aspx')
   #--------------------------------------------------------------------------------------------------------------------------------------------------------
    if 'b' in incoming_msg:
        resp.message("Pychological \n 1)"+'https://profile.keirsey.com/#/b2c/assessment/start'+"\n 2)"
                     +'https://www.16personalities.com'+"\n 3)"
                     +'https://www.crystalknows.com/personality-test')
    if 'c' in incoming_msg:
        resp.message("Certification Offered"+"\n 1)"+'https://www.alison.com'+"\n 2)"
                     +'https://www.pluralsight.com'+"\n 3)"
                     +'https://www.udemy.com'+"\n 4)"
                     +'https://www.amazon.com/certification'+"\n 5)"
                     +'https://www.microsoft.com/learning/browse-all-certifications.aspx')
    #------------------------------------------------------Options for the second selection--------------------------------------------------------------------------------------------------            
    if '2' in incoming_msg:
        resp.message("Events \n 1)"+'https://www.bizcommunity.com/Events/196/379/ndt-20201207000000.html'+" \n 2)"
                     +'https://v2.itweb.co.za/index.php?option=com_content&view=article&id=30901'+"\n 3)"
                     +'https://10times.com/southafrica/technology'+"\n 4)"
                     +'https://www.ictsummit.co.za/'+"\n 5)"
                     +'https://afriten.co.za/exhibitions-trade-shows-list-south-africa/'+"\n 6)"
                     +'https://www.itnewsafrica.com/category/africa-by-region/southern-africa-africa-by-region/')
    #------------------------------------------------------Options for the third selection--------------------------------------------------------------------------------------------------            
    if '3' in incoming_msg:
        resp.message("Skills And Platforms \n 1) ONLINE FREE COURSES \n "+"a)"+'https://codepen.io/'+"\n b)"
                     +'https://www.skillshare.com/'+"\n c)"
                     +'https://www.coursera.org/'+"\n d)"
                     +'https://www.edx.org' +"\n"+"\n"+" 2) UPSKILL APPLICATIONS"+"\n"
                     +"Dcoder \n"+'https://play.google.com/store/apps/details?id=com.paprbit.dcoder&hl=en'+"\n"
                     +"Web Development \n"+'https://play.google.com/store/apps/details?id=com.webdevelopment&hl=en'
                     +"\n SoloLearn: Learn to Code for free \n"+'https://play.google.com/store/apps/details?id=com.sololearn&hl=en'
                     +"\n Programming Hub \n"+'https://play.google.com/store/apps/details?id=com.freeit.java&hl=en'
                     +"\n W3Schools \n"+'https://play.google.com/store/apps/details?id=com.W3school.Anbu&hl=en'
                     +"\n Programming eBooks \n"+'https://play.google.com/store/apps/details?id=com.best.don.programmingbooks&hl=en'
                     +"\n 3) INCUBATION PLATFORMS \n Geekulcha \n"+'https://geekulcha.com/'
                     +"\n The InnovationHub \n"+'https://www.theinnovationhub.com'
                     +"\n Jozihub \n"+'https://jozihub.org/'
                     +"\n Amaphiko \n"+'https://www.amaphiko.redbull.com/en'
                     +"\n Tshimologong Precinct \n"+'https://tshimologong.joburg/')
    #------------------------------------------------------Options for the fourth selection--------------------------------------------------------------------------------------------------            

    if '4' in incoming_msg:
        resp.message("OPPORTUNITIES \n Learnerships \n"+'https://www.studentroom.co.za/category/learnership/'
                     +"\n"+'http://www.toplearnerships.co.za/list/'
                     +"\n"+'https://www.careersportal.co.za/learnerships-2020'
                     +"\n"+'https://availablelearnerships.com/'
                     +"\n Bursaries \n"+'https://zabusaries.com/'
                     +"\n"+'https://www.bursariesportal.co.za/'
                     +"\n"+'https://allbursaries.co.za/'
                     +"\n"+'https://www.gov.za/issues/government-and-opportunities-youth'
                     +"\n Vacation Work \n"+'https://www.rent-a-student.co.za/'
                     +"\n"+'https://www.graduates24.com/vacationwork')
    return str(resp)

   #--------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    app.run(debug=True)
