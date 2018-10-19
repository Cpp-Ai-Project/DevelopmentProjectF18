# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:25:51 2018

@author: user
"""


class Group_1():
    def __init__(self, GroupMemberList=[]):
        self.GoupMemberList = GroupMemberList

    def Meet_up(self, day, time):
        
        for member in self.GoupMemberList:
            
            i = 1 
            for course in member.ClassSchedule:
                if day == course.Day and time >= course.StartTime and time <= course.EndTime:
                    i = 0
            
            if i == 1:
                print(member.Name, " is OK for meet-up.")
    
    def print_members(self):
        for member in self.GoupMemberList:
            member.print_schedule()
                    
                    
class GroupMember():
    def __init__(self, Name, Major, ClassSchedule=[]):
        self.Name = Name
        self.Major = Major
        self.ClassSchedule = ClassSchedule
        
    def print_schedule(self):
        '''  Return members' schedule  '''
        print('\n')
        print("Name: ", self.Name)
        print("Major: ", self.Major)
        print("Class schedule: ")
        for course in self.ClassSchedule:
            course.print_class_info()
        

class Class():   
    
    def __init__(self, Department, ClassNumber, Day, StartTime, EndTime):
        self.Department = Department
        self.ClassNumber = ClassNumber
        self.Day = Day
        self.StartTime = StartTime
        self.EndTime = EndTime
        
    def print_class_info(self):
        '''  Return class information '''
        #return 'The class is {}{}, from {} {} to {}'.format(self.Department, self.ClassNumber, self.Day, self.StartTime, self.EndTime)
        print("The class is " , self.Department, self.ClassNumber, " from ", self.Day, self.StartTime, " to ", self.EndTime)
    
        
'''  Data '''
Course_1 = Class('SE', 5230, 'Monday', 18.00, 21.00)
Course_2 = Class('SE', 5160, 'Wednesday', 18.00, 21.00)
Course_3 = Class('SE', 5130, 'Thursday', 18.00, 21.00)
Course_4 = Class('ECE', 3101, 'Monday', 13.00, 14.15)
Course_5 = Class('ECE', 3101, 'Monday', 14.30, 15.15)
Course_6 = Class('MAT', 2240, 'Wednesday', 18.00, 19.15)

GM_1 = GroupMember('Luke Jiang', 'System Engineering', [Course_1, Course_2, Course_3])
GM_2 = GroupMember('Aaron Zhang', 'ECE', [Course_4, Course_5, Course_6])
GM_3 = GroupMember('Shirley Lin', 'ECE', [Course_4, Course_5, Course_6])

GP = Group_1([GM_1, GM_2, GM_3])






'''  Test  '''
GP.Meet_up('Friday', 18.00)
Class.print_class_info(Course_1)
GroupMember.print_schedule(GM_1)
Group_1.print_members(GP)



#print(help(Class))


