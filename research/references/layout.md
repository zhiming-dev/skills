# Visual reports

A compact report can use three pages. Put the question, main result, and primary chart on the first page. Use the second for interpretation, comparisons, and material caveats. Use the third for the case table, method, and source links. When a complete table will not fit legibly, attach the data and state what the report displays.

The bundled template uses a 600 × 790 pt portrait canvas, 34 pt side margins, and 532 pt content width. The header shows the report category and date. The footer shows the page number. Use a neutral background, consistent alignment, and clear spacing. Keep sentences intact and check punctuation, awkward wraps, and orphan lines in the rendered report.

Use line charts for trends, bars for comparisons, and tables for exact values. Label axes, units, groups, and denominators directly. Use color alongside text or symbols. Keep bars proportional and label any calculated ranges. Where financial results use green for gains and red for losses, state the metric and its sign. Use a neutral series for changes in rates unless the color has an explicitly stated meaning.

## PDF helper

Use Python with ReportLab and add the resolved `scripts` folder to the import path. Choose fonts appropriate to the language. The bundled font covers simplified Chinese and Latin text. Header, footer, charts, links, and text use coordinates measured in points from the top left.

```python
from report_core import Report

report = Report("report.pdf", title="Research findings", date="YYYY.MM.DD")
report.header()
report.text("Research findings", 34, 94, size=22, bold=True)
```

Add the actual findings and computed figures. Call `footer(page, total)` on each page and `next_page()` between pages. Call `save(expected_pages=total)` at the end. The count bar accepts a `count_suffix` argument so its labels can match the report language. Render and inspect every page before delivering.
