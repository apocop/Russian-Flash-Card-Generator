# python3
"""
Generate TSV for Anki Flash cards from Via Russian Conversation practice notes.
Version 1.0
"""


import re

class Flashcard:
  "Flash Card Class"

  def __init__(self):
    self.line = None
    self.russian = None
    self.english = None
    self.date = None
    self.tutor = None
    self.junk = False
    self.header = None
    self.error = ''
    self.sides = []


  def fill_out(self, line, header):
    """Fill out a new flash card"""
    self.line = line
    self.header = header
    self.create_sides()
    self.generate_tags()

  def create_sides(self):
    """Create flash card sides."""

    self.sides = self.line.split('-')
    if len(self.sides) == 2:
      if normalizer.is_cyrillic(self.sides[0]) and normalizer.is_latin(self.sides[1]):
        self.russian = self.sides[0].strip()
        self.english = self.sides[1].strip()
      elif normalizer.is_cyrillic(self.sides[1]) and normalizer.is_latin(self.sides[0]):
        self.russian = self.sides[1].strip()
        self.english = self.sides[0].strip()
      else:
        self.junk = True
        self.error += "Can't separate English from Russian"
    elif len(self.sides) != 2:
      self.junk = True
      self.error += f'Card needs 2 sides, but has {len(self.sides)}.'
    if self.english and self.russian:
      self.english, self.russian = normalizer.normalize_capitalization(self.english, self.russian)

  def generate_tags(self):
    if self.header:
      match = re.match(normalizer.lesson_header, self.header)
      if match:
        month = MONTHS[match.group('month').title()]
        self.date = f"{month}/{match.group('day')}/{match.group('year')}"
        self.tutor = match.group('tutor')
    else:
      self.error += 'Card has no header'

class Generator:
  def __init__(self):
    self.card_deck = []
    self.junk_deck = []
    self.last_header = None

  def print_report(self):
    """Print a final report about the cards."""

    print('\n--- Flash Card Maker ---')
    print(f'Total number of cards created: {len(self.card_deck)}')
    print(f'Unused lines of text: {len(self.junk_deck)}')

  def cards_to_tsv(self, path):
    """Export valid flashcards to TSV"""
  
    flashcards = ''
    for card in self.card_deck:
      flashcards += f'{card.english}\t{card.russian}\tReverse\t{card.date} {card.tutor}\n'
    with open(path, 'w', encoding='utf-8') as f:
      f.write(flashcards)

  def generate_flashcards(self, path):
    with open(path, 'r', encoding='utf-8') as f:
      lines = [line for line in f.read().splitlines() if line.strip() != '']
    for line in lines:
      if normalizer.is_lesson_header(line):
        self.last_header = line
      else:
        card = Flashcard()
        card.fill_out(line, self.last_header)
        if card.junk:
          self.junk_deck.append(card)
        else:
          self.card_deck.append(card)
    self.card_deck.sort(key=lambda card: card.english.lower())
    self.junk_deck.sort(key=lambda card: card.error.lower())
    self.print_report()

  def junk_to_tsv(self, path):
    junk_cards = 'Error\tLine\tSides\tDate\tTutor\n'
    for card in self.junk_deck:
      junk_cards += f'{card.error}\t{card.line}\t{card.sides}\t{card.date}\t{card.tutor}\n'
    with open(path, 'w', encoding='utf-8') as f:
      f.write(junk_cards)

class Normalizer():
  def __init__(self):
    self.cyrllic = '[а-яА-Я]'
    self.latin = '[a-zA-Z]'
    self.lesson_header = r'(?P<day>[0-9]{,2})\s*(?P<month>[a-zA-Z]*)\s.*(?P<year>20[0-9]{,2})\s*(?P<tutor>[a-zA-Z]+)'

  def is_cyrillic(self, string):
    return bool(re.search(self.cyrllic, string))

  def is_latin(self, string):
    return bool(re.search(self.latin, string))

  def is_lesson_header(self, string):
    return bool(re.match(self.lesson_header, string))

  def normalize(self, string):
    pass

  def normalize_capitalization(self, en, ru):
    """Normalize flashcard side capitalization."""
    if not en.islower() and not ru.islower():
      return en, ru
    else:
      return en.lower(), ru.lower()


MONTHS = {
  'January': 1,
  'February': 2,
  'March': 3,
  'April': 4,
  'May': 5,
  'June': 6,
  'July': 7,
  'August': 8,
  'September': 9,
  'October': 10,
  'November': 11,
  'December': 12
}

path = r'./conversation.txt'
export_path = r'./cards.tsv'
junk_path = r'./junk_cards.tsv'
normalizer = Normalizer()
generator = Generator()
generator.generate_flashcards(path)
generator.cards_to_tsv(export_path)
generator.junk_to_tsv(junk_path)
