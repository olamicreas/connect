"""empty message

Revision ID: 737bddd53f5f
Revises: 6bbe148ff571
Create Date: 2022-05-09 02:04:56.933472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '737bddd53f5f'
down_revision = '6bbe148ff571'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lastwallet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lastwallet')
    # ### end Alembic commands ###
