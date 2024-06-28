from pathlib import Path

import pytest

from paperless_mail.parsers import MailDocumentParser


@pytest.fixture(scope="session")
def sample_dir() -> Path:
    return (Path(__file__).parent / Path("samples")).resolve()


@pytest.fixture(scope="session")
def broken_email_file(sample_dir: Path) -> Path:
    return sample_dir / "broken.eml"


@pytest.fixture(scope="session")
def simple_txt_email_file(sample_dir: Path) -> Path:
    return sample_dir / "simple_text.eml"


@pytest.fixture(scope="session")
def simple_txt_email_pdf_file(sample_dir: Path) -> Path:
    return sample_dir / "simple_text.eml.pdf"


@pytest.fixture(scope="session")
def simple_txt_email_thumbnail_file(sample_dir: Path) -> Path:
    return sample_dir / "simple_text.eml.pdf.webp"


@pytest.fixture(scope="session")
def html_email_file(sample_dir: Path) -> Path:
    return sample_dir / "html.eml"


@pytest.fixture(scope="session")
def html_email_pdf_file(sample_dir: Path) -> Path:
    return sample_dir / "html.eml.pdf"


@pytest.fixture(scope="session")
def html_email_thumbnail_file(sample_dir: Path) -> Path:
    return sample_dir / "html.eml.pdf.webp"


@pytest.fixture(scope="session")
def html_email_html_file(sample_dir: Path) -> Path:
    return sample_dir / "html.eml.html"


@pytest.fixture(scope="session")
def merged_pdf_first(sample_dir: Path) -> Path:
    return sample_dir / "first.pdf"


@pytest.fixture(scope="session")
def merged_pdf_second(sample_dir: Path) -> Path:
    return sample_dir / "second.pdf"


@pytest.fixture()
def mail_parser() -> MailDocumentParser:
    return MailDocumentParser(logging_group=None)
