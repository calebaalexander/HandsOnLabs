# CoCo Desktop: I Downloaded CoCo Desktop... Now What?

> **Note:** PawCore is a fictional company. All data and scenarios are synthetic and for educational purposes only.

Part 1 of the CoCo Desktop series, first presented **November 10, 2026**. This lab is for people who downloaded CoCo Desktop, opened it, and weren't sure where to start. It covers where things live in the app, how it works, and how to get a first real task done with confidence, using one small PawCore support question as the example.

## What's here

```
3-CoCo-Desktop/
└── slides/
    └── index.html   # Opening slides (open in a browser; arrow keys to navigate)
```

## Get CoCo Desktop

Download it from the [official Snowflake CoCo downloads page](https://www.snowflake.com/en/product/snowflake-coco/downloads/) (macOS and Windows).

## What you need to try it yourself

- CoCo Desktop and your own Snowflake account and sign-in
- An active role with `SNOWFLAKE.CORTEX_USER` or `SNOWFLAKE.CORTEX_AGENT_USER`, and an available AI model
- A warehouse and read access to the PawCore support tickets table (`PAWCORE_ANALYTICS.SUPPORT.SUPPORT_TICKETS`)
- On a self-service trial, an account admin must add a credit card to enable AI features

This repo provides materials only. It does not grant access to any Snowflake account or data. Review setup scripts in this repo before running them, especially in a shared account.

## The PawCore question

A SmartCollar V2 support lead asks: which region needs attention, and what evidence supports that call? The lab shows how to give CoCo focused context, review the action it proposes, and check the answer against the data.

A tested Desktop take-home exercise will be added here.
