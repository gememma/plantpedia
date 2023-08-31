# Plantpedia

- A CLI program that stores and displays houseplant data (name, image, date, care)
- images are ascii-art representations from photos
- data is stored in text and image files

## Basic Features

- [x] display menu
- [x] read entry data from text/ image files
- [x] display an entry's text
- [x] create an entry
- [x] edit an entry
- [x] delete an entry
- [x] find an entry by common name and latin name

## Advanced Features

- [ ] generate html (possibly via markdown)
- [ ] display photos for each entry
- [ ] display watering dates according to watering frequency
- ~~display wikipedia info on plant~~
- [x] store data in CSV format
- [ ] replace Plant dataclass with pandas DataFrame


# Installation

To run plantpedia, you will need to have Python installed (by visiting the [Python Wiki](https://wiki.python.org/moin/BeginnersGuide/Download))
as well as the required libraries:

```bash
pip install colorama
pip install pandas
```