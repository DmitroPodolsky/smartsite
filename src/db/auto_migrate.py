from alembic.config import Config
from alembic import command
from src.config import settings

alembic_cfg = Config(settings.DB_PATH / "alembic.ini")
command.revision(alembic_cfg, autogenerate=True)
command.upgrade(alembic_cfg, "head")