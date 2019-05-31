"""Added an operator column to banphrase

Revision ID: 47bd378fd30
Revises: 141d961aeb1
Create Date: 2016-01-10 00:40:50.268491

"""

# revision identifiers, used by Alembic.
revision = '47bd378fd30'
down_revision = '141d961aeb1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_banphrase', sa.Column('operator', sa.Enum('contains', 'startswith', 'endswith'), server_default='contains', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_banphrase', 'operator')
    ### end Alembic commands ###
