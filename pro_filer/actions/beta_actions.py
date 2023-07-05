"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = ''
        for path in context["all_files"]:
            if len(path.split("/")) > len(deepest_file.split("/")):
                deepest_file = "".join(path)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files

context = {
    "all_files": [
        "/home/trybe/Documents/aula/python/tests.txt",
        "/home/trybe/Downloads/trybe_logo_nome_grande_pra_k7.png",
    ]
}

show_deepest_file(context)