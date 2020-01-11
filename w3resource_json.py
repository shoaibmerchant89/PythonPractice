print('='.center(100,'='))
print('https://www.w3resource.com/python-exercises/python-json-index.php'.center(100,'-'))
print('='.center(100,'='))

print('\n'+'1'.center(100,'-'))
from json import loads

json_data = '''
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}'''
py_obj = loads(json_data)
print(py_obj['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][1])

print('exercise 18'.center(50,'-'))
def myfunc(*args):
    list1 = []
    for x in args:
        if x % 2 == 0:
            list1.append(x)
    return list1

print(myfunc(5,6,7,8))
