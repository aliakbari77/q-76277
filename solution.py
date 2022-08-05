from gettext import find


class FactorHandler:
    
    def __init__(self):
        self.defaultFormat = "yyyy/mm/dd"

        self.timeFormats = ["dd/mm/yyyy", 
                            "dd/yyyy/mm", 
                            "yyyy/mm/dd", 
                            "yyyy/dd/mm", 
                            "mm/yyyy/dd", 
                            "mm/dd/yyyy"]

        self.totalFactor = 0
        self.factors = {}

        self.day = ""
        self.month = ""
        self.year = ""

    def add_factor(self, time_format, time, value):
        findTimeFormat = ""
        
        for i in self.timeFormats:
            if (time_format == i):
                findTimeFormat = i
        if (findTimeFormat == ""):
            print("invalid time format")
            return

        self.totalFactor += 1

        self.formatConverter(time_format, time)
        try:
            self.factors.update({self.totalFactor: {
                "day": self.day,
                "month": self.month,
                "year": self.year,
                "value": value
            }})
            print("factor added successfully")
        except:
            print("An exception occurred")

    def remove_all_factors(self, time_format, time):
        self.formatConverter(time_format, time)
        for i in self.factors:
            if (self.factors[i]["day"] == self.day and
                self.factors[i]["month"] == self.month and
                self.factors[i]["year"] == self.year):
                del self.factors[i]
                self.totalFactor -= 1
                print("deleted factor successfully")
                return
                
    def get_sum(self, time_format, start_time, finish_time):
        self.formatConverter(time_format, start_time)
        startDay = self.day
        startMonth = self.month
        startYear = self.year

        self.formatConverter(time_format, finish_time)
        endDay = self.day
        endMonth = self.month
        endYear = self.year

        sumOfFactors = 0
        for i in self.factors:
            if (self.factors[i]["year"] > startYear and
                self.factors[i]["year"] < endYear):
                sumOfFactors += self.factors[i]["value"]
            else:
                if (self.factors[i]["month"] > startMonth and 
                    self.factors[i]["month"] < endMonth):
                    sumOfFactors += self.factors[i]["value"]
                else:
                    if (self.factors[i]["day"] >= startDay and
                        self.factors[i]["day"] <= endDay):
                        sumOfFactors += self.factors[i]["value"]

        print(sumOfFactors)

    def showFactors(self):
        for i in self.factors:
            print(self.factors[i])
    
    def formatConverter(self, currentFormat, time):
        if (currentFormat == "dd/mm/yyyy"):
            self.day = time[0:2]
            self.month = time[3:5]
            self.year = time[6:]
        elif (currentFormat == "dd/yyyy/mm"):
            self.day = time[0:2]
            self.month = time[8:]
            self.year = time[3:7]
        elif (currentFormat == "yyyy/mm/dd"):
            self.day = time[8:]
            self.month = time[5:7]
            self.year = time[:4]
        elif (currentFormat == "yyyy/dd/mm"):
            self.day = time[5:7]
            self.month = time[8:]
            self.year = time[:4]
        elif (currentFormat == "mm/yyyy/dd"):
            self.day = time[8:]
            self.month = time[0:2]
            self.year = time[3:7]
        elif (currentFormat == "mm/dd/yyyy"):
            self.day = time[3:5]
            self.month = time[0:2]
            self.year = time[6:]
        

fh = FactorHandler()

fh.add_factor("dd/yyyy/mm", "18/1998/03", 23)
fh.add_factor("yyyy/mm/dd", "1998/03/20", 16)
print(fh.totalFactor)
fh.remove_all_factors("yyyy/mm/dd", "1998/03/20")
print(fh.totalFactor)
fh.add_factor("mm/yyyy/dd", "12/1996/23", 20)
print(fh.totalFactor)