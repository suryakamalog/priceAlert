from price import scrape
import time
from tkinter import *
from tkinter.ttk import *
import os
import smtplib


def sendmail(save, current):
	dest_mail = email.get()
	EMAIL_ADDRESS = os.environ.get('DB_USER')
	EMAIL_PASSWORD = os.environ.get('DB_PASS')

	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

		if int(save) - int(current) > 0:
			subject = 'Price Drop'
		else:
			subject = 'Price Up'
		body = 'Changed from ' + str(save) + ' to ' + str(current)

		msg = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(EMAIL_ADDRESS, dest_mail, msg)

def run(URL, website, duration):
	save = -1
	n = duration//10
	while n:
		current = scrape(URL, website)
		if save!=current:
			sendmail(save, current)
		save = current
		n = n - 1
		print("IN RUN ", current)
		time.sleep(10)
		var.set('Current Price: ' + str(current))
		window.update_idletasks()
	return


window = Tk()
window.title("Price Notifier")

window.geometry('800x200')

lbl = Label(window, text="Enter the link:  ")
lbl.grid(column=0, row=0)

txt = Entry(window, width=35)
txt.grid(column=1, row=0)

lbl1 = Label(window, text="Choose Website:  ")
lbl1.grid(column=0, row=1)

val = StringVar()
combo = Combobox(window, textvariable = val)
combo['values'] = ("Amazon", "Flipkart", "Myntra", "Snapdeal")
combo.grid(column=1, row=1, sticky = W)


lbl2 = Label(window, text="Enter duration: (H:M)")
lbl2.grid(column=0, row=2)

hour = Entry(window, width=5)
hour.place(x=150, y=50)

minute = Entry(window, width=5)
minute.place(x=200, y=50)


lbl4 = Label(window, text="Enter email:  ")
lbl4.grid(column=0, row=5)

email = Entry(window, width=35)
email.grid(column=1, row=5)

current = ""
def clicked():
	x = hour.get()
	y = minute.get()
	duration = int(x)*3600 + int(y)*60
	URL = txt.get()
	website = val.get()
	if website == "Amazon":
		num = 1
	elif website == "Flipkart":
		num = 2
	elif website == "Myntra":
		num = 3
	elif website == "Snapdeal":
		num = 4
	run(URL, num, duration)
	


btn = Button(window, text="Submit", command = clicked)
btn.grid(column=1, row = 6)

var = StringVar()
var.set('Current Price: ')
lbl3 = Label(window, textvariable=var)
lbl3.grid(column=5, row=3)

window.mainloop()