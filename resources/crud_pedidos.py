from flask_restful import Resource, reqparse
from models.mod_pedidos import MoldePedidosModel

molde_pedidos = [{'N_Pedidos': 'int',
    'Status': 'str',
    'Cliente_Id': 'int',
    'Nome_Cliente': 'str',
    'T_Item': 'int',
    'Nome_do_Item': 'str',
    'Quantidade': 'str'}]


class listagem_pedidos(Resource):
    def get(self):
        return {"pedidos": molde_pedidos}
    

class Pedido(Resource):
    argument = reqparse.RequestParser()
    argument.add_argument('Nome_do_Item')
    argument.add_argument('Status')
    argument.add_argument('Cliente_Id')
    argument.add_argument('T_Item')
    argument.add_argument('Nome_do_Item')
    argument.add_argument('Quantidade')


    def busca(N_Pedidos):
        for vl in molde_pedidos:
            if vl['N_Pedidos'] == N_Pedidos:
                return vl
        return None
    
    def get(self, N_Pedidos): # busca pedido
        find = Pedido.busca(N_Pedidos)
        if find:
            return find
        return {'message': 'not found.'}, 404 #


    def post(self, N_Pedidos): # cria novo pedido

        data = Pedido.argument.parse_args()

        lista_pedidos = MoldePedidosModel(N_Pedidos, **data)
        
        NotaFisca = lista_pedidos.json()

        # NotaFisca = {'N_Pedidos': N_Pedidos, **data}
        
        molde_pedidos.append(NotaFisca)
        return NotaFisca, 200


    def put(self, N_Pedidos): # cria novo item ou edita

        data = Pedido.argument.parse_args()

        lista_pedidos = MoldePedidosModel(N_Pedidos, **data)
        
        NotaFisca = lista_pedidos.json()

        # NotaFisca = {'N_Pedidos': N_Pedidos, **data }

        atualizar = Pedido.busca(N_Pedidos)

        if atualizar:
            atualizar.update(NotaFisca)
            return NotaFisca, 200
        
        molde_pedidos.append(NotaFisca)
        return NotaFisca, 201 


    def delete(self, N_Pedidos): # deleta item

        deletar = Pedido.busca(N_Pedidos)

        if deletar:
            molde_pedidos.remove(deletar)
            return {'message': 'item deletado com sucesso!'}, 200
        
        return {'message': 'Not found'},404
    
        #global nome_da_lista_com_dic # referencia o dicionairo