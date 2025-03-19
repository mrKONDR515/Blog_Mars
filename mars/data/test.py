from requests import get, post, delete, put

# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/999').json())
# # новости с id = 999 нет в базе
# print(get('http://localhost:5000/api/jobs/q').json())
# print(post('http://localhost:5000/api/jobs', json={}).json())
# # Пустой запрос
# print(post('http://localhost:5000/api/jobs',
#            json={'id': '1'}).json())
# print(post('http://localhost:5000/api/jobs',
#            json={'work_size': '15'}).json())
# Введены не все данные
# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'cabin cleaning',
#                  'work_size': '10',
#                  'collaborators': '4',
#                  'start_date': '2025-03-16 20:39:32',
#                  'end_date': '2025-03-16 20:39:32',
#                  'is_finished': True,
#                  'team_leader': 2}).json())
# Верный запрос
# print(delete('http://localhost:5000/api/jobs/999').json())
# print(delete('http://localhost:5000/api/jobs/998').json())
# print(delete('http://localhost:5000/api/jobs/997').json())
# print(delete('http://localhost:5000/api/jobs/996').json())
# # работ с такими id нет в базе
# print(delete('http://localhost:5000/api/jobs/1').json())
# # Верный запрос
# print(put('http://localhost:5000/api/jobs/999',
#           json={"job": "Very hard job",
#                 "work_size": 15}).json())
# # работы с такими id нет в базе
# print(put('http://localhost:5000/api/jobs/1', json={}).json())
# # Пустой запрос
# print(put('http://localhost:5000/api/jobs/1',
#           json={"start_date": "20-03-2025 12:00:00"}).json())
# # Неверный формат даты
# print(put('http://localhost:5000/api/jobs/1',
#           json={"job": "Updated job",
#                 "work_size": 20,
#                 "collaborators": "2, 3",
#                 "team_leader": 2,
#                 "start_date": "2025-03-20 12:00:00",
#                 "end_date": "2025-03-20 18:00:00",
#                 "is_finished": False}).json())
# # Верный запрос
print(get('http://localhost:5000/api/jobs').json())
