def bool_desc(test) -> str:
    if test:
        return 'Sim'
    return 'Não'


txt = input('Informe algo qualquer: ')

print("""
O tipo primitivo desse valor é {}
Só tem espaços? {}
É um numero? {}
É alfabético? {}
É alfanumérico? {}
Está em maiúsculas? {}
Está em minúsculas? {}
Está capitalizada? {}
""".format(
    type(txt),
    bool_desc(txt.isspace()),
    bool_desc(txt.isnumeric()),
    bool_desc(txt.isalpha()),
    bool_desc(txt.isalnum()),
    bool_desc(txt.isupper()),
    bool_desc(txt.islower()),
    bool_desc(txt.istitle())
))
