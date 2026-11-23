# Supplying a Continent: Australian Logistics

**J.A.G. Playbook, Vol. 2** · Written by George Madouris · J.A.G. Playbook · Just Ask George

A plain words guide to Australian freight for the shipper and receiver, the driver and the operator, with 30 Excel tools and a forms pack. First edition, November 2026. Every figure was checked against its primary source in November 2026.

## What Is Here

| Folder or file | What it holds |
| --- | --- |
| `Supplying_a_Continent_Vol2_Working_Draft.pdf` | The latest full build of the book |
| `vol2/md` | The text, one file per part (front, A to G) |
| `vol2/tools` | The 30 tools (T01 to T30) and the forms pack |
| `vol2/diagrams` | Specs for the hand drawn pencil diagrams |
| `vol2/img` | Charts, rendered diagrams and the pencil sketches (`img/sketches`) |
| `vol2/sketches_part_*.md` | The Gemini prompts used for each part's sketches |
| `vol2/CHANGELOG_open_gaps.md` | Figures that could not be found from a primary source, for the toolkit page |
| `engine` | The build: Markdown to HTML to PDF |
| `brand` | The J.A.G. logo in colour and one colour black, and the script that draws it |

## Building the Book

```
cd engine && pnpm install
node diagrams.js ../vol2
python3 build.py ../vol2
node render.js ../Supplying_a_Continent_Vol2_Working_Draft.pdf
```

Sketches are placed by lines such as `[[sketch C01 third]]` in the Markdown (sizes: quarter, fifth, third, half). A sketch shows as a placeholder until its image is saved in `vol2/img/sketches`.

## Still to Do

- Toolkit web address and QR code, on the front page and in Part G
- Final licence wording once the free or paid decision is made
- Vol. 1, Warehouse Operations, to be rebuilt in this same system
