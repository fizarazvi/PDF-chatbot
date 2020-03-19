13.03.2020 <br>
@Ravi - <br>
a. Classes to be included in ENGINES folder <br>
&emsp;&emsp;   1. QueryProcessor.py <br>
&emsp;&emsp;&emsp;&emsp;          Description  -     Driver class for PROCESSOR classes <br>
&emsp;&emsp;&emsp;&emsp;          Called from  -     FLASK code/UI <br>
&emsp;&emsp;&emsp;          Pseudo code: <br>
&emsp;&emsp;&emsp;&emsp;          x = QuesDataToElasticSearch(input query (RAKE), data from database layer (RAKE)) <br>
&emsp;&emsp;&emsp;&emsp;          y = ElasticSearchToEmbeddings(input query (text), x (text)) <br>
&emsp;&emsp;&emsp;&emsp;          return EmbeddingsToQANet(y) <br>
          <br>
b. Classes to be included in PROCESSOR folder <br>
&emsp;&emsp;      1. QuesDataToElasticSearch.py <br>
&emsp;&emsp;&emsp;&emsp;          Input        -       Input Query (RAKE tokens), Data (RAKE tokens) <br>
&emsp;&emsp;&emsp;&emsp;          Output       -       Selected paragraph* (which most probably contains the answer, RAKE tokens) <br>
&emsp;&emsp;      2. ElasticSearchToEmbeddings.py <br>
&emsp;&emsp;&emsp;&emsp;          Input        -       Input Query (normal text) and selected paragraph* (normal text) <br>
&emsp;&emsp;&emsp;&emsp;          Output       -       Query Vector and Set of vectors (obtained from selected paragraph*) <br>
&emsp;&emsp;      3. EmbeddingsToQANet.py <br>
&emsp;&emsp;&emsp;&emsp;          Input        -       Query Vector and Set of vectors (obtained from selected paragraph*) <br>
&emsp;&emsp;&emsp;&emsp;          Output       -       Sentence containing answer (normal text) <br>

<br><br>
20.03.2020 <br>
@Ravi - <br>
a. Setup complete and working in pycharm (earlier I was facing issues with spyder) <br>
b. Downloaded and installed mongodb, elasticsearch server <br>
c. Started with QueryProcessor class <br>

