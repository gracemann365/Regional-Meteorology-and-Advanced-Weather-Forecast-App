from inspect import currentframe
import json
from pickle import FRAME
from this import d
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

'''functions starts'''

def getWeather():
    city=textfield.get()
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city) #an location point is returned
    
    obj=TimezoneFinder()#used to convert into lat and long
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I : %M %p")
    clock.config(text=current_time)
    
    #weather
    #api="https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=a79d95aa5fe266fdc97cac3b952fd08d"
    api = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data = requests.get(api).json()
    
    
    #current 
    temp=json_data['current']['temp']
    print(temp)
    
    Humidity=json_data['current']['humidity']
    print(Humidity)
    
    Pressure=json_data['current']['pressure']
    print(Pressure)
    
    
    Wind_Speed=json_data['current']['wind_speed']
    print(Wind_Speed)
    
    
    Description=json_data['current']['weather'][0]['description']
    print(Description)
    
    #configuring
    t.config(text=(temp,"°C"))
    
    h.config(text=(Humidity,"%"))
     
    p.config(text=(Pressure,"hPa"))
      
    w.config(text=(Wind_Speed,"m/s"))
       
    d.config(text=Description)
    
    
    #configuring the LABELS of cells bottom
    
    
    
    #DAYS
    current= datetime.now()
    currentday.config(text=current.strftime("%A"))
    
    first= current + timedelta(days=1)
    firstday.config(text=first.strftime("%A"))
    
    second= current + timedelta(days=2)
    secondday.config(text=second.strftime("%A"))
    
    third= current + timedelta(days=3)
    thirdday.config(text=third.strftime("%A"))
    
    fourth= current + timedelta(days=4)
    fourthday.config(text=fourth.strftime("%A"))
    
    
    five= current + timedelta(days=5)
    fifthday.config(text=five.strftime("%A"))
    
    #cell images
    
    current_day_image=json_data['daily'][0]['weather'][0]['icon']
    photo0= ImageTk.PhotoImage(file=f"C:/Users/Gracemann365/Desktop/Python$/Regional-Meteorology-and-Advanced-Weather-Forecast-App/icons/{current_day_image}@2x.png")
    currentimage.config(image=photo0)
    currentimage.image=photo0
    
    '''   -- temp : current  night and day--  '''
    tempcurrentday=json_data['daily'][0]['temp']['day']
    tempcurrentnight=json_data['daily'][0]['temp']['night']
    
    current_day_temp.configure(text=f"Day:{tempcurrentday}°C\n\n Night:{tempcurrentnight}°C")
    '''   -- temp : current  night and day--  '''
    
    first_day_image=json_data['daily'][1]['weather'][0]['icon']
    photo1= Image.open(f"C:/Users/Gracemann365/Desktop/Python$/Regional-Meteorology-and-Advanced-Weather-Forecast-App/icons/{first_day_image}@2x.png")
    rezized_photo1=photo1.resize((70,70))
    photo_1=ImageTk.PhotoImage(rezized_photo1)
    firstimage.config(image=photo_1)
    firstimage.image=photo_1
    
    '''   -- weather desc d1 --  '''
    desday1=json_data['daily'][1]['weather'][0]['description']
    firstDes.configure(text=desday1)
    '''   -- weather desc d1 --  '''
    
    
    second_day_image=json_data['daily'][2]['weather'][0]['icon']
    photo2= Image.open(f"C:/Users/Gracemann365/Desktop/Python$/Regional-Meteorology-and-Advanced-Weather-Forecast-App/icons/{second_day_image}@2x.png")
    rezized_photo2=photo2.resize((70,70))
    photo_2=ImageTk.PhotoImage(rezized_photo2)
    secondimage.config(image=photo_2)
    secondimage.image=photo_2
    
    '''   -- weather desc d2 --  '''
    desday2=json_data['daily'][2]['weather'][0]['description']
    secondDes.configure(text=desday2)
    '''   -- weather desc d2 --  '''
    
    third_day_image=json_data['daily'][3]['weather'][0]['icon']
    photo3= Image.open(f"C:/Users/Gracemann365/Desktop/Python$/Regional-Meteorology-and-Advanced-Weather-Forecast-App/icons/{third_day_image}@2x.png")
    rezized_photo3=photo3.resize((70,70))
    photo_3=ImageTk.PhotoImage(rezized_photo3)
    thirdimage.config(image=photo_3)
    thirdimage.image=photo_3
    
    '''   -- weather desc d3 --  '''
    desday3=json_data['daily'][3]['weather'][0]['description']
    thirdDes.configure(text=desday3)
    '''   -- weather desc d3 --  '''
    
    fourth_day_image=json_data['daily'][4]['weather'][0]['icon']
    photo4= Image.open(f"C:/Users/Gracemann365/Desktop/Python$/Regional-Meteorology-and-Advanced-Weather-Forecast-App/icons/{fourth_day_image}@2x.png")
    rezized_photo4=photo4.resize((70,70))
    photo_4=ImageTk.PhotoImage(rezized_photo4)
    fourthimage.config(image=photo_4)
    fourthimage.image=photo_4
    
    '''   -- weather desc d4 --  '''
    desday4=json_data['daily'][4]['weather'][0]['description']
    fourthDes.configure(text=desday4)
    '''   -- weather desc d4 --  '''
    
    fifth_day_image=json_data['daily'][5]['weather'][0]['icon']
    photo5= Image.open(f"C:/Users/Gracemann365/Desktop/Python$/Regional-Meteorology-and-Advanced-Weather-Forecast-App/icons/{fifth_day_image}@2x.png")
    rezized_photo5=photo5.resize((70,70))
    photo_5=ImageTk.PhotoImage(rezized_photo5)
    fifthimage.config(image=photo_5)
    fifthimage.image=photo_5
    
    
    '''   -- weather desc d5--  '''
    desday5=json_data['daily'][5]['weather'][0]['description']
    fifthDes.configure(text=desday5)
    '''   -- weather desc d5 --  '''
    



'''functions ends'''


''' design of app starts here '''

#body of the app
root = Tk()
root.title(" Weather Forecast App ")
root.geometry("1080x660")
root.configure(bg="#4285f4")
root.resizable(False,False)

#icon
image_icon=PhotoImage(file=r"C:\Users\Gracemann365\Desktop\Python$\Regional-Meteorology-and-Advanced-Weather-Forecast-App\images\apple-weather.png")
root.iconphoto(False,image_icon)

#widget
box=PhotoImage(file=r"images\widget.png")
Label(root,image=box,bg="#57adff").place(x=30,y=110)

#labels
#temprature
label1=Label(root,text="Temperature",font=('Roboto',11),fg="white",bg="#212120").place(x=50,y=128) 

#Humidity
label2=Label(root,text="Humidity",font=('Roboto',11),fg="white",bg="#212120").place(x=50,y=168) 

#Pressure
label3=Label(root,text="Pressure",font=('Roboto',11),fg="white",bg="#212120").place(x=50,y=208) 

#wind speed
label4=Label(root,text="Wind Speed",font=('Roboto',11),fg="white",bg="#212120").place(x=50,y=248) 

#Description
label5=Label(root,text="Description",font=('Roboto',11),fg="white",bg="#212120").place(x=50,y=288) 


#values labels relayed from api as json
#temprature
t=Label(root,font=('Roboto',11),fg="red",bg="#212120")
t.place(x=200,y=128) 
#Humidity
h=Label(root,font=('Roboto',11),fg="white",bg="#212120")
h.place(x=200,y=168) 
#Pressure
p=Label(root,font=('Roboto',11),fg="white",bg="#212120")
p.place(x=200,y=208)
#windspeed
w=Label(root,font=('Roboto',11),fg="white",bg="#212120")
w.place(x=200,y=248) 
#Description
d=Label(root,font=('Roboto',11),fg="white",bg="#212120")
d.place(x=200,y=288) 



#search bar

search_image=PhotoImage(file=r"images\finder.png")
mySearch=Label(image=search_image,bg="black")
mySearch.place(x=560,y=110)

weat_image=PhotoImage(file=r"images\cloud.png")
weat_label=Label(image=weat_image,bg="#4285f4")
weat_label.place(x=570,y=120)

textfield=tk.Entry(root,justify="center",width=20,font=('Roboto',18,'bold'),
                   bg='#262729',border=0,fg="white")

textfield.place(x=690,y=125)
textfield.focus()

search_icon=PhotoImage(file=r"images\search.png")
myimage_icon=Button(image=search_icon,borderwidth=1,cursor="hand2",
                    bg="#4285f4",command=getWeather)
myimage_icon.place(x=1000,y=111)


#bottom box holder
frame=Frame(root,width=1400,height=280,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes:

firstbox=PhotoImage(file=r"images\box01.png")
Label(frame,image=firstbox,bg="black").place(x=30,y=50)

minibox1=PhotoImage(file=r"images\box02.png")
Label(frame,image=minibox1,bg="black").place(x=350,y=60)

minibox2=PhotoImage(file=r"images\box02.png")
Label(frame,image=minibox2,bg="black").place(x=500,y=60)

minibox3=PhotoImage(file=r"images\box02.png")
Label(frame,image=minibox3,bg="black").place(x=650,y=60)

minibox4=PhotoImage(file=r"images\box02.png")
Label(frame,image=minibox4,bg="black").place(x=800,y=60)

minibox5=PhotoImage(file=r"images\box02.png")
Label(frame,image=minibox5,bg="black").place(x=950,y=60)




#framing the data in those labels of boxes

#current day cell
currentframe=Frame(frame,width=298,height=176,bg="#282829")
currentframe.place(x=30,y=50)



currentday=Label(currentframe,font=("Roboto",16),fg="#fff",bg="#282829")
currentday.place(x=100,y=5)


currentimage=Label(currentframe,bg="#282829")
currentimage.place(x=1,y=1)


current_day_temp=Label(currentframe,font=("Roboto",12,"bold"),fg="white",bg="#282829")
current_day_temp.place(x=100,y=50)




#first day cell 

firstframe=Frame(frame,width=152,height=112,bg="white")
firstframe.place(x=350,y=60)


firstday=Label(firstframe,font=("Roboto",10),fg="#fff",bg="#282829",width=11,height=0)
firstday.place(x=150,y=5)
firstday.pack(ipadx=27,ipady=10)


firstimage=Label(frame,bg="#282829")
firstimage.place(x=365,y=110)

firstDes=Label(frame,bg="#282829",fg="white")
firstDes.place(x=365,y=190)



#second  day cell 
secondframe=Frame(frame,width=112,height=152,bg="#282829")
secondframe.place(x=500,y=60)



secondday=Label(secondframe,font=("Roboto",10),fg="#fff",bg="#282829",width=11,height=0)
secondday.place(x=150,y=5)
secondday.pack(ipadx=27,ipady=10)

secondimage=Label(frame,bg="#282829")
secondimage.place(x=515,y=110)

secondDes=Label(frame,bg="#282829",fg="white")
secondDes.place(x=515,y=190)



#third  day cell 
thirdframe=Frame(frame,width=112,height=152,bg="#282829")
thirdframe.place(x=650,y=60)


thirdday=Label(thirdframe,font=("Roboto",10),fg="#fff",bg="#282829",width=11,height=0)
thirdday.place(x=150,y=5)
thirdday.pack(ipadx=27,ipady=10)

thirdimage=Label(frame,bg="#282829")
thirdimage.place(x=670,y=110)

thirdDes=Label(frame,bg="#282829",fg="white")
thirdDes.place(x=670,y=190)

#fourth  day cell 

fourthframe=Frame(frame,width=112,height=152,bg="#282829")
fourthframe.place(x=800,y=60)


fourthday=Label(fourthframe,font=("Roboto",10),fg="#fff",bg="#282829",width=11,height=0)
fourthday.place(x=150,y=5)
fourthday.pack(ipadx=27,ipady=10)

fourthimage=Label(frame,bg="#282829")
fourthimage.place(x=815,y=110)


fourthDes=Label(frame,bg="#282829",fg="white")
fourthDes.place(x=815,y=190)



#fifth  day cell 

fifthframe=Frame(frame,width=112,height=152,bg="#282829")
fifthframe.place(x=950,y=60)


fifthday=Label(fifthframe,font=("Roboto",10),fg="#fff",bg="#282829",width=11,height=0)
fifthday.place(x=150,y=5)
fifthday.pack(ipadx=27,ipady=10)

fifthimage=Label(frame,bg="#282829")
fifthimage.place(x=965,y=110)

fifthDes=Label(frame,bg="#282829",fg="white")
fifthDes.place(x=965,y=190)






#clock
clock=Label(root,font=("Roboto",30,'bold'),fg="white",bg="#4285f4")
clock.place(x=30,y=20)



#timezone

timezone=Label(root,font=("Roboto",16),fg="white",bg="#4285f4")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Roboto",16),fg="white",bg="#4285f4")
long_lat.place(x=700,y=50)



''' design of app starts end'''

root.mainloop()






