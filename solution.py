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
            print("invalid format")
            return

        self.totalFactor += 1

        self.factors.update({self.totalFactor: {
            "timeFormat": time_format,
            "time": time,
            "value": value
        }})

    def remove_all_factors(self, time_format, time):
        pass

    def get_sum(self, time_format, start_time, finish_time):
        pass

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
        print(self.year, self.month, self.day)

fh = FactorHandler()

fh.formatConverter("dd/mm/yyyy", "02/10/2019")
fh.formatConverter("dd/yyyy/mm", "02/2019/10")
fh.formatConverter("mm/dd/yyyy", "10/02/2019")
fh.formatConverter("mm/yyyy/dd", "10/2019/02")
fh.formatConverter("yyyy/dd/mm", "2019/02/10")
fh.formatConverter("yyyy/mm/dd", "2019/10/02")