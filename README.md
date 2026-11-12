# aquire-skills

## Study materials

[`create-study-materials`](create-study-materials/SKILL.md) creates explanatory, visually structured lessons and handbooks, with source coverage, worked exercises, and A4 binder-ready formatting.

- Palette: `#001524`, `#15616D`, `#FFECD1`, `#FF7D00`, `#78290F`.
- Printing: mirrored 20 mm inside / 18 mm outside margins; odd-page chapter starts; cover and contents each have a blank reverse.
- PDF outputs: complete reading copy, even pages descending, odd pages descending, and a print-order manifest. Print even first, reload the stack, then print odd. Test four pages to establish your printer's reload orientation; disable reverse ordering and blank-page skipping.

The skill folder uses the standard `SKILL.md` entrypoint. It can also be attached to a chat with: “Follow this skill to create study materials for [topic], using [references], so I can [learning goal].”

The PDF helper requires Python and `pypdf`:

```bash
python create-study-materials/scripts/export_manual_duplex.py report.pdf --output-dir exports
```

For an odd page count, the helper inserts a blank final even back into the print set only, keeping the complete PDF unchanged. Existing output files are protected unless `--overwrite` is specified.
