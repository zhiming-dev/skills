# Research Toolkit

Research Toolkit is an agent skill for investigating a question, checking sources, and turning the evidence into a clear answer. It supports literature reviews, comparisons, historical analysis, and reports with charts. It includes dedicated methods for financial event studies and bond scenarios.

## Use in Codex

Copy the [research](research) folder into `.agents/skills` in your project or under your home directory. In Codex, invoke `$research` and state your question, the time period or scope, and the deliverable you need.

> Use $research to compare three approaches to reducing urban heat. Explain the evidence for each approach and where it applies. Create a PDF with a comparison chart and source links.

The bundled PDF helpers require Python and ReportLab. Use `pip install reportlab` in your Python environment if ReportLab is missing. The template includes fonts for simplified Chinese and Latin text. For other scripts, use fonts that cover the requested language.

Code and skill instructions use the [MIT License](LICENSE). The bundled fonts use the [SIL Open Font License](research/assets/FontLicense.txt).
