class Weather:
    def __init__(self, content):
        self.content = content[0]

    def print_info(self):
        #split the date and time
        datetime = self.content["current"]["last_updated"].split()
        date, time = datetime[0], datetime[1]
        if int(time.split(":")[0]) > 12:
            time = f"{time} PM"
        else:
            time = f"{time} AM"

        if "PM" in time:
            print("\nš\t",self.content["location"]["name"])
        else:
             print("\nšļø\t",self.content["location"]["name"])
        print(self.content["location"]["region"],",", self.content["location"]["country"])
        print("===============================================================================") 
        print("š°ļø   Last checked: ", date, ",", time)
        print("āļø   Temperature in Celsius: ", self.content["current"]["temp_c"], "C")
        print("āļø   Temperature in Fahrenheit: ", self.content["current"]["temp_f"], "F")
        print("May I also add it feels like", self.content["current"]["feelslike_c"], "C or ", self.content["current"]["feelslike_f"], "F now\n")