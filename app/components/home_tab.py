from chope import a, b, div, i, span, style, Element
from chope.css import px, vh, vw, Css


TOTAL_TIMETICKS = 200
PERCENT_SLICE = 100 / TOTAL_TIMETICKS

def get_keyframes(i, j, frames: dict) -> str:
    frame_template = '{percent}% {{ {frame} }}'
    return f'''@keyframes point-{i}-{j} {{ {" ".join(frame_template.format(percent=k * PERCENT_SLICE, frame=frames[k]) for k in range(0, TOTAL_TIMETICKS + 1, 1) if k in frames)} }}'''

def get_animate_bg_css(all_frames: dict, duration: float) -> str:
    ret = ' '.join(f'.point-{i}-{j} {{ animation: point-{i}-{j} {duration}s linear infinite both; }}' for i, j in all_frames)
    return ret + ' ' + ' '.join(get_keyframes(i, j, frame) for (i, j), frame in all_frames.items())

def color_shader(i, j, t) -> str:
    color_up_tick = (29 - i) * 5 + j
    color_up_tick_duration = 40

    if t == color_up_tick - color_up_tick_duration:
        return 'background-color: var(--bs-secondary);'
    elif t == color_up_tick:
        return 'background-color: var(--bs-success-bg-subtle);'
    elif t == (color_up_tick + color_up_tick_duration):
        return 'background-color: var(--bs-secondary);'
    else:
        return ''

def shadow_shader(i, j, t) -> str:
    shadow_on_tick = (29 - i) * 5 + j
    shadow_on_tick_duration = 100

    if t == 0:
        return 'box-shadow: none;'
    elif t == shadow_on_tick - 80:
        return 'box-shadow: none;'
    elif t == shadow_on_tick:
        return 'box-shadow: var(--bs-btn-box-shadow);'
    elif t == (shadow_on_tick + shadow_on_tick_duration):
        return 'box-shadow: none;'
    elif t == TOTAL_TIMETICKS:
        return 'box-shadow: none;'
    else:
        return ''
    
def get_frames():
    ret = {}
    for row in range(30):
        for col in range(row + 6):
            ret[(row, col)] = {}
            for t in range(0, TOTAL_TIMETICKS + 1, 1):
                frame = color_shader(row, col, t) + shadow_shader(row, col, t)
                if frame:
                    ret[(row, col)][t] = frame

    return ret

ANIMATION_CSS = get_animate_bg_css(get_frames(), 4)

class HomeTab(Element):
    TITLE = 'Home'

    def __new__(cls, active=False) -> Element:
        return div(
                f'.tab-pane.fade{".show.active" if active else ""}',
                id=f'{cls.TITLE}-tab-pane',
                role='tabpanel',
                aria_labelledby=f'{cls.TITLE}-tab',
                tabindex='0'
            )[
                style[ANIMATION_CSS],
                div('.d-flex.flex-column.justify-content-center.align-items-start.container', style='height: 100vh;')[
                    style[
                        Css[
                            '.normal': {'font-size': px/24},
                            '.name': {'font-size': px/72},
                            '.social': {'font-size  ': px/36},
                        ]
                    ],
                    div('.normal.mb-2.z-1')[
                        'Hi! ',
                        span["I'm"],
                        span('.name.text-primary-emphasis')[' Johan Tjuatja'],
                        '.'
                    ],
                    div('.normal.mb-3.z-1')[
                        'I code for ',
                        span('.text-primary-emphasis')['work '],
                        'and ', 
                        span('.text-primary-emphasis')['hobby'],
                        '.'
                    ],
                    div('.normal.z-1')[
                        'While this site shows what I do <i>during my free time</i>,'
                    ],
                    div('.normal.mb-5.z-1')[
                        "you can find out what I do <i>at work</i> ",
                        a('.link-underline.link-underline-opacity-25.link-offset-2', href='/portfolio-assets/resume.pdf', target='_blank')[b['here']],
                        '.'
                    ],
                    div('.z-1')[
                        a('.link-underline.link-underline-opacity-0.btn.btn-md.me-4', href='https://github.com/hanstjua/', target='_blank')[
                            i('.bi.bi-github.text-dark.social')
                        ],
                        a('.link-underline.link-underline-opacity-0.btn.me-4', href='https://www.linkedin.com/in/johan-tjuatja/', target='_blank')[
                            i('.bi.bi-linkedin.text-primary.social')
                        ],
                        a('.link-underline.link-underline-opacity-0.btn', href='mailto:hanstjua@yahoo.co.id')[
                            i('.bi.bi-envelope-at.text-info.social')
                        ]
                    ]
                ],
                div('.d-flex.flex-column.z-0.align-items-end.justify-content-start.blur-bg')[
                    style[
                        Css[
                            '.blur-bg': {
                                'filter': 'blur(2px)',
                                'transform': 'translate3d(0, 0, 0)',  ## force GPU acceleration on Safari to speed up blur filter
                                'position': 'absolute',
                                'top': '0',
                                'height': vh/100,
                                'width': vw/100,
                                'overflow-y': 'clip'
                            }
                        ]
                    ],
                    (div('.flex-grow-1.d-flex.justify-content-end.mb-4')[
                        (a(f'.btn.disabled.btn-sm.text-secondary.ms-3.me-{4 - (i % 2)}.my-2.point-{i}-{j}', style='')['O'] for j in range(i + 6))
                    ] for i in range(30))
                ]
            ]
