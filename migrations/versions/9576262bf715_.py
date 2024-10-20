"""empty message

Revision ID: 9576262bf715
Revises: ea22745513fe
Create Date: 2024-09-30 17:49:52.797192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9576262bf715'
down_revision: Union[str, None] = 'ea22745513fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('model', 'surname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###