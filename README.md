## Scriptures in JSON

JSON editions of the LDS scriptures. Includes changes from the [2013 edition](https://www.lds.org/scriptures/new-edition?lang=eng).


### Contents

- `book-of-mormon.json`: version 4 (bom-4)
    - Includes original headings, title page, testimonies
- `doctrine-and-covenants.json`: version 3 (dc-3)
    - Does not include introduction (under copyright) or official declarations (OD 2 came out in 1978 and is under copyright)
- `pearl-of-great-price.json`: version 3 (pgp-3)
    - Includes the facsimiles
    - Does not include introduction (under copyright)
- `old-testament.json`: version 1 (ot-1)
    - KJV
    - Does not include JST
- `new-testament.json`: version 1 (nt-1)
    - KJV
    - Does not include JST
- `flat/*`: flat editions, only includes headings and verses
    - `flat/book-of-mormon-flat.json`: version 2 (source bom-4)
    - `flat/doctrine-and-covenants-flat.json`: version 2 (source dc-3)
    - `flat/pearl-of-great-price-flat.json`: version 2 (source pgp-3)
    - `flat/old-testament-flat.json`: version 1 (source ot-1)
    - `flat/new-testament-flat.json`: version 1 (source nt-1)
- `reference/*`: reference editions, with books, chapter numbers, and verse numbers as keys, only includes headings and verses
    - `reference/book-of-mormon-reference.json`: version 2 (source bom-4)
    - `reference/doctrine-and-covenants-reference.json`: version 2 (source dc-3)
    - `reference/pearl-of-great-price-reference.json`: version 2 (source pgp-3)
    - `reference/old-testament-reference.json`: version 1 (source ot-1)
    - `reference/new-testament-reference.json`: version 1 (source nt-1)
- `scripts/*`: Python scripts for exporting flat and reference editions


### Notes

- These JSON editions do not include copyrighted material (footnotes, chapter summaries, the Book of Mormon introduction, etc.).
- The Book of Mormon text comes from the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file (from December 2011, though I compared the exported text to the latest 2013 version and there were no differences). I exported the text, added additional content (title page, the book/chapter headings that were in the original text, testimonies), and made the [adjustments](https://www.lds.org/scriptures/adjustments?lang=eng) from the [2013 edition](https://www.lds.org/scriptures/new-edition?lang=eng) (which are small enough in relation to the whole that they don't fall under copyright, being minor typographic fixes, not anything substantial).
- The text for the Doctrine & Covenants, Pearl of Great Price, Old Testament, and New Testament comes from the 2013 version of the [Mormon Documentation Project](http://scriptures.nephi.org/) SQLite file. I exported the text, added title page information, and made the [2013 adjustments](https://www.lds.org/scriptures/adjustments?lang=eng).
- The flat editions are intended for easy iteration through verses, for textual/linguistic analysis or other similar domains. Not included: title pages, testimonies, LDS.org slugs, etc.
- The reference editions are intended for easy reference in code (`data['1 Nephi']['3']['7]`, for example). Not included: title pages, testimonies, LDS.org slugs, etc.
- Typographical note: Small caps are rendered as all caps, and italics are not distinguished. (I'm still trying to figure out the best way to handle formatting. At this point, I'm leaning toward having a `formatted` property with a copy of the verse text, using some kind of XML for formatting -- `and it <i>came</i> to pass, saith the <smcp>Lord</smcp> God`, or something like that.) Curly quotes have been straightened, though I'm already having second thoughts about that.


### License

These files are in the public domain.


### Changelog

#### 2016-10-02 (the big one)

- Book of Mormon version 4: 
    - Straightens curly quotes
    - 2 Nephi 4:23 — "night-time" -> "nighttime"
    - 2 Nephi 16:13 — "teiltree" -> "teil tree"
    - Omni 1:25 — "comes from the Lord;" -> "comes from the Lord:"
    - Mosiah 13:12 — "Thou shall not make" -> "Thou shalt not make"
    - Mosiah 16:5 — "Therefore, he is" -> "Therefore he is"
    - Mosiah 23:29 — "came to pass the the Lord" -> "came to pass that the Lord"
    - Mosiah 24:18 — "gathering the flocks together" -> "gathering their flocks together"
    - Alma 10:2 — "it was the same Aminadi" -> "it was that same Aminadi"
    - Alma 12:20 — "an immortal state that the soul" -> "an immortal state, that the soul"
    - Alma 12:33 — "repent and harden not" -> "repent, and harden not"
    - Alma 18:5 — "in a Great Spirit they supposed" -> "in a Great Spirit, they supposed"
    - Alma 19:18 — "to their astonishment they beheld" -> "to their astonishment, they beheld"
    - Alma 31:32 — "and also Amulek and Zeezrom" -> "and also Amulek and Zeezrom,"
    - Alma 58:39 — "and the Lord had supported them" -> "and the Lord has supported them"
    - Alma 62:50 — "and from all manner of afflictions and he" -> "and from all manner of afflictions, and he"
    - Helaman 6:10 — "land south was called Lehi and the land" -> "land south was called Lehi, and the land"
    - Helaman 7:2 — "in the land northward and did preach" -> "in the land northward, and did preach"
    - 3 Nephi 3:15 — "no wise" -> "nowise"
    - Mormon 5:5 — "And it came to pass" -> "But it came to pass"
    - Ether 7:9 — "the city Nehor and gave" -> "the city Nehor, and gave"
    - Ether 13:5 — "the house of Israel." -> "the house of Israel—"
    - Moroni 3:3 — "or, if he be" -> "or if he be"
- Doctrine & Covenants version 3
    - Straightens curly quotes
    - D&C 11:1 — "A Great and marvelous work" -> "A great and marvelous work"
    - D&C 18:18 — "Ask the Father in my name, in faith believing" -> "Ask the Father in my name in faith, believing"
    - D&C 20:12 — "today,and" -> "today, and"
    - D&C 38:24 — "practise" -> "practice"
    - D&C 43:1 — "O HEARKEN, ye elders" -> "O hearken, ye elders"
    - D&C 46:33 — "practise" -> "practice"
    - D&C 52:39 — "practised" -> "practiced"
    - D&C 59:23 — "even peace in this world and eternal life" -> "even peace in this world, and eternal life"
    - D&C 63:26 — "Caesar" -> "Cæsar" (2 instances)
    - D&C 75:1 — "Verily, verily I say" -> "Verily, verily, I say"
    - D&C 76:17 — "they who have done good in the resurrection" -> "they who have done good, in the resurrection"
    - D&C 84:1 — "A REVELATION of Jesus Christ" -> "A revelation of Jesus Christ"
    - D&C 98:25 — "hundred fold" -> "hundred-fold"
    - D&C 102 — Added signature
    - D&C 102:34 — "Martin Harris." -> "Martin Harris. After prayer the conference adjourned."
    - D&C 103:21 — "Joseph Smith, Jun." -> "Joseph Smith, Jun.,"
    - D&C 103:22 — "Joseph Smith, Jun." -> "Joseph Smith, Jun.,"
    - D&C 107:30 — "long suffering" -> "long-suffering"
    - D&C 109:34 — "and as all men sin forgive" -> "and as all men sin, forgive"
    - D&C 111:1 — "I, THE Lord" -> "I, the Lord"
    - D&C 112:30 — "the fulness of times." -> "the fulness of times,"
    - D&C 121:1 — "O GOD, where art thou?" -> "O God, where are thou?"
    - D&C 123:5 — "practised" -> "practiced"
    - D&C 124:48 — "practise" -> "practice"
    - D&C 124:71 — "fourfold" -> "four-fold"
    - D&C 128:6 — "Revelation 20: 12" -> "Revelation 20:12"
    - D&C 128:10 — "Matthew 16: 18" -> "Matthew 16:18"
    - D&C 128:13 — "1 Corinthians 15: 46" -> "1 Corinthians 15:46"
    - D&C 128:16 — "1 Corinthians 15: 29" -> "1 Corinthians 15:29"
    - D&C 130:3 — "John 14: 23" -> "John 14:23"
    - D&C 130:10 — "Revelation 2: 17" -> "Revelation 2:17"
    - D&C 132:55 — "hundredfold" -> "hundred-fold"
    - D&C 135:5 — ". . ." -> "…"
    - D&C 138:9 — "long-suffering" -> "longsuffering"
    - D&C 138:9 — "1 Peter 3: 18—20" -> "1 Peter 3:18–20"
    - D&C 138:10 — "1 Peter 4: 6" -> "1 Peter 4:6"
- Pearl of Great Price version 3
    - Straightens curly quotes
    - Moses 1:38 — "even so shall another come," -> "even so shall another come;"
    - Moses 4:13 — "fig-leaves" -> "fig leaves"
    - Moses 5:20 — "And Abel he" -> "And Abel, he"
    - Abraham 1:5 — "My fathers having turned" -> "My fathers, having turned"
    - JS–History 1:3 — "Vermont . . ." -> "Vermont. …"
    - JS–History 1:27 — "twenty—first" -> "twenty-first"
- Old Testament version 1 — initial release
- New Testament version 1 — initial release
- Book of Mormon flat edition version 2 — updated source to bom-4
- Doctrine & Covenants flat edition version 2 — updated source to dc-3
- Pearl of Great Price flat edition version 2 — updated source to pgp-3
- Old Testament flat edition version 1 — initial release (source ot-1)
- New Testament flat edition version 1 — initial release (source nt-1)
- Book of Mormon reference edition version 2 — updated source to bom-4
- Doctrine & Covenants reference edition version 2 — updated source to dc-3
- Pearl of Great Price reference edition version 2 — updated source to pgp-3
- Old Testament reference edition version 1 — initial release (source ot-1)
- New Testament reference edition version 1 — initial release (source nt-1)

#### 2016-10-01

- Book of Mormon version 3
    - Adds version information
- Doctrine & Covenants version 2
    - Adds version information
    - D&C 127 — adds signature
    - D&C 128 — adds signature
- Pearl of Great Price version 2
    - Adds version information
- Book of Mormon flat edition version 1 — initial release (source bom-3)
- Doctrine & Covenants flat edition version 1 — initial release (source dc-2)
- Pearl of Great Price flat edition version 1 — initial release (source pgp-2)
- Book of Mormon reference edition version 1 — initial release (source bom-3)
- Doctrine & Covenants reference edition version 1 — initial release (source dc-2)
- Pearl of Great Price reference edition version 1 — initial release (source pgp-2)

#### 2016-07-31

- Doctrine & Covenants version 1 — initial release
- Pearl of Great Price version 1 — initial release

#### 2016-07-16

- Book of Mormon version 2
    - Removes LDS.org URLs for verses
    - Adds `lds_slug` to volume/book

#### 2016-07-15

- Book of Mormon version 1 — initial release
