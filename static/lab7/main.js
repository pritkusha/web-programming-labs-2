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
                let tdTitleRus = document.createElement('td');
                let tdTitleOrig = document.createElement('td');
                let tdYear = document.createElement('td');
                let tdActions = document.createElement('td');

                // Заполняем данные
                tdTitleRus.innerText = film.title_ru; // Русское название
                tdTitleOrig.innerHTML = `<i>(${film.title})</i>`; // Оригинальное название курсивом в скобках
                tdYear.innerText = film.year; // Год выпуска

                // Создаем кнопки для редактирования и удаления
                let editButton = document.createElement('button');
                editButton.innerText = 'Редактировать';
                editButton.onclick = () => editFilm(index); // Передаем index в функцию editFilm
                editButton.classList.add('edit-button'); // Добавляем класс для стилизации

                let delButton = document.createElement('button');
                delButton.innerText = 'Удалить';
                delButton.onclick = () => deleteFilm(index, films[index].title_ru); // Функция для удаления
                delButton.classList.add('delete-button'); // Добавляем класс для стилизации

                // Добавляем кнопки в ячейку действий
                tdActions.append(editButton);
                tdActions.append(delButton);

                // Добавляем ячейки в строку
                tr.append(tdTitleRus);
                tr.append(tdTitleOrig);
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

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
    document.getElementById('description-error').innerText = ''; // Очищаем сообщение об ошибке
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: parseInt(document.getElementById('year').value), // Преобразуем в число
        description: document.getElementById('description').value
    };

    // Проверки на фронтенде
    const errors = {};

    // Проверка русского названия
    if (!film.title_ru) {
        errors.title_ru = 'Русское название не должно быть пустым';
    }

    // Проверка оригинального названия
    if (!film.title && !film.title_ru) {
        errors.title = 'Оригинальное название не должно быть пустым, если русское название пустое';
    }

    // Проверка года
    if (isNaN(film.year) || film.year < 1895 || film.year > new Date().getFullYear()) {
        errors.year = `Год должен быть от 1895 до ${new Date().getFullYear()}`;
    }

    // Проверка описания
    if (!film.description) {
        errors.description = 'Описание не должно быть пустым';
    } else if (film.description.length > 2000) {
        errors.description = 'Описание не должно превышать 2000 символов';
    }

    // Если есть ошибки, отображаем их
    if (Object.keys(errors).length > 0) {
        document.getElementById('description-error').innerText = errors.description || '';
        return;
    }

    const url = id === '' ? '/lab7/rest-api/films/' : `/lab7/rest-api/films/${id}`;
    const method = id === '' ? 'POST' : 'PUT';

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(film)
    })
    .then(response => {
        if (response.ok) {
            fillFilmList();
            hideModal();
            return {};
        }
        return response.json(); // Если есть ошибка, возвращаем JSON с ошибками
    })
    .then(errors => {
        if (errors.description) {
            document.getElementById('description-error').innerText = errors.description; // Отображаем ошибку
        }
    })
    .catch(error => {
        console.error('Ошибка при отправке данных:', error);
    });
}

function editFilm(index) {
    fetch(`/lab7/rest-api/films/${index}`) // Используем переданный index
        .then(response => response.json())
        .then(film => {
            document.getElementById('id').value = index; // Устанавливаем индекс
            document.getElementById('title').value = film.title;
            document.getElementById('title-ru').value = film.title_ru;
            document.getElementById('year').value = film.year;
            document.getElementById('description').value = film.description;
            showModal();
        })
        .catch(error => {
            console.error('Ошибка при загрузке данных для редактирования:', error);
        });
}