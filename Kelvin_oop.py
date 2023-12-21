class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_Kelvin(self):
        return self.suhu

    def get_celcius(self):
        val = (float(suhu)- 273 )
        return val

    def get_reamur(self):
        val = (4/5) * (float(self.suhu) - 273)
        return val

    def get_fahrenheit(self):
        val = (9/5) * (float(self.suhu) - 273) + 32
        return val

# Entry
suhu = input("Masukkan suhu dalam Kelvin: ")
K = Kelvin(float(suhu))
val = K.get_Kelvin()

# Rumus
C = K.get_celcius()
R = K.get_reamur()
F = K.get_fahrenheit()

# Output
print(suhu + " Kelvin sama dengan:")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")