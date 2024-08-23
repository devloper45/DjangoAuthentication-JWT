# Django JWT Authentication Boilerplate

**This repository serves as a comprehensive boilerplate for implementing user authentication in Django using Django REST Framework (DRF) and JSON Web Tokens (JWT). It includes all the essential authentication features required for a modern web application.**

## Features

- **User Registration**: Allow users to sign up with an email and password. Includes email verification to confirm the user's identity.
- **Login**: Authenticate users with their credentials to provide access to protected routes.
- **JWT Authentication**: Secure your API endpoints with JSON Web Tokens. The JWTs are issued upon successful login and are required for accessing authenticated routes.
- **Password Reset**: Users can request a password reset link via email if they've forgotten their password.
- **Password Change**: Authenticated users can change their password after verifying their current password.
- **Email Confirmation**: Send a confirmation email to users upon registration to verify their email address.
- **Token Refresh**: Support for refreshing JWT tokens to maintain user sessions without re-authentication.
- **Resend Email Confirmation**: Option to resend the email confirmation link if the original link expires.
- **Logout**: Invalidate the JWT token on logout to ensure users cannot access protected resources after logging out.

## Installation

1. **Clone the repository**:
   ```bash
    https://github.com/devloper45/DjangoAuthentication-JWT.git

2 .**Navigate to the project directory:**
   ```bash
    cd django-jwt-auth-boilerplate

3.  **Create a virtual environment:**
    ```bash
    python -m venv env

4. **Activate the virtual environment:**
On Windows:
    ```bash
    .\env\Scripts\activate

**On macOS/Linux:**
    ```bash
    source env/bin/activate

5. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt

6. **Apply migrations:**
    ```bash
    python manage.py migrate

7. **Run the development server:**
    ```bash
    python manage.py runserver

8. **Usage**
Access the API documentation via the DRF Browsable API or use a tool like Postman to interact with the API endpoints.
The repository includes endpoints for:
- /auth/register/: User registration.
- /auth/login/: User login.
- /auth/logout/: User logout.
- /auth/password_reset/: Request password reset.
- /auth/password_reset_confirm/: Confirm password reset.
- /auth/password_change/: Change password.
- /auth/email_verification/: Verify email address.
- /auth/resend_email_verification/: Resend email verification.
- /auth/token_refresh/: Refresh JWT token.

9. **Contributing**
    Contributions are welcome! Feel free to submit a pull request or open an issue for any bug reports, feature requests, or suggestions.

10. **License**
This project is licensed under the MIT License - see the LICENSE file for details.



````
