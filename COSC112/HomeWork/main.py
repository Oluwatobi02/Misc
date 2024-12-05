class Calendar:
    def __init__(self, day, month):
        self.day = day
        self.month = month 
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month

    
class Month(Calendar):
    def __init__(self,day, month, holiday, stone):
        Calendar. __init__(self, day, month)
        
        self.holiday = holiday
        self.stone = stone
        
   


January = Month(range(1,31), 'January', 'MLK Day','Garnet')
February = Month(range(31,59), 'February', 'Valentines Day','Amethyst')
March = Month(range(60,90), 'March', 'St. Patricks Day','Aquamarine')
April = Month(range(91,120), 'April', 'April Fools Day','Diamond')
May = Month(range(121,151), 'May', 'Cinco de Mayo','Emerald')
June = Month(range(152,181), 'June', 'Fathers Day','Pearl')
July = Month(range(182,212), 'July', '4th of July','Ruby')
August = Month(range(213,243), 'August', 'Left Handers Day','Peridot')
September = Month(range(244,273), 'September', 'Labor Day','Sapphire')
October = Month(range(274,304), 'October', 'Halloween','Tourmaline')
November = Month(range(305,334), 'November', 'Thanksgiving','Topaz')
December = Month(range(335,365), 'December', 'Christmas','Tanzanite')



class Test:

    def check_day(day):
        if day in January.day:
            
            print(f"Month:{January.month}, Day:{day} ")
            print(f"Major Holiday: {January.holiday}")
            print(f"Birth Stones: {January.stone}")
        elif day in February.day:
            print(f"Month:{February.month}, Day:{day} ")
            print(f"Major Holiday: {February.holiday}")
            print(f"Birth Stones: {February.stone}")
        elif day in March.day:
            print(f"Month:{March.month}, Day:{day} ")
            print(f"Major Holiday: {March.holiday}")
            print(f"Birth Stones: {March.stone}")
        elif day in April.day:
            print(f"Month:{April.month}, Day:{day} ")
            print(f"Major Holiday: {April.holiday}")
            print(f"Birth Stones: {April.stone}")
        elif day in May.day:
            print(f"Month:{May.month}, Day:{day} ")
            print(f"Major Holiday: {May.holiday}")
            print(f"Birth Stones: {May.stone}")
        elif day in June.day:
            print(f"Month:{June.month}, Day:{day} ")
            print(f"Major Holiday: {June.holiday}")
            print(f"Birth Stones: {June.stone}")
        elif day in July.day:
            print(f"Month:{July.month}, Day:{day} ")
            print(f"Major Holiday: {July.holiday}")
            print(f"Birth Stones: {July.stone}")
        elif day in August.day:
            print(f"Month:{August.month}, Day:{day} ")
            print(f"Major Holiday: {August.holiday}")
            print(f"Birth Stones: {August.stone}")
        elif day in September.day:
            print(f"Month:{September.month}, Day:{day} ")
            print(f"Major Holiday: {September.holiday}")
            print(f"Birth Stones: {September.stone}")
        elif day in October.day:
            print(f"Month:{October.month}, Day:{day} ")
            print(f"Major Holiday: {October.holiday}")
            print(f"Birth Stones: {October.stone}")
        elif day in November.day:
            print(f"Month:{November.month}, Day:{day} ")
            print(f"Major Holiday: {November.holiday}")
            print(f"Birth Stones: {November.stone}")
        elif day in December.day:
            print(f"Month:{December.month}, Day:{day} ")
            print(f"Major Holiday: {December.holiday}")
            print(f"Birth Stones: {December.stone}")



    
    
with open('calendar.txt', 'r') as f:
    line = f.readline()
    while line != '':
        Test.check_day(int(line))
        print(''.center(20, '-'))
        line = f.readline()