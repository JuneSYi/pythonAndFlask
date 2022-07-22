"""added owners

Revision ID: 17249100eb0c
Revises: f36732c0e7ec
Create Date: 2022-07-21 23:45:06.404780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17249100eb0c'
down_revision = 'f36732c0e7ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    # ### end Alembic commands ###