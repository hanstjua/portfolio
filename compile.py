from pathlib import Path
from app.main import INDEX_PAGE


if __name__ == '__main__':
    Path('index.html').write_text(INDEX_PAGE.render(indent=0))