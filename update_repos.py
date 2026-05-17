#!/usr/bin/env python3
"""
Update GitHub repo descriptions and topics.
Usage: GITHUB_TOKEN=ghp_xxx python3 update_repos.py
"""
import os
import json
import urllib.request
import dotenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("Set GITHUB_TOKEN environment variable first.")
    print("Create one at: https://github.com/settings/tokens (repo scope)")
    exit(1)

OWNER = "IbnuEyni"

# Repo updates: (repo_name, description, homepage_url, topics)
UPDATES = [
    (
        "Roo-Code",
        "Intent-Code Traceability System — middleware hooks that force AI agents to declare intent before writing code. Two-stage state machine + SHA-256 audit trail.",
        "",
        ["ai-agent", "vscode-extension", "typescript", "traceability", "middleware", "langgraph"],
    ),
    (
        "10Acweek2",
        "Automaton Auditor — multi-agent Digital Courtroom for autonomous code auditing. 7 LangGraph agents, dialectical reasoning, $0.02/audit.",
        "",
        ["multi-agent", "langgraph", "code-audit", "python", "groq", "pydantic"],
    ),
    (
        "10AcWeek3",
        "Document Intelligence Refinery — agentic extraction pipeline with multi-strategy routing and confidence-gated escalation.",
        "",
        ["document-extraction", "pdf", "agentic-pipeline", "python", "pydantic", "streamlit"],
    ),
    (
        "10AcWeek4",
        "Brownfield Cartographer — codebase intelligence system that builds knowledge graphs from undocumented repos.",
        "",
        ["static-analysis", "knowledge-graph", "data-lineage", "python", "networkx", "tree-sitter"],
    ),
    (
        "10Acweek5",
        "The Ledger — CQRS/Event Sourcing stack with cryptographic audit chain, MCP server, counterfactual what-if analysis. 166 tests.",
        "",
        ["event-sourcing", "cqrs", "postgresql", "mcp", "python", "audit-trail"],
    ),
    (
        "10AcWeek7",
        "Data Contract Enforcer — schema integrity, violation attribution, and lineage-aware blast radius analysis.",
        "",
        ["data-contracts", "schema-validation", "data-quality", "python", "lineage"],
    ),
    (
        "oracle-forge",
        "Natural language data analytics agent — 3-layer KB injection on DataAgentBench (54 queries, 12 datasets). 35.2% pass@1.",
        "",
        ["ai-agent", "data-analytics", "benchmark", "context-engineering", "python", "gemini"],
    ),
    (
        "Conversion-Engine",
        "Automated lead generation & conversion system — 5-signal enrichment, ICP classification, multi-channel outreach, CRM sync.",
        "",
        ["ai-agent", "sales-automation", "fastapi", "lead-generation", "python", "crm"],
    ),
    (
        "tenacious-sales-bench",
        "Domain-specific benchmark for B2B sales agents — 250 tasks, SimPO judge model, published on HuggingFace.",
        "https://huggingface.co/datasets/shuaibam/tenacious-bench-v0.1",
        ["benchmark", "evaluation", "sales-agent", "simpo", "huggingface", "python"],
    ),
    (
        "Project_Chimera_AI-agent_Infrastructure-Challenge-",
        "Autonomous AI agent swarm infrastructure — hierarchical coordination of 10K+ agents with zero-trust security.",
        "",
        ["ai-agent", "swarm-intelligence", "fastapi", "docker", "kubernetes", "python"],
    ),
    (
        "DataAgentBench",
        "Fork of DAB — benchmark for evaluating data agents on realistic multi-database enterprise tasks.",
        "https://ucbepic.github.io/DataAgentBench/",
        ["benchmark", "data-agent", "evaluation", "python"],
    ),
]


def update_repo(repo, description, homepage, topics):
    """Update repo description and topics via GitHub API."""
    # Update description
    url = f"https://api.github.com/repos/{OWNER}/{repo}"
    data = {"description": description}
    if homepage:
        data["homepage"] = homepage

    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode(),
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        },
        method="PATCH",
    )
    try:
        urllib.request.urlopen(req)
        print(f"  ✓ {repo}: description updated")
    except Exception as e:
        print(f"  ✗ {repo}: description failed — {e}")

    # Update topics
    url_topics = f"https://api.github.com/repos/{OWNER}/{repo}/topics"
    data_topics = {"names": topics}
    req_topics = urllib.request.Request(
        url_topics,
        data=json.dumps(data_topics).encode(),
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.mercy-preview+json",
            "Content-Type": "application/json",
        },
        method="PUT",
    )
    try:
        urllib.request.urlopen(req_topics)
        print(f"  ✓ {repo}: topics updated → {topics}")
    except Exception as e:
        print(f"  ✗ {repo}: topics failed — {e}")


if __name__ == "__main__":
    print(f"Updating {len(UPDATES)} repos for {OWNER}...\n")
    for repo, desc, homepage, topics in UPDATES:
        update_repo(repo, desc, homepage, topics)
        print()
    print("Done! Now go to https://github.com/IbnuEyni and pin your top 6 repos.")
    print("\nRecommended pin order:")
    print("  1. oracle-forge")
    print("  2. tenacious-sales-bench")
    print("  3. Conversion-Engine")
    print("  4. 10Acweek5 (The Ledger)")
    print("  5. 10Acweek2 (Automaton Auditor)")
    print("  6. Roo-Code (Intent Traceability)")
