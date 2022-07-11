def add_time(start, duration,  *args):
  next_day = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursady", "Friday", "Saturday" ]
  a = start.split(" ")[0]
  start_hour = a.split(":")[0]
  start_minutes = a.split(":")[1]
  duration_hour = duration.split(":")[0]
  duration_minutes = int(duration.split(":")[1])
  meridian = start.split(" ")[1]
  number_of_days = 0
      
  total_minutes = int(start_minutes) + int(duration_minutes)
  total_hour  = int(start_hour) + int(duration_hour)
    
    
  if total_minutes > 59:
    start_hour = 1 + int(start_hour)
    total_minutes = total_minutes % 60 
  if total_minutes < 10:
    total_minutes = f"0{total_minutes}"
    total_hour  = int(start_hour) + int(duration_hour)
   
 
  if meridian =="PM" and (total_hour)//12!=0:
    number_of_days = ((total_hour//12)//2)+1
      
  elif meridian =="AM"and (total_hour)>=24 :
    number_of_days = total_hour//24
        

  if total_hour>=12 and (total_hour//12)%2!=0:
    if meridian =="PM":
      meridian ="AM"
    elif meridian =="AM":
      meridian ="PM"
            
    
    
  if total_hour >= 12 and total_hour%12!=0:
    total_hour = total_hour % 12
  else:
    if total_hour%12==0:
      total_hour = 12
    
  time = f"{str(total_hour)}:{str(total_minutes)} {meridian}"  
    
  if args:
    day =args[0].title()
    if number_of_days >-1:
      index = next_day.index(day)
      index = index + number_of_days %7
      if index >6:
        index =index-7
    day = next_day[index]
    time += f", {day}"

  if number_of_days ==1:
    time +=  "(next day)".rjust(11)
  elif(number_of_days) >1:
    time +=  f" ({number_of_days} days later)".rjust(11)


  return(time)