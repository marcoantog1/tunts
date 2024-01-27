import gspread
import math
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreedsheets'
    ]

creds = ServiceAccountCredentials.from_json_keyfile_name('.\data\secret_key.json')

file = gspread.authorize(creds)
workbook = file.open("Engenharia_de_Software_-_Desafio_[Marco_Antonio_Oliveira_Gonçalves]")
sheet = workbook.sheet1

column = 4
for student in sheet.range('B4:B27'):
  print("Aluno: "+student.value)
  list = sheet.range(f'C{column}:F{column}')
  absence = list[0].value
  print("Numero de faltas: "+absence)

  if int(absence) > 15:
    sheet.update_acell(f'G{column}', 'Reprovado por Falta')
    sheet.update_acell(f'H{column}', '0')
    print("Aluno reprovado por falta\n")

  else:
    grade = math.ceil((int(list[1].value) + int(list[2].value) + int(list[3].value))/30)
    print("Média das 3 notas, dividas por 10 e arredondadas para cima: "+str(grade))

    if grade < 5:
      sheet.update_acell(f'G{column}', 'Reprovado por Nota')
      sheet.update_acell(f'H{column}', '0')
      print("Aluno reprovado por nota\n")

    elif grade >= 5 and grade < 7:
      sheet.update_acell(f'G{column}', 'Exame Final')
      naf = 10 - grade
      sheet.update_acell(f'H{column}', naf*10)
      print("Nota necessária para passar: " +str(naf))
      print("Aluno em exame final\n")

    else:
      sheet.update_acell(f'G{column}', 'Aprovado')
      sheet.update_acell(f'H{column}', '0')
      print("Aluno aprovado\n")

  column +=1