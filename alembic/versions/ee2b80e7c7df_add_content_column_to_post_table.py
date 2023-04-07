"""add content column to post table

Revision ID: ee2b80e7c7df
Revises: 1ee4d5d7b169
Create Date: 2023-04-05 14:22:06.191564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee2b80e7c7df'
down_revision = '1ee4d5d7b169'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts","content")
    pass
