"""Create Freebie table

Revision ID: f7fd2574525d
Revises: 5f72c58bf48c
Create Date: 2023-09-06 21:17:01.361157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7fd2574525d'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('dev_id', sa.Integer(), nullable=True),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
        sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('freebies')
