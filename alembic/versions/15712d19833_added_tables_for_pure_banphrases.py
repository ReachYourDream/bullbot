"""Added tables for pure banphrases

Revision ID: 15712d19833
Revises: 162dd748b57
Create Date: 2015-12-24 02:17:41.959007

"""

# revision identifiers, used by Alembic.
revision = "15712d19833"
down_revision = "162dd748b57"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tb_banphrase",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("phrase", sa.String(length=256), nullable=False),
        sa.Column("length", sa.Integer(), nullable=False),
        sa.Column("permanent", sa.Boolean(), nullable=False),
        sa.Column("warning", sa.Boolean(), nullable=False),
        sa.Column("notify", sa.Boolean(), nullable=False),
        sa.Column("case_sensitive", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tb_banphrase_data",
        sa.Column("banphrase_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("num_uses", sa.Integer(), nullable=False),
        sa.Column("added_by", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["added_by"], ["tb_user.id"]),
        sa.ForeignKeyConstraint(["banphrase_id"], ["tb_banphrase.id"]),
        sa.PrimaryKeyConstraint("banphrase_id"),
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tb_banphrase_data")
    op.drop_table("tb_banphrase")
    ### end Alembic commands ###
