class Class:

    def __init__(self, department, classNumber, day, startTime, endTime):
        self.department = department
        self.classNumber = classNumber
        self.day = day
        self.startTime = startTime
        self.endTime = endTime


    #We could probably format the time to make it look like an actual time
    def print_class_info(self):
        print("Department: " + str(self.department) + "\nClass Number: " + str(self.classNumber) + "\nDay: " + str(self.day) + "\nStart Time: " + str(self.startTime) + "\nEnd Time: " + str(self.endTime))

dataStructures = Class("CS", "2400", "T/Th", 5.00, 6.45)
MarlonSchedule = dataStructures


