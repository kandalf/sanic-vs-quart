"""add apps table

Revision ID: e6f7dd90d95c
Revises: 
Create Date: 2019-01-24 18:22:28.400684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f7dd90d95c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'applications',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode, index=True, nullable=False),
        sa.Column('deployment_script', sa.Text),
        sa.Column('env_name', sa.String),
        sa.Column('env_file', sa.Text),
        sa.Column('last_deployed', sa.DateTime()),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), default=sa.func.now())
    )


def downgrade():
    op.drop_table('applications')
