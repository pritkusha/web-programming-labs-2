function fillFilmList() {
    console.log('Загрузка данных...'); // Отладочное сообщение
    fetch('/lab7/rest-api/films/') // Запрос к API
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка загрузки данных');
            }
            return response.json(); // Преобразуем ответ в JSON
        })
        .then(films => {
            console.log('Данные загружены:', films); // Отладочное сообщение
            let tbody = document.getElementById('film-list'); // Получаем элемент tbody
            tbody.innerHTML = ''; // Очищаем таблицу перед заполнением

            // Проходим по всем фильмам и добавляем строки в таблицу
            films.forEach((film, index) => {
                let tr = document.createElement('tr'); // Создаем строку

                // Создаем ячейки для названия, года и действий
                let tdTitle = document.createElement('td');
                let tdYear = document.createElement('td');
                let tdActions = document.createElement('td');

                // Заполняем данные
                tdTitle.innerText = film.title_ru; // Название фильма
                tdYear.innerText = film.year; // Год выпуска

                // Создаем кнопки для редактирования и удаления
                let editButton = document.createElement('button');
                editButton.innerText = 'Редактировать';
                editButton.onclick = () => editFilm(index); // Функция для редактирования

                let delButton = document.createElement('button');
                delButton.innerText = 'Удалить';
                delButton.onclick = () => deleteFilm(index, films[index].title_ru); // Функция для удаления

                // Добавляем кнопки в ячейку действий
                tdActions.append(editButton);
                tdActions.append(delButton);

                // Добавляем ячейки в строку
                tr.append(tdTitle);
                tr.append(tdYear);
                tr.append(tdActions);

                // Добавляем строку в таблицу
                tbody.append(tr);
            });
        })
        .catch(error => {
            console.error('Ошибка:', error); // Выводим ошибку в консоль
        });
}

function deleteFilm(index, title) {
    if(! confirm(`Вы точно хотите удалить фильм "${title}"?`)) // Исправлено
        return;

    fetch(`/lab7/rest-api/films/${index}`, {method: 'DELETE'}) // Исправлено
        .then(function () {
            fillFilmList();
        })
        .catch(error => {
            console.error('Ошибка при удалении фильма:', error);
        });
}