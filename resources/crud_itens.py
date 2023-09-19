from flask_restful import Resource, reqparse
from models.mod_produtos import Molde_itens_Model
import sqlite3

'''
def normalize_path_params(Nome_do_Item=None,
                          Quantidade_min=0,
                          Quantidade_max=10000,
                          limit=50,
                          offiset=0,**data):
    if Nome_do_Item:
        return{
            'Quantidade_min': Quantidade_min,
            'Quantidade_max': Quantidade_max,
            'Nome_do_Item': Nome_do_Item,
            'limit': limit,
            'offiset': offiset}
    return{
        'Quantidade_min': Quantidade_min,
        'Quantidade_max': Quantidade_max,
        'limit': limit,
        'offiset': offiset}

path_params = reqparse.RequestParser()
path_params.add_argument('Nome_do_Item', type=str)
path_params.add_argument('Quantidade_min', type=float)
path_params.add_argument('Quantidade_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offiset', type=float)


molde_itens = [{
    'T_Item': '',
    'Nome_do_Item': '',
    'Quantidade': '',
    'Local': ''
    }]


class listagem_item(Resource):
    def get(self):
        
        connection = sqlite3.connect('bank.db')
        cursor = connection.cursor()

        bc_av = path_params.parse_args()
        validar = {chv:bc_av[chv] for chv in bc_av if bc_av[chv] is not None}
        # ^^^^recusa dados nulos^^^^
        vl = normalize_path_params(**validar)

        if not vl.get('Nome_do_Item'):
            consulta01 ="SELECT * FROM Produtos \
                        WHERE (Quantidade > ? AND Quantidade < ?)\
                        LIMIT ? OFFSET ?"
            tt = tuple([vl[chv] for chv in vl])
            resultado = cursor.execute(consulta01, tt)
        else:
            consulta01 ="SELECT * FROM Produtos \
                        WHERE (Quantidade > ? AND Quantidade < ?)\
                        and Nome_do_Item = ? LIMIT ? OFFSET ?"
            tt = tuple([vl[chv] for chv in vl])
            resultado = cursor.execute(consulta01, tt)

        results = []
        for rs in resultado:
            results.append({
                'T_Item': rs[0],
                'Nome_do_Item': rs[1],
                'Quantidade': rs[2],
                'Local': rs[3]
            })
        
        return {"produtos": [itens.json() for itens in Molde_itens_Model.query.all()]}'''
    

class listagem_item(Resource):
    def get(self):
        return {"produtos": [itens.json() for itens in Molde_itens_Model.query.all()]}

class metodos(Resource):

    argument = reqparse.RequestParser()
    argument.add_argument('Nome_do_Item', type=str, required=True, help="O campo 'Nome_do_Item' não pode ficar vazio" )
    argument.add_argument('Quantidade', type=float, required=True, help="O campo 'Quantidade' não pode ficar vazio")
    argument.add_argument('Local', type=str)

    
    def get(self, T_Item): # busca item

        find = Molde_itens_Model.busca(T_Item)

        if find:
            return find.json()
        return {'message': 'not found.'}, 404 #


    def post(self, T_Item): # cria novo item
        if Molde_itens_Model.busca(T_Item):
            return {'message': 'Esse item já existe!'}, 400
        
        data = metodos.argument.parse_args()

        lista_itens = Molde_itens_Model(T_Item, **data)
        
        try:
            lista_itens.save_bd()
        except:
            return {'message': 'Algo não saiu como esperado tente novamente'}, 500

        return lista_itens.json()


    def put(self, T_Item): # cria novo item ou edita

        data = metodos.argument.parse_args()

        atualizar = Molde_itens_Model.busca(T_Item)
        if atualizar:
            atualizar.update_item(**data)
            try:
                atualizar.save_bd()
            except:
                return {'message': 'Algo não saiu como esperado tente novamente'}, 500
            return atualizar.json(), 200
        
        lista_itens = Molde_itens_Model(T_Item, **data)

        try:
            lista_itens.save_bd()
        except:
            return {'message': 'Algo não saiu como esperado tente novamente'}, 500
        return lista_itens, 201 


    def delete(self, T_Item): # deleta item
        deletar = Molde_itens_Model.busca(T_Item)

        if deletar:
            try:
                deletar.delete_item()
            except:
                return {'message': 'Algo não saiu como esperado tente novamente'}, 500
            return {'message': 'O item foi deletado com sucesso!'}, 200
        
        return {'message': 'O Item não existe!'},404