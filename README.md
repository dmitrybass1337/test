# Сайт из Markdown (GitHub Pages / GitLab Pages)

В репозитории есть:

- `index.md` — главная страница сайта на Markdown
- `audi80_b4_catalog_OFFLINE.html` — готовый каталог (открывается по ссылке с главной)
- `*.jpg` — картинки каталога
- `_config.yml` — настройки Jekyll (обработка Markdown)
- `.gitlab-ci.yml` — сборка для GitLab Pages

## Вариант 1 — GitHub Pages (проще всего)

### 1) Создай репозиторий на GitHub

- New repository → задай имя (например `audi80-b4-catalog`)
- Public (или Private, если у тебя платный тариф/организация с Pages)

### 2) Перенеси (залей) эту папку в репозиторий

Открой PowerShell в папке проекта и выполни:

```powershell
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

### 3) Включи Pages

- Repository → Settings → Pages
- **Build and deployment**
  - Source: **Deploy from a branch**
  - Branch: **main** / **root**

Через минуту появится ссылка на сайт вида:

- `https://USERNAME.github.io/REPO/`

Главная откроется из `index.md`, а каталог по кнопке ведёт на `audi80_b4_catalog_OFFLINE.html`.

## Вариант 2 — GitLab Pages

Важно: GitLab Pages раздаёт **HTML**, поэтому Markdown нужно “собрать” (Jekyll). Для этого уже добавлен `.gitlab-ci.yml`.

### 1) Создай проект в GitLab

- New project → Blank project → имя проекта

### 2) Запушь файлы

В PowerShell в папке проекта:

```powershell
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://gitlab.com/USERNAME/REPO.git
git push -u origin main
```

### 3) Включи Pages

- Project → Settings → Pages
- Дождись, пока pipeline выполнится (CI/CD → Pipelines)
- После успешной сборки появится URL Pages

### Если у тебя ветка не `main`

В `.gitlab-ci.yml` поменяй:

```yaml
only:
  - main
```

на `master` (или свою ветку).

## Как обновлять каталог

1) Обнови `audi80_b4_catalog_marketing.json` и/или картинки `*.jpg`
2) Пересобери HTML:

```powershell
python build_audi80_b4_catalog.py
```

3) Закоммить и запушь изменения:

```powershell
git add .
git commit -m "Update catalog"
git push
```

Сайт автоматически обновится.
