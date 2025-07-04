"""empty message

Revision ID: d7b9fc0dd0b4
Revises: 31f18be300d9
Create Date: 2025-06-30 14:26:56.925263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd7b9fc0dd0b4'
down_revision: Union[str, Sequence[str], None] = '31f18be300d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_factura', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venta')
    # ### end Alembic commands ###
