dict_a: dict = {'name':['어벤져스 엔드게임', '씨티 워'], 'type':'히어로 무비'}
print(dict_a)
movie_name = dict_a['name'][0]
print(movie_name, "\n")

dictionary = {'name':'7D 건조 망고', 'type':'당절임', 'ingredient':['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
              'origin':'필리핀'}

print('name:', dictionary['name'])
print('type:', dictionary['type'])
print('ingredient:', dictionary['ingredient'])
print(dictionary['ingredient'][2])
print('origin:' ,dictionary['origin'])

dictionary['name'] = "8D 건조 망고"
print('name:', dictionary['name'])