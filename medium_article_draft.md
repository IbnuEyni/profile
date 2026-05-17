# I Built 9 AI Systems in 12 Weeks — Here's What Actually Matters

_What I learned shipping event stores, evaluation benchmarks, multi-agent courtrooms, and orchestration systems back-to-back._

---

Every week for the past 12 weeks, I built a different AI agent system. Not tutorials. Not toy projects. Production-grade systems with real APIs, real data, and real failure modes.

Here's what I shipped — and the three lessons that changed how I think about building with LLMs.

---

## The Systems

**Week 1 — Intent-Code Traceability System (Roo Code)**

A middleware hook system for VS Code that solves the "Context Paradox" — agents need intent context before writing code, but must write code to establish intent. The solution: a two-stage state machine that forces agents to declare intent before any write operation. PreToolHook blocks, PostToolHook traces. Every code change maps back to a declared business intent with SHA-256 content hashing for spatial independence.

**Week 2 — Automaton Auditor**

A multi-agent "Digital Courtroom" for autonomous code auditing. Three detective agents (repo investigator, doc analyst, vision inspector) collect forensic evidence in parallel. Three judicial agents (prosecutor, defense, tech lead) evaluate dialectically. One chief justice synthesizes deterministically. Built on LangGraph with fan-out/fan-in parallelism. Audits a repo in ~45 seconds for $0.02.

**Week 3 — Document Intelligence Refinery**

An extraction pipeline that routes PDFs through three strategies: fast text parsing for clean documents, layout-aware extraction for tables, and vision-augmented (Gemini) for scanned pages. The key insight: confidence-gated escalation. Start cheap, only spend more when the cheap method isn't confident enough.

**Week 4 — Brownfield Cartographer**

A codebase intelligence system. Point it at an undocumented repo, and it builds a knowledge graph: module dependencies via tree-sitter, data lineage via sqlglot, git velocity metrics, and blast radius calculations. The output answers the five questions every engineer asks on day one at a new codebase.

**Week 5–6 — The Ledger**

A full CQRS/Event Sourcing stack for loan origination. PostgreSQL-backed event store with cryptographic audit chains, projection daemons, upcasting registry, MCP server (9 tools, 6 resources), counterfactual what-if analysis, and regulatory package generation. 166 tests. The deepest backend system I've built — every state transition is an immutable event, every decision is auditable.

**Week 7 — Data Contract Enforcer**

Schema integrity for a five-system AI platform. Auto-generates contracts from data profiles, validates snapshots against those contracts, and when something breaks — traces the violation back to the exact git commit that caused it. The "aha" moment: schema drift detection catches problems that unit tests never will.

**Week 8–9 — Oracle Forge**

A natural language data analytics agent competing on DataAgentBench — 54 queries across 12 datasets. The approach: 3-layer knowledge base injection (schema hints → domain knowledge → corrections memory). Result: 35.2% pass@1 against a 54.3% SOTA ceiling. Not winning, but competitive through pure context engineering — no fine-tuning.

**Week 10 — Conversion Engine**

A full lead generation system: 5-signal enrichment (Crunchbase, job posts, layoffs, leadership changes, AI maturity scoring), ICP classification, signal-grounded email composition, multi-turn conversation management, and CRM sync. All behind a FastAPI orchestrator with a kill switch.

**Week 11 — Tenacious Sales Bench**

I took the Conversion Engine's failures and turned them into a benchmark. 250 tasks across four dimensions: signal grounding, tone consistency, resource honesty, and workflow correctness. Trained a SimPO judge model. Published on HuggingFace. The benchmark catches failures that generic evaluations (like τ²-Bench) completely miss.

---

## Lesson 1: Event Sourcing Changes How You Think About State

The Ledger (Weeks 5–6) was the project that rewired my brain. Before it, I thought of state as "the current row in the database." After it, I think of state as "the sum of everything that happened."

In a CQRS/ES system, you never update a row. You append an event: `ApplicationSubmitted`, `CreditAnalysisCompleted`, `DecisionGenerated`. The current state is a projection — a fold over the event stream. This means:

- **Full audit trail for free.** Every decision is traceable.
- **Time travel.** "What was the compliance status at 2pm on Tuesday?" is a query, not a feature request.
- **Counterfactual analysis.** "What would have happened if the credit score was 50 points higher?" — inject a modified event, replay the projection.

The Ledger has 166 tests, a cryptographic hash chain for tamper detection, and an MCP server so AI agents can interact with the event store through tools. It's the most backend-heavy thing I've built, and it fundamentally changed how I design systems.

**Practical takeaway:** If your system needs auditability, undo, or "why did this happen?" — consider event sourcing. The upfront complexity pays for itself the first time someone asks "what changed and when."

---

## Lesson 2: Evaluation Is the Product

The biggest shift in my thinking: **the benchmark IS the system**.

When I built the Conversion Engine (Week 10), I thought the agent was the product. But the agent's failures were invisible until I built Tenacious Sales Bench (Week 11). Only then could I see that the agent fabricated funding claims 16% of the time, over-committed on bench capacity, and drifted from the style guide in multi-turn conversations.

The lesson: if you can't measure a failure mode, you can't fix it. And generic benchmarks don't measure domain-specific failures. You need benchmarks built from YOUR system's actual failure traces.

**Practical takeaway:** Before optimizing your agent, build a 50-task evaluation set from its real failures. You'll learn more from that than from any prompt engineering.

---

## Lesson 3: Centralized Orchestration Over Distributed Handlers

Every multi-tool system I built converged on the same pattern: a centralized state machine that controls which tools can fire and when.

In the Conversion Engine, leads move through states: NEW → EMAILED → REPLIED → QUALIFIED → BOOKED. The orchestrator enforces three invariants:

1. **Monotonic transitions** — state only moves forward
2. **Idempotent processing** — duplicate webhooks are harmless
3. **Global eligibility** — "can I send SMS?" depends on full lifecycle state, not local context

I tried distributed handlers first. Two duplicate webhook deliveries produced two contradictory actions (an SMS follow-up AND a booking link) from the same event. The centralized orchestrator rejects the duplicate at the gate. One event, one transition, one action.

**Practical takeaway:** If your agent uses multiple tools, don't let the LLM freely choose. Mask invalid tools at each step based on a state machine. It's constrained decoding for actions.

---

## Lesson 4: Context Engineering > Prompt Engineering

Oracle Forge taught me this. We competed on DataAgentBench with zero fine-tuning. The entire approach was context engineering — injecting the right knowledge at the right time:

- **Layer 1: Schema hints** — table structures and column descriptions
- **Layer 2: Domain knowledge** — markdown files explaining business logic per dataset
- **Layer 3: Corrections memory** — "last time you got this wrong because X, try Y instead"

We went from 28.6% to 57.1% on the Yelp dataset just by adding domain knowledge. No model change. No prompt rewriting. Just better context.

The pattern generalizes: most agent failures aren't reasoning failures — they're context failures. The model doesn't have the information it needs at decision time.

**Practical takeaway:** Before rewriting your prompt, ask: "Does the model have all the information it needs to make this decision?" If not, inject it. Knowledge bases, schema hints, and corrections memory are higher-leverage than prompt tricks.

---

## What's Next

I'm continuing to build at the intersection of agent evaluation and orchestration. Current focus:

- Publishing Oracle Forge's context engineering patterns as a reusable library
- Extending Tenacious Sales Bench with more failure dimensions
- Writing about centralized orchestration patterns for multi-tool agents

If you're building AI agent systems and thinking about evaluation, orchestration, or context engineering — let's connect.

---

_Find my work: [GitHub](https://github.com/IbnuEyni) · [HuggingFace](https://huggingface.co/shuaibam) · [LinkedIn](https://www.linkedin.com/in/amir-ahmedin)_

---

**Tags:** Artificial Intelligence, Machine Learning, Software Engineering, Python, AI Agents
