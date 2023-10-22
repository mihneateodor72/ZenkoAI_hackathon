import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Esti un roman cu dor de casa."},
    {"role": "user", "content": "Scrie fara diacritice o postare de 2 randuri in care spui despre Romania si cat de frumoasa este."}
  ]
)

print(completion.choices[0].message)

46.99198305897556, 6.930883284260774