# The Conversion Engine — Automated Lead Generation & Conversion System

**Author:** Amir Ahmedin | **GitHub:** github.com/IbnuEyni

---

## What It Does

End-to-end AI-powered system that enriches leads from raw company names into qualified prospects, composes personalized outreach, manages multi-turn conversations, and books discovery calls — all autonomously.

---

## Architecture

```
                         ┌──────────────────────────┐
                         │   FastAPI Orchestrator    │
                         │   POST /prospects/enrich  │
                         │   POST /prospects/:id/    │
                         │        outreach           │
                         │   POST /prospects/:id/    │
                         │        reply              │
                         └──────────┬───────────────┘
                                    │
          ┌──────────────┬──────────┼──────────┬──────────────┐
          ▼              ▼          ▼          ▼              ▼
   ┌─────────────┐ ┌──────────┐ ┌───────┐ ┌───────────┐ ┌────────┐
   │ Enrichment  │ │Qualifier │ │Email  │ │Conversation│ │Booking │
   │ Pipeline    │ │(ICP)     │ │+ SMS  │ │ Manager    │ │Engine  │
   └──────┬──────┘ └──────────┘ └───────┘ └────────────┘ └────────┘
          │
   ┌──────┴──────┐
   │ 5 Signal    │
   │ Sources:    │
   │             │
   │ • Crunchbase│ → Firmographics + funding rounds
   │ • Job Posts │ → Hiring velocity + tech stacks
   │ • Layoffs   │ → Headcount changes + timing
   │ • Leadership│ → Executive changes
   │ • AI Maturity│ → Readiness score (0-3)
   └─────────────┘
```

---

## Data Flow

1. **Enrich** → Runs 5 signal sources + competitor gap analysis → Classifies into ICP segment → Syncs to HubSpot CRM
2. **Outreach** → Composes signal-grounded email using enrichment data + style guide → Sends via Resend
3. **Reply** → Classifies reply intent (engaged/objection/hard_no/etc.) → Generates context-aware response → Updates CRM
4. **Booking** → Cal.com integration for discovery call scheduling → Syncs to CRM

---

## Key Design Decisions

- **Centralized orchestrator** — state machine controls which actions fire and when
- **Monotonic state transitions** — leads only move forward (NEW → EMAILED → REPLIED → QUALIFIED → BOOKED)
- **Idempotent processing** — duplicate webhooks are harmless
- **Kill switch** — all outbound routes to local sink until explicitly enabled
- **Observability** — full Langfuse tracing on every LLM call

---

## Tech Stack

Python | FastAPI | OpenRouter (LLM) | Resend (email) | Africa's Talking (SMS) | HubSpot (CRM) | Cal.com (booking) | Langfuse (observability)

---

## Results

- 5-signal enrichment pipeline producing qualified leads from raw company names
- Signal-grounded outreach (no hallucinated claims)
- Multi-turn conversation management with reply classification
- Full CRM sync with contact, company, deal, and note creation
