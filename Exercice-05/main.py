
from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]



notes = []
notes_ignorees = 0

for texte in notes_brutes:
    note = convertir_note(texte)

    if note is None:
        notes_ignorees += 1
    else:
        notes.append(note)

resultat = moyenne(notes)
resultat_mention = mention(resultat)


print(f"Notes ignorées : {notes_ignorees}")
print(f"Moyenne : {resultat:.2f}")
print(f"Mention : {resultat_mention}")