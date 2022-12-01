# Employees Structure

---

### Quickstart


1. Скопировать .envs
```
cp .env.local.dist .env.local
cp .env.local.db.dist .env.local.db
``` 
2. Запустить
```
docker-compose -f docker-compose.local.yml up -d --build
```
3. Создать тестовые данные
```
docker exec -it employees_structure_web python manage.py setup_test_data
```
4. Перейти на http://0.0.0.0:8001