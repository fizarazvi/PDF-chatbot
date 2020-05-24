from ElasticServer import ElasticServer


class uploadChunksToES:
    def __init__(self):
        self.__es = ElasticServer()

    def upload(self, chunks, pdfname):
        print(es.createIndex(pdfname))
        for chunk in chunks:
            self.__es.store_records(pdfName, chunk)
