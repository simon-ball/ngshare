"""Init

Revision ID: aa00db20c10a
Revises: 
Create Date: 2020-04-20 00:34:25.543691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa00db20c10a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('files',
    sa.Column('_id', sa.INTEGER(), nullable=False),
    sa.Column('filename', sa.TEXT(), nullable=True),
    sa.Column('checksum', sa.TEXT(), nullable=True),
    sa.Column('actual_name', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('users',
    sa.Column('id', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assignments',
    sa.Column('_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.TEXT(), nullable=True),
    sa.Column('course_id', sa.INTEGER(), nullable=True),
    sa.Column('due', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('instructor_assoc_table',
    sa.Column('left_id', sa.TEXT(), nullable=False),
    sa.Column('right_id', sa.TEXT(), nullable=False),
    sa.Column('first_name', sa.TEXT(), nullable=True),
    sa.Column('last_name', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['left_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    op.create_table('student_assoc_table',
    sa.Column('left_id', sa.TEXT(), nullable=False),
    sa.Column('right_id', sa.TEXT(), nullable=False),
    sa.Column('first_name', sa.TEXT(), nullable=True),
    sa.Column('last_name', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['left_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    op.create_table('assignment_files_assoc_table',
    sa.Column('left_id', sa.TEXT(), nullable=False),
    sa.Column('right_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['assignments._id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['files._id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    op.create_table('submissions',
    sa.Column('_id', sa.INTEGER(), nullable=False),
    sa.Column('assignment_id', sa.INTEGER(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('student_id', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignments._id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('feedback_files_assoc_table',
    sa.Column('left_id', sa.TEXT(), nullable=False),
    sa.Column('right_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['submissions._id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['files._id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    op.create_table('submission_files_assoc_table',
    sa.Column('left_id', sa.TEXT(), nullable=False),
    sa.Column('right_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['submissions._id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['files._id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission_files_assoc_table')
    op.drop_table('feedback_files_assoc_table')
    op.drop_table('submissions')
    op.drop_table('assignment_files_assoc_table')
    op.drop_table('student_assoc_table')
    op.drop_table('instructor_assoc_table')
    op.drop_table('assignments')
    op.drop_table('users')
    op.drop_table('files')
    op.drop_table('courses')
    # ### end Alembic commands ###
