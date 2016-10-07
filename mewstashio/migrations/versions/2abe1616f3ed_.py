"""empty message

Revision ID: 2abe1616f3ed
Revises: None
Create Date: 2016-10-06 20:58:30.797822

"""

# revision identifiers, used by Alembic.
revision = '2abe1616f3ed'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('robots',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('urls',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urls_user_id'), 'urls', ['user_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_user_id'), table_name='urls')
    op.drop_table('urls')
    op.drop_table('robots')
    ### end Alembic commands ###