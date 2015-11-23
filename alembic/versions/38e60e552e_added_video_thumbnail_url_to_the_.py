"""Added video thumbnail url to the StreamChunk table

Revision ID: 38e60e552e
Revises: 4842c416a96
Create Date: 2015-11-21 01:00:33.633232

"""

# revision identifiers, used by Alembic.
revision = '38e60e552e'
down_revision = '4842c416a96'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_stream_chunk', sa.Column('video_preview_image_url', sa.String(length=256), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_stream_chunk', 'video_preview_image_url')
    ### end Alembic commands ###
