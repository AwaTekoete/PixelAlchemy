"""
PixelAlchemy

create_collage.py

Erzeugt Bildcollagen für Dokumentation,
README und GitHub.
"""

from pathlib import Path

from PIL import Image


def create_collage(
    image_paths,
    rows,
    cols,
    output_path,
):
    """
    Erzeugt eine einfache Bildcollage.

    Parameters
    ----------
    image_paths : list
        Liste von Bildpfaden.

    rows : int
        Anzahl Zeilen.

    cols : int
        Anzahl Spalten.

    output_path : Path
        Zielpfad.
    """

    images = [
        Image.open(path)
        for path in image_paths
    ]

    width, height = images[0].size

    collage = Image.new(
        "RGB",
        (
            cols * width,
            rows * height,
        )
    )

    for index, image in enumerate(images):

        row = index // cols

        col = index % cols

        x = col * width

        y = row * height

        collage.paste(
            image,
            (x, y)
        )

    collage.save(
        output_path,
        quality=95
    )

    print(
        f"Gespeichert: {output_path}"
    )


if __name__ == "__main__":

    PROJECT_ROOT = Path.cwd()

    image_paths = [

        PROJECT_ROOT
        / "data"
        / "output"
        / "experiment_01"
        / "binstretch_02.jpg",

        PROJECT_ROOT
        / "data"
        / "output"
        / "experiment_01"
        / "binstretch_03.jpg",

        PROJECT_ROOT
        / "data"
        / "output"
        / "experiment_01"
        / "binstretch_04.jpg",

        PROJECT_ROOT
        / "data"
        / "output"
        / "experiment_01"
        / "binstretch_05.jpg",
    ]

    output_path = (
        PROJECT_ROOT
        / "docs"
        / "images"
        / "experiment_01_collage.jpg"
    )

    create_collage(
        image_paths=image_paths,
        rows=2,
        cols=2,
        output_path=output_path,
    )