#!/usr/bin/env python3
"""Generate local profile SVG stats from GitHub API (no external stat services)."""

from __future__ import annotations

import json
import os
import urllib.request
from collections import Counter
from xml.sax.saxutils import escape

USERNAME = os.environ.get("GITHUB_USERNAME", "Ananyanagaraj11")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"


def api_get(path: str) -> dict | list:
    req = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}" if TOKEN else "",
            "User-Agent": "profile-svg-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def fetch_all_repos() -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        batch = api_get(f"/users/{USERNAME}/repos?per_page=100&page={page}&sort=updated")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [r for r in repos if r.get("name") != USERNAME and not r.get("fork")]


def svg_header(w: int, h: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="GitHub profile statistics">\n'
        "<defs>\n"
        '  <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">\n'
        '    <stop offset="0%" stop-color="#1e1b4b"/>\n'
        '    <stop offset="100%" stop-color="#0f172a"/>\n'
        "  </linearGradient>\n"
        '  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">\n'
        '    <stop offset="0%" stop-color="#6366f1"/>\n'
        '    <stop offset="100%" stop-color="#8b5cf6"/>\n'
        "  </linearGradient>\n"
        "</defs>\n"
    )


def write_stats_svg(public_repos: int, total_stars: int, langs: Counter, out_path: str) -> None:
    w, h = 520, 200
    top_lang = langs.most_common(1)[0][0] if langs else "Python"
    parts = [
        svg_header(w, h),
        f'<rect width="{w}" height="{h}" rx="16" fill="url(#card)" stroke="#334155" stroke-width="1"/>',
        f'<text x="24" y="36" fill="#e2e8f0" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="700">GitHub Stats</text>',
        f'<text x="24" y="58" fill="#94a3b8" font-family="Segoe UI, Arial, sans-serif" font-size="12">@{escape(USERNAME)} · generated locally</text>',
        f'<text x="40" y="110" fill="#cbd5e1" font-family="Segoe UI, Arial, sans-serif" font-size="14">Public Repos</text>',
        f'<text x="40" y="140" fill="#f8fafc" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="700">{public_repos}</text>',
        f'<text x="210" y="110" fill="#cbd5e1" font-family="Segoe UI, Arial, sans-serif" font-size="14">Total Stars</text>',
        f'<text x="210" y="140" fill="#f8fafc" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="700">{total_stars}</text>',
        f'<text x="380" y="110" fill="#cbd5e1" font-family="Segoe UI, Arial, sans-serif" font-size="14">Top Language</text>',
        f'<text x="380" y="140" fill="#f8fafc" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="700">{escape(top_lang)}</text>',
        f'<rect x="24" y="168" width="{w-48}" height="6" rx="3" fill="#1e293b"/>',
        f'<rect x="24" y="168" width="{(w-48)//2}" height="6" rx="3" fill="url(#accent)">',
        '<animate attributeName="width" values="40;460;40" dur="6s" repeatCount="indefinite"/>',
        "</rect>",
        "</svg>",
    ]
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def write_langs_svg(langs: Counter, out_path: str) -> None:
    w, h = 520, 220
    total = sum(langs.values()) or 1
    colors = ["#6366f1", "#8b5cf6", "#22d3ee", "#34d399", "#f59e0b", "#f472b6", "#94a3b8"]
    parts = [
        svg_header(w, h),
        f'<rect width="{w}" height="{h}" rx="16" fill="url(#card)" stroke="#334155" stroke-width="1"/>',
        f'<text x="24" y="36" fill="#e2e8f0" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="700">Top Languages</text>',
    ]
    y = 70
    for i, (lang, count) in enumerate(langs.most_common(6)):
        pct = int(count * 100 / total)
        bar_w = int((w - 170) * count / total)
        color = colors[i % len(colors)]
        parts.extend(
            [
                f'<text x="24" y="{y}" fill="#cbd5e1" font-family="Segoe UI, Arial, sans-serif" font-size="13">{escape(lang)}</text>',
                f'<text x="{w-50}" y="{y}" fill="#94a3b8" font-family="Segoe UI, Arial, sans-serif" font-size="12">{pct}%</text>',
                f'<rect x="24" y="{y+8}" width="{w-48}" height="8" rx="4" fill="#1e293b"/>',
                f'<rect x="24" y="{y+8}" width="{bar_w}" height="8" rx="4" fill="{color}"/>',
            ]
        )
        y += 28
    parts.append("</svg>")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def main() -> None:
    user = api_get(f"/users/{USERNAME}")
    repos = fetch_all_repos()
    langs: Counter = Counter()
    stars = 0
    for r in repos:
        stars += r.get("stargazers_count", 0)
        lang = r.get("language")
        if lang:
            langs[lang] += 1

    assets = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
    os.makedirs(assets, exist_ok=True)
    write_stats_svg(user.get("public_repos", len(repos)), stars, langs, os.path.join(assets, "stats.svg"))
    write_langs_svg(langs, os.path.join(assets, "langs.svg"))
    print(f"Generated stats.svg and langs.svg for {USERNAME}")


if __name__ == "__main__":
    main()
