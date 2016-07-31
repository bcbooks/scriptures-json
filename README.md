## Scriptures in JSON

JSON editions of the LDS scriptures. Includes changes from the [2013 edition](https://www.lds.org/scriptures/new-edition?lang=eng).


### Contents

- `book-of-mormon.json`: version 2
    - Includes original headings, title page, testimonies
- `doctrine-and-covenants.json`: version 1
    - Does not include introduction (under copyright) or official declarations (OD 2 came out in 1978 and is under copyright)
- `pearl-of-great-price.json`: version 1
	- Includes the facsimiles
    - Does not include introduction (under copyright)
- Coming soon: Old Testament, New Testament


### Notes

- These JSON editions do not include copyrighted material (footnotes, chapter summaries, the Book of Mormon introduction, etc.).
- The Book of Mormon text comes from the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file (from December 2011, though I compared the exported text to the latest 2013 version and there were no differences). I exported the text, added additional content (title page, the book/chapter headings that were in the original text, testimonies), and made the [adjustments](https://www.lds.org/scriptures/adjustments?lang=eng) from the [2013 edition](https://www.lds.org/scriptures/new-edition?lang=eng) (which are small enough in relation to the whole that they don't fall under copyright, being minor typographic fixes, not anything substantial).
- The D&C text comes from the 2013 version of the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file. I exported the text, added the title page, and made the [2013 adjustments](https://www.lds.org/scriptures/adjustments?lang=eng).
- The Pearl of Great Price text comes from the 2013 version of the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file. I exported the text, added the title page, and made the [2013 adjustments](https://www.lds.org/scriptures/adjustments?lang=eng).


### License

These files are in the public domain.


### Changelog

- 2016-07-31: Doctrine & Covenants version 1 and Pearl of Great Price version 1
- 2016-07-16: Book of Mormon version 2 (removes LDS.org urls for verses, adds `lds_slug` to volume/book)
- 2016-07-15: Book of Mormon version 1
