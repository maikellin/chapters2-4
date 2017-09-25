timenow = float(input("What time is it now 0-24"))
hourswait = float(input("How many hours are you waiting?"))

alarmtime = hourswait % 24 + timenow
if alarmtime > 12:
    print("your alarm will go off at: " + str(alarmtime) + "PM")
else:
    print("your alarm will go off at:" + str(alarmtime) + "AM")
