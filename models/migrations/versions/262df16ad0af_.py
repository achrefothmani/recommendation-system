"""empty message

Revision ID: 262df16ad0af
Revises: bdf99762482b
Create Date: 2018-03-29 22:14:49.048643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '262df16ad0af'
down_revision = 'bdf99762482b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    # ### end Alembic commands ###
