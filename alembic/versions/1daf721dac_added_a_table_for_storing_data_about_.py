"""Added a table for storing data about pleblist songs.

Revision ID: 1daf721dac
Revises: 204b3e5a69e
Create Date: 2015-12-07 02:45:41.058891

"""

# revision identifiers, used by Alembic.
revision = '1daf721dac'
down_revision = '204b3e5a69e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_pleblist_song_info',
    sa.Column('pleblist_song_youtube_id', sa.String(length=64, collation='utf8mb4_bin'), autoincrement=False, nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('default_thumbnail', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['pleblist_song_youtube_id'], ['tb_pleblist_song.youtube_id'], ),
    sa.PrimaryKeyConstraint('pleblist_song_youtube_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_pleblist_song_info')
    ### end Alembic commands ###
