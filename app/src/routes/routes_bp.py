from flask import Blueprint
from controllers.primark_controller import login, index, signin, favoritos, productos, compras, contactenos, evaluar, validarUsuario, registrarUsuario, logout, perfil

routes_bp = Blueprint('', __name__)

routes_bp.route('/', methods=['GET'])(index)
routes_bp.route('/login', methods=['GET'])(login)
routes_bp.route('/signin', methods=['GET'])(signin)
routes_bp.route('/favoritos', methods=['GET'])(favoritos)
routes_bp.route('/productos', methods=['GET'])(productos)
routes_bp.route('/compras', methods=['GET'])(compras)
routes_bp.route('/contactenos', methods=['GET'])(contactenos)
routes_bp.route('/evaluar', methods=['GET'])(evaluar)
routes_bp.route('/validar_usuario', methods=['POST'])(validarUsuario)
routes_bp.route('/registrar_usuario', methods=['POST'])(registrarUsuario)
routes_bp.route('/logout',methods=['GET'])(logout)
routes_bp.route('/perfil', methods=['GET'])(perfil)