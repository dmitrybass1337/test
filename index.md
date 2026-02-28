---
title: Каталог Audi 80 B4 (TrackLine)
---

<style>
  body { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; line-height: 1.55; }
  .card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; margin: 14px 0; }
  .btn {
    display: inline-block; padding: 10px 14px; border-radius: 999px;
    background: #111827; color: #fff; text-decoration: none; font-weight: 600;
  }
  .btn:hover { opacity: .92; }
  .muted { color: #6b7280; }
</style>

## Каталог ходовой Audi 80 B4

Этот репозиторий публикует каталог как сайт на Markdown (эта страница) и включает готовый офлайн‑каталог в HTML.

<div class="card">
  <a class="btn" href="audi80_b4_catalog_OFFLINE.html">Открыть каталог (HTML)</a>
  <div class="muted" style="margin-top:10px;">
    Если обновишь JSON и пересоберёшь HTML, просто закоммить новый <code>audi80_b4_catalog_OFFLINE.html</code> — сайт обновится.
  </div>
</div>

## Как обновлять каталог локально

1) Положи рядом в этой папке:

- `audi80_b4_catalog_marketing.json`
- все `*.jpg`
- `build_audi80_b4_catalog.py`

2) Запусти сборку:

```bash
python build_audi80_b4_catalog.py
```

3) Получится обновлённый `audi80_b4_catalog_OFFLINE.html`.

## Публикация (GitHub Pages / GitLab Pages)

Инструкция — в `README.md`.
