__author__ = 'dmitryh'
import datetime

# настраиваемые параметры
day_minus = 0  # если необходимо сформировать документы не для текующей даты. При значении "1" будут созданы файлы для вчерашней даты
counter_start_from = 0 # если надо начать порядковый номер документа не с "000"
bik = '047003715'  # в имени создаваемы документов и в идентификаторе
regn = '3349'  # регномер банка в создаваемом идентификаторе
year = '2020'  # год в имени создаваемых документов и в идентификаторе

# служебные параметры:
number_of_doc=1
date_today = (datetime.datetime.today() - datetime.timedelta(days=0)).strftime("%Y%m%d")
data_for_xml = (datetime.datetime.today() - datetime.timedelta(days=0)).strftime("%d/%m/%Y")
