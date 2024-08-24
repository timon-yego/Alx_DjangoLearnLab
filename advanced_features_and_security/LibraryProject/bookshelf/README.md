# Permissions and Groups Setup

## Groups:
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can view, create, edit, and delete books.

## Permissions:
- **can_view**: Permission to view books.
- **can_create**: Permission to create books.
- **can_edit**: Permission to edit books.
- **can_delete**: Permission to delete books.

## How to Use:
- Decorators like `@permission_required('bookshelf.can_edit', raise_exception=True)` are used in views to enforce permissions.
- Assign users to appropriate groups to control their access to book-related actions.
