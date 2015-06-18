"""audiorecording

Revision ID: 35545845a94c
Revises: 14b18b469695
Create Date: 2015-06-18 14:16:07.423083

"""

# revision identifiers, used by Alembic.
revision = '35545845a94c'
down_revision = '14b18b469695'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaign_recording',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(length=100), nullable=False),
    sa.Column('selected', sa.Boolean(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign_campaign.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('campaign_id', 'key', 'selected'),
    sa.UniqueConstraint('version')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign_recording')
    ### end Alembic commands ###
