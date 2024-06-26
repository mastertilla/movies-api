"""empty message

Revision ID: 4d5ae2a957ca
Revises: 
Create Date: 2024-06-17 17:06:18.012984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d5ae2a957ca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('titles',
    sa.Column('titleId', sa.String(), nullable=False),
    sa.Column('ordering', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('region', sa.String(), nullable=False),
    sa.Column('language', sa.String(), nullable=False),
    sa.Column('types', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('attributes', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('isOriginalTitle', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('titleId', 'ordering')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('titles')
    # ### end Alembic commands ###
