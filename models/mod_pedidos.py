from sql_alchemy import bd


class MoldePedidosModel(bd.Model):
    __tablename__ = 'Produtos'


    N_Pedidos = bd.Column(bd.Integer, primary_key=True)
    Status = bd.Column(bd.String(10), primary_key=True)
    Cliente_Id = bd.Column(bd.String(10), primary_key=True)
    Nome_Cliente = bd.Column(bd.String(50), primary_key=True)

    T_Item = bd.Column(bd.Integer, primary_key=True)
    Nome_do_Item = bd.Column(bd.String(100))
    Quantidade = bd.Column(bd.Float(precision=1))

    def __init__(self, N_Pedidos, Status, Cliente_Id, Nome_Cliente, T_Item, Nome_do_Item, Quantidade):
        self.N_Pedidos = N_Pedidos
        self.Status = Status
        self.Cliente_Id = Cliente_Id
        self.Nome_Cliente = Nome_Cliente
        self.T_Item = T_Item
        self.Nome_do_Item = Nome_do_Item
        self.Quantidade = Quantidade

    def json(self):
        return {
            'N_Pedidos': self.N_Pedidos,
            'Status': self.Status,
            'Cliente_Id': self.Cliente_Id,
            'Nome_Cliente': self.Nome_Cliente,
            'T_Item': self.T_Item,
            'Nome_do_Item': self.Nome_do_Item,
            'Quantidade': self.Quantidade,
        }
