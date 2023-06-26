from pprintpp import pprint as pp
from db.database import Graph


class UsuarioDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.201.211.196:7687',
                        user='neo4j', password='residue-loans-laps')

    def create_usuario(self, usuario):
        return self.db.execute_query('CREATE (u:usuario {nome:$nome, matricula:$matricula, curso:$curso}) RETURN u',
                                     {'nome': usuario['nome'], 'matricula': usuario['matricula'],
                                      'curso': usuario['curso']})

    def read_usuario(self, usuario):
        return self.db.execute_query('MATCH (u:usuario {matricula:$matricula, curso:$curso}) RETURN u',
                                     {'matricula': usuario['matricula'], 'curso': usuario['curso']})

    def update_usuario(self, usuario):
        return self.db.execute_query('MATCH (u:usuario {nome:$nome, matricula:$matricula}) SET u.curso=$curso RETURN u',
                                     {'nome': usuario['nome'], 'matricula': usuario['matricula'],
                                      'curso': usuario['curso']})

    def delete_usuario(self, usuario):
        return self.db.execute_query('MATCH (u:usuario {matricula:$matricula, curso:$curso}) DETACH DELETE u',
                                     {'matricula': usuario['matricula'], 'curso': usuario['curso']})


class ItemDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.201.211.196:7687',
                        user='neo4j', password='residue-loans-laps')

    def create_item(self, item):
        return self.db.execute_query(
            'CREATE (i:item {nome:$nome, codigo:$codigo, categoria:$categoria, especificacao:$especificacao}) RETURN i',
            {'nome': item['nome'], 'codigo': item['codigo'], 'categoria': item['categoria'],
             'especificacao': item['especificacao']})

    def read_item(self, item):
        return self.db.execute_query('MATCH (i:item {codigo:$codigo}) RETURN i',
                                     {'codigo': item['codigo']})

    def update_item(self, item):
        return self.db.execute_query(
            'MATCH (i:item {codigo:$codigo, categoria:$categoria}) SET i.especificacao=$especificacao RETURN i',
            {'codigo': item['codigo'], 'categoria': item['categoria'], 'especificacao': item['especificacao']})

    def delete_item(self, item):
        return self.db.execute_query('MATCH (i:item {codigo:$codigo, categoria:$categoria}) DETACH DELETE i',
                                     {'codigo': item['codigo'], 'categoria': item['categoria']})


class PrateleiraDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://3.232.134.248:7687',
                        user='neo4j', password='hum-subject-hat')

    def create_prateleira(self, prateleira):
        return self.db.execute_query('CREATE (p:prateleira {numero:$numero, andar:$andar}) RETURN p',
                                     {'numero': prateleira['numero'], 'andar': prateleira['andar']})

    def read_prateleira(self, prateleira):
        return self.db.execute_query('MATCH (p:prateleira {numero:$numero}) RETURN p',
                                     {'numero': prateleira['numero']})

    def update_prateleira(self, prateleira):
        return self.db.execute_query('MATCH (p:prateleira {numero:$numero}) SET p.andar=$andar RETURN p',
                                     {'numero': prateleira['numero'], 'andar': prateleira['andar']})

    def delete_prateleira(self, prateleira):
        return self.db.execute_query('MATCH (p:prateleira {numero:$numero, andar:$andar}) DETACH DELETE p',
                                     {'numero': prateleira['numero'], 'andar': prateleira['andar']})


class RelacoesDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.201.211.196:7687',
                        user='neo4j', password='hum-subject-hat')

    def create_relation_usuario_item(self, usuario, item, info):
        return self.db.execute_query(
            'MATCH (u:usuario {matricula:$matricula, curso:$curso}), (i:item {codigo:$codigo}) CREATE (u)-[r:PEGOU {data:$data}]->(i) RETURN u, i, r',
            {'matricula': usuario['matricula'], 'curso': usuario['curso'], 'codigo': item['codigo'],
             'data': info['data']})

    def create_relation_item_prateleira(self, item, prateleira, info):
        return self.db.execute_query(
            'MATCH (i:item {codigo:$codigo}), (p:prateleira {numero:$numero}) CREATE (i)-[r:GUARDADO_EM {data:$data}]->(p) RETURN i, p, r',
            {'codigo': item['codigo'], 'numero': prateleira['numero'], 'data': info['data']})

    def read_relation_usuario_item(self, usuario, item):
        return self.db.execute_query(
            'MATCH (u:usuario {matricula:$matricula, curso:$curso})-[r]->(i:item {codigo:$codigo}) RETURN r',
            {'matricula': usuario['matricula'], 'curso': usuario['curso'], 'codigo': item['codigo']})

    def read_relation_item_prateleira(self, item, prateleira):
        return self.db.execute_query('MATCH (i:item {codigo:$codigo})-[r]->(p:prateleira {numero:$numero}) RETURN r',
                                     {'codigo': item['codigo'], 'numero': prateleira['numero']})

    def update_relation_usuario_item(self, usuario, item, info):
        return self.db.execute_query(
            'MATCH (u:usuario {matricula:$matricula, curso:$curso})-[r:PEGOU]->(i:item {codigo:$codigo}) SET r.data=$data RETURN r',
            {'matricula': usuario['matricula'], 'curso': usuario['curso'], 'codigo': item['codigo'],
             'data': info['data']})

    def update_relation_item_prateleira(self, item, prateleira, info):
        return self.db.execute_query(
            'MATCH (i:item {codigo:$codigo})-[r]->(p:prateleira {numero:$numero}) SET r.data=$data RETURN r',
            {'codigo': item['codigo'], 'numero': prateleira['numero'], 'data': info['data']})

    def delete_relation_usuario_item(self, usuario, item):
        return self.db.execute_query(
            'MATCH (u:usuario {matricula:$matricula, curso:$curso})-[r:PEGOU]->(i:item {codigo:$codigo}) DELETE r',
            {'matricula': usuario['matricula'], 'curso': usuario['curso'], 'codigo': item['codigo']})

    def delete_relation_item_prateleira(self, item, prateleira):
        return self.db.execute_query(
            'MATCH (i:item {codigo:$codigo})-[r:GUARDADO_EM]->(p:prateleira {numero:$numero}) DELETE r',
            {'codigo': item['codigo'], 'numero': prateleira['numero']})


def divider():
    print('\n' + '-' * 80 + '\n')


while 1:

    op = int(input('1. Usuario\n2. Item\n3. Prateleira\n4. Relações\n5. Sair\n'))

    if op == 1:

        dao = UsuarioDAO()

        while 1:
            option = input('1. Create\n2. Read\n3. Update_Curso\n4. Delete\n5. Voltar\n')

            if option == '1':
                nome = input('Nome: ')
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                usuario = {
                    'nome': nome,
                    'matricula': matricula,
                    'curso': curso
                }
                aux = dao.create_usuario(usuario)
                divider()

            elif option == '2':
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                usuario = {
                    'matricula': matricula,
                    'curso': curso
                }
                aux = dao.read_usuario(usuario)
                pp(aux)
                divider()

            elif option == '3':
                nome = input('Nome: ')
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                usuario = {
                    'nome': nome,
                    'matricula': matricula,
                    'curso': curso
                }
                aux = dao.update_usuario(usuario)
                divider()

            elif option == '4':
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                usuario = {
                    'matricula': matricula,
                    'curso': curso
                }
                aux = dao.delete_usuario(usuario)
                divider()

            else:
                break

        dao.db.close()

    elif op == 2:

        dao = ItemDAO()

        while 1:
            option = input('1. Create\n2. Read\n3. Update_Especificação\n4. Delete\n5. Voltar\n')

            if option == '1':
                nome = input('Nome: ')
                codigo = input('Codigo: ')
                categoria = input('Categoria: ')
                especificacao = input('Especificacao: ')
                item = {
                    'nome': nome,
                    'codigo': codigo,
                    'categoria': categoria,
                    'especificacao': especificacao
                }
                aux = dao.create_item(item)
                divider()

            elif option == '2':
                codigo = input('Codigo: ')
                item = {
                    'codigo': codigo
                }
                aux = dao.read_item(item)
                pp(aux)
                divider()

            elif option == '3':
                codigo = input('Codigo: ')
                categoria = input('Categoria: ')
                especificacao = input('Especificacao: ')
                item = {
                    'codigo': codigo,
                    'categoria': categoria,
                    'especificacao': especificacao
                }
                aux = dao.update_item(item)
                divider()

            elif option == '4':
                codigo = input('Codigo: ')
                categoria = input('Categoria: ')
                item = {
                    'codigo': codigo,
                    'categoria': categoria
                }
                aux = dao.delete_item(item)
                divider()

            else:
                break

        dao.db.close()

    elif op == 3:

        dao = PrateleiraDAO()

        while 1:
            option = input('1. Create\n2. Read\n3. Update_Andar\n4. Delete\n5. Voltar\n')

            if option == '1':
                numero = input('Numero: ')
                andar = input('Andar: ')
                prateleira = {
                    'numero': numero,
                    'andar': andar
                }
                aux = dao.create_prateleira(prateleira)
                divider()

            elif option == '2':
                numero = input('Numero: ')
                prateleira = {
                    'numero': numero
                }
                aux = dao.read_prateleira(prateleira)
                pp(aux)
                divider()

            elif option == '3':
                numero = input('Numero: ')
                andar = input('Andar: ')
                prateleira = {
                    'numero': numero,
                    'andar': andar
                }
                aux = dao.update_prateleira(prateleira)
                divider()

            elif option == '4':
                numero = input('Numero: ')
                andar = input('Andar: ')
                prateleira = {
                    'numero': numero,
                    'andar': andar
                }
                aux = dao.delete_prateleira(prateleira)
                divider()

            else:
                break

        dao.db.close()

    elif op == 4:

        dao = RelacoesDAO()

        while 1:
            option = input(
                '1. Create_Usuario_Item\n2. Create_Item_Prateleira\n3. Read_Usuario_Item\n4. Read_Item_Prateleira\n5. Update_Usuario_Item\n6. Update_Item_Prateleira\n7. Delete_Usuario_Item\n8. Delete_Item_Prateleira\n9. Voltar\n')

            if option == '1':
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                codigo = input('Codigo: ')
                data = input('Data: ')
                usuario = {
                    'matricula': matricula,
                    'curso': curso
                }
                item = {
                    'codigo': codigo
                }
                info = {
                    'data': data
                }
                aux = dao.create_relation_usuario_item(usuario, item, info)
                divider()

            elif option == '2':
                codigo = input('Codigo: ')
                numero = input('Numero: ')
                data = input('Data: ')
                item = {
                    'codigo': codigo
                }
                prateleira = {
                    'numero': numero
                }
                info = {
                    'data': data
                }
                aux = dao.create_relation_item_prateleira(item, prateleira, info)
                divider()

            elif option == '3':
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                codigo = input('Codigo: ')
                usuario = {
                    'matricula': matricula,
                    'curso': curso
                }
                item = {
                    'codigo': codigo
                }
                aux = dao.read_relation_usuario_item(usuario, item)
                pp(aux)
                divider()

            elif option == '4':
                codigo = input('Codigo: ')
                numero = input('Numero: ')
                item = {
                    'codigo': codigo
                }
                prateleira = {
                    'numero': numero
                }
                aux = dao.read_relation_item_prateleira(item, prateleira)
                pp(aux)
                divider()

            elif option == '5':
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                codigo = input('Codigo: ')
                data = input('Data: ')
                usuario = {
                    'matricula': matricula,
                    'curso': curso
                }
                item = {
                    'codigo': codigo
                }
                info = {
                    'data': data
                }
                aux = dao.update_relation_usuario_item(usuario, item, info)
                divider()

            elif option == '6':
                codigo = input('Codigo: ')
                numero = input('Numero: ')
                data = input('Data: ')
                item = {
                    'codigo': codigo
                }
                prateleira = {
                    'numero': numero
                }
                info = {
                    'data': data
                }
                aux = dao.update_relation_item_prateleira(item, prateleira, info)
                divider()

            elif option == '7':
                matricula = input('Matricula: ')
                curso = input('Curso: ')
                codigo = input('Codigo: ')
                usuario = {
                    'matricula': matricula,
                    'curso': curso
                }
                item = {
                    'codigo': codigo
                }
                aux = dao.delete_relation_usuario_item(usuario, item)
                divider()

            elif option == '8':
                codigo = input('Codigo: ')
                numero = input('Numero: ')
                item = {
                    'codigo': codigo
                }
                prateleira = {
                    'numero': numero
                }
                aux = dao.delete_relation_item_prateleira(item, prateleira)
                divider()

            else:
                break

        dao.db.close()

    else:
        break