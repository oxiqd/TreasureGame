# Detective Cat

**Detective Cat** is a small interactive Python mini-game built with **Streamlit**.

The project was created as a quick introduction to Python through a visual and playable application.  
The player searches for a hidden artifact on a 5×5 board. After each move, the game gives a hint based on how close the selected cell is to the artifact.

---

## English

## Project Goal

The main goal of this project is to get familiar with Python by building a small finished application, not by studying the whole language in advance.

This project demonstrates:

- basic Python syntax;
- functions;
- constants;
- conditions;
- tuples;
- sets;
- random values;
- simple game state;
- UI rendering with Streamlit;
- user interaction through buttons;
- session state management.

---

## Tech Stack

- **Python**
- **Streamlit**

---

## What Is Streamlit?

**Streamlit** is a Python framework for building simple interactive web applications.

Instead of writing HTML, CSS, and JavaScript manually, Streamlit allows the developer to create UI elements directly from Python code.

For example:

```python
st.title("Detective Cat")
st.button("New game")
st.progress(0.5)
```

Streamlit converts these Python commands into a web interface that runs in the browser.

This makes Streamlit useful for:

- small dashboards;
- data visualization;
- prototypes;
- internal tools;
- educational projects;
- quick interactive apps;
- small games and experiments.

In this project, Streamlit is used to render the entire game interface: title, rules, buttons, board, hints, progress bar, messages, and game status.

---

## How Streamlit Works in This Project

Streamlit works differently from frontend frameworks like React.

In a normal frontend application, the page updates when component state changes.

In Streamlit, when the user interacts with the app, the Python script is usually rerun from top to bottom.  
To keep data between reruns, Streamlit provides:

```python
st.session_state
```

In this game, `st.session_state` stores the current game state:

```python
st.session_state.artifact_position
st.session_state.visited_cells
st.session_state.moves
st.session_state.found
st.session_state.game_over
st.session_state.message
st.session_state.last_cell
```

Without `st.session_state`, the game would forget the artifact position, visited cells, and move counter after every click.

---

## Game Rules

The player sees a 5×5 board.

One hidden artifact is randomly placed inside one of the cells.

The player clicks cells to search for the artifact.

After each move, the game gives a hint:

- `❄️ Cold` — the artifact is far away;
- `🌤 Warm` — the artifact is nearby;
- `🔥 Hot` — the artifact is very close;
- `💎 Artifact found` — the player found the artifact.

The player has a limited number of moves.

Current limit:

```python
MAX_MOVES = 12
```

The player wins if the artifact is found before the move limit is reached.

The player loses if the move limit is reached before finding the artifact.

---

## Game Symbols

| Symbol | Meaning |
|---|---|
| `⬜` | Unchecked cell |
| `🐾` | Already checked cell |
| `🐈` | Last checked cell |
| `💎` | Found artifact |
| `👻` | Artifact location after game over |

---

## Project Structure

```text
python-treasure-game/
  app.py
  requirements.txt
  README.md
```

### `app.py`

Main application file.

Contains:

- game configuration;
- game state;
- game logic;
- board rendering;
- Streamlit UI.

### `requirements.txt`

Contains project dependencies.

```txt
streamlit
```

### `README.md`

Project documentation.

---

## Main Constants

### `BOARD_SIZE`

```python
BOARD_SIZE = 5
```

Defines the board size.

The game board is 5×5.

### `MAX_MOVES`

```python
MAX_MOVES = 12
```

Defines the maximum number of moves before the game is lost.

---

## Custom Functions

### `start_new_game()`

Creates a new game state.

It resets:

- artifact position;
- visited cells;
- move counter;
- win status;
- game over status;
- message;
- last clicked cell.

It also places the artifact in a random cell.

```python
st.session_state.artifact_position = (
    random.randint(0, BOARD_SIZE - 1),
    random.randint(0, BOARD_SIZE - 1),
)
```

---

### `get_distance(row, col)`

Calculates the distance between the clicked cell and the hidden artifact.

The game uses **Manhattan distance**:

```python
abs(row - artifact_row) + abs(col - artifact_col)
```

This means the distance is counted by rows and columns, not diagonally.

Example:

```text
Clicked cell:  (1, 1)
Artifact cell: (3, 2)

Distance:
abs(1 - 3) + abs(1 - 2) = 2 + 1 = 3
```

---

### `get_hint(distance)`

Converts the distance into a human-readable hint.

Examples:

```python
if distance == 0:
    return "💎 Artifact found!"

if distance == 1:
    return "🔥 Hot! The artifact is very close."

if distance <= 2:
    return "🌤 Warm. You are near the artifact."

return "❄️ Cold. Try another area."
```

---

### `get_rank()`

Returns a final rank based on the number of moves.

Possible ranks:

- `Legendary detective`
- `Sharp investigator`
- `Careful searcher`
- `Lucky cat`

The fewer moves the player uses, the better the rank.

---

### `make_move(row, col)`

Handles the player's move.

This function:

1. checks whether the game is already finished;
2. checks whether the selected cell was already visited;
3. saves the clicked cell;
4. increases the move counter;
5. calculates the distance to the artifact;
6. updates the hint message;
7. checks win condition;
8. checks lose condition.

---

### `get_cell_label(row, col)`

Returns the correct symbol for a cell.

For example:

- unchecked cell → `⬜`;
- visited cell → `🐾`;
- last clicked cell → `🐈`;
- found artifact → `💎`;
- artifact after game over → `👻`.

This function separates board display logic from move handling logic.

---

### `render_game_board()`

Renders the 5×5 board using Streamlit columns and buttons.

Each cell is a Streamlit button.

When the player clicks a cell, the app calls:

```python
make_move(row, col)
st.rerun()
```

`st.rerun()` forces the app to rerun immediately and update the UI.

---

## Streamlit Methods Used

### `st.set_page_config()`

Configures the browser tab.

Used for:

- page title;
- page icon;
- layout.

```python
st.set_page_config(
    page_title="Detective Cat",
    page_icon="🐾",
    layout="centered",
)
```

---

### `st.markdown()`

Renders Markdown or HTML-like content.

In this project, it is used for:

- title;
- subtitle;
- rules block;
- custom text;
- small UI styling.

Some calls use:

```python
unsafe_allow_html=True
```

This allows simple HTML and CSS to be rendered inside Streamlit.

---

### `st.columns()`

Creates a horizontal layout.

Used for:

- message and move counter;
- board rows;
- restart button and checked cells info.

Example:

```python
message_col, moves_col = st.columns([2, 1])
```

---

### `st.metric()`

Displays a highlighted numeric value.

Used for the move counter:

```python
st.metric("Moves", f"{st.session_state.moves} / {MAX_MOVES}")
```

---

### `st.progress()`

Displays a progress bar.

Used to show how many moves have been used:

```python
progress = st.session_state.moves / MAX_MOVES
st.progress(progress)
```

---

### `st.divider()`

Adds a visual separator between sections.

Used to separate:

- game info;
- board;
- result section;
- restart section.

---

### `st.button()`

Creates clickable buttons.

Used for:

- every board cell;
- the `New game` button.

Example:

```python
st.button("New game")
```

Each board cell also receives a unique `key`:

```python
key=f"cell-{row}-{col}"
```

This is required because Streamlit needs to distinguish between many similar buttons.

---

### `st.success()`

Shows a green success message.

Used when the player wins.

```python
st.success(f"You won! Rank: {get_rank()}.")
```

---

### `st.error()`

Shows a red error message.

Used when the player loses.

```python
st.error("Game over. The hidden artifact was not found.")
```

---

### `st.rerun()`

Immediately reruns the Streamlit script.

Used after:

- clicking a board cell;
- starting a new game.

This helps update the interface right after the state changes.

---

### `st.session_state`

Stores data between Streamlit reruns.

Used to keep the game state alive.

Without it, each click would reset the game.

---

## Are There Any Webhooks?

No, this project does **not** use webhooks.

A **webhook** is a mechanism where one service sends an HTTP request to another service when some event happens.

Example:

```text
Payment completed
→ payment provider sends a request to your backend
→ your backend processes the payment event
```

In this project, there are no external services sending requests to the app.

The game only uses local user interactions inside the Streamlit app:

```text
User clicks a button
→ Streamlit updates session state
→ Streamlit reruns the script
→ UI updates
```

So this project uses **Streamlit widgets and session state**, not webhooks.

---

## Local Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd python-treasure-game
```

### 2. Create a virtual environment

For macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open in the browser.

Default local URL:

```text
http://localhost:8501
```

---

## Possible Future Improvements

Possible improvements for the project:

- difficulty levels;
- different board sizes;
- timer;
- score history;
- better visual theme;
- sound effects;
- leaderboard;
- more random events;
- custom cat names;
- deploy to Streamlit Community Cloud.

---

# Русская версия

# Detective Cat

**Detective Cat** — это маленькая интерактивная мини-игра на Python, созданная с помощью **Streamlit**.

Проект сделан как быстрое знакомство с Python через визуальное и игровое приложение.  
Игрок ищет спрятанный артефакт на поле 5×5. После каждого хода игра даёт подсказку, насколько выбранная клетка близка к артефакту.

---

## Цель проекта

Главная цель проекта — познакомиться с Python через небольшое законченное приложение, а не через предварительное изучение всего языка.

В проекте используются:

- базовый синтаксис Python;
- функции;
- константы;
- условия;
- кортежи;
- множества;
- случайные значения;
- простое игровое состояние;
- отрисовка интерфейса через Streamlit;
- взаимодействие пользователя через кнопки;
- хранение состояния через session state.

---

## Технологии

- **Python**
- **Streamlit**

---

## Что такое Streamlit?

**Streamlit** — это Python-фреймворк для быстрого создания простых интерактивных веб-приложений.

Вместо ручного написания HTML, CSS и JavaScript Streamlit позволяет создавать элементы интерфейса прямо из Python-кода.

Например:

```python
st.title("Detective Cat")
st.button("New game")
st.progress(0.5)
```

Streamlit превращает эти Python-команды в веб-интерфейс, который открывается в браузере.

Streamlit часто используют для:

- небольших дашбордов;
- визуализации данных;
- прототипов;
- внутренних инструментов;
- учебных проектов;
- быстрых интерактивных приложений;
- небольших игр и экспериментов.

В этом проекте Streamlit отвечает за весь интерфейс игры: заголовок, правила, кнопки, игровое поле, подсказки, progress bar, сообщения и состояние игры.

---

## Как Streamlit работает в этом проекте

Streamlit работает не так, как frontend-фреймворки вроде React.

В обычном frontend-приложении страница обновляется при изменении состояния компонентов.

В Streamlit при взаимодействии пользователя с приложением Python-файл обычно запускается заново сверху вниз.  
Чтобы данные не терялись между такими перезапусками, Streamlit предоставляет:

```python
st.session_state
```

В этой игре `st.session_state` хранит текущее состояние игры:

```python
st.session_state.artifact_position
st.session_state.visited_cells
st.session_state.moves
st.session_state.found
st.session_state.game_over
st.session_state.message
st.session_state.last_cell
```

Без `st.session_state` игра забывала бы позицию артефакта, нажатые клетки и счётчик ходов после каждого клика.

---

## Правила игры

Игрок видит поле 5×5.

В одной из клеток случайно спрятан артефакт.

Игрок нажимает на клетки, чтобы найти артефакт.

После каждого хода игра даёт подсказку:

- `❄️ Cold` — артефакт далеко;
- `🌤 Warm` — артефакт где-то рядом;
- `🔥 Hot` — артефакт очень близко;
- `💎 Artifact found` — артефакт найден.

У игрока ограниченное количество ходов.

Текущий лимит:

```python
MAX_MOVES = 12
```

Игрок побеждает, если находит артефакт до окончания лимита ходов.

Игрок проигрывает, если лимит ходов закончился, а артефакт не найден.

---

## Обозначения в игре

| Символ | Значение |
|---|---|
| `⬜` | Непроверенная клетка |
| `🐾` | Уже проверенная клетка |
| `🐈` | Последняя выбранная клетка |
| `💎` | Найденный артефакт |
| `👻` | Позиция артефакта после проигрыша |

---

## Структура проекта

```text
python-treasure-game/
  app.py
  requirements.txt
  README.md
```

### `app.py`

Главный файл приложения.

Содержит:

- конфигурацию игры;
- состояние игры;
- игровую логику;
- отрисовку поля;
- интерфейс Streamlit.

### `requirements.txt`

Файл с зависимостями проекта.

```txt
streamlit
```

### `README.md`

Документация проекта.

---

## Основные константы

### `BOARD_SIZE`

```python
BOARD_SIZE = 5
```

Определяет размер игрового поля.

Поле игры — 5×5.

### `MAX_MOVES`

```python
MAX_MOVES = 12
```

Определяет максимальное количество ходов до проигрыша.

---

## Пользовательские функции

### `start_new_game()`

Создаёт новое состояние игры.

Функция сбрасывает:

- позицию артефакта;
- проверенные клетки;
- счётчик ходов;
- статус победы;
- статус проигрыша;
- сообщение;
- последнюю выбранную клетку.

Также функция размещает артефакт в случайной клетке.

```python
st.session_state.artifact_position = (
    random.randint(0, BOARD_SIZE - 1),
    random.randint(0, BOARD_SIZE - 1),
)
```

---

### `get_distance(row, col)`

Считает расстояние между выбранной клеткой и спрятанным артефактом.

Игра использует **манхэттенское расстояние**:

```python
abs(row - artifact_row) + abs(col - artifact_col)
```

Это значит, что расстояние считается по строкам и столбцам, без диагонали.

Пример:

```text
Выбранная клетка:  (1, 1)
Клетка артефакта:  (3, 2)

Расстояние:
abs(1 - 3) + abs(1 - 2) = 2 + 1 = 3
```

---

### `get_hint(distance)`

Преобразует расстояние в понятную подсказку.

Примеры:

```python
if distance == 0:
    return "💎 Artifact found!"

if distance == 1:
    return "🔥 Hot! The artifact is very close."

if distance <= 2:
    return "🌤 Warm. You are near the artifact."

return "❄️ Cold. Try another area."
```

---

### `get_rank()`

Возвращает финальный ранг игрока по количеству ходов.

Возможные ранги:

- `Legendary detective`
- `Sharp investigator`
- `Careful searcher`
- `Lucky cat`

Чем меньше ходов использовано, тем выше ранг.

---

### `make_move(row, col)`

Обрабатывает ход игрока.

Функция:

1. проверяет, не закончена ли уже игра;
2. проверяет, не была ли клетка уже выбрана;
3. сохраняет выбранную клетку;
4. увеличивает счётчик ходов;
5. считает расстояние до артефакта;
6. обновляет текст подсказки;
7. проверяет условие победы;
8. проверяет условие проигрыша.

---

### `get_cell_label(row, col)`

Возвращает правильный символ для клетки.

Например:

- непроверенная клетка → `⬜`;
- проверенная клетка → `🐾`;
- последняя выбранная клетка → `🐈`;
- найденный артефакт → `💎`;
- артефакт после проигрыша → `👻`.

Эта функция отделяет логику отображения поля от логики обработки хода.

---

### `render_game_board()`

Отрисовывает поле 5×5 через Streamlit columns и buttons.

Каждая клетка — это Streamlit-кнопка.

Когда игрок нажимает на клетку, приложение вызывает:

```python
make_move(row, col)
st.rerun()
```

`st.rerun()` сразу перезапускает приложение и обновляет интерфейс.

---

## Использованные методы Streamlit

### `st.set_page_config()`

Настраивает вкладку браузера.

Используется для:

- названия страницы;
- иконки страницы;
- layout.

```python
st.set_page_config(
    page_title="Detective Cat",
    page_icon="🐾",
    layout="centered",
)
```

---

### `st.markdown()`

Отрисовывает Markdown или HTML-подобный контент.

В проекте используется для:

- заголовка;
- подзаголовка;
- блока с правилами;
- текста;
- простого UI-стайлинга.

Некоторые вызовы используют:

```python
unsafe_allow_html=True
```

Это позволяет отрисовывать простой HTML и CSS внутри Streamlit.

---

### `st.columns()`

Создаёт горизонтальную раскладку.

Используется для:

- сообщения и счётчика ходов;
- строк игрового поля;
- кнопки рестарта и информации о проверенных клетках.

Пример:

```python
message_col, moves_col = st.columns([2, 1])
```

---

### `st.metric()`

Показывает выделенное числовое значение.

В проекте используется для счётчика ходов:

```python
st.metric("Moves", f"{st.session_state.moves} / {MAX_MOVES}")
```

---

### `st.progress()`

Показывает progress bar.

Используется, чтобы показать, сколько ходов уже потрачено:

```python
progress = st.session_state.moves / MAX_MOVES
st.progress(progress)
```

---

### `st.divider()`

Добавляет визуальный разделитель между блоками.

Используется для разделения:

- игровой информации;
- игрового поля;
- блока результата;
- блока рестарта.

---

### `st.button()`

Создаёт кликабельные кнопки.

Используется для:

- каждой клетки поля;
- кнопки `New game`.

Пример:

```python
st.button("New game")
```

Каждая клетка поля также получает уникальный `key`:

```python
key=f"cell-{row}-{col}"
```

Это нужно, потому что Streamlit должен отличать множество похожих кнопок друг от друга.

---

### `st.success()`

Показывает зелёное сообщение об успешном результате.

Используется при победе:

```python
st.success(f"You won! Rank: {get_rank()}.")
```

---

### `st.error()`

Показывает красное сообщение об ошибке или неудаче.

Используется при проигрыше:

```python
st.error("Game over. The hidden artifact was not found.")
```

---

### `st.rerun()`

Сразу перезапускает Streamlit-скрипт.

Используется после:

- клика по клетке;
- запуска новой игры.

Это нужно, чтобы интерфейс обновился сразу после изменения состояния.

---

### `st.session_state`

Хранит данные между перезапусками Streamlit-скрипта.

Используется, чтобы состояние игры не терялось.

Без него каждый клик сбрасывал бы игру.

---

## Используются ли вебхуки?

Нет, в этом проекте **вебхуки не используются**.

**Webhook** — это механизм, при котором один внешний сервис отправляет HTTP-запрос другому сервису, когда произошло какое-то событие.

Пример:

```text
Оплата завершена
→ платёжный сервис отправляет запрос на backend
→ backend обрабатывает событие оплаты
```

В этом проекте нет внешних сервисов, которые отправляют запросы в приложение.

Игра работает только с локальными действиями пользователя внутри Streamlit-приложения:

```text
Пользователь нажимает кнопку
→ Streamlit обновляет session state
→ Streamlit перезапускает Python-файл
→ интерфейс обновляется
```

То есть этот проект использует **Streamlit widgets и session state**, а не вебхуки.

---

## Локальный запуск

### 1. Склонировать репозиторий

```bash
git clone <repository-url>
cd python-treasure-game
```

### 2. Создать виртуальное окружение

Для macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Для Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить приложение

```bash
streamlit run app.py
```

Приложение откроется в браузере.

Стандартный локальный адрес:

```text
http://localhost:8501
```

---

## Возможные улучшения

Проект можно расширить:

- уровнями сложности;
- разными размерами поля;
- таймером;
- историей результатов;
- улучшенной визуальной темой;
- звуковыми эффектами;
- таблицей лидеров;
- дополнительными случайными событиями;
- кастомными именами кота;
- деплоем на Streamlit Community Cloud.