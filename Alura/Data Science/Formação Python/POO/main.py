from conta import Conta

conta_ze = Conta(1234, "Vitor Hugo", 1254.00, 25000.00)
conta_maria = Conta(1234, "Maria", 100.00, 13000.00)



conta_ze.transferir(350.00, conta_maria)

conta_ze.extrato()
conta_maria.extrato() 