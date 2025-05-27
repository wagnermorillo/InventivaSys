"""No user

Revision ID: 40a691403cb0
Revises: 7aeb8a8f1258
Create Date: 2025-05-06 11:49:23.527973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40a691403cb0'
down_revision: Union[str, None] = '7aeb8a8f1258'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
