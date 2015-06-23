line = '01:40:22PM'

hour = line[:2]
end = line[-2:]

if hour == "12" and end == 'AM':
    hour = "00"
elif hour != "12" and end == 'PM':
    hour = str(int(hour)+12)
    
print(hour + line[2:-2])
