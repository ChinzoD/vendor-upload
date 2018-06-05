"""empty message

Revision ID: 0582129ead26
Revises: 6a3da21bf541
Create Date: 2018-05-30 11:30:20.802827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0582129ead26'
down_revision = '6a3da21bf541'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('field_decimal', 'field_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('field_decimal', 'field_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###