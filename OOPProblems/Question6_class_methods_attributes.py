"""My solution"""

class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, temperature_kelvin):
        if temperature_kelvin > self.max_temperature or\
            temperature_kelvin < self.min_temperature:
            raise Exception("Invalid temperature.")
        self.temperature_kelvin = temperature_kelvin

    @classmethod
    def update_min_temperature(cls, temperature_kelvin):
        if temperature_kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")

        cls.min_temperature = temperature_kelvin

    @classmethod
    def update_max_temperature(cls, temperature_kelvin):
        if temperature_kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")

        cls.max_temperature = temperature_kelvin

t1 = Temperature(260)
Temperature.update_max_temperature(270)
Temperature.update_min_temperature(680)

