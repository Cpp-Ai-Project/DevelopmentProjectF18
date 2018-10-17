from Class import Class
class GroupMember(Class):

    def __init__(self, name, major, classSchedule = []):
        self.name = name
        self.major = major
        self.classSchedule = classSchedule

    def print_schedule(self):
        print("Name: " + str(self.name) + "\nMajor: " + str(self.major))
        print("*** Class Schedule ***")
        c = 0
        for c in range(len(self.classSchedule)):
            self.classSchedule[c].print_class_info()

