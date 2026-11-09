# CoCo Desktop: one-page guide

Everything from the November 10, 2026 lab, *I Downloaded CoCo Desktop... Now What?* PawCore is fictional; all data is synthetic.

## Set up
- Download from the [official CoCo downloads page](https://www.snowflake.com/en/product/snowflake-coco/downloads/). Sign in with your account identifier, login name, and sign-in method.
- You need a role with `SNOWFLAKE.CORTEX_USER` or `SNOWFLAKE.CORTEX_AGENT_USER`, and a warehouse. On a self-service trial, add a credit card to turn on AI features.
- **Agent view** puts the chat first. **Editor view** puts files and chat side by side. Cmd+E switches.

## Projects and sessions
- A **project** is a folder. Organize projects by topic (a customer, product, or territory). CoCo keeps the last 25 sessions per project.
- A **session** is one conversation with one goal. New goal, new session.
- Keep the folder somewhere that survives a lost laptop: a synced drive or a Git repo.

## Run the lab yourself
1. Open the unzipped `3-CoCo-Desktop` folder as a project, start a session, and send the **opening prompt** ([README: Start your first session](README.md#start-your-first-session)).
2. In the same session, send the **load prompt** ([README: Load the data into Snowflake](README.md#load-the-data-into-snowflake)). Expect 356 rows, 129 NULL `resolved_date`, 100 NULL `firmware_version`, and 3 regions.
3. Same session: *"Show me 5 sample rows and the count of tickets by region and status from `PAWCORE_ANALYTICS.SUPPORT.SUPPORT_TICKETS`."*
4. New session: *"Which region is having the roughest time with SmartCollar V2 right now? Check our support tickets in PAWCORE_ANALYTICS and show me the numbers behind your answer. Just look, don't change anything."*
5. Then: *"/human-voice Rewrite your answer as a Slack message to the SmartCollar V2 support lead. Keep every number."*

## The chat box
- **Approvals:** Default Approvals asks before SQL, commands, or edits. Approve for me runs safe read-only steps. Bypass asks nothing; avoid it in shared accounts.
- **Agent / Plan:** Agent does the work. Plan writes a plan first and changes nothing until you approve.
- **Model:** start on **Auto**. Auto Intelligent is for hard work; Auto Efficient is for simple, repetitive work.
- **`@`** points CoCo at a file. **`/`** runs a skill.

## Customize
| Section | What it is |
|---|---|
| Custom instructions | Standing preferences in `~/.snowflake/cortex/AGENTS.md`, loaded into every conversation. Keep them short. |
| Tools | Switches for Web Search, Web Fetch, and Notebooks. Web Search needs an ACCOUNTADMIN to run `ALTER ACCOUNT SET ENABLE_CORTEX_WEBSEARCH = TRUE`. |
| Memory | Plain-text notes CoCo keeps between sessions, global and per project, in `~/.snowflake/cortex/memory/`. |
| Plugins | Packages of skills, agents, hooks, and connectors. This folder includes **XO** by Dan Chaffelson ([install steps](README.md#optional-the-xo-plugin)). |
| Skills | Saved playbooks (`SKILL.md`) that CoCo runs on its own or when you type `/`. |
| MCP | A standard way to plug CoCo into other tools, like your calendar or email. |
| Agents | Helpers CoCo sends off to do part of a job in their own conversation. |
| Hooks | Scripts that run automatically at set moments, such as session start. |
| Rules | The instruction files CoCo reads first. Put team rules in the project's `AGENTS.md`. |
| Indexing | Lets CoCo search a big project by meaning, not just exact words. |

**Make CoCo sound human:** paste the writing rules from the [README](README.md#make-coco-sound-more-human) into Custom instructions, and use the `human-voice` skill for one-off rewrites.

## Habits that work
- Check the project, role, and warehouse before every task.
- Say where to look and whether CoCo may change things.
- Read each command or SQL statement before you approve it.
- Check the answer against the data. Re-run the key number yourself in **SQL Playground**.
- Review file edits in **Changes** before you keep them.
- When CoCo gets something wrong, save a rule once instead of correcting it every session.

## What's next
- **Nov 17:** [Prompt to Pipeline](https://www.snowflake.com/webinars/prompt-to-pipeline-hands-on-data-engineering-with-cortex-code-20261117/), a hands-on data engineering lab.
- **Dec 2:** CoCo Desktop: Full Potential (Part 2).
- Watch for an email when the on-demand video of this lab is available.

Questions? Contact your Snowflake account rep, or Caleb Alexander at [caleb.alexander@snowflake.com](mailto:caleb.alexander@snowflake.com).
