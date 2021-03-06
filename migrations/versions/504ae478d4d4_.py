"""empty message

Revision ID: 504ae478d4d4
Revises: 2835007862fd
Create Date: 2021-02-27 05:49:39.936735

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '504ae478d4d4'
down_revision = '2835007862fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               existing_server_default=sa.text("'1'"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    # ### end Alembic commands ###
