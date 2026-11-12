#!/usr/bin/env python3
"""Export descending even/odd print passes without modifying the source PDF."""
import argparse
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject


def export(source: Path, output_dir: Path, overwrite: bool = False) -> dict:
    source = source.resolve()
    reader = PdfReader(source)
    if reader.is_encrypted and not reader.decrypt(""):
        raise ValueError("Supply an unlocked PDF; this script does not accept passwords.")
    count = len(reader.pages)
    if not count:
        raise ValueError("The source PDF has no pages.")
    output_dir = output_dir.resolve()
    outputs = {
        "even": output_dir / f"{source.stem}-even-descending.pdf",
        "odd": output_dir / f"{source.stem}-odd-descending.pdf",
        "manifest": output_dir / f"{source.stem}-print-order.json",
    }
    for target in outputs.values():
        if target.resolve() == source:
            raise ValueError("An output path would overwrite the source PDF.")
        if target.exists() and not overwrite:
            raise FileExistsError(f"Output exists: {target}. Use --overwrite to replace exports.")
    output_dir.mkdir(parents=True, exist_ok=True)
    padded_count = count + count % 2
    report = {
        "source_filename": source.name,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_page_count": count,
        "print_set_page_count": padded_count,
        "sheets_per_pass": padded_count // 2,
        "pass_order": ["even", "odd"],
        "passes": {},
        "printing": [
            "A4 at actual size, one PDF page per sheet, single-sided for each pass.",
            "Print even first; reload the stack; print odd second.",
            "Print all pages; disable blank-page skipping, reverse order, and parity filters.",
            "Trial four pages first: output stacking, reload face, and feed edge vary by printer.",
            "Keep paired sheets aligned: highest even back receives highest odd front.",
            "These copies are for printing; use the complete source PDF for navigation.",
        ],
    }
    for parity, start in (("even", padded_count), ("odd", padded_count - 1)):
        sequence = list(range(start, 0, -2))
        writer = PdfWriter()
        entries = []
        for number in sequence:
            synthetic = number > count
            if synthetic:
                last = reader.pages[-1]
                blank = writer.add_blank_page(
                    width=float(last.mediabox.width), height=float(last.mediabox.height)
                )
                # Match the final front's physical display orientation.
                if last.rotation:
                    blank.rotate(last.rotation)
            else:
                writer.add_page(reader.pages[number - 1])
            entries.append({
                "physical_page": number,
                "source_page": None if synthetic else number,
                "synthetic_blank": synthetic,
            })
        writer.add_metadata({"/Title": f"{source.stem} - {parity} pages descending (print only)"})
        writer.root_object[NameObject("/ViewerPreferences")] = DictionaryObject({
            NameObject("/Duplex"): NameObject("/Simplex"),
            NameObject("/PrintScaling"): NameObject("/None"),
        })
        with outputs[parity].open("wb") as stream:
            writer.write(stream)
        if len(PdfReader(outputs[parity]).pages) != padded_count // 2:
            raise RuntimeError(f"Page-count verification failed for {parity} export.")
        report["passes"][parity] = {"file": outputs[parity].name, "pages": entries}
    outputs["manifest"].write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true", help="Replace existing generated exports.")
    args = parser.parse_args()
    try:
        report = export(args.source, args.output_dir, args.overwrite)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Error: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
