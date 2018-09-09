from datetime import date, timedelta
from subprocess import run
from argparse import ArgumentParser

# Number of commit needed for every colors
GITHUB_COLORS = [1, 5, 8, 13]

# List of (datetime.date.weekday, github_color)
GALERY = {
    'whale': [
        *map(lambda e: (e, 2), range(1, 3)),
        *map(lambda e: (e, 2), range(2, 5)),
        *map(lambda e: (e, 2), range(1, 3)),
        *map(lambda e: (e, 2), range(4, 6)),
        *map(lambda e: (e, 2), range(4, 6)),
        *map(lambda e: (e, 2), range(2, 6)),
        *map(lambda e: (e, 2), range(1, 6)),
        (6, 0),
        *map(lambda e: (e, 2), range(1, 6)),
        (6, 0), (0, 0),
        *map(lambda e: (e, 2), range(1, 6)),
        (6, 0),
        (1, 2),
        (2, 3),
        *map(lambda e: (e, 2), range(3, 6)),
        *map(lambda e: (e, 2), range(2, 5)),
    ],
}

GIT_COMMAND = ['git', 'commit', '--allow-empty', '--allow-empty-message',
                '--no-edit']

if __name__ == '__main__':
    parser = ArgumentParser(description='GitHub art')
    parser.add_argument('year', type=int)
    parser.add_argument('month', type=int)
    parser.add_argument('day', type=int)
    args = parser.parse_args()
    d = date(args.year, args.month, args.day)
    for pixel in GALERY['whale']:
        delta_days = (pixel[0] - d.weekday()) % 7
        if delta_days == 0: delta_days = 7
        d += timedelta(days=delta_days)
        for _ in range(GITHUB_COLORS[pixel[1]]):
            run(args=[*GIT_COMMAND, '--date='+d.strftime('%Y.%m.%d')])
