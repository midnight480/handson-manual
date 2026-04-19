# Agent Instructions for handson-manual

## Project Overview

This is a hands-on manual documentation site using Google CodeLabs / claat format.

## CodeLabs / claat Export Rules

When exporting markdown files to HTML using `claat`, please follow these specific rules regarding the output directory to maintain project consistency:

1. **Tool Path**: Use the `claat` binary located at `../tools/bin/claat`.
2. **Export Process**: Run the export command from the directory containing the markdown file: `../tools/bin/claat export <filename>.md`.
3. **Directory Renaming**:
   - By default, `claat export` will create a new directory named after the markdown file's Codelab ID.
   - **CRITICAL**: This project requires the final output directory to be named exactly `web`.
   - After running the export, you **MUST** rename the generated directory to `web`.
   - The final structure must be:
     - `web/index.html`
     - `web/css`
     - `web/img/` (if any)

### Example Workflow

```bash
# 1. Run the claat export command
../tools/bin/claat export xxx.md

# 2. Remove the old web directory (if it exists)
rm -rf web

# 3. Rename the newly generated directory 'xxx' to 'web'
mv xxx web
```

## AI-DLC (AI-Driven Development Life Cycle)

When the user invokes AI-DLC, read and follow the AI-DLC adaptive workflow.

The rule details are located at (check in order, use the first that exists):
- `.aidlc-rule-details/` (symlink to `.kiro/aws-aidlc-rule-details/`)
- `.kiro/aws-aidlc-rule-details/`

Start by reading `.aidlc-rule-details/common/process-overview.md` and follow the core workflow defined in `.kiro/steering/aws-aidlc-rules/core-workflow.md`.
