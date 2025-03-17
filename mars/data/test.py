from requests import get, post, delete

# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/999').json())
# # новости с id = 999 нет в базе
# print(get('http://localhost:5000/api/jobs/q').json())
print(post('http://localhost:5000/api/jobs', json={}).json())
# Пустой запрос
print(post('http://localhost:5000/api/jobs',
           json={'id': '1'}).json())
print(post('http://localhost:5000/api/jobs',
           json={'work_size': '15'}).json())
# Введены не все данные
print(post('http://localhost:5000/api/jobs',
           json={'job': 'cabin cleaning',
                 'work_size': '10',
                 'collaborators': '4',
                 'start_date': '2025-03-16 20:39:32',
                 'end_date': '2025-03-16 20:39:32',
                 'is_finished': True,
                 'team_leader': 2}).json())
# Верный запрос, но почему-то он не проходит
# print(delete('http://localhost:5000/api/jobs/999').json())
# # новости с id = 999 нет в базе
# print(delete('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs').json())
