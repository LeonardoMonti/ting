def exists_word(word, instance):
    result = []
    occurences = []

    for index, line in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurences.append({"linha": index + 1})

    if len(occurences) > 0:
        result.append({
            "palavra": word,
            "arquivo": instance._data[0]["nome_do_arquivo"],
            "ocorrencias": occurences,
        })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
