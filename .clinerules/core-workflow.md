# AI-DLC Core Workflow for handson-manual

## Project-Specific Rules

### CodeLabs / claat Export Rules

When exporting markdown files to HTML using `claat`:

1. **Tool Path**: Use `../tools/bin/claat`
2. **Export**: Run `../tools/bin/claat export <filename>.md` from the markdown file's directory
3. **Rename output directory to `web`** (CRITICAL)

```bash
../tools/bin/claat export xxx.md
rm -rf web
mv xxx web
```

## AI-DLC Workflow

When the user invokes AI-DLC, read and follow the full core workflow from `.kiro/steering/aws-aidlc-rules/core-workflow.md`.

Rule details are at `.aidlc-rule-details/` (symlink to `.kiro/aws-aidlc-rule-details/`).

Start by reading `.aidlc-rule-details/common/process-overview.md`.
