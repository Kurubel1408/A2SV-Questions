class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]

sol = Solution()
print(sol.convertTemperature(36.50))  
print(sol.convertTemperature(122.11))
