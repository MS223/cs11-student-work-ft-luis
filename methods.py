class Time(object):
    def __init__(self, hour, minute, second):
         self.hour = hour
         self.minute = minute
         self.second = second
    def __str__(self):
        return str(self.hour)  + ":" + str(self.minute) + ":" +str(self.second)
    def __add__ (self, other):
        return Time(self.hour + other.hour,self.minute,self.second + other.second)
Time1 = Time(5, 6, 7)
Time2 = Time(8, 9 ,10)
Time3 = Time(11, 12, 13)
print Time1
print Time1 + Time2
print Time1 + Time2 + Time3
# A method is a function inside of a class
