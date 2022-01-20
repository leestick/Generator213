#UKK_2020
import config
import re
from filenames_collect import filenames_collect


def generate_doc(docs_to_generate):
    for item in docs_to_generate:
        print("\nГенерация ",item,"...")
        params = filenames_collect()
        xx='OUT\\'+item+'\\'+item+'_'+config.bik+'_'+ config.date_today + '_'
        doc_count = config.counter_start_from  # счетчик количества созданных документов определенного типа
        while doc_count < config.number_of_doc:
            cc = str(int(doc_count + 1)).zfill(3)  # дополнить счетчик нулями до трех знаков
            fin = open('sys\\'+params[item], 'r', encoding="utf-8")  # in file
            fout = open(xx+cc+'.xml', 'w', encoding="utf-8")  # out file
            for line in fin:
                if '<ИдентифИнфКО>' in line:
                    identificator_str = re.compile('<ИдентифИнфКО>\w+</ИдентифИнфКО>') # pattern
                    if item == 'GOZKO':  # разное строение идентификатора для GOZKO и SKO
                        newline = identificator_str.sub('<ИдентифИнфКО>'+config.year+'_'+config.regn+'_0001_01_00000' + str(cc)+ '</ИдентифИнфКО>',line) # replace matching strings
                        fout.write(newline)
                    else:
                        newline = identificator_str.sub('<ИдентифИнфКО>'+config.year+'_'+config.regn+'_0001_00000' + str(cc)+ '</ИдентифИнфКО>',line) # replace matching strings
                        fout.write(newline)
                elif '<ДатаСооб>' in line:
                    date_str = re.compile('<ДатаСооб>(\w|/)+</ДатаСооб>') # pattern
                    newline = date_str.sub('<ДатаСооб>'+ config.data_for_xml + '</ДатаСооб>',line) # replace matching strings
                    fout.write(newline)
                else:
                    fout.write(line)
            if len(str(doc_count)) <= 2 or 3:
                doc_count+=1
            else:
                None
        fin.close()
        fout.close()

    print("\nВ каталоге OUT создано документов:" + str(config.number_of_doc*len(docs_to_generate)))
