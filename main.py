# Sum up 13 November's world news in one image (news-image-01): writes the
# pre-rendered front page news.png to /output/entry.png. Deterministic, no
# network, stdlib only. Outside the grader's container, MAKEFUN_OUTPUT_DIR
# stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
src = HERE / "news.png"
dst = output_dir / "entry.png"
data = src.read_bytes()
assert data[:8] == b"\x89PNG\r\n\x1a\n", "news.png is not a PNG"
assert len(data) <= 1048576, "news.png exceeds the 1 MiB cap"
dst.write_bytes(data)
print(f"wrote {dst} ({len(data)} bytes, 1024x1024)")
