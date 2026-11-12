from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GENIMAGE_ROOT = ROOT.parent / "genimage"
GENIMAGE_SCRIPT = GENIMAGE_ROOT / "genimage.py"
BATCH_ROOT = GENIMAGE_ROOT / "generated" / "histschool" / "genimage_batch_01"
PROMPT_ROOT = BATCH_ROOT / "prompts"
IMAGE_OUT_DIR = BATCH_ROOT / "images"
VIDEO_OUT_DIR = BATCH_ROOT / "videos"
GLOBAL_STYLE_SUFFIX = (
    " Full color only, natural color photography, realistic skin tones, realistic classroom and gym colors, "
    "not sepia, not monochrome, not desaturated, not watercolor, not illustration, not painting, not sketch."
)
IMAGE_TEXT_SUFFIX = (
    " If any visible writing appears in the scene, it must be correct Czech text with proper accents, "
    "never English, never gibberish."
)
VIDEO_LANGUAGE_SUFFIX = (
    " All spoken dialogue and any audible counting or commands must be in Czech only, never English. "
    "Any visible writing must be correct Czech text with proper accents. "
    "Teacher voices must sound mature and role-appropriate; pupil voices must sound youthful and role-appropriate."
)


@dataclass(frozen=True)
class BatchItem:
    item_id: str
    kind: str
    out_name: str
    prompt: str
    seconds: int | None = None


IMAGES = [
    BatchItem(
        "IMG-001",
        "image",
        "img-001-standing-corner.png",
        "Photoreal documentary-style historical classroom in a Czech village school around 1900. One punished pupil stands motionless in the corner facing the wall, full body visible, realistic anatomy, natural daylight, respectful tone, non-erotic, non-graphic.",
    ),
    BatchItem(
        "IMG-006",
        "image",
        "img-006-kneeling-floor.png",
        "Photoreal documentary-style historical classroom around 1900. One punished pupil kneels upright on both knees in the corner facing the wall, on the wooden floor, torso vertical, full body visible, respectful tone, non-erotic, non-graphic.",
    ),
    BatchItem(
        "IMG-042",
        "image",
        "img-042-dunce-bench.png",
        "Photoreal documentary-style historical classroom around 1900. One isolated pupil sits alone at the donkey bench wearing a traditional dunce cap while the lesson continues, classmates and teacher visible, respectful reconstruction style, non-erotic, non-graphic.",
    ),
    BatchItem(
        "IMG-030",
        "image",
        "img-030-spanking-bench.png",
        "Photoreal documentary-style historical classroom around 1900. A pupil is positioned across a wooden desk or bench for a non-graphic historical spanking, teacher standing behind with a period instrument, clothed child, no exposed skin, no visible injury, respectful reconstruction style.",
    ),
    BatchItem(
        "IMG-033",
        "image",
        "img-033-hand-punishment.png",
        "Photoreal documentary-style historical classroom around 1900. A teacher administers a non-graphic hand punishment to a pupil holding one palm above the other in the prescribed historical pose, both faces visible, respectful reconstruction style, no visible injury.",
    ),
    BatchItem(
        "IMG-051",
        "image",
        "img-051-squat-exercise.png",
        "Photoreal documentary-style gym scene around 1900. A pupil performs a strict squat with thighs approximately horizontal and hands behind the head with fingers interlaced, full body visible, realistic anatomy, instructional style.",
    ),
    BatchItem(
        "IMG-052",
        "image",
        "img-052-pushup-standard.png",
        "Photoreal documentary-style gym scene around 1900. A schoolboy performs a strict full push-up with straight body line, chest touching the floor, hands wide, elbows out, feet pressed together, realistic anatomy, instructional style.",
    ),
    BatchItem(
        "IMG-053",
        "image",
        "img-053-pushup-knees.png",
        "Photoreal documentary-style gym scene around 1900. A schoolgirl performs a strict knee push-up with knees on the floor and lower legs raised and crossed, dominant foot underneath, chest touching the floor, realistic anatomy, instructional style.",
    ),
    BatchItem(
        "IMG-054",
        "image",
        "img-054-situp.png",
        "Photoreal documentary-style gym scene around 1900. A pupil performs a strict sit-up with fingers interlaced behind the head, elbows open, knees bent, feet together on the floor, elbows reaching the knees, realistic anatomy, instructional style.",
    ),
    BatchItem(
        "IMG-061",
        "image",
        "img-061-wall-sit.png",
        "Photoreal documentary-style gym or school corridor wall scene around 1900. A pupil holds a strict wall sit with back flat against the wall, thighs horizontal, knees at right angles, feet flat on the floor, hands behind the head with fingers interlaced, instructional style.",
    ),
    BatchItem(
        "IMG-062",
        "image",
        "img-062-step-up.png",
        "Photoreal documentary-style gym scene around 1900. A pupil performs a step-up onto a wooden platform, standing fully upright at the top, hands behind the head with fingers interlaced, realistic anatomy, instructional style.",
    ),
    BatchItem(
        "IMG-069",
        "image",
        "img-069-hand-raise.png",
        "Photoreal documentary-style historical classroom around 1900. One pupil sits at a wooden desk with one hand raised in a formal school gesture, waiting to be called on, classmates and blackboard visible, respectful reconstruction style.",
    ),
    BatchItem(
        "IMG-072",
        "image",
        "img-072-oral-exam-podium.png",
        "Photoreal documentary-style historical classroom around 1900. A pupil stands on the small podium near the blackboard during a formal oral examination, teacher facing the pupil, classmates seated, respectful reconstruction style.",
    ),
    BatchItem(
        "IMG-073",
        "image",
        "img-073-dictation.png",
        "Photoreal documentary-style historical classroom around 1900. The teacher dictates while pupils write quickly into notebooks, clearly legible Czech writing on the blackboard, focused silence, respectful reconstruction style.",
    ),
    BatchItem(
        "IMG-085",
        "image",
        "img-085-hand-inspection.png",
        "Photoreal documentary-style historical classroom around 1900. A teacher inspects a pupil's hands for cleanliness during class, close enough to show dirty palms or fingers, respectful reconstruction style.",
    ),
    BatchItem(
        "IMG-090",
        "image",
        "img-090-opening-prayer.png",
        "Photoreal documentary-style historical classroom around 1900. The whole class stands for the opening prayer, teacher leading, proper formal posture, blackboard and wooden benches visible, respectful reconstruction style.",
    ),
]

VIDEOS = [
    BatchItem(
        "VID-001",
        "video",
        "vid-001-go-to-corner.mp4",
        'Photoreal documentary-style historical classroom video in a Czech village school around 1900. A strict teacher points toward the corner and says in Czech: "Nováku, do kouta. Ruce za hlavu." The pupil walks to the corner, faces the wall, places both hands behind the head with fingers interlaced, lowers the head and stands completely still. Respectful tone, non-erotic, non-graphic.',
        seconds=8,
    ),
    BatchItem(
        "VID-013",
        "video",
        "vid-013-announce-spanking.mp4",
        'Photoreal documentary-style historical classroom video around 1900. A teacher formally announces a spanking in Czech: "Dostaneš tři rány přes dlaň. Nastav ruku." The pupil assumes the prescribed position and waits tensely. Respectful reconstruction style, non-erotic, non-graphic, no visible injury.',
        seconds=8,
    ),
    BatchItem(
        "VID-015",
        "video",
        "vid-015-one-stroke-return.mp4",
        "Photoreal documentary-style historical classroom video around 1900. A non-graphic historical punishment moment: one clear stroke, the pupil gasps and recoils, then returns to the proper punishment position. Respectful reconstruction style, no visible injury, no erotic framing.",
        seconds=8,
    ),
    BatchItem(
        "VID-019",
        "video",
        "vid-019-thank-you-for-punishment.mp4",
        'Photoreal documentary-style historical classroom or home video around 1900. After a punishment, the pupil straightens up, bows respectfully and says clearly in Czech: "Děkuji za trest za neposlušnost." Calm end of scene, respectful reconstruction style.',
        seconds=8,
    ),
    BatchItem(
        "VID-021",
        "video",
        "vid-021-pushup-standard.mp4",
        "Photoreal documentary-style gym video around 1900. A schoolboy performs several strict full push-ups: straight body line, chest touches the floor, elbows out, hands wide, feet pressed together. Instructional style, realistic anatomy.",
        seconds=8,
    ),
    BatchItem(
        "VID-022",
        "video",
        "vid-022-pushup-knees.mp4",
        "Photoreal documentary-style gym video around 1900. A schoolgirl performs several strict knee push-ups: knees on the floor, lower legs lifted and crossed, chest touches the floor, body aligned correctly. Instructional style, realistic anatomy.",
        seconds=8,
    ),
    BatchItem(
        "VID-023",
        "video",
        "vid-023-situp.mp4",
        "Photoreal documentary-style gym video around 1900. A pupil performs several strict sit-ups with fingers interlaced behind the head, elbows open, feet on the floor, elbows reaching the knees. Instructional style.",
        seconds=8,
    ),
    BatchItem(
        "VID-030",
        "video",
        "vid-030-wall-sit.mp4",
        "Photoreal documentary-style gym video around 1900. A pupil slides down a wall into a strict wall sit, back flat against the wall, thighs horizontal, knees at right angles, one approved arm position. Instructional style.",
        seconds=8,
    ),
    BatchItem(
        "VID-037",
        "video",
        "vid-037-hand-raise-called-on.mp4",
        'Photoreal documentary-style historical classroom video around 1900. One pupil raises a hand. The teacher points and says in Czech: "Nováku, mluv." The pupil stands beside the bench and begins to answer. Respectful reconstruction style.',
        seconds=8,
    ),
    BatchItem(
        "VID-038",
        "video",
        "vid-038-short-oral-exam.mp4",
        "Photoreal documentary-style historical classroom video around 1900. A pupil stands by the desk while the teacher asks one short question in Czech and the pupil answers aloud. Respectful reconstruction style.",
        seconds=8,
    ),
    BatchItem(
        "VID-040",
        "video",
        "vid-040-dictation.mp4",
        "Photoreal documentary-style historical classroom video around 1900. The teacher dictates one Czech sentence slowly and clearly while the pupils write under time pressure. Czech speech must be clearly audible. Respectful reconstruction style.",
        seconds=8,
    ),
]


def write_prompt_file(item: BatchItem) -> Path:
    PROMPT_ROOT.mkdir(parents=True, exist_ok=True)
    prompt_path = PROMPT_ROOT / f"{item.item_id}.txt"
    suffix = GLOBAL_STYLE_SUFFIX
    if item.kind == "image":
        suffix += IMAGE_TEXT_SUFFIX
    else:
        suffix += VIDEO_LANGUAGE_SUFFIX
    prompt_path.write_text(f"{item.prompt}{suffix}", encoding="utf-8")
    return prompt_path


def run_item(item: BatchItem) -> int:
    prompt_path = write_prompt_file(item)
    out_dir = IMAGE_OUT_DIR if item.kind == "image" else VIDEO_OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / item.out_name

    command = [
        sys.executable,
        str(GENIMAGE_SCRIPT),
        item.kind,
        "--prompt-file",
        str(prompt_path),
        "--out",
        str(out_path),
    ]

    if item.kind == "image":
        command += ["--model", "gpt-image-1.5"]
    else:
        command += ["--model", "sora-2-pro", "--seconds", str(item.seconds or 8)]

    print(f"Generating {item.kind} {item.item_id} -> {out_path}")
    completed = subprocess.run(command, cwd=GENIMAGE_ROOT)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--images-only", action="store_true")
    parser.add_argument("--videos-only", action="store_true")
    parser.add_argument("--only", nargs="*", default=[])
    args = parser.parse_args()

    failures: list[str] = []
    only_ids = {item_id.upper() for item_id in args.only}

    if not args.videos_only:
        for item in IMAGES:
            if only_ids and item.item_id.upper() not in only_ids:
                continue
            if run_item(item) != 0:
                failures.append(item.item_id)

    if not args.images_only:
        for item in VIDEOS:
            if only_ids and item.item_id.upper() not in only_ids:
                continue
            if run_item(item) != 0:
                failures.append(item.item_id)

    if failures:
        print("Failed items:")
        for item_id in failures:
            print(f"- {item_id}")
        return 1

    print("Batch finished successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
