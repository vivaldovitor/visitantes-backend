"""Adiciona data_visita

Revision ID: 4902f3e88e56
Revises: 
Create Date: 2024-10-31 15:27:22.982101

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4902f3e88e56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visitantes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_visita', sa.DateTime(), nullable=False))
        batch_op.drop_column('visita_data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visitantes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visita_data', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.drop_column('data_visita')

    # ### end Alembic commands ###
