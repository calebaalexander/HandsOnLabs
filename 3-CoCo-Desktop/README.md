# CoCo Desktop: I Downloaded CoCo Desktop... Now What?

> **Note:** PawCore is a fictional company. All data and scenarios are synthetic and for educational purposes only.

Part 1 of the CoCo Desktop series, first presented **November 10, 2026**. This lab is for people who downloaded CoCo Desktop, opened it, and weren't sure where to start. It covers where things live in the app, how it works, and how to get a first real task done with confidence, using one small PawCore support question as the example.

## What's here

```
3-CoCo-Desktop/
├── 3-CoCo-Desktop.zip            # This whole folder as one download
├── data/
│   ├── support_tickets.csv           # 356 fictional PawCore support tickets (Aug-Oct 2026)
│   └── generate_support_tickets.py   # Script that generated the data
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

CoCo should report 356 rows and 12 columns, with some empty `resolved_date` values (tickets not yet resolved).

### Columns

`ticket_id`, `created_date`, `region` (Americas, EMEA, APAC), `country`, `product`, `firmware_version`, `category`, `priority` (Low to Critical), `status` (Open, In Progress, Resolved), `channel`, `resolved_date`, `description`

## The PawCore question

A SmartCollar V2 support lead asks: which region needs attention, and what evidence supports that call? The lab shows how to give CoCo focused context, review the action it proposes, and check the answer against the data.

A tested Desktop take-home exercise will be added here.

## Optional: the XO plugin

[XO](https://github.com/Snowflake-Labs/coco-skills/tree/main/plugins/xo) is an open-source CoCo plugin built by Dan Chaffelson and published on Snowflake Labs (Apache 2.0). It keeps plain-text notes of your sessions in a vault you own, so work picks up where you left off, saves rules when you correct it, and works in steps (survey, plan, build, prove) sized to the job.

1. Make sure `node`, `git`, `gh`, and `jq` are on your PATH.
2. In CoCo Desktop, open **Customize > Plugins** and add the plugin from GitHub: `Snowflake-Labs/coco-skills`, plugin `xo`.
3. Run the bundled setup once in a terminal:

   ```bash
   ~/.snowflake/cortex/plugins/xo/setup.sh install
   ```

   For a private, git-backed vault on your GitHub account instead, clone the repo and run `coco-skills/plugins/xo/setup.sh init` (requires `gh auth login`).
4. Check it with `setup.sh status`.

See XO's [SETUP.md](https://github.com/Snowflake-Labs/coco-skills/blob/main/plugins/xo/SETUP.md) for details. Review a plugin's hooks and scripts before you install it.
