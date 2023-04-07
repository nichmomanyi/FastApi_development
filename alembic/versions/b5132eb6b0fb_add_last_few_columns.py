"""add last few columns

Revision ID: b5132eb6b0fb
Revises: d8822c3d2ecd
Create Date: 2023-04-06 08:46:49.825143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5132eb6b0fb'
down_revision = 'd8822c3d2ecd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")))
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
