
---

## `accounts/` Directory

This directory handles all functionality related to user accounts, including registration, authentication, and profile management.

### `accounts/models.py`
- **Purpose**: Defines the `CustomUser` model that extends Django's `AbstractUser` model. This custom model includes additional fields such as `bio`, `profile_picture`, and a `followers` field (ManyToMany relationship).
- **Key Code**:
    - `bio`: Text field to store a user's bio.
    - `profile_picture`: Image field for uploading a profile picture.
    - `followers`: Many-to-Many relationship allowing users to follow each other.

### `accounts/serializers.py`
- **Purpose**: Defines the serializers for handling data related to the `CustomUser` model.
- **Key Code**:
    - `UserRegistrationSerializer`: Handles validation and creation of users during registration. Automatically creates a new user and returns the relevant data.

### `accounts/views.py`
- **Purpose**: Implements views for user-related actions like registration.
- **Key Code**:
    - `UserRegistrationView`: A view that handles user registration, validates the input data, creates a new user, and generates a token for authentication.

### `accounts/urls.py`
- **Purpose**: Defines URL routes for user-related actions like registration.
- **Key Code**:
    - `path('register/', UserRegistrationView.as_view())`: Defines the registration route at `/api/accounts/register/`.

---

## `posts/` Directory

This directory contains functionality for handling posts and comments within the social media platform.

### `posts/models.py`
- **Purpose**: Defines the `Post` and `Comment` models used in the application.
- **Key Code**:
    - `Post`: Model representing a social media post with fields like `author`, `title`, `content`, and timestamps for creation and updates.
    - `Comment`: Model representing a comment on a post, with fields for the `author`, `post`, and `content`.

### `posts/serializers.py`
- **Purpose**: Defines serializers for handling data related to the `Post` and `Comment` models.
- **Key Code**:
    - `PostSerializer`: Serializes post data, ensuring that users can view, create, and edit their own posts.
    - `CommentSerializer`: Serializes comment data, associating comments with their respective posts and authors.

### `posts/views.py`
- **Purpose**: Implements views for handling CRUD operations for posts and comments.
- **Key Code**:
    - `PostViewSet`: A viewset that provides create, read, update, and delete operations for posts. It restricts editing and deletion to the post author.
    - `CommentViewSet`: A viewset that handles CRUD operations for comments on posts, ensuring that only the author of a comment can modify or delete it.

### `posts/urls.py`
- **Purpose**: Defines URL routes for managing posts and comments.
- **Key Code**:
    - Registers `PostViewSet` and `CommentViewSet` with the DRF router, making routes available at `/api/posts/` and `/api/comments/`.

---

## `social_media_api/` Directory

This directory contains the project settings and configuration files.

### `social_media_api/settings.py`
- **Purpose**: Manages the project’s settings, including installed apps, middleware, database configuration, and more.
- **Key Code**:
    - `INSTALLED_APPS`: Includes `rest_framework`, `rest_framework.authtoken`, `accounts`, and `posts` to enable authentication and post management functionality.
    - `AUTH_USER_MODEL`: Specifies the custom user model (`'accounts.CustomUser'`) for the project.

### `social_media_api/urls.py`
- **Purpose**: Main URL configuration file that includes routes for user account and post/comment management.
- **Key Code**:
    - `path('api/accounts/', include('accounts.urls'))`: Includes the user-related routes under `/api/accounts/`.
    - `path('api/', include('posts.urls'))`: Includes the post and comment-related routes under `/api/`.

---

## `manage.py`
- **Purpose**: A command-line utility for interacting with the Django project (e.g., running migrations, starting the development server).

---

## Features

1. **User Registration and Authentication**:
    - Users can register, log in, and retrieve authentication tokens.
    - Custom user model with additional fields like `bio` and `profile_picture`.

2. **Post and Comment Management**:
    - Authenticated users can create, view, edit, and delete posts.
    - Users can comment on posts, with full control over their comments (CRUD operations).

3. **Permissions**:
    - Only post authors can edit or delete their posts.
    - Only comment authors can modify or delete their comments.

4. **API Features**:
    - Token-based authentication using Django REST Framework.
    - Viewsets and routers for efficient CRUD operations on posts and comments.
    - Pagination and filtering for posts and comments to improve usability with large datasets.

---

## Testing

To test the API, you can run the development server and use tools like Postman or cURL to interact with the endpoints. Use the following command to start the server:

```bash
python manage.py runserver


---

### Summary of Files and their Roles:

1. **`accounts/models.py`**:
   - Defines the `CustomUser` model, with `following` to manage user follow relationships.

2. **`accounts/views.py`**:
   - Implements views to handle follow and unfollow actions.

3. **`accounts/urls.py`**:
   - Defines URL routes for following and unfollowing users.

4. **`posts/models.py`**:
   - Defines the `Post` model (assumed to be already present).

5. **`posts/views.py`**:
   - Implements the `FeedView` to show posts from followed users.

6. **`posts/urls.py`**:
   - Adds the URL route for accessing the user’s post feed.

7. **`posts/serializers.py`**:
   - Serializes post data for API responses.

8. **Testing**:
   - Use Postman or Django API browser to ensure everything works as expected.
