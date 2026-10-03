#!/usr/bin/env python3
"""Build and inspect a single-root Skill ZIP; excludes the repository gallery."""

import argparse
import hashlib
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "zy-cinematic-realism"


def build(output_dir: Path) -> Path:
    match = re.search(r"Public edition:.*?v(\d+\.\d+\.\d+)", (SKILL / "SKILL.md").read_text(encoding="utf-8"))
    if match is None:
        raise ValueError("Missing public version in SKILL.md")
    version = match.group(1)
    # The existing root LICENSE has extra explanatory links; preserve both texts.
    for location in (ROOT / "LICENSE", SKILL / "LICENSE"):
        license_text = location.read_text(encoding="utf-8")
        if "SPDX-License-Identifier: CC-BY-NC-4.0" not in license_text or "Copyright (c) 2026 ZY / popopo-99" not in license_text:
            raise ValueError(f"License identifier or attribution missing: {location}")
    if (SKILL / "NOTICE.md").read_bytes() != (ROOT / "NOTICE.md").read_bytes():
        raise ValueError("Package NOTICE.md differs from repository NOTICE.md")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"zy-cinematic-realism-v{version}.zip"
    files = sorted(path for path in SKILL.rglob("*") if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"})
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            entry = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        names = set(archive.namelist())
        expected = {path.relative_to(ROOT).as_posix() for path in files}
        if names != expected or any(not name.startswith("zy-cinematic-realism/") for name in names):
            raise ValueError("ZIP has an unexpected root or file set")
        for path in files:
            if archive.read(path.relative_to(ROOT).as_posix()) != path.read_bytes():
                raise ValueError(f"Archive content differs: {path.name}")
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    target.with_suffix(".zip.sha256").write_text(f"{digest}  {target.name}\n", encoding="utf-8")
    print(f"Built {target.name}: {len(files)} files, {target.stat().st_size:,} bytes; single root and content verified")
    print(f"SHA256 {digest}")
    return target


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output_dir.resolve())
