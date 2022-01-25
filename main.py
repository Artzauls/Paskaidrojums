text = input("Ievadi tekstu: " ) #Lūdzot lietotājam ievadīt tekstu
def deleteCombo(text): #deklarējam funkciju, arguments = teksts
  if text.count("abc")>0: #pārbaudām, vai ir kaut viena kombinācija "abc"
    text = text.replace("abc","") #aizvietojam "abc" ar ""
  else:#pretējā gadījumā
    text = "Meklējamā kombonācija netika atrasta!" #aizvietojam tekstu ar paziņojumu
  print(text) #rezultātu printēsim konsolē
  return text #atgriežam vertību teksts
deleteCombo(text) #Izsaucam funkciju