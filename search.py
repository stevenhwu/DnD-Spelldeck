#!/usr/bin/python3

import argparse
import sys
import textwrap
import json

MAX_TEXT_LENGTH = 950

SPELLS_TRUNCATED = 0
SPELLS_TOTAL = 0

LEVEL_STRING = {
    0: '{school} cantrip {ritual}',
    1: '1st level {school} {ritual}',
    2: '2nd level {school} {ritual}',
    3: '3rd level {school} {ritual}',
    4: '4th level {school} {ritual}',
    5: '5th level {school} {ritual}',
    6: '6th level {school} {ritual}',
    7: '7th level {school} {ritual}',
    8: '8th level {school} {ritual}',
    9: '9th level {school} {ritual}',
}

with open('data/spells.json') as json_data:
    SPELLS = json.load(json_data)


def truncate_string(string, source, max_len=MAX_TEXT_LENGTH):
    rv = ""

    for sentence in string.split(".")[:-1]:
        if len(rv + sentence) < MAX_TEXT_LENGTH - 20:
            rv += sentence + "."
        else:
            rv += "...." + source
            break

    return rv


def print_spell(name, level, school, range, time, ritual, duration, components,
                material, text, classes, source=None, source_page=None, single_class=None, **kwargs):
    global SPELLS_TRUNCATED, SPELLS_TOTAL
    header = LEVEL_STRING[level].format(
        school=school.lower(), ritual='ritual' if ritual else '').strip()

    if material is not None:
        text = "Requires " + material + ". " + text

    new_text = truncate_string(text, source=source)

    # print(classes)
    source = classes
    source_page = None

    #if single_class is not None and len(single_class) == 1:
    #        source = single_class[0].capitalize() + " only"
    #if source_page is not None:
    #    source += ' page %d' % source_page


    if new_text != text:
        SPELLS_TRUNCATED += 1

    SPELLS_TOTAL += 1

    print("\\begin{spell}{%s}{%s}{%s}{%s}{%s}{%s}{%s}\n\n%s\n\n\\end{spell}\n" %
          (name, header, range, time, duration, ", ".join(components), source or '', textwrap.fill(new_text, 80)))


def get_spells(classes=None, no_classes=None, levels=None, schools=None, names=None, duration=None):
    classes = {i.lower() for i in classes} if classes is not None else None
    no_classes = {i.lower() for i in no_classes} if no_classes is not None else None
    schools = {i.lower() for i in schools} if schools is not None else None
    names = {i.lower() for i in names} if names is not None else None
    duration = {i.lower() for i in duration} if duration is not None else None

    return [
        (name, spell) for name, spell in sorted(SPELLS.items(), key=lambda x: x[0]) if
        (classes is None or len(classes & {i.lower() for i in spell['classes']}) > 0) and
        (no_classes is None or len(no_classes & {i.lower() for i in spell['classes']}) == 0) and
        (schools is None or spell['school'].lower() in schools) and
        (levels is None or spell['level'] in levels) and
        (duration is None or spell['duration'] in duration) and
        (names is None or name.lower() in names)
    ]


def parse_levels(levels):
    rv = None

    if levels is not None:
        rv = set()

        for level_spec in levels:
            tmp = level_spec.split('-')
            if len(tmp) == 1:
                rv.add(int(tmp[0]))
            elif len(tmp) == 2:
                rv |= set(range(int(tmp[0]), int(tmp[1]) + 1))

    return rv


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--class", type=str, action='append', dest='classes',
        help="only select spells for this class, can be used multiple times "
             "to select multiple classes."
    )
    parser.add_argument(
        "-d", "--no-class", type=str, action='append', dest='no_classes',
        help="only select spells NOT in this class, can be used multiple times "
             "to select multiple classes."
    )
    parser.add_argument(
        "-l", "--level", type=str, action='append', dest='levels',
        help="only select spells of a certain level, can be used multiple "
             "times and can contain a range such as `1-3`."
    )
    parser.add_argument(
        "-s", "--school", type=str, action='append', dest='schools',
        help="only select spells of a school, can be used multiple times."
    )
    parser.add_argument(
        "-n", "--name", type=str, action='append', dest='names',
        help="select spells with one of several given names."
    )
    parser.add_argument(
        "--duration", type=str, action='append', dest='duration'
    )
    args = parser.parse_args()

    for name, spell in get_spells(args.classes, args.no_classes,
                                  parse_levels(args.levels), args.schools, args.names, args.duration):
        print_spell(name, **spell, single_class=args.classes)

    print('Had to truncate %d out of %d spells at %d characters. Class %s' % (SPELLS_TRUNCATED, SPELLS_TOTAL, MAX_TEXT_LENGTH, args.classes), file=sys.stderr)
