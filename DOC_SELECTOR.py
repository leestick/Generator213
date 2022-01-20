__author__ = 'dmitryh'
from FILE_MODIFY import generate_doc


def doc_selector(type_of_doc):
    '''выбор типа генератора'''
    docs_to_generate = []
    if type_of_doc in ('GOZKO','SKO443_01','SKO443_02','SKO443_03','SKO443_11','SKO443_13','SKO443_21','SKO443_23'):
        docs_to_generate.append(type_of_doc)
        generate_doc(docs_to_generate)
    elif type_of_doc == 'SKO':
        docs_to_generate = ('SKO443_01','SKO443_02','SKO443_03','SKO443_11','SKO443_13','SKO443_21','SKO443_23')
        generate_doc(docs_to_generate)
    elif type_of_doc == '*':
        docs_to_generate = ('GOZKO', 'SKO443_01','SKO443_02','SKO443_03','SKO443_11','SKO443_13','SKO443_21','SKO443_23')
        generate_doc(docs_to_generate)
    else:
        print ("Не выбран тип документа, новые документы не созданы.")
