"""empty message

Revision ID: e503c00b48b3
Revises: 0a8049bba315
Create Date: 2021-09-06 15:00:18.540727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e503c00b48b3'
down_revision = '0a8049bba315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('teacher', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subjects', 'teacher')
    # ### end Alembic commands ###