from GroupMember import GroupMember
from Class import Class
class Group_2:
    dataStructures = Class("CS", "2400", "T/Th", 5.00, 6.45)
    MarlonSchedule = [dataStructures]
    Marlon = GroupMember("Marlon", "Computer Science", MarlonSchedule)

    #Add Names
    memberslist = [Marlon]

    def __init__(self, members):
        self.memberlist = members

    def print_members(self):
        print(self.memberlist)

    for GroupMember in memberslist:
        GroupMember.print_schedule()
