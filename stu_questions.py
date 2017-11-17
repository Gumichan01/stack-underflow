
from math import sqrt

def stats_questions():
    """
        Preprocessing function that generates basics statistics about
        the score of the questions posted on stack Overflow from questions.csv.

        return: a n-tuple (min_score, max_score, average_score, variance, standard deviation)

        note: You need to call this function once
    """
    vmin   = 0
    vmax   = 0
    vtotal = 0
    n      = 0
    vtotal_sq = 0
    with open('data/questions.csv','r') as f:
        f.readline()    # I ignore the 1st line because is just metadata
        for line in f:
            v = int(line.strip('\n').split(',')[4])
            vmin = v if v < vmin else vmin
            vmax = v if v > vmax else vmax
            vtotal += v
            # Variance
            n += 1
            vtotal_sq += v ** 2
        avg = (vtotal / n)
        variance = ((1 / n) * vtotal_sq) - (avg ** 2)
        return (vmin, vmax, avg, variance, sqrt(variance))

def write_stats_in(stat, filename):
    with open(filename, "w+") as f:
        metadata = 'min, max, average, variance, standard deviation\n'
        s = str(stat).strip('()') + '\n'
        f.write(metadata)
        f.write(s)

qstats = stats_questions()
print(qstats)
