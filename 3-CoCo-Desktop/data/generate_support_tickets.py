# Generates fictional PawCore support tickets for the CoCo Desktop Part 1 HOL.
# Story: EMEA has the most tickets overall (largest install base, mostly resolved),
# but APAC has a recent spike of open High/Critical SmartCollar V2 connectivity
# tickets on firmware 2.1.0. Counts point where to look; they don't prove root cause.
import csv, random
from datetime import date, timedelta

random.seed(1110)
START, END = date(2026, 8, 1), date(2026, 10, 31)
SPIKE_START = date(2026, 10, 10)

COUNTRIES = {
    "Americas": ["United States", "Canada", "Brazil", "Mexico"],
    "EMEA": ["United Kingdom", "Germany", "France", "Netherlands", "Spain"],
    "APAC": ["Australia", "Japan", "Singapore", "South Korea"],
}
PRODUCTS = ["SmartCollar V2", "SmartCollar V1", "SmartLeash Connect", "HomeBase Station"]
CHANNELS = ["App", "Email", "Chat", "Phone"]
DESCRIPTIONS = {
    "Battery": ["Battery drains in under a day", "Collar won't hold a charge overnight", "Charging dock not recognized"],
    "Connectivity": ["Collar disconnects from the app every few minutes", "Bluetooth pairing fails after update", "Device shows offline while pet is home"],
    "GPS accuracy": ["Location jumps several blocks", "Walk route not recorded", "Geofence alert triggered while pet was inside"],
    "Health alerts": ["Heart-rate alert seems wrong during play", "Activity score stuck at zero", "Temperature alert sent repeatedly"],
    "App sync": ["Activity history missing for last week", "App stuck on syncing", "Pet profile reset after login"],
    "Fit & comfort": ["Strap irritating pet's neck", "Clasp opens on its own", "Collar too heavy for small breed"],
}

def pick_date(lo, hi):
    return lo + timedelta(days=random.randint(0, (hi - lo).days))

rows = []
def add(region, product, category, created, priority, firmware=None, open_bias=0.12):
    status = random.choices(["Resolved", "In Progress", "Open"],
                            [1 - open_bias * 2, open_bias, open_bias])[0]
    if (END - created).days < 5 and status == "Resolved":
        status = random.choice(["Open", "In Progress"])
    resolved = (created + timedelta(days=random.randint(1, 9))) if status == "Resolved" else None
    if resolved and resolved > END:
        resolved, status = None, "In Progress"
    if firmware is None:
        firmware = random.choice(["2.0.3", "2.0.4"]) if product == "SmartCollar V2" else (
            "1.8.2" if product == "SmartCollar V1" else "n/a")
    rows.append(dict(region=region, country=random.choice(COUNTRIES[region]), product=product,
                     firmware_version=firmware, category=category, priority=priority, status=status,
                     channel=random.choice(CHANNELS), created_date=created, resolved_date=resolved,
                     description=random.choice(DESCRIPTIONS[category])))

def baseline(region, n):
    for _ in range(n):
        product = random.choices(PRODUCTS, [0.45, 0.25, 0.15, 0.15])[0]
        category = random.choice(list(DESCRIPTIONS))
        priority = random.choices(["Low", "Medium", "High", "Critical"], [0.35, 0.40, 0.20, 0.05])[0]
        add(region, product, category, pick_date(START, END), priority)

baseline("EMEA", 150)
baseline("Americas", 105)
baseline("APAC", 55)

# APAC spike: SmartCollar V2 on firmware 2.1.0, connectivity, recent, mostly unresolved and high priority.
for _ in range(38):
    add("APAC", "SmartCollar V2", "Connectivity", pick_date(SPIKE_START, END),
        random.choices(["High", "Critical", "Medium"], [0.55, 0.30, 0.15])[0],
        firmware="2.1.0", open_bias=0.38)
# A few 2.1.0 tickets elsewhere, so firmware alone isn't the whole story.
for region in ["EMEA", "Americas"]:
    for _ in range(4):
        add(region, "SmartCollar V2", random.choice(["Connectivity", "App sync"]),
            pick_date(SPIKE_START, END), random.choice(["Medium", "High"]), firmware="2.1.0")

rows.sort(key=lambda r: r["created_date"])
with open("support_tickets.csv", "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["ticket_id", "created_date", "region", "country", "product", "firmware_version",
                "category", "priority", "status", "channel", "resolved_date", "description"])
    for i, r in enumerate(rows, 1):
        w.writerow([f"PC-{i:04d}", r["created_date"], r["region"], r["country"], r["product"],
                    r["firmware_version"], r["category"], r["priority"], r["status"], r["channel"],
                    r["resolved_date"] or "", r["description"]])
print(len(rows), "rows")
