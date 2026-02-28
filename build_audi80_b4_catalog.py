import json
from pathlib import Path

JSON_FILE = "audi80_b4_catalog_marketing.json"
HTML_FILE = "audi80_b4_catalog_OFFLINE.html"

def build_html():
    # Загружаем данные из JSON
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    model = data.get("model", {})
    parts = data.get("parts", [])

    html = []

    # Шапка HTML + стили
    html.append("<!DOCTYPE html>")
    html.append("<html lang='ru'>")
    html.append("<head>")
    html.append("  <meta charset='UTF-8'>")
    html.append("  <title>TrackLine каталог ходовой Audi 80 B4</title>")
    html.append("  <meta name='viewport' content='width=device-width, initial-scale=1'>")
    html.append("  <style>")
    html.append("""
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:#0f172a;
  color:#e5e7eb;
  margin:0;
  padding:0;
}
header {
  padding:16px 20px;
  background:linear-gradient(90deg,#1e293b,#0f172a);
  border-bottom:1px solid #1f2937;
}
header h1 {
  margin:0;
  font-size:20px;
}
header p {
  margin:4px 0 0;
  font-size:13px;
  color:#9ca3af;
}
.badge-row {
  margin-top:8px;
  font-size:12px;
  color:#a5b4fc;
}
.badge {
  display:inline-block;
  margin-right:8px;
  padding:2px 8px;
  border-radius:999px;
  background:#111827;
  border:1px solid #374151;
}
main {
  padding:16px 10px 40px;
  max-width:1100px;
  margin:0 auto;
}
.model-card {
  background:#111827;
  border-radius:10px;
  padding:12px 14px;
  border:1px solid #1f2937;
  margin-bottom:14px;
  font-size:13px;
}
.model-grid {
  display:flex;
  flex-wrap:wrap;
  gap:10px 24px;
}
.model-grid div {
  min-width:150px;
}
.cta-banner {
  background:#1d283a;
  border-radius:10px;
  padding:10px 14px;
  border:1px solid #374151;
  margin-bottom:14px;
  font-size:13px;
  display:flex;
  flex-wrap:wrap;
  justify-content:space-between;
  align-items:center;
  gap:8px;
}
.cta-main {
  font-weight:600;
  color:#facc15;
}
.cta-pill {
  padding:6px 12px;
  border-radius:999px;
  background:#f97316;
  color:#111827;
  font-weight:600;
  font-size:13px;
  white-space:nowrap;
}
table {
  width:100%;
  border-collapse:collapse;
  font-size:13px;
  background:#020617;
  border-radius:10px;
  overflow:hidden;
}
thead {
  background:#020617;
}
thead th {
  padding:8px 6px;
  text-align:left;
  border-bottom:1px solid #1f2937;
  color:#9ca3af;
  white-space:nowrap;
}
tbody tr:nth-child(even){
  background:#020617;
}
tbody tr:nth-child(odd){
  background:#020617;
}
tbody td {
  padding:7px 6px;
  border-bottom:1px solid #0f172a;
  vertical-align:top;
}
td img {
  width:64px;
  height:64px;
  object-fit:contain;
  border-radius:6px;
  background:#020617;
  border:1px solid #1f2937;
}
.rts-code {
  font-weight:600;
  color:#bfdbfe;
  font-size:13px;
}
.oem {
  color:#e5e7eb;
  font-size:12px;
}
.tag {
  display:inline-block;
  padding:2px 6px;
  border-radius:999px;
  background:#111827;
  border:1px solid #374151;
  font-size:11px;
  margin-right:4px;
  margin-bottom:2px;
}
.buy-pill {
  display:inline-block;
  padding:6px 10px;
  border-radius:999px;
  background:#22c55e;
  color:#052e16;
  font-weight:600;
  font-size:12px;
  text-align:center;
}
.buy-note {
  font-size:11px;
  color:#9ca3af;
  margin-top:4px;
}
.expert-block,
.howto-block,
.positioning-block {
  margin-top:18px;
  background:#020617;
  border-radius:10px;
  border:1px solid #1f2937;
  padding:12px 14px;
  font-size:13px;
}
.expert-block h2,
.howto-block h2,
.positioning-block h2 {
  margin:0 0 6px;
  font-size:14px;
}
.howto-block ol {
  margin:4px 0 0 16px;
  padding:0;
}
.howto-block li {
  margin-bottom:4px;
}
.expert-block ul {
  margin:4px 0 0 16px;
  padding:0;
}
.expert-block li {
  margin-bottom:4px;
}
footer {
  text-align:center;
  font-size:11px;
  color:#6b7280;
  padding:12px 6px 18px;
}
@media (max-width:720px){
  thead {display:none;}
  table, tbody, tr, td {display:block; width:100%;}
  tbody tr {margin-bottom:10px; border:1px solid #111827; border-radius:8px; overflow:hidden;}
  tbody td {border:none; border-bottom:1px solid #0f172a;}
  tbody td:last-child {border-bottom:none;}
}
    """)
    html.append("  </style>")
    html.append("</head>")
    html.append("<body>")

    # Шапка
    title = "TrackLine каталог ходовой Audi 80 B4"
    subtitle = f"{model.get('manufacturer','AUDI')} {model.get('range','80 B4')} · {model.get('engine','2.0 (ABT)')} · {model.get('year','')}"
    html.append("<header>")
    html.append(f"  <h1>{title}</h1>")
    html.append(f"  <p>{subtitle}</p>")
    html.append("  <div class='badge-row'>")
    html.append("    <span class='badge'>Работает офлайн</span>")
    html.append("    <span class='badge'>TrackLine подвеска и рулевое</span>")
    html.append("    <span class='badge'>Специально для СТО и магазинов</span>")
    html.append("  </div>")
    html.append("</header>")

    html.append("<main>")

    # Карточка модели
    html.append("<section class='model-card'>")
    html.append("  <div class='model-grid'>")
    html.append(f"    <div><strong>Производитель:</strong> {model.get('manufacturer','AUDI')}</div>")
    html.append(f"    <div><strong>Модель:</strong> {model.get('range','80 B4 8C2, 8C5')}</div>")
    html.append(f"    <div><strong>Двигатель:</strong> {model.get('engine','2.0 (ABT)')} {model.get('power','')}</div>")
    html.append(f"    <div><strong>Годы:</strong> {model.get('year','')}</div>")
    html.append(f"    <div><strong>Шасси:</strong> {model.get('chassis','8C-R-125 0-')}</div>")
    html.append("  </div>")
    html.append("</section>")

    # CTA-баннер
    html.append("<section class='cta-banner'>")
    html.append("  <div>")
    html.append("    <div class='cta-main'>Подбор детали по ходовой Audi 80 B4 за 30 секунд.</div>")
    html.append("    <div>Найдите строку в таблице и назовите продавцу код TrackLine.</div>")
    html.append("  </div>")
    html.append("  <div class='cta-pill'>Шаг 3: скажите код TrackLine</div>")
    html.append("</section>")

    # Таблица
    html.append("<table>")
    html.append("  <thead>")
    html.append("    <tr>")
    html.append("      <th>Фото</th>")
    html.append("      <th>TrackLine / Деталь</th>")
    html.append("      <th>OEM / Применяемость</th>")
    html.append("      <th>Позиция</th>")
    html.append("      <th>Стр.</th>")
    html.append("      <th>Заказ в 1 шаг</th>")
    html.append("    </tr>")
    html.append("  </thead>")
    html.append("  <tbody>")

    for part in parts:
        rts = part.get("rts", "")
        name = part.get("name", "")
        category = part.get("category", "")
        oem_list = ", ".join(part.get("oem", []))
        notes = part.get("notes", "")
        position = part.get("position", "")
        page = part.get("page", "")
        image_local = part.get("image_local", "")

        img_src = image_local if image_local else ""
        img_alt = f"{name} TrackLine {rts}".strip()

        html.append("    <tr>")
        # Фото
        if img_src:
            html.append(f"      <td><img src='{img_src}' alt='{img_alt}'></td>")
        else:
            html.append("      <td></td>")

        # TrackLine / название
        html.append("      <td>")
        html.append(f"        <div class='rts-code'>{rts}</div>")
        html.append(f"        <div>{name}</div>")
        if category:
            html.append(f"        <div class='tag'>{category}</div>")
        html.append("      </td>")

        # OEM / примечания
        html.append("      <td>")
        if oem_list:
            html.append(f"        <div class='oem'>OEM: {oem_list}</div>")
        if notes:
            html.append(f"        <div class='oem'>Применение: {notes}</div>")
        html.append("      </td>")

        # Позиция
        html.append(f"      <td>{position}</td>")

        # Страница
        html.append(f"      <td>{page}</td>")

        # Заказ
        html.append("      <td>")
        html.append(f"        <div class='buy-pill'>Назовите код TrackLine {rts}</div>")
        html.append("        <div class='buy-note'>Покажите эту строку продавцу или сфотографируйте экран.</div>")
        html.append("      </td>")

        html.append("    </tr>")

    html.append("  </tbody>")
    html.append("</table>")

    # Блок «Как использовать»
    html.append("<section class='howto-block'>")
    html.append("  <h2>Как использовать этот каталог</h2>")
    html.append("  <ol>")
    html.append("    <li><strong>Найдите модель.</strong> Убедитесь, что у клиента Audi 80 B4 2.0 ABT с нужным годом и шасси.</li>")
    html.append("    <li><strong>Выберите деталь по позиции.</strong> Сверьте узел, сторону, OEM и примечания (ГУР, комплект, шасси).</li>")
    html.append("    <li><strong>Назовите код TrackLine.</strong> Сообщите продавцу код из таблицы или покажите экран.</li>")
    html.append("  </ol>")
    html.append("</section>")

    # Экспертный блок
    html.append("<section class='expert-block'>")
    html.append("  <h2>Экспертные рекомендации</h2>")
    html.append("  <ul>")
    html.append("    <li>Меняйте парные элементы (стойки стабилизатора, рычаги, шаровые, наконечники) с обеих сторон оси.</li>")
    html.append("    <li>После работ по рулевому выполняйте регулировку сход-развала.</li>")
    html.append("    <li>Для проверки применяемости всегда сверяйте OEM-номер с оригинальными каталогами VAG.</li>")
    html.append("  </ul>")
    html.append("</section>")

    # Позиционирование
    html.append("<section class='positioning-block'>")
    html.append("  <h2>Позиционирование каталога</h2>")
    html.append("  <p>Офлайн-каталог TrackLine для Audi 80 B4 создан для СТО и магазинов, которые хотят быстрее подбирать детали ходовой и рулевого, снижать количество ошибок и демонстрировать экспертизу по моделям VAG.</p>")
    html.append("</section>")

    html.append("</main>")

    html.append("<footer>")
    html.append("TrackLine · Каталог ходовой Audi 80 B4 · Офлайн-версия для внутреннего использования СТО и магазинов")
    html.append("</footer>")

    html.append("</body>")
    html.append("</html>")

    # Сохраняем HTML
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"Готово: создан файл {HTML_FILE}")

if __name__ == "__main__":
    if not Path(JSON_FILE).exists():
        print(f"Не найден {JSON_FILE}. Проверь имя и расположение файла.")
    else:
        build_html()
