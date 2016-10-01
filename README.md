## Scriptures in JSON

JSON editions of the LDS scriptures. Includes changes from the [2013 edition](https://www.lds.org/scriptures/new-edition?lang=eng).


### Contents

- `book-of-mormon.json`: version 3
    - Includes original headings, title page, testimonies
- `doctrine-and-covenants.json`: version 2
    - Does not include introduction (under copyright) or official declarations (OD 2 came out in 1978 and is under copyright)
- `pearl-of-great-price.json`: version 2
    - Includes the facsimiles
    - Does not include introduction (under copyright)
- `flat/*`: flat editions, only includes headings and verses
    - `flat/book-of-mormon-flat.json`: version 1, pulled from `book-of-mormon.json` version 3
    - `flat/doctrine-and-covenants-flat.json`: version 1, pulled from `doctrine-and-covenants.json` version 2
    - `flat/pearl-of-great-price-flat.json`: version 1, pulled from `pearl-of-great-price.json` version 2
- `reference/*`: reference editions, with books, chapter numbers, and verse numbers as keys, only includes headings and verses
    - `reference/book-of-mormon-reference.json`: version 1, pulled from `book-of-mormon.json` version 3
    - `reference/doctrine-and-covenants-reference.json`: version 1, pulled from `doctrine-and-covenants.json` version 2
    - `reference/pearl-of-great-price-reference.json`: version 1, pulled from `pearl-of-great-price.json` version 2
- `scripts/*`: Python scripts for exporting flat and reference editions
- Coming soon: Old Testament, New Testament


### Notes

- These JSON editions do not include copyrighted material (footnotes, chapter summaries, the Book of Mormon introduction, etc.).
- The Book of Mormon text comes from the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file (from December 2011, though I compared the exported text to the latest 2013 version and there were no differences). I exported the text, added additional content (title page, the book/chapter headings that were in the original text, testimonies), and made the [adjustments](https://www.lds.org/scriptures/adjustments?lang=eng) from the [2013 edition](https://www.lds.org/scriptures/new-edition?lang=eng) (which are small enough in relation to the whole that they don't fall under copyright, being minor typographic fixes, not anything substantial).
- The D&C text comes from the 2013 version of the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file. I exported the text, added the title page, and made the [2013 adjustments](https://www.lds.org/scriptures/adjustments?lang=eng).
- The Pearl of Great Price text comes from the 2013 version of the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file. I exported the text, added the title page, and made the [2013 adjustments](https://www.lds.org/scriptures/adjustments?lang=eng).
- The flat editions are intended for easy iteration through verses, for textual/linguistic analysis or other similar domains. Not included: title pages, testimonies, LDS.org slugs, etc.
- The reference editions are intended for easy reference in code (`data['1 Nephi']['3']['7]`, for example). Not included: title pages, testimonies, LDS.org slugs, etc.


### License

These files are in the public domain.


### Changelog

- 2016-10-01: Flat editions of Book of Mormon version 1, Doctrine & Covenants version 1, and Pearl of Great Price version 1; reference editions of Book of Mormon version 1, Doctrine & Covenants version 1, and Pearl of Great Price version 1; Book of Mormon version 3 (adds version info), Doctrine & Covenants version 2 (adds version info), Pearl of Great Price version 2 (adds version info)
- 2016-07-31: Doctrine & Covenants version 1 and Pearl of Great Price version 1
- 2016-07-16: Book of Mormon version 2 (removes LDS.org urls for verses, adds `lds_slug` to volume/book)
- 2016-07-15: Book of Mormon version 1
