from chope import a, div, h1, h2, i, img, Element

class JaigerTab(Element):
    TITLE = 'Jaiger'

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
                        h1('.display-1.mb-3')['Jaiger'],
                        h2('.mb-3')[
                            'An MCP-inspired LLM tool framework.'
                        ],
                        div('.fs-5.mb-1')[
                            '<i>Like MCP</i>, it allows you to <b>build AI agents</b>.'
                        ],
                        div('.fs-5.mb-4')[
                            '<i>Unlike MCP</i>, it makes <b>building CPU-intensive tools</b> and <b>parallelizing tool calls</b> easy.'
                        ],
                        a('.btn.btn-secondary', href='https://github.com/hanstjua/jaiger', target='_blank')[
                            i('.bi.bi-github.fs-5.me-2'),
                            'Check it out'
                        ]
                    ],
                    div('.flex-grow-1.d-flex.align-items-start.flex-column.justify-content-center')[
                        img(
                            src='/portfolio-assets/jaiger.png',
                            alt='An example of AI agent built with Jaiger.',
                            style='object-fit: contain; height: 100%; width: 100%'
                        )
                    ]
                ]
            ]
