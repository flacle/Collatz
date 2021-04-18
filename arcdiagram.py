from mpmath import mp
mp.dps = 300 # adjust precision as needed
import functools
import drawSvg as draw
import math

# Binary opposite modulo function, returns 1 if 0 or 0 if 1
@functools.lru_cache(maxsize=None)
def bomod(x, y):
    if mp.fsub(x, mp.fmul(y, mp.floor(mp.fdiv(x, y)))) > 0:
        return 0
    else:
        return 1

# General n-adic valuation function in primitive form (a = n-adic number)
@functools.lru_cache(maxsize=None)
def v(n, a):
    k = 0
    # in Python, end of range function is exclusive, hence + 1
    for i in range(1, int(mp.floor(mp.fadd(mp.log(n, a), 1)))):
        k = k + bomod(n, mp.power(a, i))
    return k

# Parity Collatz function (see paper)
def c(n):
    nm = mp.fadd(n, mp.fmod(n, 2))
    d = mp.fdiv(nm, mp.power(2, v(nm, 2)))
    three = mp.power(3, v(mp.fadd(n, 1), 2))
    return int(mp.fsub(mp.fmul(d, three), mp.fmod(n, 2)))


# Returns nt, increments, and decrements of c(n) needed for the graph
def altC(n):
    inc = []
    dec = []
    nt  = []
    n_diff = n - 1
    inc.append(n_diff)
    nt.append(n)
    #print("n_diff ", n_diff)
    while n > 1:
        n_diff = n
        n = c(n)
        if n % 2 == 0:
            n_diff = n_diff - n
            dec.append(n_diff)
        else:
            n_diff = n - n_diff
            inc.append(n_diff)
        nt.append(n)
    return [nt, inc, dec]

# Creates the graph and returns the drawSVG object
def createGraph(nt, inc, dec, edgeLabels=False, hideNodes=False):
    # Define Canvas
    m = max(nt)
    width = (100 * m) / 2
    height = width
    s_width = math.log(m, 5)
    if s_width < 2:
        s_width = 2
    y_radius = 1
    d = draw.Drawing(width, height, origin = (0, 0), displayInline = False)

    # Define number line
    margin = nt[0] * 10
    nl_width = width - margin
    l_shift = margin
    y_line = height / 2
    d.append(draw.Line(l_shift, y_line, nl_width, y_line, stroke = 'black'))
    nl_steps = (width - 2 * margin) / (m - 1)

    # Define the nodes + text
    if hideNodes == False:
        y_radius = int(s_width * 4)
        for i in range(0, m):
            shift = l_shift + i * nl_steps
            d.append(draw.Circle(
                shift, y_line, y_radius,
                fill = 'white',
                stroke_width = s_width,
                stroke = 'black'))

            d.append(draw.Text(
                str(i + 1), y_radius,
                shift, 2 + y_line,
                center = True,
                fill = 'black'))

    # Define the RS arcs
    for n in range(0, len(nt)-1):
        start = l_shift + nt[n] * nl_steps - nl_steps
        end = l_shift + nt[n + 1] * nl_steps - nl_steps
        r = (end - start) / 2
        y = y_radius
        if end < start:
            y = -y_radius
        d.append(draw.Arc(
            start + r, y_line + y, r, 0, 180,
            cw = False,
            stroke = 'black',
            stroke_width = s_width,
            fill = 'none'))
        if edgeLabels == True:
            margin = y
            if margin < 0:
                margin = 2 * margin
            d.append(draw.Text(
                str(abs(nt[n + 1] - nt[n])), y_radius * 3,
                start + r, y_line + r - margin,
                center = True,
                fill = 'black'))

    # Render
    d.setRenderSize(width, height)
    return d

# Renders the arc diagram of parity reformulated Collatz function
def renderArcDiag(n, showGraph = True, edgeLabels = False, hideNodes = False):
    if n == 1:
        inc = []
        dec = []
        nt  = []
        inc.append(1)
        dec.append(1)
        nt.append(1)
        nt.append(2)
        nt.append(1)
    else:
        [nt, inc, dec] = altC(n)

    ups = 0
    for i in inc:
        ups = ups + i

    ups = ups - (n -1)

    downs = 0
    for d in dec:
        downs = downs + d

    print(nt)
    print("ups: ", ups)
    print("downs: ", downs)
    print("ups-downs: ", ups - downs)
    print("sum: ", ups+downs)

    d = createGraph(nt, inc, dec, edgeLabels, hideNodes)
    return showGraph and d

#  Example
renderArcDiag(25)#.saveSvg('n_0_25.svg')
