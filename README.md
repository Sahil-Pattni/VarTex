# VarTex
A CLI tool to generate LaTeX files from a template and a JSON file.

### Usage

---
To run the command, use the following command:

```bash
vartex tex_filename <flag> variable_filename 
```

For example, in the `example` directory, to use the JSON file `variables.json` to generate the LaTeX file `template.tex`:

```bash
vartex example/cover_letter.tex --json variables.json
```