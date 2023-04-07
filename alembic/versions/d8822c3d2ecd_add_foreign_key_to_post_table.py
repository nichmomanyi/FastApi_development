"""add foreign key to post table

Revision ID: d8822c3d2ecd
Revises: bb9bb46cf351
Create Date: 2023-04-06 08:21:53.196783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8822c3d2ecd'
down_revision = 'bb9bb46cf351'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts",referent_table="users", local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", table_name="posts")
    pass
