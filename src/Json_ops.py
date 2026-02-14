a= {
  "name": "Jonathan Smith",
  "age": 70,
  "children": [
    {
      "name": "Adam Smith",
      "age": 45,
      "children": [
        {
          "name": "Suzy Smith",
          "age": 20,
          "children": []
        },
        {
          "name": "Clare Smith",
          "age": 18,
          "children": []
        }
      ]
    },
    {
      "name": "Alison Smith",
      "age": 42,
      "children": [
        {
          "name": "Zak Smith",
          "age": 16,
          "children": []
        }
      ]
    },
    {
      "name": "Timmy Smith",
      "age": 40,
      "children": []
    }
  ]
}


def jsonops(d : dict):
  for i, j in d.items():
    if i =='age':
      d[i]+=1
    elif i == 'children' and isinstance(j, list) and j:
      for child in j:
        jsonops(child)
    else: continue
  return d

b= jsonops(a)
print(b)

cents= 167
quarters= cents//25
cents=cents%25
dimes= cents//10
cents%=10

print(cents)
print(f'quarters: {quarters}')
print(f'dimes: {dimes}')
print(f'cents:{cents}')

print(123%10)


