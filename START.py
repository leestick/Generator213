__author__ = 'dmitryh'
import config
from clean_all_xml import clean_all_xml
from DOC_SELECTOR import doc_selector

#очищаем каталоги OUT
clean_all_xml()

type_of_doc=input('\nВведите тип документа (SKO, GOZKO или *):')
number_of_doc=int(input('\nВведите количество документов:'))
if number_of_doc:
    config.number_of_doc = number_of_doc

doc_selector(type_of_doc)

