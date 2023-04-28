import numpy as np
import pandas as pd
verbs = [
    'above', 'accompany', 'address', 'advance', 'aim', 'align', 'anchor', 'approach', 'ascend', 'assemble',
    'attach', 'back', 'balance', 'bend', 'beside', 'block', 'boost', 'buckle', 'build', 'burrow',
    'buttress', 'bypass', 'calibrate', 'cease', 'center', 'charge', 'chase', 'circle', 'climb', 'close',
    'cluster', 'coast', 'collect', 'combine', 'compare', 'compass', 'complete', 'compress', 'concentrate', 'connect',
    'consider', 'contain', 'continue', 'contrast', 'convert', 'cover', 'cross', 'curve', 'cut', 'dash',
    'deal', 'defend', 'deliver', 'depart', 'descend', 'dig', 'disappear', 'disconnect', 'discover', 'dismount',
    'distribute', 'divide', 'dock', 'drag', 'drift', 'drop', 'end', 'enter', 'escalate', 'exit',
    'explore', 'extend', 'face', 'fall', 'fasten', 'fill', 'finish', 'fit', 'float', 'follow',
    'force', 'form', 'found', 'frame', 'gather', 'get', 'give', 'glide', 'go', 'grasp',
    'grip', 'grow', 'guide', 'hang', 'head', 'hold', 'hover', 'hug', 'illuminating', 'impact',
    'improve', 'include', 'insert', 'inspect', 'interface', 'interlock', 'interpose', 'intersect', 'intertwine', 'introduce',
    'investigate', 'join', 'jump', 'lead', 'leave', 'level', 'lift', 'link', 'list', 'load',
    'locate', 'lock', 'loop', 'lower', 'march', 'mark', 'meet', 'merge', 'miss', 'move',
    'navigate', 'offset', 'open', 'orbit', 'outline', 'overhang', 'overlap', 'overtake', 'pass', 'patrol',
    'pause', 'peer', 'perch', 'pivot', 'place', 'plant', 'plunge', 'point', 'position', 'power',
    'prepare', 'preserve', 'press', 'prevent', 'probe', 'process', 'progress', 'protect', 'protrude', 'pull',
    'push', 'put', 'race', 'reach', 'realize', 'rebound', 'recede', 'record', 'reduce', 'remove',
    'replace', 'replicate', 'reside', 'rest', 'ride', 'rise', 'roll', 'rotate', 'run', 'sail',
    'scale', 'scan', 'scatter', 'scramble', 'scrub', 'seal', 'secure', 'seize', 'set', 'shift',
    'shoot', 'sidle', 'skew', 'skim', 'slide', 'slip', 'slow', 'smash', 'snap', 'soar',
    'sort', 'space', 'spawn', 'speed', 'spin', 'spiral', 'split', 'spread', 'square', 'stabilize',
    'stand', 'start', 'station', 'steer', 'step', 'stick', 'stop', 'straddle', 'stretch', 'strike',
    'strive', 'structure', 'submerge', 'substitute', 'succeed', 'suffice', 'support', 'surmount', 'swing', 'switch',
    'tack', 'tail', 'take', 'tandem', 'tap', 'taper', 'target', 'taxi', 'terminate', 'test',
    'thrust', 'tighten', 'tip', 'touch', 'trace', 'track', 'traverse', 'trek', 'trim', 'trip',
    'tumble', 'turn', 'twist', 'unite', 'unload', 'unlock', 'unveil', 'uplift', 'vary', 'venture',
    'visit', 'wander', 'wedge', 'weigh', 'wheel', 'wind', 'withdraw', 'withstand', 'wrap', 'zipper'
]
adjectives = [
  'above-ground', 'aerial', 'aligned', 'ascending', 'atop', 'attached', 'bankside', 'below-ground', 'beneath', 'beside',
  'broadside', 'centered', 'cliffside', 'climbing', 'close-up', 'coastal', 'concentric', 'connected', 'contiguous', 'cornering',
  'cresting', 'cross-sectional', 'curled', 'curved', 'descending', 'distant', 'downhill', 'drooping', 'eastern', 'elevated',
  'enclosed', 'even', 'exposed', 'extended', 'extruded', 'falling', 'far-off', 'floating', 'flowing', 'focused',
  'foreshortened', 'forming', 'framed', 'frontal', 'gradual', 'growing', 'hanging', 'heightened', 'hidden', 'high-speed',
  'horizontal', 'inclined', 'intertwining', 'intersecting', 'joined', 'lateral', 'leaning', 'level', 'looping', 'low-angle',
  'lowered', 'moored', 'mountainous', 'narrow', 'near', 'offset', 'oncoming', 'opening', 'oriented', 'overhanging',
  'overlapping', 'oversized', 'panoramic', 'parallel', 'perched', 'perpendicular', 'pivoting', 'plunging', 'pointed', 'pointing',
  'prismatic', 'propped', 'proud', 'punctuated', 'reaching', 'receding', 'reflective', 'rising', 'rolling', 'rounded',
  'rugged', 'run-down', 'sandy', 'scenic', 'scrambling', 'shaded', 'shallow', 'shifting', 'shimmering', 'shrouded',
  'silhouetted', 'sloping', 'slow-moving', 'southern', 'spiral', 'split-level', 'spreading', 'springing', 'square', 'staggered',
  'stair-like', 'stark', 'steep', 'still', 'streaking', 'stretching', 'striking', 'structural', 'stylish', 'submerged',
  'surrounding', 'suspended', 'swaying', 'tapering', 'terraced', 'thick', 'tilted', 'top-heavy', 'towering', 'trailed',
  'tranquil', 'translucent', 'transparent', 'trellised', 'truncated', 'twisted', 'two-story', 'undulating', 'uphill', 'upscale',
  'upward', 'v-shaped', 'vaulted', 'veering', 'vertical', 'vibrant', 'viewable', 'visible', 'wavy', 'western',
  'wide-angle', 'widening', 'wide-open', 'wind-swept', 'winding', 'wing-like', 'winning', 'wispy', 'wrapping', 'zigzag'
]

adverbs = [
  'above', 'abreast', 'abroad', 'ahead', 'along', 'aloof', 'around', 'aside', 'asunder', 'athwart',
  'away', 'back', 'backward', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'by',
  'close', 'closer', 'closest', 'crosswise', 'downhill', 'downward', 'east', 'eastward', 'evenly', 'far',
  'farther', 'fore', 'forward', 'front', 'further', 'here', 'higher', 'inland', 'inside', 'later',
  'left', 'lengthwise', 'low', 'near', 'nearer', 'nearest', 'north', 'northeast', 'northerly', 'northward',
  'off', 'onward', 'out', 'outdoors', 'outside', 'over', 'overhead', 'past', 'perpendicularly', 'presently',
  'rather', 'rear', 'right', 'sideways', 'since', 'south', 'southeast', 'southerly', 'southward', 'still',
  'there', 'through', 'thru', 'together', 'transversely', 'uphill', 'upward', 'west', 'westward', 'within',
  'without', 'yearly', 'anew', 'apart', 'aside', 'astern', 'atop', 'away', 'barely', 'behindhand',
  'below', 'beneath', 'besides', 'betimes', 'bottom', 'carefully', 'clamorously', 'clockwise', 'considerably', 'conversely',
  'counter-clockwise', 'deep', 'deeply', 'deliberately', 'dexterously', 'down', 'downstream', 'downwind', 'due', 'elsewhere',
  'enough', 'eternally', 'everywhere', 'exactly', 'fast', 'fiercely', 'finally', 'forever', 'forth', 'furiously',
  'generally', 'hereabouts', 'home', 'hopelessly', 'hourly', 'how', 'insofar', 'inside-out', 'instantly', 'internally',
  'inward', 'lastly', 'laterally', 'leftwards', 'lightly', 'longitudinally', 'loudly', 'low-down', 'madly', 'meanwhile',
  'naturally', 'nearly', 'never', 'noisily', 'now', 'nowadays', 'nowhere', 'occasionally', 'oft', 'only',
  'outward', 'outwardly', 'painstakingly', 'partly', 'plumb', 'proudly', 'quick', 'radially', 'rarely', 'ratherly',
  'regularly', 'reluctantly', 'rightwards', 'rigidly', 'roughly', 'round', 'sideward', 'sidewards', 'simultaneously', 'slow',
  'smoothly', 'soft', 'somewhere', 'speedily', 'sporadically', 'squarely', 'steadfastly', 'supremely', 'swiftly', 'thereby',
  'thick', 'thin', 'throughout', 'togetherly', 'transversal', 'upwardly', 'vertically', 'vigilantly', 'vigorously', 'wholly'
]

words = verbs + adjectives + adverbs

words2 = words = ['approach', 'ascend', 'descend', 'direct', 'enter', 'exit', 'face', 'follow', 'head', 'lean', 'locate',
         'move', 'pass', 'point', 'reach', 'rise', 'run', 'settle', 'situate', 'stand', 'stay', 'stop', 'stretch',
         'surround', 'travel', 'turn', 'walk', 'watch', 'aboveground', 'adjacent', 'clockwise', 'counterclockwise',
         'downward', 'eastbound', 'elevated', 'horizontal', 'lateral', 'northbound', 'perpendicular', 'southbound',
         'upward', 'vertical', 'westbound', 'above', 'ahead', 'aloft', 'aside', 'away', 'backward', 'below',
         'downwards', 'eastwards', 'elsewhere', 'faraway', 'forward', 'here', 'high', 'inwards', 'leftwards',
         'nearby', 'nowhere', 'off', 'onwards', 'outwards', 'overboard', 'sideways', 'southwards', 'straight',
         'there', 'underfoot', 'upwards', 'westwards']

df = pd.DataFrame(words2)
df.to_csv("Relnet_data2.csv")
