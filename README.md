# prediction_of_cardiovascular_disease
Прогноз наличия сердечно-сосудистого заболевания. (Итоговый проект курса "Машинное обучение в бизнесе")

##### Стек:
- ML: sklearn, pandas, numpy
- API: flask
##### Данные: соревнование - https://mlbootcamp.ru/ru/round/12/sandbox/
##### Описание: Датасет сформирован из 100.000 реальных клинических анализов, и в нём используются признаки, которые можно разбить на 3 группы:

| Объективные признаки  | Результаты измерения                   | Субъективные признаки (0/1) |
|-----------------------|----------------------------------------|-----------------------------|
| Возраст (в днях)      | Артериальное давление верхнее и нижнее | Курение                     |
| Рост                  | Холестерин                             | Употребление Алкоголя       |
| Вес                   | Глюкоза                                | Физическая активность       |
| Пол                   |                                        |                             |

Все показатели даны на момент осмотра.

##### Задача: предсказать по описанию вакансии является ли она фейком или нет (поле fraudulent). Бинарная классификация
##### Модель: [sklearn.tree.DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)


### Запуск
##### Клонируем репозиторий и создаем образ 
```bash
$ git clone https://github.com/koryagin2006/prediction_of_cardiovascular_disease.git
$ cd prediction_of_cardiovascular_disease
$ docker build -t koryagin2006/prediction_of_cardiovascular_disease .
```
##### Запускаем контейнер
```bash
$ docker run -d -p 8180:8180 -p 8181:8181 koryagin2006/prediction_of_cardiovascular_disease
```
##### Переходим на [localhost:8181](172.0.0.1:8181)
