from flask import Flask
from flask_restful import Api
from resources.crud_itens import metodos, listagem_item
from resources.crud_pedidos import Pedido , listagem_pedidos


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


@app.before_request
def criar_banco():
    bd.create_all()


# Produtos
api.add_resource(listagem_item, "/produtos")
api.add_resource(metodos, "/produtos/<string:T_Item>")

# Pedidos
api.add_resource(listagem_pedidos, "/pedidos")
api.add_resource(Pedido, "/pedidos/<string:N_Pedidos>")


if __name__=='__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(debug=True)


# ^^^^ estrutura padrão de inicio de api ^^^^
