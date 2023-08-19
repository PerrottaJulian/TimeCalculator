def add_time(start, duration, weekday = ""):
  days_count = 0
  week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  weekday = weekday.lower()
  
  time = start.split(" ")[0]
  day_time = start.split(" ")[1]
  hours = time.split(":")[0]
  minutes = time.split(":")[1]

  duration_hours = duration.split(":")[0]
  duration_minutes = duration.split(":")[1]

  if day_time != "AM" and day_time != "PM" : 
    return "ERROR: must clarify if its AM or PM"
    #mover si luego uso un if con AM/PM

  try:
    hours = int(hours)
    minutes = int(minutes)
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)
  except:
    return "ERROR: time must be digits"
  if hours>12:
    return "ERROR: Time is in a 12 hours clock"
  if minutes > 59 or duration_minutes > 59:
    return "ERROR: Unlogical minutes"

  #main process
  new_hours = hours + duration_hours
  new_minutes = minutes + duration_minutes
  while new_minutes >= 60 :
    new_hours += 1
    new_minutes -= 60
    
  while new_hours > 11:
      
    if day_time == "PM":
      day_time = "AM"
      days_count += 1 
    else:
      day_time = "PM"

    if new_hours == 12:
      break
    else:
      new_hours -= 12
      
    
  #days
  if days_count == 1:
    days = " (next day)"
  elif days_count == 0:
    days = ""
  else:
    days = f" ({days_count} days later)"

  #FINAL STRING
  new_hours = str(new_hours)
  if new_minutes <10:
    new_minutes = "0"+str(new_minutes)
  else:
    new_minutes = str(new_minutes)

  #weekday
  if weekday in week:
      
    for i in range (days_count):
      try:
        weekday = week[week.index(weekday) + 1] 
      except: 
        weekday = week[0]

    new_time = new_hours+":"+new_minutes+ " "+day_time +", "+weekday.capitalize() + days
  else:
    new_time = new_hours+":"+new_minutes+ " "+day_time + days
  



  return new_time
