# Study guide source

`lessons.html` contains the supplementary lessons. `answer_details.py` adds reasoning to selected practice explanations. `build.py` reads those files plus the question data in the parent directory and generates printable lesson, question and answer HTML files. `original-retypeset.html` contains the original guide's re-typeset text, with Prompt embedded via local font files. The final PDF combines the original lesson pages, supplementary lessons, original review questions, both question sets, and then all answer sections. Code examples use a monospace font; mathematical symbols may use a fallback font.

Run `python public/guide/build.py` after editing the questions or supplementary lessons. Print the generated HTML to A4 PDF with browser print headers disabled, then combine the sections in the order above; update PDF bookmarks and page numbers before publishing. Prompt is licensed under the included OFL.txt.
