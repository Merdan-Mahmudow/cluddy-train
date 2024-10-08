"""empty message

Revision ID: 0988c5130ddb
Revises: 2c0a217abb1a
Create Date: 2024-09-10 15:56:16.195080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0988c5130ddb'
down_revision: Union[str, None] = '2c0a217abb1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('model', sa.Column('cloth', sa.String(), nullable=True))
    op.add_column('model', sa.Column('shoes', sa.Integer(), nullable=True))
    op.add_column('model', sa.Column('hair', sa.String(), nullable=True))
    op.add_column('model', sa.Column('appereance', sa.String(), nullable=True))
    op.add_column('model', sa.Column('day_1_hour', sa.Integer(), nullable=True))
    op.add_column('model', sa.Column('day_2_hour', sa.Integer(), nullable=True))
    op.add_column('model', sa.Column('night_1_hour', sa.Integer(), nullable=True))
    op.add_column('model', sa.Column('night_all', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('model', 'night_all')
    op.drop_column('model', 'night_1_hour')
    op.drop_column('model', 'day_2_hour')
    op.drop_column('model', 'day_1_hour')
    op.drop_column('model', 'appereance')
    op.drop_column('model', 'hair')
    op.drop_column('model', 'shoes')
    op.drop_column('model', 'cloth')
    op.drop_column('model', 'phone')
    # ### end Alembic commands ###
