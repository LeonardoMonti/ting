from ting_file_management.file_management import txt_importer


def output_words_found(path_file, word):
    file = txt_importer(path_file)

    if file is not None:
        occurences = []
        for index, line in enumerate(file):
            if word.lower() in line.lower():
                occurences.append({'linha': index + 1})

        if len(occurences) > 0:
            return {
                'palavra': word,
                'arquivo': path_file,
                'ocorrencias': occurences,
            }
    return None


def exists_word(word, instance):
    result = []
    occurences = []

    for index in range(0, len(instance)):
        occurences.append(instance.search(index))

    for path_file in occurences:
        output_file = output_words_found(path_file, word)
        if output_file is not None:
            result.append(output_file)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
