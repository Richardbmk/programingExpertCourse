"""My SOlution"""

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.name = name
        self.members.append(name)

    def delete(self, name):
        self.name = name
        if name not in self.members:
            raise Exception("Member not in group")
        self.members.remove(self.name)

    def get_members(self):
        return sorted(self.members)


g1 = Group("A-Team", ["Tim", "Joe"])
g1.add("Sally")
g1.add("Billy")
members = g1.get_members()
print(members)

g1.delete("Joe")
members = g1.get_members()
print(members)

# g1.delete("Joe")





"""TIM Solution"""
class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)


"""Correction of my SOLUTION"""

class Group:
    def __init__(self, name, members=[]):
        # self.name = name (There no need)
        self.members = members 

    def add(self, name):
        # self.name = name (There no need)
        self.members.append(name)

    def delete(self, name):
        # self.name = name (There no need)
        if name not in self.members:
            raise Exception("Member not in group")
        # self.members.remove(self.name) (What I did)
        self.members.remove(name) # What I should do

    def get_members(self):
        return sorted(self.members)

