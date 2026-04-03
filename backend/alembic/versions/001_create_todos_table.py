"""create todos table

Revision ID: 001
Revises:
Create Date: 2026-04-02
"""

from alembic import op

revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        DO $$ BEGIN
            CREATE TYPE todo_status AS ENUM ('backlog', 'todo', 'in_progress', 'done');
        EXCEPTION WHEN duplicate_object THEN NULL;
        END $$;

        CREATE TABLE IF NOT EXISTS todos (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            title VARCHAR(255) NOT NULL,
            description TEXT,
            status todo_status NOT NULL DEFAULT 'todo',
            position INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
        );
    """)


def downgrade():
    op.execute("DROP TABLE IF EXISTS todos")
    op.execute("DROP TYPE IF EXISTS todo_status")
