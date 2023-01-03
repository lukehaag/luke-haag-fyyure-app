"""empty message

Revision ID: 90036d833370
Revises: f7bd4dced616
Create Date: 2023-01-02 21:41:14.304174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90036d833370'
down_revision = 'f7bd4dced616'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seeking_description', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')

    # ### end Alembic commands ###