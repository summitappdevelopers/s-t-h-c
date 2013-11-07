import cgi,webapp2
from google.appengine.api import mail, oauth, users

MAIN_PAGE_HTML="""\
<!DOCTYPE html>
<!--
Created by Ajay Ramesh, 2013
Last revision 9/21/13
All of this code is mine, don't take it...or else.
-->
<html>
	<head>
		<title>Summit Tech Help</title>
		<!--CUSTOM STYLESHEETS-->
		<link href='/stylesheets/style_home.css' type='text/css' rel='stylesheet'/>
		<!--JQUERYUI STYLESHEET-->
		<link href='/stylesheets/jquery-ui-1.10.3.custom.min.css' rel='stylesheet'/>
		<!--JQUERY + NOTIFIER SCRIPTS-->
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
		<script type="text/javascript" src="/js/jquery-ui-1.10.3.custom.min.js"></script>"
		<script type="text/javascript" src="/js/notifier.js"></script>
		<!--CUSTOM JAVASCRIPT-->
		<script type="text/javascript" src="/js/controller_formSubmit.js"></script>
		<!--DROP DOWN SCRIPT-->
		<script>
			$(document).ready(function(){
				$('#infobox').hide();
				$('#faqbox').hide();
				$('#infobox').dialog({

						autoOpen: false,
						modal: true,
						show: {
							effect: "fade",
							duration: 200
						},

						hide: {
							effect: "fade",
							duration: 200
						},

						width: 500

					});
				$('#faqbox').dialog({

						autoOpen: false,
						modal: true,
						show: {
							effect: "fade",
							duration: 200
						},

						hide: {
							effect: "fade",
							duration: 200
						},

						width: 500

					});
				$('#header_title').click(function(){
					$('#infobox').dialog("open");					
				});
				$('#faq_button').click(function(){
                                        $('#faqbox').dialog("open");
				});

			
			});
		</script>
		<script>
			NotifierjsConfig.position = ["top", "right"];
		</script>
	</head>

	<!--HEADER-->
	<div id="header_container">
	        <span id="faq_button">FAQ</span>
		<span id="header_title">> Summit Tech Help <</span>
	</div>
	<!--END HEADER-->

	<body>
		<!--JAVASCRIPT HANDLED-->
		<div id="infobox">
			<div id="tagline">Something went wrong? We can help!</div>
			<p>Please note the following:</p>
			<ul>
			<li>Diagnosis is first, possible fix is second.</li>
			<li>Most hardware issues are not handled by us. </li>
			<li>Describe the issue as best as possible. </li>
			<li>You may be contacted by email with a simple fix. </li>
			<li>All inquiries will be addressed within 24 hours. </li>
			<li>We need more volunteers. If interested, contact: </li>
				aramesh.sj@mysummitps.org
			</ul>
		</div>
		<div id="faqbox">
                        <div id="tagline">FAQ</div>
                        <p>Please check out some of these tips before sending a ticket!</p>
                        <p>If you have a suggestion to improve this list, let me know!</p>
                        Q: My computer can't connect to the WiFi</br>
                        A: Settings>Disable WiFi>Enable WiFi. Restart</br>
                        Q: My trackpad is spazzing out!</br>
                        A: Settings>Advanced Settings>Reset Browser Settings</br>
                        Q: Websites aren't loading correctly</br>
                        A: Settings>Clear browser history>select Cookies and Cache</br>
                        Q: My internet is slow</br>
                        A: Tell your friend to stop streaming videos in 1080p</br>
                </div>
		<!--END JAVASCRIPT HANDLED-->

		<!--MAIN SUBMISSION FORM-->
		<div id="mainForm">
			<form id="problem_form" class="problem_form" action="/dispatch"method="post">
				<textarea id="problemText" placeholder="Explain your problem in detail. Click the black bar on top, for rules!" form="problem_form" rows="15" cols="45" name="problem_text" autofocus required></textarea></br>
				<!--<input type="text" value="___EMAIL___"placeholder="Enter your email..." name="student_email"></br>-->
				<input type="text" placeholder="Your name..." name="student_name" required/></br>
				<input id="submitButton" type="submit" value="Submit!" required/>
			</form>
		</div>
		<p>Submitting as: ___EMAIL___</p> 
		<!--END MAIN SUBMISSION FORM-->
		<form action="___LOGOUT_URL___" method="post">
                       <input type="submit" value="Logout!"/>
		</form>
		
	
	</body>

	<!--START FOOTER-->
		<div id="footer_container">
				<span id="copyright_notice">Copyright &#169 2013 by Ajay Ramesh. <a href="https://github.com/Carpetfizz/s-t-h-c">Fork me on Github!</a></span>
		</div>
	<!--END FOOTER-->

</html>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            self.response.write(MAIN_PAGE_HTML.replace('___EMAIL___',user.email()).replace('___LOGOUT_URL___',users.create_logout_url('http://www.s-t-h-c.appspot.com')))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
class ProblemRedirect(webapp2.RequestHandler):

    def post(self):

        #print cgi.escape(self.request.get('problem_text'))
        user = users.get_current_user()
        self.response.headers['Access-Control-Allow-Origin']='*'
        self.response.headers['Access-Control-Allow-Methods'] = 'POST'
        sender_address ="Summit Tech Help Bot <aramesh.sj@mysummitps.org>"
        reciever_address="Summit Tech Help Google Group <summit-tech-help@googlegroups.com>"
        subject=""
        problem_text=cgi.escape(self.request.get('problem_text'))
        student_name=cgi.escape(self.request.get('student_name'))
        student_email=user.email()
        body= "Hi! Here's a new ticket, good luck!:"+"\n"+"\n"+"Sender: "+student_name+"\n"+"Email: "+student_email+"\n"+"Problem: "+problem_text+"\n"+"\n"+"\n"+"\n"+"This was an automated message, please do not reply to this email. Reply to "+student_email
        mail.send_mail(sender_address, reciever_address, subject, body)     #send mail to Google Group
        confirmationSubject="Ticket Confirmation for "+student_name
        confirmationBody="Hi! Thanks for submitting a ticket. This is just an email confirmation. We wil be with you as soon as possible. Here is a copy of your problem: "+"\n"+"\n"+problem_text+"\n"+"\n"+"This was an automated message, please do not reply to this email."
        mail.send_mail(sender_address, student_email, confirmationSubject, confirmationBody)     #send mail to student
        
        

    
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/dispatch', ProblemRedirect),
    
], debug=True)
