class CuentaBancaria:

    cuentas = []

    def __init__(self, tasa_interés, balance):
        self.tasa_interés = tasa_interés 
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        return self
        
    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}')
        return self
        
    def generar_interés(self):
        if self.balance > 0:
            interés_generado = self.balance * self.tasa_interés
            self.balance += interés_generado
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()


cuenta1 = CuentaBancaria(0.05, 300)
cuenta1.depósito(100).depósito(100).depósito(200).retiro(50).generar_interés().mostrar_info_cuenta()

cuenta2 = CuentaBancaria(0.05, 0)
cuenta2.depósito(500).depósito(100).retiro(200).retiro(100).retiro(50).retiro(100).generar_interés().mostrar_info_cuenta()

cuenta3 = CuentaBancaria(0.05, 50)
cuenta3.retiro(500)

print('---')

CuentaBancaria.mostrar_todas_las_cuentas()

