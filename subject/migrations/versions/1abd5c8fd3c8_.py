"""empty message

Revision ID: 1abd5c8fd3c8
Revises: da0323747a72
Create Date: 2021-09-27 14:31:26.934082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1abd5c8fd3c8'
down_revision = 'da0323747a72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('exammid', sa.Text(), nullable=True))
    op.add_column('subjects', sa.Column('datemid', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subjects', 'datemid')
    op.drop_column('subjects', 'exammid')
    # ### end Alembic commands ###
