#!/usr/bin/env python3

# NOTE could do all of this or just find and replace
# with a lot of if statement.
# Find and replace would probably be a lot more efficient
# def convert(tex: str) -> str:
#     """Convert passed in TeX to unicode

#     >>> convert('\\forall x \\in \\R')
#     '∀x∈ℝ'
#     """
#     for i in range(len(tex)):
#         if tex[i] == '\\':
#             command, length = get_command(tex, i)
#             # do if operations here like:
#             # if command == '\\forall': ... replace
#     output = tex
#     return output


# def get_command(tex: str, index: int) -> (str, int):
#     """Return the TeX command starting at the current index

#     >>> get_command('01\\forall', 2)
#     '\\forall'
#     >>> get_command('01\\forall\\exists', 2)
#     '\\forall'
#     >>> get_command('01\\forall \\exists', 2)
#     '\\forall'
#     """
#     command_so_far = ''

#     for i in range(index, len(tex)):
#         if tex[i] == ' ' or (tex[i] == '\\' and i > index + 1):
#             return command_so_far

#         command_so_far += tex[i]

#     return command_so_far


# Option 2: as written at the start of the file
def convert_replace(tex: str) -> str:
    """Replace tex commands with their unicode symbols"""
    # quantifiers
    tex = tex.replace('\\forall', '∀')
    tex = tex.replace('\\exists', '∃')

    # comparison operators
    tex = tex.replace('\\geq', '≥')
    tex = tex.replace('\\leq', '≥')
    tex = tex.replace('\\neq', '≠')
    tex = tex.replace('\\equiv', '≡')
    tex = tex.replace('\\nequiv', '≢')

    # logical operators
    # in, not in, contains, does not contain
    tex = tex.replace('\\in', '∈')
    tex = tex.replace('\\lnot', '¬')
    tex = tex.replace('\\land', '∧')
    tex = tex.replace('\\wedge', '∧')
    tex = tex.replace('\\lor', '∨')
    tex = tex.replace('\\vee', '∨')
    # tex = tex.replace('\\contains')

    # TODO have these from the longest to the shortest so
    # there's no overlap
    tex = mathcal(tex)
    tex = mathbr(tex)
    tex = mathbfit(tex)
    tex = superscript(tex)
    tex = subscript(tex)
    tex = greek_letters(tex)
    tex = blackboard(tex)
    tex = normal_letters(tex)

    return tex


def blackboard(tex: str) -> str:
    """blackboard letters"""
    tex = tex.replace('\\mathbb{A}', '𝔸')
    tex = tex.replace('\\mathbb{B}', '𝔹')
    tex = tex.replace('\\mathbb{C}', 'ℂ')
    tex = tex.replace('\\mathbb{D}', '𝔻')
    tex = tex.replace('\\mathbb{E}', '𝔼')
    tex = tex.replace('\\mathbb{F}', '𝔽')
    tex = tex.replace('\\mathbb{G}', '𝔾')
    tex = tex.replace('\\mathbb{H}', 'ℍ')
    tex = tex.replace('\\mathbb{I}', '𝕀')
    tex = tex.replace('\\mathbb{J}', '𝕁')
    tex = tex.replace('\\mathbb{K}', '𝕂')
    tex = tex.replace('\\mathbb{L}', '𝕃')
    tex = tex.replace('\\mathbb{M}', '𝕄')
    tex = tex.replace('\\mathbb{N}', 'ℕ')
    tex = tex.replace('\\mathbb{O}', '𝕆')
    tex = tex.replace('\\mathbb{P}', 'ℙ')
    tex = tex.replace('\\mathbb{Q}', 'ℚ')
    tex = tex.replace('\\mathbb{R}', 'ℝ')
    tex = tex.replace('\\mathbb{S}', '𝕊')
    tex = tex.replace('\\mathbb{T}', '𝕋')
    tex = tex.replace('\\mathbb{U}', '𝕌')
    tex = tex.replace('\\mathbb{V}', '𝕍')
    tex = tex.replace('\\mathbb{W}', '𝕎')
    tex = tex.replace('\\mathbb{X}', '𝕏')
    tex = tex.replace('\\mathbb{Y}', '𝕐')
    tex = tex.replace('\\mathbb{Z}', 'ℤ')

    tex = tex.replace('\\mathbb{a}', '𝕒')
    tex = tex.replace('\\mathbb{b}', '𝕓')
    tex = tex.replace('\\mathbb{c}', '𝕔')
    tex = tex.replace('\\mathbb{d}', '𝕕')
    tex = tex.replace('\\mathbb{e}', '𝕖')
    tex = tex.replace('\\mathbb{f}', '𝕗')
    tex = tex.replace('\\mathbb{g}', '𝕘')
    tex = tex.replace('\\mathbb{h}', '𝕙')
    tex = tex.replace('\\mathbb{i}', '𝕚')
    tex = tex.replace('\\mathbb{j}', '𝕛')
    tex = tex.replace('\\mathbb{k}', '𝕜')
    tex = tex.replace('\\mathbb{l}', '𝕝')
    tex = tex.replace('\\mathbb{m}', '𝕞')
    tex = tex.replace('\\mathbb{n}', '𝕟')
    tex = tex.replace('\\mathbb{o}', '𝕠')
    tex = tex.replace('\\mathbb{p}', '𝕡')
    tex = tex.replace('\\mathbb{q}', '𝕢')
    tex = tex.replace('\\mathbb{r}', '𝕣')
    tex = tex.replace('\\mathbb{s}', '𝕤')
    tex = tex.replace('\\mathbb{t}', '𝕥')
    tex = tex.replace('\\mathbb{u}', '𝕦')
    tex = tex.replace('\\mathbb{v}', '𝕧')
    tex = tex.replace('\\mathbb{w}', '𝕨')
    tex = tex.replace('\\mathbb{x}', '𝕩')
    tex = tex.replace('\\mathbb{y}', '𝕪')
    tex = tex.replace('\\mathbb{z}', '𝕫')

    tex = tex.replace('\\mathbb A', '𝔸')
    tex = tex.replace('\\mathbb B', '𝔹')
    tex = tex.replace('\\mathbb C', 'ℂ')
    tex = tex.replace('\\mathbb D', '𝔻')
    tex = tex.replace('\\mathbb E', '𝔼')
    tex = tex.replace('\\mathbb F', '𝔽')
    tex = tex.replace('\\mathbb G', '𝔾')
    tex = tex.replace('\\mathbb H', 'ℍ')
    tex = tex.replace('\\mathbb I', '𝕀')
    tex = tex.replace('\\mathbb J', '𝕁')
    tex = tex.replace('\\mathbb K', '𝕂')
    tex = tex.replace('\\mathbb L', '𝕃')
    tex = tex.replace('\\mathbb M', '𝕄')
    tex = tex.replace('\\mathbb N', 'ℕ')
    tex = tex.replace('\\mathbb O', '𝕆')
    tex = tex.replace('\\mathbb P', 'ℙ')
    tex = tex.replace('\\mathbb Q', 'ℚ')
    tex = tex.replace('\\mathbb R', 'ℝ')
    tex = tex.replace('\\mathbb S', '𝕊')
    tex = tex.replace('\\mathbb T', '𝕋')
    tex = tex.replace('\\mathbb U', '𝕌')
    tex = tex.replace('\\mathbb V', '𝕍')
    tex = tex.replace('\\mathbb W', '𝕎')
    tex = tex.replace('\\mathbb X', '𝕏')
    tex = tex.replace('\\mathbb Y', '𝕐')
    tex = tex.replace('\\mathbb Z', 'ℤ')

    tex = tex.replace('\\mathbb a', '𝕒')
    tex = tex.replace('\\mathbb b', '𝕓')
    tex = tex.replace('\\mathbb c', '𝕔')
    tex = tex.replace('\\mathbb d', '𝕕')
    tex = tex.replace('\\mathbb e', '𝕖')
    tex = tex.replace('\\mathbb f', '𝕗')
    tex = tex.replace('\\mathbb g', '𝕘')
    tex = tex.replace('\\mathbb h', '𝕙')
    tex = tex.replace('\\mathbb i', '𝕚')
    tex = tex.replace('\\mathbb j', '𝕛')
    tex = tex.replace('\\mathbb k', '𝕜')
    tex = tex.replace('\\mathbb l', '𝕝')
    tex = tex.replace('\\mathbb m', '𝕞')
    tex = tex.replace('\\mathbb n', '𝕟')
    tex = tex.replace('\\mathbb o', '𝕠')
    tex = tex.replace('\\mathbb p', '𝕡')
    tex = tex.replace('\\mathbb q', '𝕢')
    tex = tex.replace('\\mathbb r', '𝕣')
    tex = tex.replace('\\mathbb s', '𝕤')
    tex = tex.replace('\\mathbb t', '𝕥')
    tex = tex.replace('\\mathbb u', '𝕦')
    tex = tex.replace('\\mathbb v', '𝕧')
    tex = tex.replace('\\mathbb w', '𝕨')
    tex = tex.replace('\\mathbb x', '𝕩')
    tex = tex.replace('\\mathbb y', '𝕪')
    tex = tex.replace('\\mathbb z', '𝕫')

    # tex = tex.replace('\\A', '𝔸')
    # tex = tex.replace('\\B', '𝔹')
    # tex = tex.replace('\\C', 'ℂ')
    # tex = tex.replace('\\D', '𝔻')
    # tex = tex.replace('\\E', '𝔼')
    # tex = tex.replace('\\F', '𝔽')
    # tex = tex.replace('\\G', '𝔾')
    # tex = tex.replace('\\H', 'ℍ')
    # tex = tex.replace('\\I', '𝕀')
    # tex = tex.replace('\\J', '𝕁')
    # tex = tex.replace('\\K', '𝕂')
    # tex = tex.replace('\\L', '𝕃')
    # tex = tex.replace('\\M', '𝕄')
    tex = tex.replace('\\N', 'ℕ')
    # tex = tex.replace('\\O', '𝕆')
    # tex = tex.replace('\\P', 'ℙ')
    # tex = tex.replace('\\Q', 'ℚ')
    tex = tex.replace('\\R', 'ℝ')
    # tex = tex.replace('\\S', '𝕊')
    # tex = tex.replace('\\T', '𝕋')
    # tex = tex.replace('\\U', '𝕌')
    # tex = tex.replace('\\V', '𝕍')
    # tex = tex.replace('\\W', '𝕎')
    # tex = tex.replace('\\X', '𝕏')
    # tex = tex.replace('\\Y', '𝕐')
    # tex = tex.replace('\\Z', 'ℤ')

    # tex = tex.replace('\\a', '𝕒')
    # tex = tex.replace('\\b', '𝕓')
    # tex = tex.replace('\\c', '𝕔')
    # tex = tex.replace('\\d', '𝕕')
    # tex = tex.replace('\\e', '𝕖')
    # tex = tex.replace('\\f', '𝕗')
    # tex = tex.replace('\\g', '𝕘')
    # tex = tex.replace('\\h', '𝕙')
    # tex = tex.replace('\\i', '𝕚')
    # tex = tex.replace('\\j', '𝕛')
    # tex = tex.replace('\\k', '𝕜')
    # tex = tex.replace('\\l', '𝕝')
    # tex = tex.replace('\\m', '𝕞')
    # tex = tex.replace('\\n', '𝕟')
    # tex = tex.replace('\\o', '𝕠')
    # tex = tex.replace('\\p', '𝕡')
    # tex = tex.replace('\\q', '𝕢')
    # tex = tex.replace('\\r', '𝕣')
    # tex = tex.replace('\\s', '𝕤')
    # tex = tex.replace('\\t', '𝕥')
    # tex = tex.replace('\\u', '𝕦')
    # tex = tex.replace('\\v', '𝕧')
    # tex = tex.replace('\\w', '𝕨')
    # tex = tex.replace('\\x', '𝕩')
    # tex = tex.replace('\\y', '𝕪')
    # tex = tex.replace('\\z', '𝕫')

    # tex = tex.replace('\\mathbb{0}', '𝟘')
    # tex = tex.replace('\\mathbb{1}', '𝟙')
    # tex = tex.replace('\\mathbb{2}', '𝟚')
    # tex = tex.replace('\\mathbb{3}', '𝟛')
    # tex = tex.replace('\\mathbb{4}', '𝟜')
    # tex = tex.replace('\\mathbb{5}', '𝟝')
    # tex = tex.replace('\\mathbb{6}', '𝟞')
    # tex = tex.replace('\\mathbb{7}', '𝟟')
    # tex = tex.replace('\\mathbb{8}', '𝟠')
    # tex = tex.replace('\\mathbb{9}', '𝟡')

    return tex


def mathcal(tex: str) -> str:
    tex = tex.replace('\\mathcal{A}', '𝒜')
    tex = tex.replace('\\mathcal{B}', 'ℬ')
    tex = tex.replace('\\mathcal{C}', '𝒞')
    tex = tex.replace('\\mathcal{D}', '𝒟')
    tex = tex.replace('\\mathcal{E}', 'ℰ')
    tex = tex.replace('\\mathcal{F}', 'ℱ')
    tex = tex.replace('\\mathcal{G}', '𝒢')
    tex = tex.replace('\\mathcal{H}', 'ℋ')
    tex = tex.replace('\\mathcal{I}', 'ℐ')
    tex = tex.replace('\\mathcal{J}', '𝒥')
    tex = tex.replace('\\mathcal{K}', '𝒦')
    tex = tex.replace('\\mathcal{L}', 'ℒ')
    tex = tex.replace('\\mathcal{M}', 'ℳ')
    tex = tex.replace('\\mathcal{N}', '𝒩')
    tex = tex.replace('\\mathcal{O}', '𝒪')
    tex = tex.replace('\\mathcal{P}', '𝒫')
    tex = tex.replace('\\mathcal{Q}', '𝒬')
    tex = tex.replace('\\mathcal{R}', 'ℛ')
    tex = tex.replace('\\mathcal{S}', '𝒮')
    tex = tex.replace('\\mathcal{T}', '𝒯')
    tex = tex.replace('\\mathcal{U}', '𝒰')
    tex = tex.replace('\\mathcal{V}', '𝒱')
    tex = tex.replace('\\mathcal{W}', '𝒲')
    tex = tex.replace('\\mathcal{X}', '𝒳')
    tex = tex.replace('\\mathcal{Y}', '𝒴')
    tex = tex.replace('\\mathcal{Z}', '𝒵')

    tex = tex.replace('\\mathcal{a}', '𝒶')
    tex = tex.replace('\\mathcal{b}', '𝒷')
    tex = tex.replace('\\mathcal{c}', '𝒸')
    tex = tex.replace('\\mathcal{d}', '𝒹')
    tex = tex.replace('\\mathcal{e}', 'ℯ')
    tex = tex.replace('\\mathcal{f}', '𝒻')
    tex = tex.replace('\\mathcal{g}', 'ℊ')
    tex = tex.replace('\\mathcal{h}', '𝒽')
    tex = tex.replace('\\mathcal{i}', '𝒾')
    tex = tex.replace('\\mathcal{j}', '𝒿')
    tex = tex.replace('\\mathcal{k}', '𝓀')
    tex = tex.replace('\\mathcal{l}', '𝓁')
    tex = tex.replace('\\mathcal{m}', '𝓂')
    tex = tex.replace('\\mathcal{n}', '𝓃')
    tex = tex.replace('\\mathcal{o}', 'ℴ')
    tex = tex.replace('\\mathcal{p}', '𝓅')
    tex = tex.replace('\\mathcal{q}', '𝓆')
    tex = tex.replace('\\mathcal{r}', '𝓇')
    tex = tex.replace('\\mathcal{s}', '𝓈')
    tex = tex.replace('\\mathcal{t}', '𝓉')
    tex = tex.replace('\\mathcal{u}', '𝓊')
    tex = tex.replace('\\mathcal{v}', '𝓋')
    tex = tex.replace('\\mathcal{w}', '𝓌')
    tex = tex.replace('\\mathcal{x}', '𝓍')
    tex = tex.replace('\\mathcal{y}', '𝓎')
    tex = tex.replace('\\mathcal{z}', '𝓏')

    return tex


def mathbr(tex: str) -> str:
    tex = tex.replace('\\mathbf{A}'                , '𝐀')
    tex = tex.replace('\\mathbf{B}'                , '𝐁')
    tex = tex.replace('\\mathbf{C}'                , '𝐂')
    tex = tex.replace('\\mathbf{D}'                , '𝐃')
    tex = tex.replace('\\mathbf{E}'                , '𝐄')
    tex = tex.replace('\\mathbf{F}'                , '𝐅')
    tex = tex.replace('\\mathbf{G}'                , '𝐆')
    tex = tex.replace('\\mathbf{H}'                , '𝐇')
    tex = tex.replace('\\mathbf{I}'                , '𝐈')
    tex = tex.replace('\\mathbf{J}'                , '𝐉')
    tex = tex.replace('\\mathbf{K}'                , '𝐊')
    tex = tex.replace('\\mathbf{L}'                , '𝐋')
    tex = tex.replace('\\mathbf{M}'                , '𝐌')
    tex = tex.replace('\\mathbf{N}'                , '𝐍')
    tex = tex.replace('\\mathbf{O}'                , '𝐎')
    tex = tex.replace('\\mathbf{P}'                , '𝐏')
    tex = tex.replace('\\mathbf{Q}'                , '𝐐')
    tex = tex.replace('\\mathbf{R}'                , '𝐑')
    tex = tex.replace('\\mathbf{S}'                , '𝐒')
    tex = tex.replace('\\mathbf{T}'                , '𝐓')
    tex = tex.replace('\\mathbf{U}'                , '𝐔')
    tex = tex.replace('\\mathbf{V}'                , '𝐕')
    tex = tex.replace('\\mathbf{W}'                , '𝐖')
    tex = tex.replace('\\mathbf{X}'                , '𝐗')
    tex = tex.replace('\\mathbf{Y}'                , '𝐘')
    tex = tex.replace('\\mathbf{Z}'                , '𝐙')
    tex = tex.replace('\\mathbf{a}'                , '𝐚')
    tex = tex.replace('\\mathbf{b}'                , '𝐛')
    tex = tex.replace('\\mathbf{c}'                , '𝐜')
    tex = tex.replace('\\mathbf{d}'                , '𝐝')
    tex = tex.replace('\\mathbf{e}'                , '𝐞')
    tex = tex.replace('\\mathbf{f}'                , '𝐟')
    tex = tex.replace('\\mathbf{g}'                , '𝐠')
    tex = tex.replace('\\mathbf{h}'                , '𝐡')
    tex = tex.replace('\\mathbf{i}'                , '𝐢')
    tex = tex.replace('\\mathbf{j}'                , '𝐣')
    tex = tex.replace('\\mathbf{k}'                , '𝐤')
    tex = tex.replace('\\mathbf{l}'                , '𝐥')
    tex = tex.replace('\\mathbf{m}'                , '𝐦')
    tex = tex.replace('\\mathbf{n}'                , '𝐧')
    tex = tex.replace('\\mathbf{o}'                , '𝐨')
    tex = tex.replace('\\mathbf{p}'                , '𝐩')
    tex = tex.replace('\\mathbf{q}'                , '𝐪')
    tex = tex.replace('\\mathbf{r}'                , '𝐫')
    tex = tex.replace('\\mathbf{s}'                , '𝐬')
    tex = tex.replace('\\mathbf{t}'                , '𝐭')
    tex = tex.replace('\\mathbf{u}'                , '𝐮')
    tex = tex.replace('\\mathbf{v}'                , '𝐯')
    tex = tex.replace('\\mathbf{w}'                , '𝐰')
    tex = tex.replace('\\mathbf{x}'                , '𝐱')
    tex = tex.replace('\\mathbf{y}'                , '𝐲')
    tex = tex.replace('\\mathbf{z}'                , '𝐳')

    return tex


def normal_letters(tex: str) -> str:
    """normal letters"""
    tex = tex.replace('A', '𝐴')
    tex = tex.replace('B', '𝐵')
    tex = tex.replace('C', '𝐶')
    tex = tex.replace('D', '𝐷')
    tex = tex.replace('E', '𝐸')
    tex = tex.replace('F', '𝐹')
    tex = tex.replace('G', '𝐺')
    tex = tex.replace('H' ,'𝐻')
    tex = tex.replace('I' ,'𝐼')
    tex = tex.replace('J', '𝐽')
    tex = tex.replace('K', '𝐾')
    tex = tex.replace('L', '𝐿')
    tex = tex.replace('M', '𝑀')
    tex = tex.replace('N', '𝑁')
    tex = tex.replace('O', '𝑂')
    tex = tex.replace('P', '𝑃')
    tex = tex.replace('Q', '𝑄')
    tex = tex.replace('R', '𝑅')
    tex = tex.replace('S', '𝑆')
    tex = tex.replace('T', '𝑇')
    tex = tex.replace('U', '𝑈')
    tex = tex.replace('V', '𝑉')
    tex = tex.replace('W', '𝑊')
    tex = tex.replace('X', '𝑋')
    tex = tex.replace('Y', '𝑌')
    tex = tex.replace('Z', '𝑍')

    tex = tex.replace('a', '𝑎')
    tex = tex.replace('b', '𝑏')
    tex = tex.replace('c', '𝑐')
    tex = tex.replace('d', '𝑑')
    tex = tex.replace('e', '𝑒')
    tex = tex.replace('f', '𝑓')
    tex = tex.replace('g', '𝑔')
    tex = tex.replace('h', 'ℎ')
    tex = tex.replace('i', '𝑖')
    tex = tex.replace('j', '𝑗')
    tex = tex.replace('k', '𝑘')
    tex = tex.replace('l', '𝑙')
    tex = tex.replace('m', '𝑚')
    tex = tex.replace('n', '𝑛')
    tex = tex.replace('o', '𝑜')
    tex = tex.replace('p', '𝑝')
    tex = tex.replace('q', '𝑞')
    tex = tex.replace('r', '𝑟')
    tex = tex.replace('s', '𝑠')
    tex = tex.replace('t', '𝑡')
    tex = tex.replace('u', '𝑢')
    tex = tex.replace('v', '𝑣')
    tex = tex.replace('w', '𝑤')
    tex = tex.replace('x', '𝑥')
    tex = tex.replace('y', '𝑦')
    tex = tex.replace('z', '𝑧')

    return tex


def greek_letters(tex: str) -> str:
    tex = tex.replace('\\Alpha'                      , 'Α')
    tex = tex.replace('\\Beta'                       , 'Β')
    tex = tex.replace('\\Gamma'                      , 'Γ')
    tex = tex.replace('\\Delta'                      , 'Δ')
    tex = tex.replace('\\Epsilon'                    , 'Ε')
    tex = tex.replace('\\Zeta'                       , 'Ζ')
    kex = tex.replace('\\Eta'                        , 'Η')
    tex = tex.replace('\\Theta'                      , 'Θ')
    tex = tex.replace('\\Iota'                       , 'Ι')
    tex = tex.replace('\\Kappa'                      , 'Κ')
    tex = tex.replace('\\Lambda'                     , 'Λ')
    tex = tex.replace('\\upMu'                       , 'Μ')
    tex = tex.replace('\\upNu'                       , 'Ν')
    tex = tex.replace('\\Xi'                         , 'Ξ')
    tex = tex.replace('\\upOmicron'                  , 'Ο')
    tex = tex.replace('\\Pi'                         , 'Π')
    tex = tex.replace('\\Rho'                        , 'Ρ')
    tex = tex.replace('\\Sigma'                      , 'Σ')
    tex = tex.replace('\\Tau'                        , 'Τ')
    tex = tex.replace('\\Upsilon'                    , 'Υ')
    tex = tex.replace('\\Phi'                        , 'Φ')
    tex = tex.replace('\\Chi'                        , 'Χ')
    tex = tex.replace('\\Psi'                        , 'Ψ')
    tex = tex.replace('\\Omega'                      , 'Ω')

    tex = tex.replace('\\alpha'                      , 'α')
    tex = tex.replace('\\beta'                       , 'β')
    tex = tex.replace('\\gamma'                      , 'γ')
    tex = tex.replace('\\delta'                      , 'δ')
    tex = tex.replace('\\upepsilon'                  , 'ε')
    tex = tex.replace('\\zeta'                       , 'ζ')
    tex = tex.replace('\\eta'                        , 'η')
    tex = tex.replace('\\theta'                      , 'θ')
    tex = tex.replace('\\iota'                       , 'ι')
    tex = tex.replace('\\kappa'                      , 'κ')
    tex = tex.replace('\\lambda'                     , 'λ')
    tex = tex.replace('\\mu'                         , 'μ')
    tex = tex.replace('\\nu'                         , 'ν')
    tex = tex.replace('\\xi'                         , 'ξ')
    tex = tex.replace('\\upomicron'                  , 'ο')
    tex = tex.replace('\\pi'                         , 'π')
    tex = tex.replace('\\rho'                        , 'ρ')
    tex = tex.replace('\\varsigma'                   , 'ς')
    tex = tex.replace('\\sigma'                      , 'σ')
    tex = tex.replace('\\tau'                        , 'τ')
    tex = tex.replace('\\upsilon'                    , 'υ')
    tex = tex.replace('\\varphi'                     , 'φ')
    tex = tex.replace('\\chi'                        , 'χ')
    tex = tex.replace('\\psi'                        , 'ψ')
    tex = tex.replace('\\omega'                      , 'ω')

    tex = tex.replace('\\upvarbeta'                  , 'ϐ')
    tex = tex.replace('\\vartheta'                   , 'ϑ')
    tex = tex.replace('\\phi'                        , 'ϕ')
    tex = tex.replace('\\varpi'                      , 'ϖ')
    tex = tex.replace('\\upoldKoppa'                 , 'Ϙ')
    tex = tex.replace('\\upoldkoppa'                 , 'ϙ')
    tex = tex.replace('\\Stigma'                     , 'Ϛ')
    tex = tex.replace('\\upstigma'                   , 'ϛ')
    tex = tex.replace('\\Digamma'                    , 'Ϝ')
    tex = tex.replace('\\digamma'                    , 'ϝ')
    tex = tex.replace('\\Koppa'                      , 'Ϟ')
    tex = tex.replace('\\upkoppa'                    , 'ϟ')
    tex = tex.replace('\\Sampi'                      , 'Ϡ')
    tex = tex.replace('\\upsampi'                    , 'ϡ')
    tex = tex.replace('\\varkappa'                   , 'ϰ')
    tex = tex.replace('\\varrho'                     , 'ϱ')
    tex = tex.replace('\\textTheta'                  , 'ϴ')
    tex = tex.replace('\\epsilon'                    , 'ϵ')
    tex = tex.replace('\\varepsilon'                 , 'ε')
    tex = tex.replace('\\backepsilon'                , '϶')

    return tex


def mathbfit(tex: str) -> str:
    tex = tex.replace('\\mathbfit{A}'              , '𝑨')
    tex = tex.replace('\\mathbfit{B}'              , '𝑩')
    tex = tex.replace('\\mathbfit{C}'              , '𝑪')
    tex = tex.replace('\\mathbfit{D}'              , '𝑫')
    tex = tex.replace('\\mathbfit{E}'              , '𝑬')
    tex = tex.replace('\\mathbfit{F}'              , '𝑭')
    tex = tex.replace('\\mathbfit{G}'              , '𝑮')
    tex = tex.replace('\\mathbfit{H}'              , '𝑯')
    tex = tex.replace('\\mathbfit{I}'              , '𝑰')
    tex = tex.replace('\\mathbfit{J}'              , '𝑱')
    tex = tex.replace('\\mathbfit{K}'              , '𝑲')
    tex = tex.replace('\\mathbfit{L}'              , '𝑳')
    tex = tex.replace('\\mathbfit{M}'              , '𝑴')
    tex = tex.replace('\\mathbfit{N}'              , '𝑵')
    tex = tex.replace('\\mathbfit{O}'              , '𝑶')
    tex = tex.replace('\\mathbfit{P}'              , '𝑷')
    tex = tex.replace('\\mathbfit{Q}'              , '𝑸')
    tex = tex.replace('\\mathbfit{R}'              , '𝑹')
    tex = tex.replace('\\mathbfit{S}'              , '𝑺')
    tex = tex.replace('\\mathbfit{T}'              , '𝑻')
    tex = tex.replace('\\mathbfit{U}'              , '𝑼')
    tex = tex.replace('\\mathbfit{V}'              , '𝑽')
    tex = tex.replace('\\mathbfit{W}'              , '𝑾')
    tex = tex.replace('\\mathbfit{X}'              , '𝑿')
    tex = tex.replace('\\mathbfit{Y}'              , '𝒀')
    tex = tex.replace('\\mathbfit{Z}'              , '𝒁')

    tex = tex.replace('\\mathbfit{a}'              , '𝒂')
    tex = tex.replace('\\mathbfit{b}'              , '𝒃')
    tex = tex.replace('\\mathbfit{c}'              , '𝒄')
    tex = tex.replace('\\mathbfit{d}'              , '𝒅')
    tex = tex.replace('\\mathbfit{e}'              , '𝒆')
    tex = tex.replace('\\mathbfit{f}'              , '𝒇')
    tex = tex.replace('\\mathbfit{g}'              , '𝒈')
    tex = tex.replace('\\mathbfit{h}'              , '𝒉')
    tex = tex.replace('\\mathbfit{i}'              , '𝒊')
    tex = tex.replace('\\mathbfit{j}'              , '𝒋')
    tex = tex.replace('\\mathbfit{k}'              , '𝒌')
    tex = tex.replace('\\mathbfit{l}'              , '𝒍')
    tex = tex.replace('\\mathbfit{m}'              , '𝒎')
    tex = tex.replace('\\mathbfit{n}'              , '𝒏')
    tex = tex.replace('\\mathbfit{o}'              , '𝒐')
    tex = tex.replace('\\mathbfit{p}'              , '𝒑')
    tex = tex.replace('\\mathbfit{q}'              , '𝒒')
    tex = tex.replace('\\mathbfit{r}'              , '𝒓')
    tex = tex.replace('\\mathbfit{s}'              , '𝒔')
    tex = tex.replace('\\mathbfit{t}'              , '𝒕')
    tex = tex.replace('\\mathbfit{u}'              , '𝒖')
    tex = tex.replace('\\mathbfit{v}'              , '𝒗')
    tex = tex.replace('\\mathbfit{w}'              , '𝒘')
    tex = tex.replace('\\mathbfit{x}'              , '𝒙')
    tex = tex.replace('\\mathbfit{y}'              , '𝒚')
    tex = tex.replace('\\mathbfit{z}'              , '𝒛')

    return tex


def superscript(tex: str) -> str:
    tex = tex.replace('^0', '⁰')
    tex = tex.replace('^1', '¹')
    tex = tex.replace('^2', '²')
    tex = tex.replace('^3', '³')
    tex = tex.replace('^4', '⁴')
    tex = tex.replace('^5', '⁵')
    tex = tex.replace('^6', '⁶')
    tex = tex.replace('^7', '⁷')
    tex = tex.replace('^8', '⁸')
    tex = tex.replace('^9', '⁹')
    tex = tex.replace('^+', '⁺')
    tex = tex.replace('^-', '⁻')
    tex = tex.replace('^=', '⁼')
    tex = tex.replace('^(', '⁽')
    tex = tex.replace('^)', '⁾')
    tex = tex.replace('^a', 'ᵃ')
    tex = tex.replace('^b', 'ᵇ')
    tex = tex.replace('^c', 'ᶜ')
    tex = tex.replace('^d', 'ᵈ')
    tex = tex.replace('^e', 'ᵉ')
    tex = tex.replace('^f', 'ᶠ')
    tex = tex.replace('^g', 'ᵍ')
    tex = tex.replace('^h', 'ʰ')
    tex = tex.replace('^i', 'ⁱ')
    tex = tex.replace('^j', 'ʲ')
    tex = tex.replace('^k', 'ᵏ')
    tex = tex.replace('^l', 'ˡ')
    tex = tex.replace('^m', 'ᵐ')
    tex = tex.replace('^n', 'ⁿ')
    tex = tex.replace('^o', 'ᵒ')
    tex = tex.replace('^p', 'ᵖ')
    tex = tex.replace('^r', 'ʳ')
    tex = tex.replace('^s', 'ˢ')
    tex = tex.replace('^t', 'ᵗ')
    tex = tex.replace('^u', 'ᵘ')
    tex = tex.replace('^v', 'ᵛ')
    tex = tex.replace('^w', 'ʷ')
    tex = tex.replace('^x', 'ˣ')
    tex = tex.replace('^y', 'ʸ')
    tex = tex.replace('^z', 'ᶻ')
    tex = tex.replace('^A', 'ᴬ')
    tex = tex.replace('^B', 'ᴮ')
    tex = tex.replace('^D', 'ᴰ')
    tex = tex.replace('^E', 'ᴱ')
    tex = tex.replace('^G', 'ᴳ')
    tex = tex.replace('^H', 'ᴴ')
    tex = tex.replace('^I', 'ᴵ')
    tex = tex.replace('^J', 'ᴶ')
    tex = tex.replace('^K', 'ᴷ')
    tex = tex.replace('^L', 'ᴸ')
    tex = tex.replace('^M', 'ᴹ')
    tex = tex.replace('^N', 'ᴺ')
    tex = tex.replace('^O', 'ᴼ')
    tex = tex.replace('^P', 'ᴾ')
    tex = tex.replace('^R', 'ᴿ')
    tex = tex.replace('^T', 'ᵀ')
    tex = tex.replace('^U', 'ᵁ')
    tex = tex.replace('^V', 'ⱽ')
    tex = tex.replace('^W', 'ᵂ')

    tex = tex.replace('^{0}', '⁰')
    tex = tex.replace('^{1}', '¹')
    tex = tex.replace('^{2}', '²')
    tex = tex.replace('^{3}', '³')
    tex = tex.replace('^{4}', '⁴')
    tex = tex.replace('^{5}', '⁵')
    tex = tex.replace('^{6}', '⁶')
    tex = tex.replace('^{7}', '⁷')
    tex = tex.replace('^{8}', '⁸')
    tex = tex.replace('^{9}', '⁹')
    tex = tex.replace('^{+}', '⁺')
    tex = tex.replace('^{-}', '⁻')
    tex = tex.replace('^{=}', '⁼')
    tex = tex.replace('^{(}', '⁽')
    tex = tex.replace('^{)}', '⁾')
    tex = tex.replace('^{a}', 'ᵃ')
    tex = tex.replace('^{b}', 'ᵇ')
    tex = tex.replace('^{c}', 'ᶜ')
    tex = tex.replace('^{d}', 'ᵈ')
    tex = tex.replace('^{e}', 'ᵉ')
    tex = tex.replace('^{f}', 'ᶠ')
    tex = tex.replace('^{g}', 'ᵍ')
    tex = tex.replace('^{h}', 'ʰ')
    tex = tex.replace('^{i}', 'ⁱ')
    tex = tex.replace('^{j}', 'ʲ')
    tex = tex.replace('^{k}', 'ᵏ')
    tex = tex.replace('^{l}', 'ˡ')
    tex = tex.replace('^{m}', 'ᵐ')
    tex = tex.replace('^{n}', 'ⁿ')
    tex = tex.replace('^{o}', 'ᵒ')
    tex = tex.replace('^{p}', 'ᵖ')
    tex = tex.replace('^{r}', 'ʳ')
    tex = tex.replace('^{s}', 'ˢ')
    tex = tex.replace('^{t}', 'ᵗ')
    tex = tex.replace('^{u}', 'ᵘ')
    tex = tex.replace('^{v}', 'ᵛ')
    tex = tex.replace('^{w}', 'ʷ')
    tex = tex.replace('^{x}', 'ˣ')
    tex = tex.replace('^{y}', 'ʸ')
    tex = tex.replace('^{z}', 'ᶻ')
    tex = tex.replace('^{A}', 'ᴬ')
    tex = tex.replace('^{B}', 'ᴮ')
    tex = tex.replace('^{D}', 'ᴰ')
    tex = tex.replace('^{E}', 'ᴱ')
    tex = tex.replace('^{G}', 'ᴳ')
    tex = tex.replace('^{H}', 'ᴴ')
    tex = tex.replace('^{I}', 'ᴵ')
    tex = tex.replace('^{J}', 'ᴶ')
    tex = tex.replace('^{K}', 'ᴷ')
    tex = tex.replace('^{L}', 'ᴸ')
    tex = tex.replace('^{M}', 'ᴹ')
    tex = tex.replace('^{N}', 'ᴺ')
    tex = tex.replace('^{O}', 'ᴼ')
    tex = tex.replace('^{P}', 'ᴾ')
    tex = tex.replace('^{R}', 'ᴿ')
    tex = tex.replace('^{T}', 'ᵀ')
    tex = tex.replace('^{U}', 'ᵁ')
    tex = tex.replace('^{V}', 'ⱽ')
    tex = tex.replace('^{W}', 'ᵂ')

    return tex


def subscript(tex: str) -> str:
    tex = tex.replace('_0', '₀')
    tex = tex.replace('_1', '₁')
    tex = tex.replace('_2', '₂')
    tex = tex.replace('_3', '₃')
    tex = tex.replace('_4', '₄')
    tex = tex.replace('_5', '₅')
    tex = tex.replace('_6', '₆')
    tex = tex.replace('_7', '₇')
    tex = tex.replace('_8', '₈')
    tex = tex.replace('_9', '₉')
    tex = tex.replace('_+', '₊')
    tex = tex.replace('_-', '₋')
    tex = tex.replace('_=', '₌')
    tex = tex.replace('_(', '₍')
    tex = tex.replace('_)', '₎')
    tex = tex.replace('_a', 'ₐ')
    tex = tex.replace('_e', 'ₑ')
    tex = tex.replace('_h', 'ₕ')
    tex = tex.replace('_i', 'ᵢ')
    tex = tex.replace('_j', 'ⱼ')
    tex = tex.replace('_k', 'ₖ')
    tex = tex.replace('_l', 'ₗ')
    tex = tex.replace('_m', 'ₘ')
    tex = tex.replace('_n', 'ₙ')
    tex = tex.replace('_o', 'ₒ')
    tex = tex.replace('_p', 'ₚ')
    tex = tex.replace('_r', 'ᵣ')
    tex = tex.replace('_s', 'ₛ')
    tex = tex.replace('_t', 'ₜ')
    tex = tex.replace('_u', 'ᵤ')
    tex = tex.replace('_v', 'ᵥ')
    tex = tex.replace('_x', 'ₓ')

    tex = tex.replace('_{0}', '₀')
    tex = tex.replace('_{1}', '₁')
    tex = tex.replace('_{2}', '₂')
    tex = tex.replace('_{3}', '₃')
    tex = tex.replace('_{4}', '₄')
    tex = tex.replace('_{5}', '₅')
    tex = tex.replace('_{6}', '₆')
    tex = tex.replace('_{7}', '₇')
    tex = tex.replace('_{8}', '₈')
    tex = tex.replace('_{9}', '₉')
    tex = tex.replace('_{+}', '₊')
    tex = tex.replace('_{-}', '₋')
    tex = tex.replace('_{=}', '₌')
    tex = tex.replace('_{(}', '₍')
    tex = tex.replace('_{)}', '₎')
    tex = tex.replace('_{a}', 'ₐ')
    tex = tex.replace('_{e}', 'ₑ')
    tex = tex.replace('_{h}', 'ₕ')
    tex = tex.replace('_{i}', 'ᵢ')
    tex = tex.replace('_{j}', 'ⱼ')
    tex = tex.replace('_{k}', 'ₖ')
    tex = tex.replace('_{l}', 'ₗ')
    tex = tex.replace('_{m}', 'ₘ')
    tex = tex.replace('_{n}', 'ₙ')
    tex = tex.replace('_{o}', 'ₒ')
    tex = tex.replace('_{p}', 'ₚ')
    tex = tex.replace('_{r}', 'ᵣ')
    tex = tex.replace('_{s}', 'ₛ')
    tex = tex.replace('_{t}', 'ₜ')
    tex = tex.replace('_{u}', 'ᵤ')
    tex = tex.replace('_{v}', 'ᵥ')
    tex = tex.replace('_{x}', 'ₓ')

    return tex
