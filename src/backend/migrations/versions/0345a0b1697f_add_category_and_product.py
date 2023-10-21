"""Add category and product

Revision ID: 0345a0b1697f
Revises: 346c3528c01e
Create Date: 2023-10-21 20:19:24.524965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0345a0b1697f'
down_revision = '346c3528c01e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('category')
    # ### end Alembic commands ###
