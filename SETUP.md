# GitHub Profile Polish — Execution Guide

## Step 1: Create Profile README Repo

```bash
# Create the special repo (username/username) on GitHub
# Go to: https://github.com/new
# Repo name: IbnuEyni
# Make it PUBLIC
# Check "Add a README file"
# Create repository

# Then replace the README with ours:
cd /tmp
git clone https://github.com/IbnuEyni/IbnuEyni.git
cp ~/Desktop/python/10Acd/github-profile/README.md IbnuEyni/README.md
cd IbnuEyni
git add README.md
git commit -m "feat: add profile README"
git push
```

## Step 2: Update Repo Descriptions & Topics

```bash
# Create a personal access token:
# https://github.com/settings/tokens → Generate new token (classic)
# Scope: repo (full control)
# Copy the token

# Run the update script:
cd ~/Desktop/python/10Acd/github-profile
GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE python3 update_repos.py
```

## Step 3: Pin Your Top 6 Repos

Go to https://github.com/IbnuEyni → "Customize your pins" → Select:

1. **oracle-forge** — Shows benchmark evaluation + context engineering
2. **tenacious-sales-bench** — Shows you can build & publish research artifacts
3. **Conversion-Engine** — Shows end-to-end production system
4. **10Acweek5** — The Ledger (event sourcing + CQRS + MCP)
5. **10Acweek2** — Automaton Auditor (multi-agent + LangGraph)
6. **Roo-Code** — Intent Traceability (TypeScript + middleware hooks)

## Step 4: Profile Settings

Go to https://github.com/settings/profile:

- **Bio**: `Building AI agent systems — evaluation benchmarks, multi-tool orchestration, data pipelines | Python`
- **Company**: `10 Academy`
- **Location**: `Ethiopia`
- **Website**: Your LinkedIn URL or blog
- **Pronouns**: (optional)

## What This Achieves

| Before | After |
|--------|-------|
| 25+ repos with NO DESCRIPTION | Top 8 repos have clear one-line descriptions |
| No profile README | Profile README showcases 6 projects with what/how/why |
| No topics/tags | Repos tagged for discoverability |
| No pinned repos | 6 pinned repos showing range (benchmarks, agents, pipelines, analysis) |
| Generic profile | Bio + stack badges + connect links |
