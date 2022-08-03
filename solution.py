from gettext import find


class FactorHandler:
    
    def __init__(self):
        self.timeFormats = ["dd/mm/yyyy", "dd/yyyy/mm", "yyyy/mm/dd", "yyyy/dd/mm", "mm/yyyy/dd", "mm/dd/yyyy"]
        self.totalFactor = 0
        self.factors = {}

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

fh = FactorHandler()

fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
fh.add_factor("yyyy/dd/mm", "05/10/2019", 3)
fh.showFactors()