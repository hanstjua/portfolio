from chope import body, head, html, link, meta, script, style, ul, div
from chope.css import Css
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.components.chope_tab import ChopeTab
from app.components.home_tab import HomeTab
from app.components.jaiger_tab import JaigerTab
from app.components.strata_tab import StrataTab
from app.components.tab_nav import TabNav


INDEX_PAGE = html[
    head[
        meta(charset='utf-8'),
        meta(name='viewport', content="width=device-width, initial-scale=1"),
        link(
            href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.8/morph/bootstrap.min.css",
            rel="stylesheet"
        ),
        link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css"
        )
    ],
    body[
        style[
            Css[
                '.nav-link.active': {
                    'background-color': 'var(--bs-secondary-color) !important'
                },
                '.btn:hover': {
                    'background-color': 'var(--bs-btn-hover-bg)'
                }
            ]
        ],
        div('.mt-3.d-flex.justify-content-center', style='z-index: 1020')[
            ul('#main-tab.nav.nav-tabs', style='z-index: 1030', role='tablist')[
                TabNav(HomeTab.TITLE, active=True),
                TabNav(StrataTab.TITLE),
                TabNav(JaigerTab.TITLE),
                TabNav(ChopeTab.TITLE)
            ],
        ],
        div('#main-tab-content.tab-content', style='position: absolute; top: 0; width: 100%; height: 100%')[
            HomeTab(active=True),
            StrataTab(),
            JaigerTab(),
            ChopeTab()
        ],
        script(
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js",
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI",
            crossorigin="anonymous"
        )
    ]
]

app = FastAPI()

app.mount('/portfolio-assets', StaticFiles(directory='assets'), name='assets')

@app.get("/", response_class=HTMLResponse)
async def index():
    return INDEX_PAGE.render(indent=0)
