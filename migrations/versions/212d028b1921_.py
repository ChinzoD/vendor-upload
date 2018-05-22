"""empty message

Revision ID: 212d028b1921
Revises: 14fd23d39855
Create Date: 2018-05-17 15:26:22.308964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '212d028b1921'
down_revision = '14fd23d39855'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('field_name', sa.String(length=100), nullable=True),
    sa.Column('field_type', sa.String(length=100), nullable=True),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('max', sa.Float(), nullable=True),
    sa.Column('number_of_decimal', sa.Integer(), nullable=True),
    sa.Column('number_of_decimal2', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_settings_field_name'), 'settings', ['field_name'], unique=False)
    op.create_index(op.f('ix_settings_field_type'), 'settings', ['field_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_settings_field_type'), table_name='settings')
    op.drop_index(op.f('ix_settings_field_name'), table_name='settings')
    op.drop_table('settings')
    # ### end Alembic commands ###