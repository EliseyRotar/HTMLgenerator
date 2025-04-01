
```markdown
# 🚀 HTMLGenerator  

**Genera pagine HTML dinamiche in pochi secondi!**  

Un semplice ma efficace script Python che trasforma un dizionario di frasi in una pagina HTML pronta all'uso. Perfetto per esercitazioni, template rapidi o come base per progetti più complessi.  

![HTML Generator Demo](https://via.placeholder.com/800x400?text=HTMLGenerator+Demo) *(Puoi sostituire questo placeholder con un'immagine reale del tuo progetto)*  

## 🔥 Funzionalità  

✔ **Generazione automatica di file HTML**  
✔ **Struttura base completa** (head, body, footer)  
✔ **Conversione da dizionario a lista HTML**  
✔ **Footer personalizzabile**  
✔ **Semplice e leggero**  

## 📦 Installazione  

1. **Clona il repository**  
   ```bash
   git clone https://github.com/tuo-username/HTMLGenerator.git
   cd HTMLGenerator
   ```

2. **Esegui lo script**  
   ```bash
   python htmlgenerator.py
   ```

3. **Apri il file generato** (`es01.html`) nel tuo browser preferito!  

## 🛠 Come modificare  

### Aggiungere nuove frasi  
Modifica la lista `dizionario_delle_sciocchezze` nel file `htmlgenerator.py`:  
```python
dizionario_delle_sciocchezze = [
    {
        "autore": "Nuovo Autore",
        "frase": "Nuova frase divertente!"
    }
]
```

### Personalizzare il footer  
Cambia il testo nel parametro della funzione `footer()`:  
```python
file.write(footer("Il Tuo Nome o Messaggio Personalizzato"))
```

## 📄 File generati  
Lo script crea un file `es01.html` con questa struttura:  
```html
<!DOCTYPE html>
<html>
<head>...</head>
<body>
  <h1>test per la pagina HTML</h1>
  <ul>
    <li>Autore: Frase</li>
    ...
  </ul>
  <footer>Copyright 2025 - Sigma Boy</footer>
</body>
</html>
```

## 🤝 Contribuire  
I contributi sono benvenuti! Apri una **issue** o una **pull request** per:  
- Migliorare la struttura HTML  
- Aggiungere nuove funzionalità  
- Correggere bug  

## 📜 Licenza  
Questo progetto è rilasciato sotto licenza **MIT**.  

---

⭐ **Se ti piace il progetto, lascia una stella su GitHub!** ⭐  
```

### Extra:
- Aggiungi una **badge** (es. per la licenza, versione Python, ecc.) in cima al README
- Sostituisci il placeholder con una gif o immagine reale del progetto
- Includi una sezione "Autore" con il tuo nome e link ai social (se vuoi)

Vuoi che aggiunga qualcos'altro? 😊
