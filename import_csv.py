import csv
import os
import string

from bs4 import BeautifulSoup


def save(title, content, date):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in title if c in valid_chars).replace(' ', '-').lower()
    f = open(os.path.join('flask_recipe', 'recipes', '%s.md' % filename), 'w')
    content=content.replace("<br>", "\n")

    content = BeautifulSoup(content, 'html.parser')

    f.write("title: %s\n" % title)
    f.write("date: %s\n" % date[0:10])
    f.write("tags: [paleo, grootmoeder]\n\n")

    f.write(content.get_text("\n").encode('utf-8'))
    f.close()


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

reader = unicode_csv_reader(open('recipes.csv'))
for row in reader:
    if row[1] != 'name':
        save(row[1], row[2], row[4])
