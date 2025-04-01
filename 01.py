#creare una pagina come quella in streaming nominata es01.html
#ed incollare un paragrafo per dizionario, a partire dalla lista fornita
 
 
#scrivere la frase sotto in un file html
frase = "test per la pagina HTML"
#scrivere
dizionario_delle_sciocchezze = [
    {
        "autore":"Moretti",
        "frase":"non so cosa dire"
    },
    {
        "autore":"ceresoli",
        "frase":"voglio dormire"
    },
    {
        "autore":"zorza",
        "frase":"buongiorno"
    },
    {
        "autore":"elisey",
        "frase":"gennaro miglior prof del mondo"
    },
    {
        "autore":"verde",
        "frase":"Va bene cosi"
    },
    {
        "autore":"greco",
        "frase":"quest'anno promosso"
    }
]
#creiamo il file
file = open("es01.html","w",encoding="UTF-8")
 
#funzione per mettere una frase in un paragrafo
def ScriviParagrafo(frase:str):
    return f"<h1>{frase}</h1>"
 
#creiamo l'head
def intestazione():
    intestazione = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
'''
    return intestazione
 
 
 
 
#footer
def footer(stringa:str = "Sigma Boy"):
    return f"<footer>Copyright 2025 - {stringa}</footer>"
   
#creiamo un elenco delle chiavi dei dizionari
def elenco(iterabile: list[dict]):
    uElenco = '''    <ul>
'''
    for i in dizionario_delle_sciocchezze:
        frase = f'''        <li>{i["autore"]}:{i["frase"]}</li>
'''
        uElenco += frase
    uElenco += "    </ul>"
    return uElenco
 
#creiamo il body
def body():
    testo_finale = f'''
<body>
    {ScriviParagrafo(frase)}
'''
   
 
    testo_finale += f'''{elenco(dizionario_delle_sciocchezze)}
'''
 
   
    return testo_finale + '''</body>
'''
#mettiamo i dati nel file
file.write(intestazione())
file.write(body())
file.write(footer())
#chiudiamo il file
file.close()
 