13.03.2020
@Ravi - 
a. Classes to be included in ENGINES folder
     1. QueryProcessor.py
          Description  -     Driver class for PROCESSOR classes
          Called from  -     FLASK code/UI 
          Pseudo code:
                x = QuesDataToElasticSearch(input query (RAKE), data from database layer (RAKE))
                y = ElasticSearchToEmbeddings(input query (text), x (text))
                return EmbeddingsToQANet(y)
          
b. Classes to be included in PROCESSOR folder
     1. QuesDataToElasticSearch.py
          Input        -       Input Query (RAKE tokens), Data (RAKE tokens)
          Output       -       Selected paragraph* (which most probably contains the answer, RAKE tokens)
     2. ElasticSearchToEmbeddings.py
          Input        -       Input Query (normal text) and selected paragraph* (normal text)
          Output       -       Query Vector and Set of vectors (obtained from selected paragraph*)
     3. EmbeddingsToQANet.py
          Input        -       Query Vector and Set of vectors (obtained from selected paragraph*)
          Output       -       Sentence containing answer (normal text)