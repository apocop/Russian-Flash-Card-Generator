# Russian-Flash-Card-Generator

Create a [TSV](https://en.wikipedia.org/wiki/Tab-separated_values) file from [viaRussian](https://viarussian.com/) conversational notes which can be imported into [Anki](https://apps.ankiweb.net/) as Basic (optional reverse) flash cards.


### About

This tool was created to be used alongside [viaRussian](https://viarussian.com/). It is offered "as is".

### Setup:

1. Download and install the latest Python 3 release. See [python.org](https://www.python.org/) for instructions and file downloads.
2. Download program from GitHub.
   -  Click the green "Code" button in the right had corner
   -  Select *Download Zip* 


### Steps to Run:

1. Copy & Paste Russian conversation text into "conversation.txt". (See a sample of this in `conversation_sample.txt`.)
2. Open the `via_russian_flashcard_maker` folder.
3. Holding down the `Shift` key, right click in the folder and select **Open PowerShell window here**.
4. Run the program with the following command.

```
python generate_flashcards.py
```

> Tip! When typing the first few letters of "generate_flashcards.py". Press the **Tab** key to auto-complete the file name.  It may auto-complete  `generate_flashcards.py` as `.\generate_flashcards.py`. This is fine. :)

If you have more than one version of Python installed, you may have to specify Python 3 like so: 

```
python3 generate_flashcards.py
```

When successfully run, the program will :

- Create a `cards.tsv` file.
- Create a `junk_cards.tsv` file.
- Print a summary in the PowerShell window. For example:

```
--- Flash Card Maker ---
Total number of cards created: 444
Unused lines of text: 187
```
5.  After making any manual changes. Import `cards.tsv` into Anki.  See the [Anki manual](https://docs.ankiweb.net/importing.html) for more information.

### TSV Fields

The generated `cards.tsv` file consists of four columns, where each row will create two flash cards if using the Basic (optional reverse)
| Front | Back | Optional Reverse| Tags |
| --- | --- | --- | --- |
| a doctor | врач, доктор | Reverse | 5/03/2021 Natalia |
| I decided | Я решил | Reverse | 2/17/2021 Natalia |
| i got burned |я сгорел | Reverse | 3/29/2021 Natalia |


The TSV can easily be edited in any spreadsheet program such as Open Office, Google Sheets, Microsoft Excel, etc, but make sure that it's still saved as `*.tsv` and not a proprietary file type.

### Miscellaneous Notes

-  All flash card text is lowercased unless the Russian and English both contain a capital letter.
-  Card sides are created by splitting text at the hyphen: "-". (002D HYPHEN-MINUS).  This is too strong a hammer as sometimes "-" is actually used in Russian/English text.
-  Russian text corresponds to a side containing a match to the regex: `[а-яА-Я]`.  This means that any Cyrllic script language can be used.
-  English text corresponds to a side containing a match to the regex: `[a-zA-Z]`.  This means that any Latin Script language can be used.
-  If a `cards.tsv` and `junk_cards.tsv` already exists, the program will edit them rather than create new files.
-  This command line program has no optional flags
