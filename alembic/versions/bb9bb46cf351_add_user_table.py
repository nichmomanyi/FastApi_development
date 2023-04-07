"""add user table

Revision ID: bb9bb46cf351
Revises: ee2b80e7c7df
Create Date: 2023-04-05 14:29:48.893272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb9bb46cf351'
down_revision = 'ee2b80e7c7df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", 
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"),
                    )
    
    pass


def downgrade():
    op.drop_table("users")
    pass
