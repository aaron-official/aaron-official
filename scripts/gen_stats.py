#!/usr/bin/env python3
"""Generate self-hosted GitHub stat cards as animated SVG.

No third-party services: queries the GitHub GraphQL API directly and renders
assets/stats.svg and assets/langs.svg. Standard library only.
"""
import json
import os
import urllib.request

USER = os.environ.get("GH_USER", "aaron-official")
TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com/graphql"

QUERY = """
query($login:String!, $cursor:String) {
  user(login:$login) {
    followers { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar { totalContributions }
    }
    repositories(first:100, after:$cursor, ownerAffiliations:OWNER, isFork:false) {
      pageInfo { hasNextPage endCursor }
      totalCount
      nodes {
        stargazerCount
        isPrivate
        languages(first:12, orderBy:{field:SIZE, direction:DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def gql(cursor=None):
    body = json.dumps({"query": QUERY,
                       "variables": {"login": USER, "cursor": cursor}}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": f"bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": USER,
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    return payload["data"]["user"]


def collect():
    stars = repos = 0
    saw_private = False
    langs: dict[str, dict] = {}
    followers = contribs = commits = prs = 0
    cursor = None
    while True:
        u = gql(cursor)
        followers = u["followers"]["totalCount"]
        cc = u["contributionsCollection"]
        commits = cc["totalCommitContributions"]
        prs = cc["totalPullRequestContributions"]
        contribs = cc["contributionCalendar"]["totalContributions"]
        rs = u["repositories"]
        repos = rs["totalCount"]
        for n in rs["nodes"]:
            if n["isPrivate"]:
                saw_private = True
            stars += n["stargazerCount"]
            for e in n["languages"]["edges"]:
                name = e["node"]["name"]
                d = langs.setdefault(name, {"size": 0, "color": e["node"]["color"] or "#8b949e"})
                d["size"] += e["size"]
        if not rs["pageInfo"]["hasNextPage"]:
            break
        cursor = rs["pageInfo"]["endCursor"]
    top = sorted(langs.items(), key=lambda kv: -kv[1]["size"])[:6]
    total = sum(v["size"] for _, v in top) or 1
    return {
        "stars": stars, "repos": repos, "followers": followers,
        "contribs": contribs, "commits": commits, "prs": prs,
        "langs": [(k, v["color"], v["size"] / total * 100) for k, v in top],
        "saw_private": saw_private,
    }


HEAD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{alt}">
<defs>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.75"/>
    <stop offset="50%" stop-color="#8b5cf6" stop-opacity="0.75"/>
    <stop offset="100%" stop-color="#06b6d4" stop-opacity="0.75"/>
  </linearGradient>
  <style>
    .t {{ font-family: ui-monospace,SFMono-Regular,'DejaVu Sans Mono',Menlo,monospace; }}
    .lbl {{ fill:#8b949e; font-size:13px; }}
    .val {{ fill:#e6edf3; font-size:19px; font-weight:700; }}
    .ttl {{ fill:#e6edf3; font-size:15px; font-weight:700; letter-spacing:2px; }}
  </style>
</defs>
<rect x="1" y="1" width="{w2}" height="{h2}" rx="12" fill="#0d1117" stroke="url(#edge)" stroke-width="1.5"/>
"""


def card(rows, w=420, h=210):
    s = HEAD.format(w=w, h=h, w2=w - 2, h2=h - 2, alt="GitHub statistics")
    s += '<text class="t ttl" x="24" y="36">STATISTICS</text>'
    s += ('<rect x="24" y="48" width="60" height="2" fill="url(#edge)">'
          '<animate attributeName="width" values="0;60" dur="0.9s" fill="freeze"/></rect>')
    y = 80
    for i, (label, value) in enumerate(rows):
        d = 0.15 * i
        s += f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="{d}s" fill="freeze"/>'
        s += f'<text class="t lbl" x="24" y="{y}">{label}</text>'
        s += f'<text class="t val" x="{w-24}" y="{y+1}" text-anchor="end">{value}</text>'
        s += f'<rect x="24" y="{y+9}" width="0" height="1" fill="#30363d">' \
             f'<animate attributeName="width" values="0;{w-48}" dur="0.7s" begin="{d}s" fill="freeze"/></rect></g>'
        y += 32
    return s + "</svg>\n"


def langcard(langs, w=420, h=210):
    s = HEAD.format(w=w, h=h, w2=w - 2, h2=h - 2, alt="Most used languages")
    s += '<text class="t ttl" x="24" y="36">LANGUAGES</text>'
    s += ('<rect x="24" y="48" width="60" height="2" fill="url(#edge)">'
          '<animate attributeName="width" values="0;60" dur="0.9s" fill="freeze"/></rect>')
    # stacked bar
    x, bar_w = 24.0, float(w - 48)
    s += f'<g><rect x="24" y="62" width="{bar_w}" height="10" rx="5" fill="#161b22"/>'
    for name, color, pct in langs:
        seg = bar_w * pct / 100
        s += (f'<rect x="{x:.1f}" y="62" width="0" height="10" fill="{color}">'
              f'<animate attributeName="width" values="0;{seg:.1f}" dur="1s" fill="freeze"/></rect>')
        x += seg
    s += "</g>"
    y = 104
    for i, (name, color, pct) in enumerate(langs):
        col = 24 if i % 2 == 0 else w // 2 + 4
        row = y + (i // 2) * 30
        d = 0.12 * i
        s += (f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="{d}s" fill="freeze"/>'
              f'<circle cx="{col+6}" cy="{row-4}" r="5" fill="{color}"/>'
              f'<text class="t lbl" x="{col+20}" y="{row}">{name}</text>'
              f'<text class="t lbl" x="{col+170}" y="{row}" text-anchor="end" fill="#e6edf3">{pct:.1f}%</text></g>')
    return s + "</svg>\n"


if __name__ == "__main__":
    d = collect()
    os.makedirs("assets", exist_ok=True)
    with open("assets/stats.svg", "w") as f:
        f.write(card([
            ("Repositories" if d["saw_private"] else "Public repositories", d["repos"]),
            ("Stars earned", d["stars"]),
            ("Pull requests", d["prs"]),
            ("Contributions (past year)", f'{d["contribs"]:,}'),
            ("Followers", d["followers"]),
        ]))
    # A token without private access sees a skewed language mix, so only
    # rewrite the card when the private repositories are visible.
    if d["saw_private"] or not os.path.exists("assets/langs.svg"):
        with open("assets/langs.svg", "w") as f:
            f.write(langcard(d["langs"]))
    else:
        print("skipping langs.svg: token cannot see private repositories")
    print("stars=%(stars)s repos=%(repos)s commits=%(commits)s" % d)
    print("langs:", ", ".join(f"{n} {p:.1f}%" for n, _, p in d["langs"]))
