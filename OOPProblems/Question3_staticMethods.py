class Physics:
    # Write your code here
    @staticmethod
    def calculate_net_force(mass, acceleration):
        if type(mass) not in [int, float] or\
            type(acceleration) not in [int, float] or\
                mass <= 0 or acceleration <= 0:
            return 0.0
        return mass * acceleration

    @staticmethod
    def calculate_acceleration(mass, net_force):
        if type(mass) not in [int, float] or\
            type(net_force) not in [int, float] or\
                mass <= 0 or net_force <= 0:
            return 0.0
        return   net_force / mass

    @staticmethod
    def calculate_mass(net_force, acceleration):
        if type(acceleration) not in [int, float] or\
            type(net_force) not in [int, float] or\
                acceleration <= 0 or net_force <= 0:
            return 0.0
        return net_force / acceleration


net_force = Physics.calculate_net_force(2, 4)
print(net_force)

acceleration = Physics.calculate_acceleration(2.5, 35)
print(acceleration)

mass = Physics.calculate_mass(40, 10)
print(mass)


print(Physics.calculate_net_force(-50, -2))
print(Physics.calculate_acceleration(-5, 10))
print(Physics.calculate_mass(-50, -2))