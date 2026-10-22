-- 1. Список всех рецептов (SELECT)
SELECT id, title, cooking_time FROM recipes ORDER BY title;

-- 2. Список всех категорий (SELECT)
SELECT id, name FROM categories ORDER BY name;

-- 3. Поиск быстрых рецептов (WHERE)
SELECT title, cooking_time FROM recipes WHERE cooking_time <= 40 ORDER BY cooking_time;

-- 4. Фильтр по сложности (WHERE)
SELECT title, difficulty FROM recipes WHERE difficulty = 'легко';

-- 5. JOIN: Рецепты с названиями категорий
SELECT r.title, c.name AS category_name 
FROM recipes r 
JOIN categories c ON r.category_id = c.id;

-- 6. JOIN: Рецепты с именами авторов
SELECT r.title, m.name AS author_name 
FROM recipes r 
JOIN members m ON r.author_id = m.id;

-- 7. COUNT: Общее количество рецептов (Агрегатная функция)
SELECT COUNT(*) AS total_recipes FROM recipes;

-- 8. COUNT: Количество рецептов в избранном (Агрегатная функция + WHERE)
SELECT COUNT(*) AS fav_count FROM recipes WHERE is_favorite = 1;

-- 9. GROUP BY: Сколько рецептов в каждой категории (Группировка)
SELECT c.name, COUNT(r.id) AS recipes_count 
FROM categories c 
LEFT JOIN recipes r ON c.id = r.category_id 
GROUP BY c.id, c.name;

-- 10. GROUP BY + HAVING: Категории, где больше 1 рецепта (Фильтрация групп)
SELECT c.name, COUNT(r.id) AS recipes_count 
FROM categories c 
JOIN recipes r ON c.id = r.category_id 
GROUP BY c.id, c.name 
HAVING COUNT(r.id) > 1;
