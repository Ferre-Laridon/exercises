import csv


def second(xs):
    return xs[1]


def get_runtime(row):
    result = row['runtimeMinutes']
    if result == r'\N':
        return 0
    else:
        try:
            return int(result)
        except:
            print(row)
            raise


with open('title-basics.tsv', encoding='utf-8') as input:
    reader = csv.DictReader(input, delimiter='\t', quoting=csv.QUOTE_NONE)
    results = [ (row['originalTitle'], get_runtime(row)) for row in reader if row['runtimeMinutes'] != r'\N' ]


results.sort(key=second, reverse=True)
top_100 = results[:100]

for title, get_runtime in top_100:
    print(f"{str(get_runtime).rjust(5)} {title}")
