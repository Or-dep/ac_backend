from flask_restful import Resource
from models.mod_produtos import Molde_itens_Model
import sqlite3

'''
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