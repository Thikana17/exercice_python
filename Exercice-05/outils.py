def convertir_notes(texte):
    try : 
        return int(texte)
    except ValueError:
        return None

