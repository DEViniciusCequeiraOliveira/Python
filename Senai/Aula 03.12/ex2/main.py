with open("documento.txt","r") as doc:
    documentos = doc.readlines()
    documentos.reverse()

with open("documentoInverso.txt", "w") as docInverso:
    for char in documentos:
        docInverso.write(char)
