# Authentication System for django_blog

## Overview
This document describes the setup and functionality of the authentication system in the `django_blog` project, including user registration, login, logout, and profile management.

## Features
- **User Registration:** Users can create an account by providing a username, email, and password.
- **User Login/Logout:** Users can log in and log out using Django's built-in authentication views.
- **Profile Management:** Users can view their profile and see their username and email.

## Setup Instructions
1. Ensure that `blog/forms.py` defines the `CustomUserCreationForm` for user registration.
2. Add the authentication views in `blog/urls.py` to handle login, logout, registration, and profile management.
3. Create the necessary HTML templates (`login.html`, `register.html`, `profile.html`).
4. Add CSRF protection in all forms to prevent CSRF attacks.
5. Password security is handled using Django’s default password validators.

## Testing
- **Registration:** Navigate to `/register/` and create a new user.
- **Login:** After registration, navigate to `/login/` to log in.
- **Logout:** Log out by visiting `/logout/`.
- **Profile:** Once logged in, visit `/profile/` to view your profile information.
