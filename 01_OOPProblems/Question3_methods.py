"""TIM SOLUTION"""


class Group:
    def __init__(self, name, members=[]):
        self.members = members 

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name not in self.members:
            raise Exception("Member not in group")
        self.members.remove(name)

    def merge(self, group):
        combined_members = self.members + group.members
        new_group = Group("Any Name", combined_members)
        return new_group

    def get_members(self):
        return sorted(self.members)



# g1 = Group("A-Team", ["Tim", "Joe"])
# g1.add("Sally")
# g1.add("Billy")
# members = g1.get_members()
# print(members)

# g1.delete("Joe")
# members = g1.get_members()
# print(members)

# g1.delete("Joe")

g1 = Group("A-Team", ["Tim", "Joe"])
g2 = Group("B-Team", ["Antoine"])
g3 = g1.merge(g2)

print(g3.get_members())

