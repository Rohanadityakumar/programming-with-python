#sending email
import smtplib
#creating SMTP session
s = smtplib.SMTP('smtp.gmail.com',587)
#start TLS for security
s.starttls()
#AUTHENTIFICATION
s.login("rohan201120@gmail.com ","India9008605944")
#message to be sent
message= "HI MY NAME IS ROHAN"
#sending the email
s.sendmail("rohan201120@gmail.com", "syedulla7@gmail.com",message)
#terminating the session
s.quit()