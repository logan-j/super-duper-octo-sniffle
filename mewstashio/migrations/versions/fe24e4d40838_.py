"""empty message

Revision ID: fe24e4d40838
Revises: e71dbb41cf52
Create Date: 2016-09-30 18:44:19.097152

"""

# revision identifiers, used by Alembic.
revision = 'fe24e4d40838'
down_revision = 'e71dbb41cf52'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urls_user_id'), 'urls', ['user_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_user_id'), table_name='urls')
    op.drop_table('urls')
    ### end Alembic commands ###
