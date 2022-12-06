import sys

def txt_importer(path_file):
    lines = []
    
    try:
        with open(path_file, mode='r') as file:
            value = file.name.lower().split('.')[-1]
            if value not in ['txt']:
                print("Formato inválido", file=sys.stderr)

            for line in file.readlines():
                lines.append(line.split('\n')[0])

        return lines

    except:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
