"""tables

Revision ID: 9ae7503655ec
Revises: 
Create Date: 2024-08-15 23:36:13.324645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy.enums as sa_enum


# revision identifiers, used by Alembic.
revision: str = '9ae7503655ec'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

        op.create_table(
            'users',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('username', sa.String(100), unique=True, index=True),
            sa.Column('hashed_password', sa.String(255)),
            sa.Column('role', sa_enum.Enum('admin', 'user', name='userrole'), default='user'),
        )

        # Create tests table
        op.create_table(
            'tests',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('title', sa.String(255), index=True),
            sa.Column('description', sa.Text),
        )

        # Create questions table
        op.create_table(
            'questions',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('text', sa.Text),
            sa.Column('test_id', sa.Integer, sa.ForeignKey('tests.id')),
        )

        # Create answers table
        op.create_table(
            'answers',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('text', sa.Text),
            sa.Column('is_correct', sa.Boolean, default=False),
            sa.Column('question_id', sa.Integer, sa.ForeignKey('questions.id')),
        )

        # Create results table
        op.create_table(
            'results',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
            sa.Column('test_id', sa.Integer, sa.ForeignKey('tests.id')),
            sa.Column('score', sa.Integer),
        )



def downgrade() -> None:
    pass
