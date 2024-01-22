# Репозиторий домашних работ OTUS
## Домашняя работа №1
TODO
## Домашняя работа №2
TODO
## Домашняя работа №3
В данной домашней работе требуется обеспечить тестовым покрытием код, ранее созданный в рамках домашнего задания №2. А точнее реализовать тестовые сценарии для каждого из ранее разработанных классов:
1. Rectangle;
2. Circle;
3. Square;
4. Triangle.
Для обеспечения тестового покрытия предлагаются следующие варианты тестов (для каждого из классов):
1. позитивный тест;
2. негативный тест:
* попарное тестирование с входными данными априорно приводящие к получению ошибки для классов Rectangle, Triangle. Например, для Rectangle: (-4, -5); (-4, 5); (4, -5); (4, 5);
* тестирование эквивалентных значений (применяем только граничные значения) для классов Circle, Square. Например, для Circle -4; 4.

Реализация тестовых прогонов выполнена средствами:
1. параметризации (файл otus/HW_3/test_classes.py);
2. фикстур (файл otus/HW_3/test_classes_fixtures.py).
