from pprint import pprint as pp
import circlify as circ
circles = circ.circlify([19, 17, 13, 11, 7, 5, 3, 2, 1], show_enclosure=True)
pp(circles)
circ.bubbles(circles)