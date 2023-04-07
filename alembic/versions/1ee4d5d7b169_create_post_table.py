"""create post table

Revision ID: 1ee4d5d7b169
Revises: 
Create Date: 2023-04-05 14:19:31.509935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ee4d5d7b169'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts",sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
