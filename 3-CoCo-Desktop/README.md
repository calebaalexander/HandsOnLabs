# CoCo Desktop: I Downloaded CoCo Desktop... Now What?

> **Note:** PawCore is a fictional company. All data and scenarios are synthetic and for educational purposes only.

Part 1 of the CoCo Desktop series, first presented **November 10, 2026**. This lab is for people who downloaded CoCo Desktop, opened it, and weren't sure where to start. It covers where things live in the app, how it works, and how to get a first real task done with confidence, using one small PawCore support question as the example.

## What's here

```
3-CoCo-Desktop/
├── 3-CoCo-Desktop.zip            # This whole folder as one download
├── .snowflake/cortex/skills/
│   └── human-voice/SKILL.md      # Skill that rewrites output in a plain, human voice
├── data/
│   ├── support_tickets.csv           # 356 fictional PawCore support tickets (Aug-Oct 2026)
│   └── generate_support_tickets.py   # Script that generated the data
├── plugins/
│   └── xo/                   # XO plugin by Dan Chaffelson (Apache 2.0), ready to install
└── slides/
    └── index.html            # Opening slides (open in a browser; arrow keys to navigate)
```

## Get CoCo Desktop

Download it from the [official Snowflake CoCo downloads page](https://www.snowflake.com/en/product/snowflake-coco/downloads/) (macOS and Windows).

## What you need to try it yourself

- CoCo Desktop and your own Snowflake account and sign-in
- An active role with `SNOWFLAKE.CORTEX_USER` or `SNOWFLAKE.CORTEX_AGENT_USER`, and an available AI model
- A warehouse, and a role that can create the `PAWCORE_ANALYTICS` database and `SUPPORT` schema (or an account admin who creates them for you)
- On a self-service trial, an account admin must add a credit card to enable AI features

This repo provides materials only. It does not grant access to any Snowflake account or data. Review setup scripts in this repo before running them, especially in a shared account.

## Get the data

Download [`3-CoCo-Desktop.zip`](3-CoCo-Desktop.zip) from this folder and unzip it. You get a `3-CoCo-Desktop` folder with the data and slides. In the lab, CoCo Desktop loads `data/support_tickets.csv` into `PAWCORE_ANALYTICS.SUPPORT.SUPPORT_TICKETS` in your own Snowflake account.

## Start your first session

1. In CoCo Desktop, click the add-project icon next to **Projects**, choose **Open Folder**, and select the unzipped `3-CoCo-Desktop` folder. This is your PawCore project.
2. Start a **New session** in that project and send this prompt. It tells CoCo the goal and where the data should go, and only reads the file:

> This session has one goal: load `data/support_tickets.csv` from this project into Snowflake as the table `PAWCORE_ANALYTICS.SUPPORT.SUPPORT_TICKETS`, in database `PAWCORE_ANALYTICS` and schema `SUPPORT`. Don't create or load anything yet. First, read the file and tell me how many rows and columns it has, the column names, and anything I should know before loading it, such as empty values or date formats.

CoCo should report 356 rows and 12 columns, with 129 empty `resolved_date` values (tickets not yet resolved) and 100 rows where `firmware_version` is the text `n/a` (HomeBase Station and SmartLeash Connect have no firmware).

## Load the data into Snowflake

In the **same session**, send this prompt. CoCo shows each SQL statement and waits for your approval before it runs it; read each one before you approve.

> Using my current Snowflake connection, role, and warehouse, load the file `data/support_tickets.csv` from this project into a new Snowflake table, `PAWCORE_ANALYTICS.SUPPORT.SUPPORT_TICKETS`. Work through these steps in order:
>
> 1. Show me the current role, warehouse, database, and schema. If no warehouse is active, stop and ask me which one to use.
> 2. Create the database `PAWCORE_ANALYTICS` and the schema `SUPPORT` if they don't exist. If my role can't create them, stop and tell me which privilege is missing.
> 3. Create an internal stage, `PAWCORE_ANALYTICS.SUPPORT.PAWCORE_STAGE`, and upload the file to it with `PUT`.
> 4. Create a CSV file format, `PAWCORE_ANALYTICS.SUPPORT.PAWCORE_CSV`, that reads the column names from the header row, treats empty fields and the text `n/a` as NULL, and trims extra spaces.
> 5. Use `INFER_SCHEMA` on the staged file to work out the columns and types, show me the result, then create the table from it. Dates should load as `DATE`. `ticket_id` and `firmware_version` should stay text, because versions like 1.8.2 aren't numbers.
> 6. Load the data with `COPY INTO`, matching columns by name, and stop on the first error.
> 7. Verify the load: total rows (expect 356), rows where `resolved_date` is NULL (expect 129), rows where `firmware_version` is NULL (expect 100), the distinct regions (expect 3), and the result in `COPY_HISTORY`.
>
> Rules: show me each SQL statement and wait for my approval before you run it. Only create objects inside `PAWCORE_ANALYTICS`. Don't drop or replace anything. If the table already exists, stop and ask me what to do.

If a check doesn't match, ask CoCo why before you move on. Common causes: no active warehouse, a role that can't create the database, or a table left over from an earlier run.

### Columns

`ticket_id`, `created_date`, `region` (Americas, EMEA, APAC), `country`, `product`, `firmware_version`, `category`, `priority` (Low to Critical), `status` (Open, In Progress, Resolved), `channel`, `resolved_date`, `description`

## The PawCore question

A SmartCollar V2 support lead asks: which region needs attention, and what evidence supports that call? The lab shows how to give CoCo focused context, review the action it proposes, and check the answer against the data.

A tested Desktop take-home exercise will be added here.

## Make CoCo sound more human

There are two ways to do this, and you can use both.

**1. Custom instructions (every conversation).** In CoCo Desktop, open **Customize > Personalization > Custom instructions**, paste this, and click **Save**. It's saved to `~/.snowflake/cortex/AGENTS.md` and applies in every project, starting with your next new session.

```markdown
## How to write responses
- Write like a colleague talking, not a report. Plain words, short sentences, contractions.
- Lead with the answer in one or two sentences, then the evidence.
- Use bullets only for three or more parallel items. No headers in short answers.
- Don't open with "Great question" or "Certainly." Don't close with "I hope this helps."
- Don't use em dashes or filler words: delve, leverage, robust, seamless, crucial, comprehensive.
- Say what you checked and what you're guessing. If you don't know, say so.
- End with one clear next step or one question, not a menu of options.
```

To use it for one project only, put the same text in an `AGENTS.md` at the project root instead.

**2. The `human-voice` skill (on demand).** This folder includes a skill at [`.snowflake/cortex/skills/human-voice/SKILL.md`](.snowflake/cortex/skills/human-voice/SKILL.md). When you open `3-CoCo-Desktop` as a project, CoCo finds it automatically; check **Customize > Skills > Local Skills**. (Folders that start with a dot are hidden in Finder by default; press Cmd+Shift+. to show them.) Run it after any answer:

> /human-voice Rewrite your answer as a Slack message to the SmartCollar V2 support lead. Keep every number.

It keeps the facts, leads with the point, cuts filler, fits the length to the channel, and ends with a "Changed:" line so you can check what it dropped. Read the output before you send it.

Building your own agent? Put the same guidance in its **System Prompt** (**Customize > Agents > + New**). For a Cortex Agent in Snowflake, put it in the agent's response instructions.

## Optional: the XO plugin

[XO](https://github.com/Snowflake-Labs/coco-skills/tree/main/plugins/xo) is an open-source CoCo plugin built by Dan Chaffelson and published on Snowflake Labs (Apache 2.0). It keeps plain-text notes of your sessions in a vault you own, so work picks up where you left off, saves rules when you correct it, and works in steps (survey, plan, build, prove) sized to the job.

A copy is included in this folder at [`plugins/xo/`](plugins/xo/), so you don't need to download anything else.

1. Make sure `node`, `git`, `gh`, and `jq` are on your PATH.
2. Move the unzipped `3-CoCo-Desktop` folder to wherever you'll keep it. XO is registered from this location, so don't move or delete the folder afterwards.
3. In a terminal, from the `3-CoCo-Desktop` folder, run the setup once:

   ```bash
   bash plugins/xo/setup.sh install
   ```

4. Start a new session in CoCo Desktop and check that XO appears under **Customize > Plugins**. To check its health at any time, run `bash plugins/xo/setup.sh status`.

For a private, git-backed vault on your GitHub account, run `bash plugins/xo/setup.sh init` instead (requires `gh auth login`). The copy here is pinned to the version noted in [`plugins/README.md`](plugins/README.md); for updates, install from [Snowflake-Labs/coco-skills](https://github.com/Snowflake-Labs/coco-skills/tree/main/plugins/xo). See XO's [SETUP.md](plugins/xo/SETUP.md) for details. Review a plugin's hooks and scripts before you install it.

## Questions

Reach out to your Snowflake account rep, or contact Caleb Alexander at [caleb.alexander@snowflake.com](mailto:caleb.alexander@snowflake.com).
