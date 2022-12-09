import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    instance_list = []
    for i in range(0, len(instance)):
        instance_list.append(instance.search(i))

    if path_file not in instance_list:
        instance.enqueue(path_file)
        file = txt_importer(path_file)

        result = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(file),
            'linhas_do_arquivo': file,
        }

        print(f'{result}', file=sys.stdout)


def remove(instance):
    if not len(instance):
        print('Não há elementos', file=sys.stdout)
        return

    result = instance.dequeue()

    print(f'Arquivo {result} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
