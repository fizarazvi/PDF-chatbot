from ElasticServer import ElasticServer
pdfName = 'pdfname'
es = ElasticServer()
print(es.createIndex(pdfName))
es.store_records(pdfName)
es.get_shard(pdfName)
