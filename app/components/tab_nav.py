from chope import a, li, Element

class TabNav(Element):
    def __new__(cls, title: str, active=False) -> Element:
        return li('.nav-item', role='presentation')[
                    a(
                        f'#{title}-tab.nav-link{".active" if active else ""}',
                        href='#',
                        data_bs_toggle='tab',
                        data_bs_target=f'#{title}-tab-pane',
                        type='button',
                        aria_controls=f'{title}-tab-pane',
                        aria_selected='false',
                        role='tab'
                    )[title]
                ]
