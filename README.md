![CI](https://github.com/MichaelSusiCS/cecs174-water-billing/actions/workflows/python.yml/badge.svg)

Water Billing (Python CLI)

Calculates gallons used and charges for **Residential / Commercial / Industrial** customers.
- Handles input validation and edge cases (e.g., meter rollover).
- Prints a clear usage + cost breakdown.

## Run
```bash
python water_billing.py

python -m py_compile water_billing.py

/bin/bash -s <<'DO'
set -euo pipefail

# === EDIT THIS to the real path of your file ===
FILE="$HOME/Downloads/cs174_proj2.py"
# ===============================================

REPO="cecs174-water-billing"
DESC="Water utility billing calculator (Python CLI) — CSULB Intro to Programming"

# 0) Make a dev folder and create (or clone) the repo
mkdir -p "$HOME/dev" && cd "$HOME/dev"
if ! gh status >/dev/null 2>&1; then echo "❌ Run: gh auth login"; exit 1; fi
gh repo create "$REPO" --public --clone || git clone "https://github.com/$(gh api user -q .login)/$REPO.git"
cd "$REPO"

# 1) Hygiene
printf "__pycache__/\n*.pyc\n.venv/\n.env\n.ipynb_checkpoints/\n" > .gitignore
: > requirements.txt

# 2) Add your code (rename nicely)
[ -f "$FILE" ] || { echo "❌ Can't find: $FILE"; exit 1; }
cp "$FILE" water_billing.py

# 3) README (no code fences to avoid shell confusion)
cat > README.md <<'MD'
# Intro to Programming — Water Billing (Python CLI)

Calculates gallons used and charges for Residential / Commercial / Industrial customers.
- Handles input validation and meter rollover edge cases.
- Prints a clear usage + cost breakdown.

## Run
python water_billing.py

## Test (syntax only)
python -m py_compile water_billing.py

## What I practiced
Conditionals, arithmetic, input validation, and CLI UX.
