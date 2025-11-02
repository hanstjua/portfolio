from chope import a, div, h1, h2, i, li, script, style, ul, Element
from chope.css import Css, percent

class ChopeTab(Element):
    TITLE = 'Chope'

    def __new__(cls, active=False) -> Element:
        return div(
                f'.tab-pane.fade{".show.active" if active else ""}',
                id=f'{cls.TITLE}-tab-pane',
                role='tabpanel',
                aria_labelledby=f'{cls.TITLE}-tab',
                tabindex='0'
            )[
                div('.container-lg.d-flex', style='height: 100vh')[
                    div('.flex-grow-1.d-flex.align-items-start.flex-column.justify-content-center.mx-5')[
                        h1('.display-1.mb-3')['Chope'],
                        h2('.mb-3')[
                            'A HTML and CSS DSL for Python.'
                        ],
                        div('.fs-5.mb-1')[
                            'It allows you to write HTML and CSS directly in Python.'
                        ],
                        i('.fs-5.mb-4')[
                            'Fun fact: ',
                            a(
                                '.link-underline.link-underline-opacity-25.link-offset-2',
                                href='https://github.com/hanstjua/portfolio/blob/main/app/main.py'
                            )[
                                'This site is written entirely with Chope'
                            ],
                            '.'
                        ],
                        a('.btn.btn-secondary', href='https://github.com/hanstjua/chope', target='_blank')[
                            i('.bi.bi-github.fs-5.me-2'),
                            'Check it out'
                        ]
                    ],
                    div('.flex-grow-1.d-flex.align-items-start.flex-column.justify-content-center')[
                        style[
                            Css[
                                '.nav-link.active.chope': {
                                    'background-color': 'var(--bs-success) !important'
                                },
                                '.card': {
                                    'width': '35vw !important',
                                    'max-height': percent/60,
                                    'overflow-y': 'auto'
                                },
                                '.nav-link.active.html': {
                                    'background-color': 'var(--bs-warning) !important'
                                }
                            ]
                        ],
                        div[ul('#chope-tab.nav.nav-tabs.nav-fill.mb-4', role='tablist')[
                            (li('.nav-item', role='presentation')[
                                a(
                                    f'#chope-{title}-tab.{title}.nav-link{".show.active" if title == "chope" else ""}.btn-sm',
                                    href='#',
                                    data_bs_toggle='tab',
                                    data_bs_target=f'#chope-{title}-tab-pane',
                                    type='button',
                                    aria_controls=f'chope-{title}-tab-pane',
                                    aria_selected='false',
                                    role='tab'
                                )[title]
                            ]  for title in ['chope', 'html'])
                        ]],
                        div(f'.card.bg-white')[
                            div('.card-body')[
                                div('#chope-tab-content.tab-content')[
                                    (div(
                                        f'.tab-pane.fade{".show.active" if title == "chope" else ""}',
                                        id=f'chope-{title}-tab-pane',
                                        role='tabpanel',
                                        aria_labelledby=f'chope-{title}-tab',
                                        tabindex='0'
                                    )[
                                        script(src="https://gist.github.com/hanstjua/e8f284a4e057340d66f805dd90f1c677.js") if title == 'chope' \
                                        else script(src="https://gist.github.com/hanstjua/0efc0db5465d05280034d9a4c7ae626e.js")
                                    ] for title in ['chope', 'html'])
                                ]
                            ]
                        ]
                        
                    ]
                ]
            ]
