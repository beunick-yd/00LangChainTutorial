# PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert each page into a Document Object.

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

#limitation

#PyPDF library under the hood not good with scanned pdfs

#PDFPlumberLoader
#UnstructuredPDFLoader