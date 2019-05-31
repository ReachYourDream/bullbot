"""Added a table for duel stats

Revision ID: 3841cd597e
Revises: d5f1b8bd68
Create Date: 2015-12-02 00:12:07.548855

"""

# revision identifiers, used by Alembic.
revision = '3841cd597e'
down_revision = 'd5f1b8bd68'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_user_duel_stats',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('duels_won', sa.Integer(), nullable=False),
    sa.Column('duels_total', sa.Integer(), nullable=False),
    sa.Column('points_won', sa.Integer(), nullable=False),
    sa.Column('points_lost', sa.Integer(), nullable=False),
    sa.Column('last_duel', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_user_duel_stats')
    ### end Alembic commands ###
