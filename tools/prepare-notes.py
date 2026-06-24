#!/usr/bin/env python3
"""
prepare-notes.py — make Markdown notes render correctly under kramdown + MathJax.

Why this exists
---------------
GitHub Pages renders Markdown with kramdown (GFM). With kramdown's math engine ON
(our config), it protects `$$...$$` math from being mangled — but it does NOT treat
single-dollar `$...$` as math. Left alone, inline `$x_i$` gets eaten by Markdown:
underscores become <em>, `|` turns lines into tables, `\#`/`\{` lose their backslash.

This script normalises a note so everything renders:

  1. Top-level display blocks (a line starting with `$$`) get blank lines around them,
     so kramdown emits real display math  \[ ... \]  (centred, full-size).
  2. Remaining inline `$...$` become `$$...$$`, which kramdown renders as inline \( ... \)
     with its content protected.

Existing `$$...$$` blocks are never double-wrapped. Front matter is left untouched.
Idempotent: running it twice is a no-op.

Usage
-----
    python3 tools/prepare-notes.py _notes/my-note.md          # edit in place
    python3 tools/prepare-notes.py _notes/*.md                # several files
    python3 tools/prepare-notes.py --check _notes/*.md        # report, don't write
"""
import re
import sys

FM_RE = re.compile(r"^(---\n.*?\n---\n)", re.S)
# Match an existing display block first (so we skip it), else an inline $...$ span.
# The inline branch allows soft-wrapped newlines but stops at a blank line, so a span
# never swallows a paragraph break: `\n(?!\n)` permits a single newline only.
INLINE_RE = re.compile(r"\$\$.*?\$\$|\$(?!\$)(?:[^$\n]|\n(?!\n))*?\$", re.S)


def split_front_matter(text):
    m = FM_RE.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def _is_display_open(line):
    """True if `line` opens a display equation — either at column 0 or indented inside a
    list. The line's content (ignoring leading whitespace) must start with `$$` and be the
    *whole* equation: a multi-line opener, or a single line whose closing `$$` is trailed
    only by whitespace. The trailing-whitespace rule keeps the pass idempotent and avoids
    misreading inline math that merely happens to start a line."""
    s = line.lstrip()
    if not s.startswith("$$"):
        return False
    rest = s[2:]
    close = rest.find("$$")
    if close == -1:
        return True  # multi-line block opener
    return rest[close + 2:].strip() == ""  # single-line block only if nothing trails


def separate_display_blocks(body):
    """Ensure a blank line before/after every top-level `$$ ... $$` block.

    A *top-level* display block is one whose opening `$$` is at column 0 (not indented
    inside a list) AND that is the whole equation — i.e. either it spans multiple lines,
    or its closing `$$` is followed by nothing but whitespace. This second condition is
    what makes the pass idempotent: inline math that happens to start a line (e.g.
    `$$\omega = ...$$.`) has trailing prose after its close, so it is left as inline.
    """
    lines = body.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if _is_display_open(line):
            # Collect the block. Single-line if it holds a closing `$$` after the opener.
            block = [line]
            if line.count("$$") < 2:
                i += 1
                while i < len(lines):
                    block.append(lines[i])
                    if "$$" in lines[i]:
                        break
                    i += 1
            # Blank line before.
            if out and out[-1].strip() != "":
                out.append("")
            out.extend(block)
            # Blank line after.
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt.strip() != "":
                out.append("")
            i += 1
        else:
            out.append(line)
            i += 1
    return "\n".join(out)


def wrap_inline(body):
    def repl(m):
        s = m.group(0)
        return s if s.startswith("$$") else "$$" + s[1:-1] + "$$"
    return INLINE_RE.sub(repl, body)


def transform(text):
    fm, body = split_front_matter(text)
    body = separate_display_blocks(body)
    body = wrap_inline(body)
    return fm + body


def main(argv):
    check = "--check" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__.strip().splitlines()[-1])
        return 1
    changed = 0
    for p in paths:
        with open(p, encoding="utf-8") as f:
            src = f.read()
        out = transform(src)
        if out != src:
            changed += 1
            if check:
                print(f"would change: {p}")
            else:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(out)
                print(f"prepared: {p}")
        else:
            print(f"ok (no change): {p}")
    if check and changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
