from alembic.config import Config
from alembic import command

alembic_cfg = Config("./alembic.ini")

command.revision(alembic_cfg, autogenerate=True)
command.upgrade(alembic_cfg, "head")