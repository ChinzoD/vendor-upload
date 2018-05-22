"""empty message

Revision ID: 14fd23d39855
Revises: ba1e78bd2c2c
Create Date: 2018-05-14 15:22:52.790073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14fd23d39855'
down_revision = 'ba1e78bd2c2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('field_name', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.Column('history_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['history_id'], ['history.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_catalog_field_name'), 'catalog', ['field_name'], unique=False)
    op.create_index(op.f('ix_catalog_type'), 'catalog', ['type'], unique=False)
    op.create_index(op.f('ix_catalog_value'), 'catalog', ['value'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_catalog_value'), table_name='catalog')
    op.drop_index(op.f('ix_catalog_type'), table_name='catalog')
    op.drop_index(op.f('ix_catalog_field_name'), table_name='catalog')
    op.drop_table('catalog')
    # ### end Alembic commands ###