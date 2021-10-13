import time
from plyer import notification
 if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**Hey Drink Water Now!!",
 			message ="Drinking water is like washing out your insides. The water will cleanse the system, fill you up, decrease your caloric load and improve the function of all your tissues.",
 			app_icon = "ico.jpg",
 			timeout= 30
 			)
 		#	time.sleep(6)
 			time.sleep(60*60)
