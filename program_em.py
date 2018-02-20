#email schedulimg
import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("sumaiyachachiya65@gmail.com","saifali1234")
msg="hi how are you"
s.sendmail("sumaiyachachiya65@gmail.com","sumaiyachachiya65@gmail.com",msg)
print("sucess")
s.quit()
