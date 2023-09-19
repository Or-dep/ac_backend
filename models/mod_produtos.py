from sql_alchemy import bd

class Molde_itens_Model(bd.Model):
    __tablename__ = 'Produtos'

    T_Item = bd.Column(bd.String(51), primary_key=True)
    Nome_do_Item = bd.Column(bd.String(100))
    Quantidade = bd.Column(bd.Float(precision=1))
    Local = bd.Column(bd.String(51))

    def __init__(self, T_Item, Nome_do_Item, Quantidade, Local):
        self.T_Item = T_Item
        self.Nome_do_Item = Nome_do_Item
        self.Quantidade = Quantidade
        self.Local = Local

    def json(self):
        return {
            'T_Item': self.T_Item,
            'Nome_do_Item': self.Nome_do_Item,
            'Quantidade': self.Quantidade,
            'Local': self.Local
        }
    
    @classmethod
    def busca(cls, T_Item):
        verificar = cls.query.filter_by(T_Item=T_Item).first()
        if verificar:
            return verificar
        return None
    

    def save_bd(self):
        bd.session.add(self)
        bd.session.commit()


    def update_item(self, Nome_do_Item, Quantidade, Local):
        self.Nome_do_Item = Nome_do_Item
        self.Quantidade = Quantidade
        self.Local = Local

    
    def delete_item(self):
        bd.session.delete(self)
        bd.session.commit()