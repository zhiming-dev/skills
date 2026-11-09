# Skills

This repository currently contains one skill, [Research Toolkit](research/SKILL.md). It helps you verify sources, compare evidence, and write research briefs or visual reports.

## How to install

### Install with npx

You need Node.js 22.20.0 or later, npm, and Git. Run this command from the project where you want to use the skill.

```sh
npx skills add https://github.com/zhiming%2Ddev/skills
```

The [skills installer](https://www.npmjs.com/package/skills) fetches Research Toolkit from this repository. If prompted, select Codex or another supported agent and choose an installation scope. Project scope installs the skill for the current project. Global scope makes it available across projects.

### Install manually

For Codex, [download the repository ZIP](https://github.com/zhiming%2Ddev/skills/archive/refs/heads/main.zip) and extract it. Copy the entire `research` folder into `.agents/skills/` in your project or `~/.agents/skills/` in your home directory. Keep `SKILL.md` and all supporting files together.

## How to use

Open your agent in the project where you installed the skill and ask it to use Research Toolkit. In Codex, invoke it with `$research`.

> Use $research to compare three ways to reduce urban heat. Explain where each approach works and cite the evidence.

For PDF reports that use the bundled template, install ReportLab in your Python environment with `pip install reportlab`.

## License

The skill instructions and code use the [MIT License](LICENSE). The fonts use the [SIL Open Font License](research/assets/FontLicense.txt).
