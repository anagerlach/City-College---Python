## Weather Analyser

#The following code creates a list of size 30 with random integers between 
# 0 and 35 using the randint() function from the random library. 
# The list represents daily temperatures between 0°C and 35°C for a month (30 days).
#Run this code and print the daily_temperatures. (The values will be different every time you run the code).
#Using this list of daily temperatures, write separate for-loops to do the following. 
# You can use the enumerate method in the for-loop statement to keep track of the days.

import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]
print(daily_temperatures)

# Find the day with the lowest temperature.
min_temp = 40

for daily, temp in enumerate(daily_temperatures, start=1):
    if temp < min_temp:
        min_temp = temp
        min_day = daily

print(f"The day with the lowest temperature is {min_day} with {min_temp}°C.")
    
# Find the day with the highest temperature.
max_temp = 1

for daily2, temp2 in enumerate(daily_temperatures, start=1):
    if temp2 > max_temp:
        max_temp = temp2
        max_day = daily2

print(f"The day with the highest temperature is {max_day} with {max_temp}°C.")

#Find the days where the temperature rises above 20°C.

print("The days where the temperature rises above 20°C:")
for daily3, temp3 in enumerate(daily_temperatures, start =1):
    if temp3>20:
        print (f"{daily3}: {temp3}°C.")
        
#Find the days where the temperature drops below 10°C
print("The days where the temperature drops below 10°C:")
for daily4, temp4 in enumerate(daily_temperatures, start =1):
    if temp4<10:
        print (f"{daily4}: {temp4}°C.")
        

# Find the days where the temperature increased from the day before
print("Days where the temperature increased from the day before.")
for daily5, temp5 in enumerate(daily_temperatures[1:], start=1):
    if temp5 > daily_temperatures[daily5 - 1]:
        print(f"{daily5+1}: {temp5}°C")


#Find the days where the temperature was hotter than any of the days previous in the month.
temp_max = daily_temperatures[0]
print("Days where the temperature was hotter than any of the days previous in the month")
for daily6, temp6 in enumerate(daily_temperatures, start=1):
    if temp6 > temp_max:
        print(f"{daily6}:{temp6}°C")
        temp_max = temp6

#2) Now generate another list for rainfall values between 0mm and 10mm for a month (30 days).
#Imagine these are the same 30 days as the daily temperatures list. For example, one day could have 
#a temperature of 11°C and a rainfall of 3mm.

daily_rainfall = [random.randint(0, 10) for _ in range(30)]

#Using the list of daily temperatures and daily rainfall, write separate for-loops to do the following.
#You can use the zip method in the for-loop statements to traverse through both lists simultaneously.

# Record the amount of ‘bad weather’ days, 
# the number of days that the rainfall is above 3mm and the temperature is below 10°C.

print("Weather")
print(daily_rainfall)

bad_weather = 0
for temp7, rain in zip(daily_temperatures, daily_rainfall):
    if temp7 < 10 and rain > 3:
        bad_weather = bad_weather +1
print(f"The number of days with a bad weather is {bad_weather}")


# Record the amount of ‘average weather’ days, the number of days that the rainfall is 
#between 1mm and 5mm and the temperature is between 10°C and 18°C.

avarage_weather = 0
for temp8, rain2 in zip(daily_temperatures, daily_rainfall):
    if temp8 > 10 and temp8 <18  and rain2 >1 and rain2 <5:
        avarage_weather = avarage_weather +1

print(f"The number of days avarage weather is {avarage_weather}")    

#Record the amount ‘good weather’ days, the number of days that the rainfall is below 2mm, 
#and the temperature is above 18°C.

good_weather = 0
for temp9, rain3 in zip(daily_temperatures, daily_rainfall):
    if temp9 >18 and rain3 <2:
        good_weather = good_weather +1


print(f"The number of days good weather is {good_weather}")
        

