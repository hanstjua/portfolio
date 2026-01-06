from chope import a, div, h1, h2, i, img, li, ul, Element

class StrataTab(Element):
    TITLE = 'Strata'

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
                        h1('.display-1.mb-3')['Strata'],
                        h2('.mb-3')[
                            'A convenient backtesting app.'
                        ],
                        ul[
                            li('.fs-5.mb-1')[
                                'Implement your strategy quickly in <i>Python</i> with <code>pandas</code>.'
                            ],
                            li('.fs-5.mb-1')[
                                'Install your favourite (<code>pyodide</code>-supported) <i>Python</i> packages.'
                            ],
                            li('.fs-5.mb-1')[
                                'Access historical OHLCV of <b>400+</b> stocks in <b>different frequencies</b>.'
                            ],
                            li('.fs-5.mb-4')[
                                'Quickly display your strategy returns.'
                            ]
                        ],
                        div('.d-flex.gap-3')[
                            a('.btn.btn-secondary', href='https://hanstjua.work/strata/index.html', target='_blank')[
                                i('.bi.bi-arrow-right-square-fill.fs-5.me-2'),
                                'Try it!'
                            ],
                            a('.btn.btn-secondary', href='https://github.com/hanstjua/strata', target='_blank')[
                                i('.bi.bi-github.fs-5.me-2'),
                                'Check it out'
                            ]
                        ]
                    ],
                    div('.d-flex.align-items-start.flex-column.justify-content-center')[
                        img(
                            src='/portfolio-assets/strata.png',
                            alt='An example of AI agent built with Jaiger.',
                            style='object-fit: contain; height: 100%; width: 640',
                        )
                    ]
                ]
            ]
