<<<<<<<< HEAD:server/migrations/versions/7e48d960395c_add_new_columns.py
"""Add new columns

Revision ID: 7e48d960395c
Revises: 
Create Date: 2024-02-29 11:35:26.106159
========
"""initial migration

Revision ID: 9cdd5d5cda66
Revises: 
Create Date: 2024-02-29 00:02:00.161196
>>>>>>>> origin/main:server/migrations/versions/9cdd5d5cda66_initial_migration.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:server/migrations/versions/7e48d960395c_add_new_columns.py
revision = '7e48d960395c'
========
revision = '9cdd5d5cda66'
>>>>>>>> origin/main:server/migrations/versions/9cdd5d5cda66_initial_migration.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tokenblocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tokenblocklist', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tokenblocklist_jti'), ['jti'], unique=False)

    op.create_table('trainings',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('personal_no', sa.String(length=10), nullable=False),
    sa.Column('dept_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dept_id'], ['departments.id'], name=op.f('fk_employees_dept_id_departments')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('personal_no')
    )
    op.create_table('hr_personnels',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('personal_no', sa.String(length=10), nullable=False),
    sa.Column('dept_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dept_id'], ['departments.id'], name=op.f('fk_hr_personnels_dept_id_departments')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('personal_no')
    )
    op.create_table('managers',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('personal_no', sa.String(length=10), nullable=False),
    sa.Column('dept_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dept_id'], ['departments.id'], name=op.f('fk_managers_dept_id_departments')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('personal_no')
    )
    op.create_table('documents',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('link_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('official', 'institution', 'other'), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_documents_employee_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('educations',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('institution', sa.String(), nullable=False),
    sa.Column('course', sa.String(), nullable=False),
    sa.Column('qualification', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_educations_employee_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_profiles',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('mantra', sa.String(), nullable=False),
    sa.Column('phone_contact', sa.Integer(), nullable=False),
    sa.Column('profile_photo', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employee_profiles_employee_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_trainings',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('training_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employee_trainings_employee_id_employees')),
    sa.ForeignKeyConstraint(['training_id'], ['trainings.id'], name=op.f('fk_employee_trainings_training_id_trainings')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experiences',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('job_title', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_experiences_employee_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('manager_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('session_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_goals_employee_id_employees')),
    sa.ForeignKeyConstraint(['manager_id'], ['managers.id'], name=op.f('fk_goals_manager_id_managers')),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], name=op.f('fk_goals_session_id_sessions')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hr_profiles',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('hr_id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('mantra', sa.String(), nullable=False),
    sa.Column('phone_contact', sa.Integer(), nullable=False),
    sa.Column('profile_photo', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['hr_id'], ['hr_personnels.id'], name=op.f('fk_hr_profiles_hr_id_hr_personnels')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('leaves',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_leaves_employee_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manager_profiles',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('manager_id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('mantra', sa.String(), nullable=False),
    sa.Column('phone_contact', sa.Integer(), nullable=False),
    sa.Column('profile_photo', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['managers.id'], name=op.f('fk_manager_profiles_manager_id_managers')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('remunerations',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('salary', sa.Float(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('remuneration_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_remunerations_employee_id_employees')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('leave_approvals',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('leave_id', sa.String(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('manager_id', sa.String(), nullable=True),
    sa.Column('hr_id', sa.String(), nullable=True),
    sa.Column('approved_by_manager', sa.Boolean(), nullable=True),
    sa.Column('approved_by_hr', sa.Boolean(), nullable=True),
    sa.Column('manager_app_date', sa.DateTime(), nullable=True),
    sa.Column('hr_approval_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_leave_approvals_employee_id_employees')),
    sa.ForeignKeyConstraint(['hr_id'], ['hr_personnels.id'], name=op.f('fk_leave_approvals_hr_id_hr_personnels')),
    sa.ForeignKeyConstraint(['leave_id'], ['leaves.id'], name=op.f('fk_leave_approvals_leave_id_leaves')),
    sa.ForeignKeyConstraint(['manager_id'], ['managers.id'], name=op.f('fk_leave_approvals_manager_id_managers')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('remuneration_descriptions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('remuneration_id', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('deduction', 'bonus', 'allowance', 'normal'), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['remuneration_id'], ['remunerations.id'], name=op.f('fk_remuneration_descriptions_remuneration_id_remunerations')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('remuneration_descriptions')
    op.drop_table('leave_approvals')
    op.drop_table('remunerations')
    op.drop_table('manager_profiles')
    op.drop_table('leaves')
    op.drop_table('hr_profiles')
    op.drop_table('goals')
    op.drop_table('experiences')
    op.drop_table('employee_trainings')
    op.drop_table('employee_profiles')
    op.drop_table('educations')
    op.drop_table('documents')
    op.drop_table('managers')
    op.drop_table('hr_personnels')
    op.drop_table('employees')
    op.drop_table('trainings')
    with op.batch_alter_table('tokenblocklist', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tokenblocklist_jti'))

    op.drop_table('tokenblocklist')
    op.drop_table('sessions')
    op.drop_table('departments')
    # ### end Alembic commands ###
