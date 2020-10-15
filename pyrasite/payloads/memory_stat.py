from pympler import muppy
from pympler import summary


s = summary.summarize(muppy.get_objects())
summary.print_(s, limit=100)
