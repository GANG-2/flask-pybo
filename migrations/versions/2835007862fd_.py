"""empty message

Revision ID: 2835007862fd
Revises: 2f39056e4c64
Create Date: 2021-02-27 05:48:34.406790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2835007862fd'
down_revision = '2f39056e4c64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    # ### end Alembic commands ###